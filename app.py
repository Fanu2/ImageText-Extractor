import streamlit as st
from PIL import Image
import pytesseract

# 🎯 App title and description
st.set_page_config(page_title="Tesseract OCR App", layout="centered")
st.title("📝 Tesseract OCR Text Recognition")
st.markdown("Upload an image to extract text using Tesseract OCR.")

# 📤 Image upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        # 🖼️ Load and display image
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # 🔍 OCR
        with st.spinner("Running OCR..."):
            extracted_text = pytesseract.image_to_string(image)

        # 📄 Display results
        if extracted_text.strip():
            st.subheader("📌 Extracted Text:")
            st.text_area("Text Output", extracted_text, height=300)
        else:
            st.warning("No text found in the image.")

    except Exception as e:
        st.error(f"⚠️ OCR failed: {e}")
else:
    st.info("Please upload an image to begin.")
