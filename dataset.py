import os
import torch
from torch.utils.data import Dataset
from PIL import Image
import numpy as np

class CropWeedDataset(Dataset):
    def __init__(self, image_dir, label_dir, indices):
        self.image_dir = image_dir
        self.label_dir = label_dir
        self.images = sorted(os.listdir(image_dir))
        self.labels = sorted(os.listdir(label_dir))
        self.images = [self.images[i] for i in indices]
        self.labels = [self.labels[i] for i in indices]
        
    def __len__(self):
            return len(self.images)

    def mask_to_label(self, mask):
        mask = np.array(mask)
        label = np.zeros((mask.shape[0], mask.shape[1]), dtype=np.int64)
        label[np.all(mask == [0, 255, 0], axis=2)] = 1  # green = crop
        label[np.all(mask == [255, 0, 0], axis=2)] = 2  # red = weed
        return label

    def __getitem__(self, idx):
        image = Image.open(os.path.join(self.image_dir, self.images[idx])).convert("RGB")
        label = Image.open(os.path.join(self.label_dir, self.labels[idx])).convert("RGB")
        
        image = image.resize((1280, 960), Image.BILINEAR)
        label = label.resize((1280, 960), Image.NEAREST)
        
        image = torch.tensor(np.array(image), dtype=torch.float32).permute(2, 0, 1) / 255.0
        label = torch.tensor(self.mask_to_label(label), dtype=torch.long)
        
        return image, label
    
if __name__ == "__main__":
    dataset = CropWeedDataset(
        image_dir="data/images",
        label_dir="data/segmentation",
        indices=range(50)
    )
    print(f"Dataset size: {len(dataset)}")
    image, label = dataset[0]
    print(f"Image shape: {image.shape}")
    print(f"Label shape: {label.shape}")
    print(f"Unique label values: {torch.unique(label)}")