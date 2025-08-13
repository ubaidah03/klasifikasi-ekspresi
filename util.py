import base64
import streamlit as st
from PIL import ImageOps, Image
import numpy as np
import os
import mimetypes
import base64

def set_background(image_file):
    if not os.path.exists(image_file):
        st.error(f"Background '{image_file}' tidak ditemukan.")
        return
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64_encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

def classify(image, model, class_names):
    if not isinstance(image, Image.Image):
        raise ValueError("Input harus berupa objek PIL.Image.")
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction[0])
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    return class_name, confidence_score

def image_to_base64(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Gambar '{image_path}' tidak ditemukan.")
    mime_type, _ = mimetypes.guess_type(image_path)
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return f"data:{mime_type};base64,{encoded}"
