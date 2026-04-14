import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models

class DoubleConv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.block = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
        )

    def forward(self, x):
        return self.block(x)

class PretrainedEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        resnet = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
        self.initial = nn.Sequential(resnet.conv1, resnet.bn1, resnet.relu)  # 64, h/2
        self.pool = resnet.maxpool # h/4
        self.layer1 = resnet.layer1  # 64, h/4
        self.layer2 = resnet.layer2  # 128, h/8
        self.layer3 = resnet.layer3  # 256, h/16
        self.layer4 = resnet.layer4  # 512, h/32

        # ImageNet normalisation baked in
        self.register_buffer("mean", torch.tensor([0.485, 0.456, 0.406]).view(1, 3, 1, 1))
        self.register_buffer("std", torch.tensor([0.229, 0.224, 0.225]).view(1, 3, 1, 1))

    def forward(self, x):
        x = (x - self.mean) / self.std
        s1 = self.initial(x) # 64,  h/2
        x = self.pool(s1) # 64,  h/4
        s2 = self.layer1(x) # 64,  h/4
        s3 = self.layer2(s2) # 128, h/8
        s4 = self.layer3(s3) # 256, h/16
        out = self.layer4(s4) # 512, h/32
        return out, s1, s2, s3, s4


class PretrainedDecoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.up1 = nn.ConvTranspose2d(512, 256, kernel_size=2, stride=2)
        self.conv1 = DoubleConv(512, 256)  # 256 + 256(s4)
        self.up2 = nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2)
        self.conv2 = DoubleConv(256, 128) # 128 + 128(s3)
        self.up3 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.conv3 = DoubleConv(128, 64) # 64 + 64(s2)
        self.up4 = nn.ConvTranspose2d(64, 64, kernel_size=2, stride=2)
        self.conv4 = DoubleConv(128, 64) # 64 + 64(s1)

    def forward(self, x, s1, s2, s3, s4):
        x = torch.cat([self.up1(x), s4], dim=1)
        x = self.conv1(x)
        x = torch.cat([self.up2(x), s3], dim=1)
        x = self.conv2(x)
        x = torch.cat([self.up3(x), s2], dim=1)
        x = self.conv3(x)
        x = torch.cat([self.up4(x), s1], dim=1)
        x = self.conv4(x)
        return x


class UNetPretrained(nn.Module):
    def __init__(self, num_classes=3, dropout=False):
        super().__init__()
        self.encoder = PretrainedEncoder()
        self.dropout = nn.Dropout2d(0.4) if dropout else None
        self.decoder = PretrainedDecoder()
        self.output = nn.Conv2d(64, num_classes, kernel_size=1)

    def forward(self, x):
        input_size = x.shape[2:]
        out, s1, s2, s3, s4 = self.encoder(x)
        if self.dropout:
            out = self.dropout(out)
        out = self.decoder(out, s1, s2, s3, s4)
        out = self.output(out)
        # Decoder recovers to H/2 due to ResNet's initial stride-2 conv
        out = F.interpolate(out, size=input_size, mode="bilinear", align_corners=True)
        return out


if __name__ == "__main__":
    model = UNetPretrained(num_classes=3)
    x = torch.randn(1, 3, 480, 640)
    out = model(x)
    print(f"Input:  {x.shape}")
    print(f"Output: {out.shape}")
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Total parameters:     {total:,}")
    print(f"Trainable parameters: {trainable:,}")