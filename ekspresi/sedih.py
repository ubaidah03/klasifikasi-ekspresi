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
    set_background("assets/bg_sedih.png")  # Ganti dengan background khusus sedih jika ada
    load_css("style/style.css")  # Load CSS

    # ==== Tombol Kembali ke Beranda (dipindahkan ke atas) ====
    if st.button("← Kembali ke Beranda"):
        st.session_state.current_page = 'beranda'
        st.session_state.selected_expression_param = None
        st.rerun()

    st.title("Ekspresi: Sedih")

    # ==== Load Gambar ====
    image_path = Path("assets/sedih.jpg")
    if image_path.exists():
        image = Image.open(image_path)
        st.image(image, caption="Contoh ekspresi sedih", width=400)
    else:
        st.warning("Gambar ekspresi sedih tidak ditemukan.")

    # ==== Konten Markdown ====
    st.markdown("""
    ## Karakteristik Ekspresi Sedih

    Ekspresi sedih biasanya ditandai oleh beberapa ciri fisik berikut:

    - Alis mengerucut ke atas
    - Kulit di bawah alis membentuk segitiga dengan ujung dalamnya naik
    - Sudut bibir tertarik ke bawah
    - Kelopak mata atas terkulai
                
    Ekspresi ini biasanya muncul saat seseorang merasakan kesedihan atau kehilangan.

    ---

    ### Contoh Situasi
    - Kehilangan orang yang dicintai
    - Gagal meraih harapan atau impian
    - Merasakan empati terhadap penderitaan orang lain
    - Mengalami putus asa karena kehilangan harapan
    - Menghadapi perpisahan dengan orang yang berarti

    ---

    ### Catatan Tambahan
    Ekspresi sedih merupakan respons alami terhadap kehilangan dan kekecewaan, dan 
    dapat membantu seseorang memproses perasaan tersebut serta mendapatkan dukungan sosial.
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