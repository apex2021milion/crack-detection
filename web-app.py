import streamlit as st
from PIL import Image
from ultralytics import YOLO

#@st.cache_data()

model = YOLO('yolov8-m.pt')

def main():
    st.title("Crack Segmentation")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        inputs = Image.open(uploaded_file)
        st.image(inputs, caption='Uploaded Image.', use_column_width=True)

        results = model(inputs)
        res_plotted = results[0].plot()
        
        st.subheader("Object Detection Results:")
        st.image(res_plotted, caption='Predicted Image.', use_column_width=True)
if __name__ == '__main__':
    main()