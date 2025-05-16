import os
import shutil

# Expected Cityscapes Dataset Directory Structure in Downloads directory
#
# Cityscapes/
# ├── gtFine/
# │   ├── train/
# │   │   ├── berlin/
# │   │   │   └── <label files: *_gtFine_labelIds.png, *_gtFine_instanceIds.png, etc.>
# │   │   ├── bielefeld/
# │   │   │   └── <label files>
# │   ├── val/
# │   │   ├── berlin/
# │   │   └── bielefeld/
# │   └── test/
# │       ├── berlin/
# │       └── bielefeld/
#
# ├── leftImg8bit/
# │   ├── train/
# │   │   ├── berlin/
# │   │   │   └── <image files: *_leftImg8bit.png>
# │   │   ├── bielefeld/
# │   │   │   └── <image files>
# │   ├── val/
# │   │   ├── berlin/
# │   │   └── bielefeld/
# │   └── test/
# │       ├── berlin/
# │       └── bielefeld/


def move_cityscapes_images_and_labels(downloads_dir, project_dir):
    """
    Moves all leftImg8bit images and all gtFine label files from Cityscapes
    using the provided 'trainvaltest' folder names.
    """
    splits = ["train", "val", "test"]

    # File types to move from gtFine
    label_suffixes = [
        "_gtFine_labelIds.png",
        "_gtFine_color.png",
        "_gtFine_instanceIds.png",
        "_gtFine_polygons.json"
    ]

    # Safety check: make sure 'data/' exists
    if not os.path.exists(os.path.dirname(project_dir)):
        raise FileNotFoundError(
            "The 'data' folder does not exist. Please create it before running the script.")

    for split in splits:
        print(f"\n--- Processing {split} split ---")

        # Source directories
        img_src_root = os.path.join(
            downloads_dir, "leftImg8bit", split)
        lbl_src_root = os.path.join(
            downloads_dir, "gtFine", split)

        # Destination directories
        img_dest = os.path.join(project_dir, split, "images")
        lbl_dest = os.path.join(project_dir, split, "labels")
        os.makedirs(img_dest, exist_ok=True)
        os.makedirs(lbl_dest, exist_ok=True)

        # Move images
        for root, _, files in os.walk(img_src_root):
            for file in files:
                if file.endswith("_leftImg8bit.png"):
                    src_file = os.path.join(root, file)
                    dst_file = os.path.join(img_dest, file)
                    print(f"Moving image: {file}")
                    shutil.copy2(src_file, dst_file)

        # Move labels (all 4 types)
        for root, _, files in os.walk(lbl_src_root):
            for file in files:
                if any(file.endswith(suffix) for suffix in label_suffixes):
                    src_file = os.path.join(root, file)
                    dst_file = os.path.join(lbl_dest, file)
                    print(f"Moving label: {file}")
                    shutil.copy2(src_file, dst_file)

    print("\n Done, all images and label files have been moved.")


# UPDATE YOUR PATHS HERE!
DOWNLOADS_DIR = "/Users/enriquef/Downloads/Cityscapes"
PROJECT_DATA_DIR = "/Users/enriquef/Documents/Code/EMAI/Sapienza/ComputerVision/maybe-obstacle/data/cityscapes"

# Run it
move_cityscapes_images_and_labels(DOWNLOADS_DIR, PROJECT_DATA_DIR)

# Run this script using:
# python organize_cityscapes.py
# Make sure to update the DOWNLOADS_DIR and PROJECT_DATA_DIR variables
# to point to your actual directories.
