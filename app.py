import streamlit as st
from engine import GovernmentChatbot
import time

# Konfigurasi Halaman (Harus diletakkan paling atas)
st.set_page_config(
    page_title="SIPA - Layanan Publik",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk UI yang lebih modern
st.markdown("""
<style>
    /* Menyembunyikan menu default Streamlit untuk tampilan aplikasi native */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Styling Hero Section */
    .hero {
        background: linear-gradient(135deg, #0f172a 0%, #3b82f6 100%);
        color: white;
        padding: 40px 30px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.5);
        animation: fadeIn 1s ease-in-out;
    }
    
    .hero h1 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 2.8rem;
        margin-bottom: 10px;
        font-weight: 800;
        letter-spacing: -1px;
    }
    
    .hero p {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 300;
    }

    /* Footer modern */
    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 60px;
        padding: 20px;
        border-top: 1px solid #e2e8f0;
        font-size: 0.9rem;
    }

    /* Animasi sederhana */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# Banner Hero
st.markdown("""
<div class="hero">
    <h1>🏛️ SIPA Chatbot</h1>
    <p>Sistem Informasi Pelayanan Administrasi Publik Berbasis AI & FSM</p>
</div>
""", unsafe_allow_html=True)

# Inisialisasi Session State
if "bot" not in st.session_state:
    st.session_state.bot = GovernmentChatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []
    welcome = st.session_state.bot.process("start")
    st.session_state.messages.append({
        "role": "assistant",
        "content": welcome
    })

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/8060/8060378.png", width=100) # Bisa diganti logo lokal Anda
    st.title("Pusat Kendali")
    
    st.markdown("### 📋 Daftar Layanan")
    st.info("""
    🪪 **KTP** | 👨‍👩‍👧 **KK** | 📜 **Akta**  
    🚗 **SIM** | 🛂 **Paspor** | 🏥 **BPJS**  
    💰 **Pajak** | 📢 **Pengaduan**
    """)
    
    st.divider()
    
    # Tombol Reset dengan tipe Primary
    st.markdown("### 🔄 Sesi Obrolan")
    if st.button("🗑️ Reset Chatbot", type="primary", use_container_width=True):
        st.session_state.bot = GovernmentChatbot()
        st.session_state.messages = []
        welcome = st.session_state.bot.process("start")
        st.session_state.messages.append({
            "role": "assistant",
            "content": welcome
        })
        st.toast('Berhasil mereset sesi obrolan!', icon='✅')
        time.sleep(0.5)
        st.rerun()

    st.divider()

    # Menyembunyikan FSM dalam expander agar sidebar lebih rapi
    with st.expander("📊 Lihat Diagram FSM Sistem", expanded=False):
        st.code("""
START
 ↓
MENU
 ├─ KTP
 ├─ KK
 ├─ AKTA
 ├─ SIM
 ├─ PASPOR
 ├─ BPJS
 ├─ PAJAK
 ├─ PENGADUAN
 └─ EXIT
        """, language="text")

# --- MAIN CONTENT ---
st.subheader("⚡ Akses Cepat", divider="blue")

# Tombol Cepat yang diperlebar menyesuaikan container
c1, c2, c3, c4 = st.columns(4)

def trigger_quick_action(label, value):
    st.session_state.messages.append({"role": "user", "content": value})
    st.session_state.messages.append({
        "role": "assistant",
        "content": st.session_state.bot.process(value)
    })
    st.rerun()

with c1:
    if st.button("🪪 Layanan KTP", use_container_width=True):
        trigger_quick_action("KTP", "1")
with c2:
    if st.button("👨‍👩‍👧‍👦 Layanan KK", use_container_width=True):
        trigger_quick_action("KK", "2")
with c3:
    if st.button("🚗 Layanan SIM", use_container_width=True):
        trigger_quick_action("SIM", "4")
with c4:
    if st.button("🏥 Layanan BPJS", use_container_width=True):
        trigger_quick_action("BPJS", "6")

st.write("") # Spacer

# Menampilkan Riwayat Obrolan dengan Avatar kustom
for msg in st.session_state.messages:
    # Set avatar berdasarkan role
    avatar_icon = "🏛️" if msg["role"] == "assistant" else "👤"
    
    with st.chat_message(msg["role"], avatar=avatar_icon):
        st.markdown(msg["content"])

# Input Chat
prompt = st.chat_input("Ketik angka menu, pilihan huruf, atau pengaduan Anda di sini...")

if prompt:
    # Tampilkan input user
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Respons Bot
    response = st.session_state.bot.process(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()

# Footer
st.markdown(
    "<div class='footer'>© 2026 SIPA Smart Public Service - Ditenagai oleh Finite State Machine</div>",
    unsafe_allow_html=True
)