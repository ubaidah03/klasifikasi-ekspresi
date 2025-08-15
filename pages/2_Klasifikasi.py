import streamlit as st
from keras.models import load_model
from PIL import Image
from util import classify, set_background
import os
from util import image_to_base64

# ===== Konfigurasi Halaman =====
st.set_page_config(
    page_title="Klasifikasi Ekspresi Wajah",
    page_icon="assets/logo_ekspresi.png",  # Path ke file PNG
    layout="wide"
)

# set background
set_background('assets/background.png')

def load_local_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_local_css("style/style.css")  # Pastikan path-nya sesuai


# ===== Header =====
st.markdown("""
<div class="overlay-box">
    <h1 class="overlay-title"> Klasifikasi Ekspresi Wajah</h1>
    <div class="overlay-subtitle">
        Unggah gambar wajah atau gunakan kamera, lalu biarkan AI mendeteksi ekspresinya.
    </div>
</div>
""", unsafe_allow_html=True)

# ===== Cek dan Load Model =====
model_path = "model/model_ekspresi.h5"
label_path = "model/labels.txt"

if not os.path.exists(model_path) or not os.path.exists(label_path):
    st.error("❌ File model atau label tidak ditemukan. Pastikan berada di folder `model/`.")
    st.stop()

@st.cache_resource
def load_my_model():
    return load_model(model_path)

model = load_my_model()

# ===== Load Label Kelas =====
with open(label_path, "r") as f:
    class_names = [line.strip().split(' ', 1)[1] for line in f.readlines()]

# ===== Pilih Metode Input =====
option = st.radio("Pilih Metode Input:", ["Upload Gambar", "Kamera"])

# ===== Upload Gambar =====
if option == "Upload Gambar":
    uploaded_file = st.file_uploader("Unggah Gambar", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        if image.mode != "RGB":
            image = image.convert("RGB")

        st.image(image, caption="Gambar yang diunggah", width=300)

        if st.button("Klasifikasi"):
            loading = st.empty()
            loading.markdown('<div class="loading-text">Mendeteksi ekspresi...</div>', unsafe_allow_html=True)


            class_name, confidence_score = classify(image, model, class_names)

            loading.empty()
            st.markdown(f'<div class="result-box">Ekspresi: {class_name}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="accuracy-box">Akurasi: {confidence_score:.2%}</div>', unsafe_allow_html=True)


# ===== Kamera =====
else:
    camera_image = st.camera_input("Ambil Gambar Wajah")
    if camera_image is not None:
        image = Image.open(camera_image)
        if image.mode != "RGB":
            image = image.convert("RGB")

        st.image(image, caption="Gambar dari kamera", width=300)

        if st.button("Klasifikasi"):
            loading = st.empty()
            loading.markdown('<div class="loading-text">Mendeteksi ekspresi...</div>', unsafe_allow_html=True)


            class_name, confidence_score = classify(image, model, class_names)

            loading.empty()
            st.markdown(f'<div class="result-box">Ekspresi: {class_name}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="accuracy-box">Akurasi: {confidence_score:.2%}</div>', unsafe_allow_html=True)

# === Petunjuk langkah-langkah klasifikasi ===
# Dapatkan gambar dalam format base64
img_base64_url = image_to_base64("assets/deteksi.jpg")

# HTML untuk overlay box dengan gambar dan petunjuk
st.markdown(f"""
<div class="overlay-box">
    <h2 style="font-size: 1.5rem;">Cara Menggunakan Klasifikasi Ekspresi Wajah</h2>
    <div style="display: flex; flex-wrap: wrap; gap: 2rem; align-items: center;">
        <div style="flex: 1.5; min-width: 250px; line-height: 2;">
            <p>
                <span style="color: #a36fe4; font-weight: bold;">1️⃣ Langkah 1:</span> 
                <span class="custom-text">Pilih metode input gambar (Upload atau Kamera).</span>
            </p>
            <p>
                <span style="color: #a36fe4; font-weight: bold;">2️⃣ Langkah 2:</span> 
                <span class="custom-text">nggah gambar wajah atau ambil gambar langsung. Hanya bisa mendeteksi satu wajah.</span>
            </p>
            <p>
                <span style="color: #a36fe4; font-weight: bold;">3️⃣ Langkah 3:</span> 
                <span class="custom-text">Klik tombol <b>Klasifikasi</b> untuk mendeteksi ekspresi.</span>
            </p>
            <p>
                <span style="color: #a36fe4; font-weight: bold;">4️⃣ Langkah 4:</span> 
                <span class="custom-text">Lihat hasil ekspresi dan tingkat akurasinya.</span>
            </p>
        </div>
        <div style="flex: 1; min-width: 200px;">
            <img src="{img_base64_url}" alt="Panduan Gambar" style="max-width: 100%; max-height: 300px; height: auto; border-radius: 6px; object-fit: cover;">
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==== Footer ==== 
st.markdown(
    """
    <div class="custom-footer">
        <p>© 2025 Klasifikasi Ekspresi Wajah — Dibuat dengan ❤ oleh Ubaidah Luthfiyah Zain</p>
    </div>
    """,
    unsafe_allow_html=True
)
