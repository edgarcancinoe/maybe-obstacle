import torchvision.transforms as T


def get_default_transforms():
    return T.Compose([
        T.ToTensor(),
        T.Resize((256, 512)),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
