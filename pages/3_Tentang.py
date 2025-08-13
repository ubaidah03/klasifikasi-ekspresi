import streamlit as st
from util import set_background
from pathlib import Path

# Fungsi untuk memuat CSS
def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found: {file_path}")

# Konfigurasi halaman (harus di baris atas sebelum komponen lain)
st.set_page_config(
    page_title="Klasifikasi Ekspresi Wajah",
    page_icon="assets/logo_ekspresi.png",  # Path ke file PNG
    layout="wide"
)

# ==== Set Background ====
set_background('assets/background.png')

# ==== Muat css ====
load_css("style/style.css")

# Judul halaman
st.title("Tentang Website")

# Tambahkan gambar
st.image("assets/logo_ekspresi.png", width=250)

# Deskripsi Aplikasi
st.markdown("""
### Klasifikasi Ekspresi Wajah
Aplikasi ini dikembangkan untuk mendeteksi ekspresi wajah manusia menggunakan teknologi kecerdasan buatan (AI).  
Pengguna dapat mengunggah gambar atau menggunakan kamera langsung untuk melihat hasil klasifikasi dari model yang telah dilatih.

Model ini mampu mengenali berbagai ekspresi seperti:
- Senang 
- Sedih   
- Marah  
- Terkejut
- Takut
- Jijik
- Netral
""")

# Tentang Pengembang
st.markdown("""
### Tentang Pengembang
Halo! Saya **Ubaidah Luthfiyah Zain**, pengembang website ini. Saat ini saya menempuh perkuliahan di Universitas Gunadarma
jurusan Informatika.
""")

# Teknologi yang digunakan
st.markdown("""
### Teknologi yang Digunakan
- Python + Streamlit (untuk membuat website)
- Keras / TensorFlow (untuk pelatihan model)  
- PIL & OpenCV (untuk pemrosesan gambar)  
- CSS (untuk tampilan yang modern)
""")

# Kontak
st.markdown("""
### Kontak
Jika Anda memiliki pertanyaan, saran, atau ingin terhubung:
- Email: **zainubaidah@gmail.com**  
- GitHub: [github.com/ubaidah03](https://github.com/ubaidah03)
""")

# ==== Footer ==== 
st.markdown(
    """
    <div class="custom-footer">
        <p>© 2025 Klasifikasi Ekspresi Wajah — Dibuat dengan ❤ oleh Ubaidah Luthfiyah Zain</p>
    </div>
    """,
    unsafe_allow_html=True
)