import cv2
import os

video_path = r"C:\Users\aashr\video_cars.mp4"
output_dir = "frames"

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ ERROR: Cannot open video")
    exit()

fps_target = 10
video_fps = cap.get(cv2.CAP_PROP_FPS)

print("Original FPS:", video_fps)

frame_interval = max(1, int(video_fps // fps_target))

count = 0
saved = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if count % frame_interval == 0:
        cv2.imwrite(f"{output_dir}/frame_{saved}.jpg", frame)
        saved += 1

    count += 1

cap.release()
print("✅ Frames saved:", saved)
