from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

model = YOLO('best.pt')

results = model.predict(source='DJI_20210929115851_0092_SUPR.JPG', show=True)

print(results)