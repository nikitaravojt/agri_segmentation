import torch
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
import random

MODEL_PATH = "segmentnet_imp_fold1.pth"
IMAGE_DIR = "data/images"
LABEL_DIR = "data/segmentation"
NUM_IMAGES = 5
RESOLUTION = (1280, 960)

# Colour map: background=black, crop=green, weed=red
COLOURS = np.array([
    [0, 0, 0], # background
    [0, 255, 0], # crop
    [255, 0, 0], # weed
], dtype=np.uint8)

def load_model(model_path, device):
    from pretrained_unet import UNetPretrained
    model = UNetPretrained(num_classes=3).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()

    return model

def predict(model, image_path, device):
    image = Image.open(image_path).convert("RGB")
    image_resized = image.resize(RESOLUTION, Image.BILINEAR)
    
    tensor = torch.tensor(np.array(image_resized), dtype=torch.float32).permute(2, 0, 1) / 255.0
    tensor = tensor.unsqueeze(0).to(device)
    
    with torch.no_grad():
        output = model(tensor)
        pred = torch.argmax(output, dim=1).squeeze(0).cpu().numpy()
    
    return np.array(image_resized), pred

def label_to_colour(label_map):
    h, w = label_map.shape
    colour = np.zeros((h, w, 3), dtype=np.uint8)
    for c in range(3):
        colour[label_map == c] = COLOURS[c]
    return colour

def load_gt(label_path):
    label = Image.open(label_path).convert("RGB")
    label = label.resize(RESOLUTION, Image.NEAREST)
    mask = np.array(label)
    gt = np.zeros((mask.shape[0], mask.shape[1]), dtype=np.int64)
    gt[np.all(mask == [0, 255, 0], axis=2)] = 1
    gt[np.all(mask == [255, 0, 0], axis=2)] = 2
    return gt

def visualise(model, image_dir, label_dir, num_images, device):
    images = sorted(os.listdir(image_dir))
    labels = sorted(os.listdir(label_dir))
    
    indices = random.sample(range(len(images)), min(num_images, len(images)))
    
    fig, axes = plt.subplots(num_images, 3, figsize=(15, 5 * num_images))
    if num_images == 1:
        axes = axes[np.newaxis, :]
    
    for row, idx in enumerate(indices):
        image_path = os.path.join(image_dir, images[idx])
        label_path = os.path.join(label_dir, labels[idx])
        
        original, pred = predict(model, image_path, device)
        gt = load_gt(label_path)
        
        pred_colour = label_to_colour(pred)
        gt_colour = label_to_colour(gt)
        
        axes[row, 0].imshow(original)
        axes[row, 0].set_title(f"Input: {images[idx]}", fontsize=10)
        axes[row, 0].axis("off")
        
        axes[row, 1].imshow(gt_colour)
        axes[row, 1].set_title("Ground Truth", fontsize=10)
        axes[row, 1].axis("off")
        
        axes[row, 2].imshow(pred_colour)
        axes[row, 2].set_title("Prediction", fontsize=10)
        axes[row, 2].axis("off")
    
    plt.suptitle("Segmentation Results - Fold 1 Best Model", fontsize=14)
    plt.tight_layout()
    plt.savefig("results.png", dpi=150, bbox_inches="tight")
    print("Saved to results.png")

if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    model = load_model(MODEL_PATH, device)
    print("Model loaded.")
    visualise(model, IMAGE_DIR, LABEL_DIR, NUM_IMAGES, device)