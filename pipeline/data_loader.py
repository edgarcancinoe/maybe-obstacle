import os
import cv2
import torch
import glob
import json
from torch.utils.data import Dataset


class CityscapesDataset(Dataset):

    def __init__(
        self,
        root_dir,
        split="train",
        img_transform=None,
        lbl_transform=None,
        label_type="labelIds"  # Options: "labelIds", "instanceIds", "color", "json"
    ):
        self.image_dir = os.path.join(root_dir, split, "images")
        self.label_dir = os.path.join(root_dir, split, "labels")
        self.img_transform = img_transform
        self.lbl_transform = lbl_transform
        self.label_type = label_type

        # Load image file paths
        self.image_files = sorted(
            glob.glob(os.path.join(self.image_dir, "*_leftImg8bit.png")))

        # Build corresponding label filenames
        suffix_map = {
            "labelIds": "_gtFine_labelIds.png",
            "instanceIds": "_gtFine_instanceIds.png",
            "color": "_gtFine_color.png",
            "json": "_gtFine_polygons.json",
        }

        if label_type not in suffix_map:
            raise ValueError(f"Unsupported label_type: {label_type}")

        suffix = suffix_map[label_type]
        self.label_files = [
            os.path.join(self.label_dir, os.path.basename(
                f).replace("_leftImg8bit.png", suffix))
            for f in self.image_files
        ]

        # Verify that label files exist
        missing = []
        for i, label_file in enumerate(self.label_files):
            if not os.path.exists(label_file):
                print(f"[{i}] Missing label: {label_file}")
                missing.append(label_file)

        if missing:
            raise FileNotFoundError(
                f"Missing {len(missing)} label files for type '{label_type}'.")

        print(
            f"Loaded {len(self.image_files)} {split} samples with label type '{label_type}'.")

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        image_path = self.image_files[idx]
        label_path = self.label_files[idx]

        image = cv2.imread(image_path)

        # Load label according to type
        if self.label_type == "json":
            with open(label_path, "r") as f:
                # You’ll need custom logic if you use this
                label = json.load(f)
        else:
            flag = cv2.IMREAD_COLOR if self.label_type == "color" else cv2.IMREAD_GRAYSCALE
            label = cv2.imread(label_path, flag)

        # Apply transformations
        if self.img_transform:
            image = self.img_transform(image)
        if self.lbl_transform and not isinstance(label, dict):
            label = self.lbl_transform(label)

        return image, label
