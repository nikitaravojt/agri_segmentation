import torch
import torch.nn as nn

class DoubleConv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.block = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.block(x)

class Encoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.enc1 = DoubleConv(3, 32)
        self.enc2 = DoubleConv(32, 64)
        self.enc3 = DoubleConv(64, 128)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

    def forward(self, x):
        s1 = self.enc1(x)
        s2 = self.enc2(self.pool(s1))
        s3 = self.enc3(self.pool(s2))
        out = self.pool(s3)
        return out, s1, s2, s3
    
class Bottleneck(nn.Module):
    def __init__(self, dropout=False):
        super().__init__()
        self.block = DoubleConv(128, 256)
        self.dropout = nn.Dropout2d(0.4) if dropout else None

    def forward(self, x):
        x = self.block(x)
        if self.dropout:
            x = self.dropout(x)
        return x
    
class Decoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.up1 = nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2)
        self.conv1 = DoubleConv(256, 128)
        self.up2 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.conv2 = DoubleConv(128, 64)
        self.up3 = nn.ConvTranspose2d(64, 32, kernel_size=2, stride=2)
        self.conv3 = DoubleConv(64, 32)

    def forward(self, x, s1, s2, s3):
        x = self.up1(x)
        x = torch.cat([x, s3], dim=1)
        x = self.conv1(x)
        x = self.up2(x)
        x = torch.cat([x, s2], dim=1)
        x = self.conv2(x)
        x = self.up3(x)
        x = torch.cat([x, s1], dim=1)
        x = self.conv3(x)
        return x
    
class UNet(nn.Module):
    def __init__(self, num_classes=3, dropout=False):
        super().__init__()
        self.encoder = Encoder()
        self.bottleneck = Bottleneck(dropout=dropout)
        self.decoder = Decoder()
        self.output = nn.Conv2d(32, num_classes, kernel_size=1)

    def forward(self, x):
        out, s1, s2, s3 = self.encoder(x)
        out = self.bottleneck(out)
        out = self.decoder(out, s1, s2, s3)
        out = self.output(out)
        return out
    
if __name__ == "__main__":
    model = UNet(num_classes=3)
    x = torch.randn(1, 3, 960, 1280)
    out = model(x)
    print(out.shape)
    total = sum(p.numel() for p in model.parameters())
    print(f"Total parameters: {total:,}")
