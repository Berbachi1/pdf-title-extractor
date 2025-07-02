import streamlit as st
import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image

st.set_page_config(page_title="PDF Title Extractor", layout="centered")
st.title("📄 Extraction de Titre PDF")

uploaded_file = st.file_uploader("📤 Téléverser un fichier PDF", type=["pdf"])

if uploaded_file:
    images = convert_from_bytes(uploaded_file.read(), first_page=1, last_page=1)
    st.image(images[0], caption="🖼️ Aperçu de la première page", use_column_width=True)

    with st.spinner("🔍 Lecture OCR..."):
        text = pytesseract.image_to_string(images[0])
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        title = lines[0] if lines else "Aucun titre détecté."

    st.subheader("📌 Titre détecté :")
    st.write(f"**{title}**")
