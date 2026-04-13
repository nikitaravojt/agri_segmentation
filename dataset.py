import os
import torch
from torch.utils.data import Dataset
from PIL import Image
import numpy as np
from torchvision.transforms import v2
import torchvision.transforms.functional as TF
import random

class CropWeedDataset(Dataset):
    def __init__(self, image_dir, label_dir, indices, augment=False):
        self.image_dir = image_dir
        self.label_dir = label_dir
        self.images = sorted(os.listdir(image_dir))
        self.labels = sorted(os.listdir(label_dir))
        self.images = [self.images[i] for i in indices]
        self.labels = [self.labels[i] for i in indices]
        self.augment = augment
        
    def __len__(self):
            return len(self.images)

    def mask_to_label(self, mask):
        mask = np.array(mask)
        label = np.zeros((mask.shape[0], mask.shape[1]), dtype=np.int64)
        label[np.all(mask == [0, 255, 0], axis=2)] = 1  # green = crop
        label[np.all(mask == [255, 0, 0], axis=2)] = 2  # red = weed
        return label

    def apply_augmentation(self, image, label):
        if random.random() > 0.5:
            image = TF.hflip(image)
            label = TF.hflip(label)
        
        if random.random() > 0.5:
            image = TF.vflip(image)
            label = TF.vflip(label)
        
        # if random.random() > 0.5:
        #     image = TF.rotate(image, 180)
        #     label = TF.rotate(label, 180)
        
        # Colour jitter on img only
        # if random.random() > 0.5:
        #     image = TF.adjust_brightness(image, random.uniform(0.7, 1.4))
        # if random.random() > 0.5:
        #     image = TF.adjust_contrast(image, random.uniform(0.7, 1.3))
        # if random.random() > 0.5:
        #     image = TF.adjust_saturation(image, random.uniform(0.7, 1.3))
        # if random.random() > 0.5:
        #     image = TF.adjust_hue(image, random.uniform(-0.05, 0.05))
        # if random.random() > 0.5:
        #     image = TF.gaussian_blur(image, kernel_size=5, sigma=(0.1, 1.5))

        return image, label

    def __getitem__(self, idx):
        image = Image.open(os.path.join(self.image_dir, self.images[idx])).convert("RGB")
        label = Image.open(os.path.join(self.label_dir, self.labels[idx])).convert("RGB")
        
        image = image.resize((640, 480), Image.BILINEAR)
        label = label.resize((640, 480), Image.NEAREST)

        if self.augment:
            image, label = self.apply_augmentation(image, label)
        
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