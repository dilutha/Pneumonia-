# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vGjdeND4szE_qcX0wO7zRlX85m-yc9bD
"""


import streamlit as st
import numpy as np
from PIL import Image, ImageOps
from keras.models import load_model

# Function to load and preprocess the image
def preprocess_image(image):
    # Load the image
    img = Image.open(image).convert('RGB')
    # Resize the image to the model's expected sizing
    img = img.resize((150, 150))
    # Image preprocessing specific to your model
    img_array = np.array(img) / 255.0  # Normalization
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Function to import and predict with the model
def import_and_predict(image, model):
    img = preprocess_image(image)
    prediction = model.predict(img)
    return prediction

def main():
    # Load the pre-trained model
    model = load_model('pneumonia_model.h5')

    st.title('Pneumonia Detection from Chest X-ray')

    # File uploader widget
    uploaded_file = st.file_uploader("Upload a chest X-ray image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Perform prediction on the uploaded image
        if st.button('Predict'):
            prediction = import_and_predict(uploaded_file, model)
            if prediction[0][0] > 0.5:
                st.write('Prediction: Pneumonia')
            else:
                st.write('Prediction: Normal')

if __name__ == '__main__':
    main()