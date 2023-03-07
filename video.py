from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

model = YOLO('best.pt')

results = model.predict(source='0', show=True, conf=0.7)

print(results)