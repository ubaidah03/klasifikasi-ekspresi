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
    set_background("assets/bg_marah.png")
    load_css("style/style.css")  # Load CSS

    # ==== Tombol Kembali ke Beranda ====
    if st.button("← Kembali ke Beranda"):
        st.session_state.current_page = 'beranda'
        st.session_state.selected_expression_param = None
        st.rerun()

    st.title("Ekspresi: Marah")

    # ==== Load Gambar ====
    image_path = Path("assets/marah.jpg")
    if image_path.exists():
        image = Image.open(image_path)
        st.image(image, caption="Contoh ekspresi marah", width=400)
    else:
        st.warning("Gambar ekspresi marah tidak ditemukan.")

    # ==== Konten Markdown ====
    st.markdown("""
    ## Karakteristik Ekspresi Marah

    Ekspresi marah biasanya ditandai oleh beberapa ciri fisik berikut:

    - Sisi alis bagian dalam menyatu dan condong ke bawah
    - Bibir tampak menyempit
    - Kelopak mata bagian bawah menegang
    - Mata menatap dengan tajam

    Ekspresi ini biasanya muncul saat seseorang merasakan kemarahan atau frustrasi.

    ---

    ### Contoh Situasi
    - Hasil yang diperoleh tidak sesuai rencana
    - Merasa direndahkan atau dihina
    - Mengalami frustrasi
    - Merasa keselamatannya terancam
    - Mendapatkan perlakuan yang tidak semestinya
    - Terpaksa melakukan sesuatu di luar kehendaknya

    ---

    ### Catatan Tambahan
    Ekspresi marah sering menjadi sinyal bahwa seseorang 
    sedang menghadapi tekanan atau konflik, dan penting untuk mengenali serta mengelola emosi ini secara sehat agar tidak berdampak negatif.
    """)

    # ==== Footer (dipindahkan ke dalam fungsi) ====
    st.markdown(
        """
        <div class="custom-footer">
            <p>© 2025 Klasifikasi Ekspresi Wajah — Dibuat dengan ❤ oleh Ubaidah Luthfiyah Zain</p>
        </div>
        """,
        unsafe_allow_html=True
    )