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
    set_background("assets/bg_takut.png")  # background khusus ekspresi takut
    load_css("style/style.css")  # Load CSS

    # ==== Tombol Kembali ke Beranda (dipindahkan ke atas) ====
    if st.button("← Kembali ke Beranda"):
        st.session_state.current_page = 'beranda'
        st.session_state.selected_expression_param = None
        st.rerun()
    
    st.title("Ekspresi: Takut")

    # ==== Load Gambar ====
    image_path = Path("assets/takut.jpg")
    if image_path.exists():
        image = Image.open(image_path)
        st.image(image, caption="Contoh ekspresi takut", width=400)
    else:
        st.warning("Gambar ekspresi takut tidak ditemukan.")

    # ==== Konten Markdown ====
    st.markdown(
        """
        <div class='custom-text'>

        ### Karakteristik Ekspresi Takut

        Ekspresi takut biasanya ditandai oleh beberapa ciri fisik berikut:

        - Alis terangkat naik
        - Dahi berkerut horizontal
        - Mata terbuka lebar
        - Mulut terbuka secara horizontal
        - Kelopak mata menegang

        Ekspresi ini biasanya muncul saat seseorang merasa takut atau terancam.

        ---

        ### Contoh Situasi
        - Menghadapi situasi yang dirasa sulit atau berbahaya
        - Merasa terancam secara verbal atau fisik (misalnya dimarahi, dihukum, dihina)
        - Merasa dikucilkan oleh teman
        - Berada di lingkungan yang dianggap menakutkan

        ---

        ### Catatan Tambahan
        Ekspresi takut berfungsi sebagai respons perlindungan tubuh terhadap bahaya, 
        membantu seseorang untuk bersiap menghadapi ancaman atau melarikan diri.
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

