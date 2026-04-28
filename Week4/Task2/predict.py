from ultralytics import YOLO

model = YOLO("C:/Users/aashr/yolo_dataset/runs/detect/train-2/weights/best.pt")

results = model.predict(
    source="C:/Users/aashr/yolo_dataset/images/test",
    save=True
)

print("Prediction done ✅")