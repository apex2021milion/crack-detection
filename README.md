# Crack Detection and Segmentation

## Requirements
- streamlit
- pillow
- ultralytics
- opencv-python-headless

Usage: pip install -r requirements.txt

### Installation
Pip install the ultralytics package including all requirements in requirements.txt in a Python>=3.7 environment


## Usage
photo.py
```
model = YOLO('best.pt') #load current model
inputs = ['CRACK500_20160222_080933_361_1.jpg'] #load input image
```

video.py (real-time)
```
model = YOLO('best.pt') #load current model
results = model.predict(source='0', show=True, conf=0.7) #use source '0' for camera input
```

## Prototype
[Prototype](https://deguzmankarladrian-crack-detection-web-app-uki2w3.streamlit.app/) was deployed in streamlit using github

To run in local: 

web-app.py
```
model = YOLO('best.pt') #load current model
```
then run at terminal:
```
>streamlit run web-app.py
```
