import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from dataset import CropWeedDataset

dataset = CropWeedDataset("data/images", "data/segmentation", 
                           indices=range(5), augment=True)

fig, axes = plt.subplots(5, 2, figsize=(10, 20))
for i in range(5):
    image, label = dataset[0]  # same image, different augmentation each time
    axes[i, 0].imshow(image.permute(1, 2, 0))
    axes[i, 1].imshow(label)
    axes[i, 0].set_title(f'Augmented image {i+1}')
    axes[i, 1].set_title(f'Augmented label {i+1}')

plt.tight_layout()
plt.savefig('augmentation_check.png')
print("Saved to augmentation_check.png")