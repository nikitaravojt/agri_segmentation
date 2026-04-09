import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from unet import UNet
from dataset import CropWeedDataset

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

def evaluate(model, loader, criterion, device, num_classes=3):
    model.eval()
    total_loss = 0
    intersection = torch.zeros(num_classes)
    union = torch.zeros(num_classes)
    
    with torch.no_grad():
        for images, labels in loader:
            images = images.to(device)
            labels = labels.to(device)
            
            outputs = model(images)
            loss = criterion(outputs, labels)
            total_loss += loss.item()
            
            preds = torch.argmax(outputs, dim=1)
            
            for c in range(num_classes):
                pred_c = (preds == c)
                label_c = (labels == c)
                intersection[c] += (pred_c & label_c).sum().item()
                union[c] += (pred_c | label_c).sum().item()
    
    iou = intersection / (union + 1e-6)
    return total_loss / len(loader), iou

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

    for epoch in range(20):
        train_loss = train(model, train_loader, optimizer, criterion, device)
        val_loss, iou = evaluate(model, test_loader, criterion, device)
        print(f"Epoch {epoch+1:02d} | Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f} | IoU bg: {iou[0]:.3f} crop: {iou[1]:.3f} weed: {iou[2]:.3f}")

    torch.save(model.state_dict(), "segmentnet_base.pth")
    print("Model saved.")
