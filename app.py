import streamlit as st
import easyocr
import cv2
import numpy as np
from PIL import Image

# 🎯 App title and description
st.set_page_config(page_title="EasyOCR Text Recognition", layout="centered")
st.title("📝 EasyOCR Text Recognition App")
st.markdown("Upload an image and select a language to extract text using EasyOCR.")

# 🌐 Language selection
languages = {
    "English": "en", "French": "fr", "German": "de", "Spanish": "es",
    "Italian": "it", "Portuguese": "pt", "Chinese": "zh", "Japanese": "ja", "Russian": "ru",
    "Hindi": "hi", "Arabic": "ar", "Bengali": "bn", "Urdu": "ur"
}
selected_language = st.selectbox("Select Language:", list(languages.keys()))
lang_code = languages[selected_language]

# 📤 Image upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        # 🖼️ Load and display image
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # 🔄 Convert to NumPy array
        image_np = np.array(image)

        # 🔍 OCR reader
        with st.spinner("Running OCR..."):
            reader = easyocr.Reader([lang_code], gpu=False)
            result = reader.readtext(image_np)

        # 📄 Display results
        if result:
            st.subheader("📌 Extracted Text:")
            for bbox, text, confidence in result:
                st.markdown(f"- **{text}** (Confidence: `{confidence:.2f}`)")
        else:
            st.warning("No text found in the image.")

    except Exception as e:
        st.error(f"⚠️ OCR failed: {e}")
else:
    st.info("Please upload an image to begin.")
