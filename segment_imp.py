import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from unet import UNet
from dataset import CropWeedDataset
from skimage.segmentation import find_boundaries
from scipy.ndimage import distance_transform_edt

# Configuration for ablation study
config = {
    "weighted_ce": False,
    "augmentation": False,
    "dropout": False,
    "lr_scheduler": False,
    "pretrained_encoder": False,
    "kfold": False,
}

def train(model, loader, optimizer, criterion, device):
    model.train()
    total_loss = 0
    for batch_idx, (images, labels) in enumerate(loader):
        images = images.to(device)
        labels = labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        print(f"  Batch {batch_idx+1}/{len(loader)} | Loss: {loss.item():.4f}", end="\r")
    return total_loss / len(loader)

def boundary_f1(pred, label, num_classes, tolerance=2):
    bf_scores = []
    for c in range(num_classes):
        pred_c = (pred == c).numpy().astype(bool)
        label_c = (label == c).numpy().astype(bool)

        pred_boundary = find_boundaries(pred_c, mode='outer')
        label_boundary = find_boundaries(label_c, mode='outer')

        if label_boundary.sum() == 0 and pred_boundary.sum() == 0:
            bf_scores.append(1.0)
            continue
        if label_boundary.sum() == 0 or pred_boundary.sum() == 0:
            bf_scores.append(0.0)
            continue

        dist_pred = distance_transform_edt(~pred_boundary)
        dist_label = distance_transform_edt(~label_boundary)

        precision = (dist_label[pred_boundary] <= tolerance).mean()
        recall = (dist_pred[label_boundary] <= tolerance).mean()

        if precision + recall == 0:
            bf_scores.append(0.0)
        else:
            bf_scores.append(2 * precision * recall / (precision + recall))

    return torch.tensor(bf_scores)

def evaluate(model, loader, criterion, device, num_classes=3):
    model.eval()
    total_loss = 0
    intersection = torch.zeros(num_classes)
    union = torch.zeros(num_classes)
    total = torch.zeros(num_classes)

    # F1 score
    bf_scores = torch.zeros(num_classes)
    num_batches = 0
    
    with torch.no_grad():
        for images, labels in loader:
            images = images.to(device)
            labels = labels.to(device)
            
            outputs = model(images)
            loss = criterion(outputs, labels)
            total_loss += loss.item()
            
            preds = torch.argmax(outputs, dim=1)

            for i in range(preds.shape[0]):
                bf_scores += boundary_f1(preds[i].cpu(), labels[i].cpu(), num_classes)
                num_batches += 1
            
            for c in range(num_classes):
                pred_c = (preds == c)
                label_c = (labels == c)
                intersection[c] += (pred_c & label_c).sum().item()
                union[c] += (pred_c | label_c).sum().item()
                total[c] += label_c.sum().item()
    
    iou = intersection / (union + 1e-6)
    accuracy = intersection / (total + 1e-6)
    bf_scores = bf_scores / num_batches
    return total_loss / len(loader), iou, accuracy, bf_scores

if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    train_dataset = CropWeedDataset("data/images", "data/segmentation", indices=range(40))
    test_dataset = CropWeedDataset("data/images", "data/segmentation", indices=range(40, 50))

    train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=4, shuffle=False)

    model = UNet(num_classes=3).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    best_val_loss = float('inf')

    for epoch in range(20):
        train_loss = train(model, train_loader, optimizer, criterion, device)
        val_loss, iou, accuracy, bf_scores = evaluate(model, test_loader, criterion, device)
        print(f"Epoch {epoch+1:02d} | Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f} | "
            f"IoU bg: {iou[0]:.3f} crop: {iou[1]:.3f} weed: {iou[2]:.3f} | "
            f"Acc bg: {accuracy[0]:.3f} crop: {accuracy[1]:.3f} weed: {accuracy[2]:.3f} | "
            f"BF bg: {bf_scores[0]:.3f} crop: {bf_scores[1]:.3f} weed: {bf_scores[2]:.3f}")

        if val_loss < best_val_loss: # checkpointing
            best_val_loss = val_loss
            best_epoch = epoch + 1
            torch.save(model.state_dict(), "segmentnet_imp.pth")

    print(f"\nTraining complete. Best model at epoch {best_epoch} with val loss {best_val_loss:.4f}. Saved to segmentnet_imp.pth")
    torch.save(model.state_dict(), "segmentnet_imp.pth")
    print("Model saved.")


