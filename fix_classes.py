import os

base = r"C:\Users\aashr\yolo_dataset\labels"

for split in ["train", "val", "test"]:
    folder = os.path.join(base, split)

    if not os.path.exists(folder):
        continue

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            path = os.path.join(folder, file)

            with open(path, "r") as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) > 0:
                    parts[0] = str(int(parts[0]) - 1)
                new_lines.append(" ".join(parts))

            with open(path, "w") as f:
                f.write("\n".join(new_lines))

print("✅ Class indices fixed!")