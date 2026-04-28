import os

base = r"C:\Users\aashr\yolo_dataset"

for split in ["train", "val"]:
    img_dir = os.path.join(base, "images", split)
    lbl_dir = os.path.join(base, "labels", split)

    print(f"\nChecking {split}...")

    images = set([os.path.splitext(f)[0] for f in os.listdir(img_dir)])
    labels = set([os.path.splitext(f)[0] for f in os.listdir(lbl_dir)])

    print(f"Images: {len(images)}")
    print(f"Labels: {len(labels)}")

    missing_labels = images - labels
    missing_images = labels - images

    if missing_labels:
        print("Missing labels for:", list(missing_labels)[:5])
    if missing_images:
        print("Missing images for:", list(missing_images)[:5])