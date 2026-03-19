from ultralytics import YOLO

model = YOLO("yolo11n.pt")

model.train(
    data="data.yaml",
    epochs=30,
    imgsz=640,
    batch=16,
    project="rayoscan_runs",
    name="yolo11n_baseline",
    patience=10,
    pretrained=True
)
