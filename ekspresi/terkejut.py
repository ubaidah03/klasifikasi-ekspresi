import streamlit as st
from PIL import Image
from pathlib import Path
from util import set_background

# Fungsi untuk memuat CSS
def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found: {file_path}")
        
def tampilkan_halaman():
    set_background("assets/bg_terkejut.png")  # background khusus ekspresi terkejut
    load_css("style/style.css")  # Load CSS

    # ==== Tombol Kembali ke Beranda (dipindahkan ke atas) ====
    if st.button("← Kembali ke Beranda"):
        st.session_state.current_page = 'beranda'
        st.session_state.selected_expression_param = None
        st.rerun()

    st.title("Ekspresi: Terkejut")

    # ==== Load Gambar ====
    image_path = Path("assets/terkejut.jpg")
    if image_path.exists():
        image = Image.open(image_path)
        st.image(image, caption="Contoh ekspresi terkejut", width=400)
    else:
        st.warning("Gambar ekspresi terkejut tidak ditemukan.")

    # ==== Konten Markdown ====
    st.markdown(
        """
        <div class='custom-text'>
        
        ## Karakteristik Ekspresi Terkejut

        Ekspresi terkejut biasanya ditandai oleh beberapa ciri fisik berikut:

        - Kedua alis naik dan melengkung
        - Dahi membentuk kerutan horizontal
        - Kelopak mata terbuka lebar
        - Rahang bawah terbuka

        Ekspresi ini biasanya muncul sebagai respons terhadap kejadian yang tiba-tiba atau tak terduga.

        ---

        ### Contoh Situasi
        - Mendengar kabar atau informasi yang belum diketahui sebelumnya
        - Mendapat kejutan yang tidak disangka-sangka
        - Mengalami peristiwa tak terduga secara langsung

        ---

        ### Catatan Tambahan
        Ekspresi terkejut membantu seseorang merespons cepat terhadap perubahan lingkungan yang mendadak, 
        mempersiapkan reaksi yang tepat terhadap situasi baru.
        """,
        unsafe_allow_html=True
        )
    
    # ==== Footer ====
    st.markdown(
        """
        <div class="custom-footer">
            <p>© 2025 Klasifikasi Ekspresi Wajah — Dibuat dengan ❤ oleh Ubaidah Luthfiyah Zain</p>
        </div>
        """,
        unsafe_allow_html=True
    )
