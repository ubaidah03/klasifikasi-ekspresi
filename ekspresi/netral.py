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
    set_background("assets/bg_netral.png")
    load_css("style/style.css")  # Load CSS
    
    # ==== Tombol Kembali ke Beranda (dipindahkan ke atas) ====
    if st.button("← Kembali ke Beranda"):
        st.session_state.current_page = 'beranda'
        st.session_state.selected_expression_param = None
        st.rerun()
        
    st.title("Ekspresi: Netral")

    # ==== Load Gambar ====
    image_path = Path("assets/netral.jpg")
    if image_path.exists():
        image = Image.open(image_path)
        st.image(image, caption="Contoh ekspresi netral", width=400)
    else:
        st.warning("Gambar ekspresi netral tidak ditemukan.")

    # ==== Konten Markdown ====
    st.markdown(
        """         
        <div class='custom-text'>
        
        ### Karakteristik Ekspresi Netral

        Ekspresi netral biasanya ditandai oleh beberapa ciri fisik seperti berikut:

        - Otot wajah dalam kondisi rileks
        - Alis dan mata dalam posisi normal tanpa ketegangan
        - Bibir tertutup tanpa ekspresi (tidak tersenyum atau mengerut)
        - Rahang tidak menegang

        Ekspresi ini sering muncul ketika seseorang tidak sedang mengalami emosi tertentu atau dalam keadaan fokus dan tenang.

        ---

        ### Contoh Situasi
        - Tidak sedang merasakan emosi yang kuat
        - Dalam keadaan fokus saat bekerja atau berpikir
        - Saat berpikir atau berkonsentrasi

        ---

        ### Catatan Tambahan
        Ekspresi netral mencerminkan keadaan wajah yang alami dan rileks, seringkali sulit untuk menilai perasaan seseorang 
        hanya dari ekspresi ini karena tidak ada tanda emosional yang jelas terlihat.
        """,
        unsafe_allow_html=True
        )

    # ==== Footer (dipindahkan ke dalam fungsi) ====
    st.markdown(
        """
        <div class="custom-footer">
            <p>© 2025 Klasifikasi Ekspresi Wajah — Dibuat dengan ❤ oleh Ubaidah Luthfiyah Zain</p>
        </div>
        """,
        unsafe_allow_html=True
    )
