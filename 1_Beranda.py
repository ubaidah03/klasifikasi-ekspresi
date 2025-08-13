import streamlit as st
from util import image_to_base64, set_background
from pathlib import Path
from ekspresi import netral, senang, sedih, marah, takut, terkejut, jijik

# ==== Konfigurasi Halaman ====
st.set_page_config(
    page_title="Klasifikasi Ekspresi Wajah",
    page_icon="assets/logo_ekspresi.png",  # Path ke file PNG
    layout="wide"
)

# ==== Load CSS sebagai string ====
def load_css(file_path):
    """Loads a CSS file and injects it into the Streamlit app."""
    try:
        with open(file_path) as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"CSS file not found: {file_path}. Please check the path.")
        return ""

css_string = load_css("style/style.css")
if css_string:
    st.markdown(f"<style>{css_string}</style>", unsafe_allow_html=True)

# ==== Routing ekspresi ====
ekspresi_valid = {
    "netral": netral,
    "senang": senang,
    "sedih": sedih,
    "marah": marah,
    "takut": takut,
    "terkejut": terkejut,
    "jijik": jijik
}

# --- Inisialisasi session_state untuk navigasi ---
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'beranda'
if 'selected_expression_param' not in st.session_state:
    st.session_state.selected_expression_param = None

# Cek query parameter URL untuk deep linking
query_params = st.query_params
ekspresi_param_url = query_params.get("ekspresi", [""])[0].strip().lower()

if ekspresi_param_url and ekspresi_param_url in ekspresi_valid:
    st.session_state.current_page = 'detail'
    st.session_state.selected_expression_param = ekspresi_param_url
    
# Logika navigasi utama
# Penting: Ini harus dieksekusi sebelum konten beranda ditampilkan
if st.session_state.current_page == 'detail':
    if st.session_state.selected_expression_param and st.session_state.selected_expression_param in ekspresi_valid:
        # Panggil fungsi tampilkan_halaman dari modul ekspresi yang sesuai
        ekspresi_valid[st.session_state.selected_expression_param].tampilkan_halaman()
    else:
        st.warning("Invalid or missing expression parameter. Returning to home page.")
        st.session_state.current_page = 'beranda'
        st.session_state.selected_expression_param = None # Reset
        st.rerun() # Kembali ke beranda jika param tidak valid atau hilang
    st.stop() # Hentikan eksekusi kode di bawah jika sudah di halaman detail

# ==== Set Background (hanya akan dieksekusi jika current_page adalah 'beranda') ====
set_background('assets/background.png')

# ==== Header dengan judul dan gambar di samping ====
st.markdown("<br>", unsafe_allow_html=True) # Jeda sedikit
col1, col2 = st.columns([5, 4])

with col1:
    st.title("WEBSITE KLASIFIKASI EKSPRESI WAJAH")
    st.markdown(
        """
        Selamat datang! Platform ini dirancang khusus untuk membantu Anda mengenali 
        dan memahami ekspresi wajah secara otomatis menggunakan teknologi AI (*Artificial Intelligence*). 
        Silakan pilih menu di sidebar untuk memulai proses klasifikasi ekspresi wajah atau jelajahi berbagai 
        jenis ekspresi yang berada di bawah ini:
        """
    )

with col2:
    logo_path = "assets/logo_home.png"
    if Path(logo_path).exists():
        st.image(logo_path, width=500)
    else:
        st.warning(f"Logo image '{logo_path}' not found. Please ensure it's in the 'assets' folder.")

st.markdown("---") # Garis pemisah
st.markdown("<h2 style='text-align: center; color: #4b3b97;'>Jelajahi Berbagai Ekspresi</h2>", unsafe_allow_html=True)

st.markdown(
    """
    <p style='text-align: center; font-size: 17px; color: #444;'>
        Wajah adalah bagian tubuh yang dapat mencerminkan emosi seseorang melalui ekspresi yang ditampilkan. 
        Ekspresi merupakan salah satu komunikasi secara nonverbal dengan menunjukkan emosi dari wajah. 
        Ekspresi terdiri dari berbagai macam, seperti senang, sedih, marah, jijik, takut, terkejut, maupun netral.
        Berikut adalah beberapa ekspresi wajah yang umum ditemui. Klik salah satu untuk mempelajari lebih lanjut.
    </p>
    """,
    unsafe_allow_html=True
)


# ==== Load gambar dengan base64 ====
def safe_load_image(path):
    """Loads an image and converts it to base64, with error handling."""
    try:
        return image_to_base64(str(Path(path)))
    except FileNotFoundError:
        st.warning(f"Image '{path}' not found. Skipping this image.")
        return ""
    except Exception as e:
        st.warning(f"Error loading image '{path}': {e}. Skipping this image.")
        return ""

# ==== Data Kartu ====
data_ekspresi = [
    {
        "nama": "Netral",
        "deskripsi": "Ekspresi yang menunjukkan ketidakadaan emosi atau ekspresi datar.",
        "gambar": safe_load_image("assets/netral.jpg"),
        "param": "netral"
    },
    {
        "nama": "Senang",
        "deskripsi": "Ekspresi wajah yang menunjukkan rasa senang, bahagia, atau puas.",
        "gambar": safe_load_image("assets/senang.jpg"),
        "param": "senang"
    },
    {
        "nama": "Sedih",
        "deskripsi": "Ekspresi yang menunjukkan kesedihan, kehilangan, atau rasa kecewa.",
        "gambar": safe_load_image("assets/sedih.jpg"),
        "param": "sedih"
    },
    {
        "nama": "Marah",
        "deskripsi": "Ekspresi yang menunjukkan kemarahan, frustrasi, atau ketidaksenangan.",
        "gambar": safe_load_image("assets/marah.jpg"),
        "param": "marah"
    },
    {
        "nama": "Takut",
        "deskripsi": "Ekspresi yang menunjukkan perasaan tertekan atau terancam.",
        "gambar": safe_load_image("assets/takut.jpg"),
        "param": "takut"
    },
    {
        "nama": "Terkejut",
        "deskripsi": "Ekspresi yang muncul sebagai respons terhadap kejadian yang tiba-tiba (tak terduga).",
        "gambar": safe_load_image("assets/terkejut.jpg"),
        "param": "terkejut"
    },
    {
        "nama": "Jijik",
        "deskripsi": "Ekspresi yang menunjukkan rasa tidak suka, muak, atau ketidaksenangan terhadap sesuatu.",
        "gambar": safe_load_image("assets/jijik.jpg"),
        "param": "jijik"
    }
]

# ==== Tampilkan Kartu Ekspresi ====
# Mulai card-container
st.markdown('<div class="card-container">', unsafe_allow_html=True)

cols_per_row = 3 # Tentukan jumlah kolom per baris untuk Streamlit

for i in range(0, len(data_ekspresi), cols_per_row):
    cols = st.columns(cols_per_row)
    for idx, ekspresi in enumerate(data_ekspresi[i:i + cols_per_row]):
        with cols[idx]:
            # === Mulai struktur HTML untuk setiap kartu ===
            card_html = f"""
            <div class="card">
                <div class="card-body">
                    {"<img src='" + ekspresi["gambar"] + "' alt='" + ekspresi["nama"] + "' />" if ekspresi["gambar"] else ""}
                    <h3>{ekspresi['nama']}</h3>
                    <p>{ekspresi['deskripsi']}</p>
                    </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
            # --- Tombol Streamlit untuk interaktivitas ---
            if st.button("Pelajari Selengkapnya", key=f"btn_{ekspresi['param']}"):
                st.session_state.current_page = 'detail'
                st.session_state.selected_expression_param = ekspresi['param']
                st.rerun() # Untuk memicu perpindahan halaman

# Tutup card-container
st.markdown('</div>', unsafe_allow_html=True)

# ==== Footer ==== 
st.markdown(
    """
    <div class="custom-footer">
        <p>© 2025 Klasifikasi Ekspresi Wajah — Dibuat dengan ❤ oleh Ubaidah Luthfiyah Zain</p>
    </div>
    """,
    unsafe_allow_html=True
)