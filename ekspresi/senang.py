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
    set_background("assets/bg_senang.png")
    load_css("style/style.css")  # Load CSS

    # ==== Tombol Kembali ke Beranda (dipindahkan ke atas) ====
    if st.button("← Kembali ke Beranda"):
        st.session_state.current_page = 'beranda'
        st.session_state.selected_expression_param = None
        st.rerun()
    
    st.title("Ekspresi: Senang")

    # ==== Load Gambar ====
    image_path = Path("assets/senang.jpg")
    if image_path.exists():
        image = Image.open(image_path)
        st.image(image, caption="Contoh ekspresi senang", width=400)
    else:
        st.warning("Gambar ekspresi senang tidak ditemukan.")

    # ==== Konten Markdown ====
    st.markdown("""
    ## Karakteristik Ekspresi Senang

    Ekspresi senang biasanya ditandai oleh beberapa ciri fisik berikut:

    - Otot pipi dan ujung bibir naik
    - Gigi terlihat saat tersenyum
    - Kerutan di antara bagian luar hidung dan mulut
    - Kelopak mata bawah tampak menegang atau berkerut
    - Guratan halus di sudut luar mata

    Ekspresi ini biasanya muncul saat seseorang merasakan kebahagiaan atau kepuasan.

    ---

    ### Contoh Situasi
    - Mencapai tujuan yang diharapkan
    - Memperoleh keuntungan atau keberhasilan
    - Mengingat hal-hal yang menyenangkan
    - Melihat atau mendengar sesuatu yang menyenangkan

    ---

    ### Catatan Tambahan
    Ekspresi senang tidak hanya menunjukkan perasaan positif, tetapi juga dapat memperkuat 
    hubungan sosial melalui komunikasi nonverbal yang menyenangkan dan hangat.
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