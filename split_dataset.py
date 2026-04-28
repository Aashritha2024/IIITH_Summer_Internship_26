import os
import random
import shutil

source = "frames"
train_dir = "images/train"
val_dir = "images/val"
test_dir = "images/test"

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

images = os.listdir(source)
random.shuffle(images)

train_split = 100
val_split = 40

train_imgs = images[:train_split]
val_imgs = images[train_split:train_split+val_split]
test_imgs = images[train_split+val_split:]

for img in train_imgs:
    shutil.copy(os.path.join(source, img), train_dir)

for img in val_imgs:
    shutil.copy(os.path.join(source, img), val_dir)

for img in test_imgs:
    shutil.copy(os.path.join(source, img), test_dir)

print("Dataset split done!")
print(len(train_imgs), len(val_imgs), len(test_imgs))