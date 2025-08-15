import streamlit as st
import easyocr
import cv2
import numpy as np
from PIL import Image

# Set the title of the app
st.title("EasyOCR Text Recognition App")

# Language selection
languages = ["en", "fr", "de", "es", "it", "pt", "zh", "ja", "ru"]  # List more languages as needed
selected_language = st.selectbox("Select Language:", languages)

# Upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert the image to a format suitable for EasyOCR
    image_np = np.array(image)

    # Create an EasyOCR reader instance with the selected language
    reader = easyocr.Reader([selected_language])

    # Perform OCR on the image
    st.write("Recognizing text...")
    result = reader.readtext(image_np)

    # Extract and display recognized text
    if result:
        extracted_text = "\n".join([text[1] for text in result])
        st.subheader("Extracted Text:")
        st.write(extracted_text)
    else:
        st.write("No text found.")
