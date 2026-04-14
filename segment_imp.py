import sys
import os
from datetime import datetime
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from unet import UNet
from dataset import CropWeedDataset
from skimage.segmentation import find_boundaries
from scipy.ndimage import distance_transform_edt
from sklearn.model_selection import KFold

# Configuration for ablation study
config = {
    "epochs": 50,
    "early_stopping_patience": 7,
    "weighted_ce": False,
    "augmentation": True,
    "dropout": False,
    "lr_scheduler": True,
    "pretrained_encoder": True,
    "kfold": True,
    "lr": 5e-4,
    "eta_min": 5e-7,
    "weight_decay": 1e-4,
    "warmup_epochs": 5,
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
        print(f"  Batch {batch_idx+1}/{len(loader)} | Loss: {loss.item():.4f}", end="\r", flush=True)
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

def run_experiment(train_idx, test_idx, device, criterion, fold=None):
    train_dataset = CropWeedDataset("data/images", "data/segmentation", indices=train_idx, augment=config["augmentation"])
    test_dataset = CropWeedDataset("data/images", "data/segmentation", indices=test_idx)
    
    train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=4, shuffle=False)
    
    if config["pretrained_encoder"]:
        from pretrained_unet import UNetPretrained
        model = UNetPretrained(num_classes=3, dropout=config["dropout"]).to(device)
        print("Selected model: UNet with pretrained ResNet18 encoder")
    else:
        from unet import UNet
        model = UNet(num_classes=3, dropout=config["dropout"]).to(device)
        print("Selected model: UNet with custom 3-level encoder")

    optimizer = torch.optim.AdamW(model.parameters(), lr=config["lr"], weight_decay=config["weight_decay"])

    if config["lr_scheduler"]:
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=config["epochs"] - config["warmup_epochs"], eta_min=config["eta_min"]
        ) 
    
    best_val_loss = float('inf')    
    best_metrics = None
    best_epoch = 0
    patience = config["early_stopping_patience"]
    epochs_no_improve = 0

    # Freeze encoder during warmup
    for param in model.encoder.parameters():
        param.requires_grad = False
    
    for epoch in range(config["epochs"]):
        # Unfreeze encoder after warmup
        if epoch == config["warmup_epochs"]:
            for param in model.encoder.parameters():
                param.requires_grad = True
        # warmup
        if epoch < config["warmup_epochs"]:
            lr = config["lr"] * (epoch + 1) / config["warmup_epochs"]
            for param_group in optimizer.param_groups:
                param_group['lr'] = lr
        
        train_loss = train(model, train_loader, optimizer, criterion, device)
        val_loss, iou, accuracy, bf_scores = evaluate(model, test_loader, criterion, device)
        
        # Turn on cosineLR after warmup completes
        if config["lr_scheduler"] and epoch >= config["warmup_epochs"]:
            scheduler.step()

        current_lr = optimizer.param_groups[0]['lr']
        print(f"  Epoch {epoch+1:02d} | Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f} | "
            f"IoU bg: {iou[0]:.3f} crop: {iou[1]:.3f} weed: {iou[2]:.3f} | LR: {current_lr:.6f}")
        
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_epoch = epoch + 1
            best_metrics = (iou.clone(), accuracy.clone(), bf_scores.clone())
            save_name = f"segmentnet_imp_fold{fold}.pth" if fold else "segmentnet_imp.pth"
            torch.save(model.state_dict(), save_name)
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1
            if epochs_no_improve >= patience:
                print(f"  Early stopping at epoch {epoch+1}")
                break
    
    print(f"  Best epoch {best_epoch} | IoU crop: {best_metrics[0][1]:.3f} weed: {best_metrics[0][2]:.3f}")
    return best_metrics

if __name__ == "__main__":
    # Redirect output to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"results_{timestamp}.txt"
    log_file = open(log_filename, 'w')
    
    class Tee:
        def __init__(self, *files):
            self.files = files
            self.last_was_batch = False
        def write(self, obj):
            is_batch = 'Batch' in obj
            for f in self.files:
                if f is log_file:
                    if is_batch:
                        self.last_was_batch = True
                        continue
                    if self.last_was_batch and not obj.strip():
                        continue  # skip blank lines immediately after batch lines
                    self.last_was_batch = False
                f.write(obj)
                f.flush()
        def flush(self):
            for f in self.files:
                f.flush()
        
    original_stdout = sys.stdout
    sys.stdout = Tee(original_stdout, log_file)
    
    # log config
    print(f"Run timestamp: {timestamp}")
    print(f"Config: {config}\n")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if config["weighted_ce"]:
        class_weights = torch.tensor([0.035, 1.855, 1.110], dtype=torch.float32).to(device) # handling class imbalance
        criterion = nn.CrossEntropyLoss(weight=class_weights)
    else:
        criterion = nn.CrossEntropyLoss()

    if config["kfold"]:
        kf = KFold(n_splits=5, shuffle=True, random_state=42)
        fold_metrics = []
        for fold, (train_idx, test_idx) in enumerate(kf.split(range(50))):
            print(f"\nFold {fold+1}/5")
            fold_metrics.append(run_experiment(train_idx, test_idx, device, criterion, fold=fold+1))
        
        iou_avg = torch.stack([m[0] for m in fold_metrics]).mean(dim=0)
        acc_avg = torch.stack([m[1] for m in fold_metrics]).mean(dim=0)
        bf_avg = torch.stack([m[2] for m in fold_metrics]).mean(dim=0)
        print(f"\nK-Fold Results:")
        print(f"IoU      | bg: {iou_avg[0]:.3f} crop: {iou_avg[1]:.3f} weed: {iou_avg[2]:.3f}")
        print(f"Accuracy | bg: {acc_avg[0]:.3f} crop: {acc_avg[1]:.3f} weed: {acc_avg[2]:.3f}")
        print(f"BFScore  | bg: {bf_avg[0]:.3f} crop: {bf_avg[1]:.3f} weed: {bf_avg[2]:.3f}")
    else:
        run_experiment(range(40), range(40, 50), device, criterion)

    log_file.close()


