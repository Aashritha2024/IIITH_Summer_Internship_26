from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="C:/Users/aashr/yolo_dataset/dataset.yaml",
    epochs=50,
    imgsz=640
)