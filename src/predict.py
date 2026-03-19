from ultralytics import YOLO

model = YOLO("weights/best.pt")

model.predict(
    source="sample_test_images",
    save=True,
    conf=0.25,
    project="rayoscan_runs",
    name="predictions"
)
