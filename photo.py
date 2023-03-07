from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

model = YOLO('best.pt')
inputs = ['CRACK500_20160222_080933_361_1.jpg']
results = model(inputs)

res_plotted = results[0].plot()
cv2.imshow("result", res_plotted)
cv2.waitKey(0)
cv2.destroyAllWindows()