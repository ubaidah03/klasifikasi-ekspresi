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
    set_background("assets/bg_jijik.png")  # background untuk ekspresi jijik
    load_css("style/style.css")  # Load CSS

    # ==== Tombol Kembali ke Beranda ====
    if st.button("← Kembali ke Beranda"):
        st.session_state.current_page = 'beranda'
        st.session_state.selected_expression_param = None
        st.rerun()
        
    st.title("Ekspresi: Jijik")

    # ==== Load Gambar ====
    image_path = Path("assets/jijik.jpg")
    if image_path.exists():
        image = Image.open(image_path)
        st.image(image, caption="Contoh ekspresi jijik", width=400)
    else:
        st.warning("Gambar ekspresi jijik tidak ditemukan.")

    # ==== Konten Markdown ====
    st.markdown(
        """
        <div class='custom-text'>

        ### Karakteristik Ekspresi Jijik

        Ekspresi jijik biasanya ditandai oleh beberapa ciri fisik berikut:

        - Kelopak mata atas naik
        - Bibir bagian bawah naik
        - Hidung berkerut
        - Pipi naik
        - Bagian bawah kelopak mata membentuk garis

        Ekspresi ini biasanya muncul saat seseorang menghadapi sesuatu yang tidak menyenangkan atau menjijikkan.

        ---

        ### Contoh Situasi
        - Merasakan sesuatu yang tidak enak atau bau busuk
        - Menyentuh benda berminyak atau berlendir yang menimbulkan rasa ingin muntah
        - Melihat sesuatu atau seseorang yang kotor
        - Menyaksikan perilaku yang bertentangan dengan norma, agama, moral, atau kebiasaan sosial

        ---

        ### Catatan Tambahan
        Ekspresi jijik merupakan bentuk perlindungan alami tubuh untuk menghindari hal-hal yang berpotensi membahayakan 
        kesehatan atau moral sosial.

        </div>
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
