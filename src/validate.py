from ultralytics import YOLO

model = YOLO("weights/best.pt")
metrics = model.val(data="data.yaml")
print(metrics)
