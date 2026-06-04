import streamlit as st
from engine import GovernmentChatbot

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Layanan Publik Digital",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS & JAVASCRIPT ---
st.markdown("""
<style>
    /* Import Font Poppins */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Reset & Base Style */
    .stApp {
        font-family: 'Poppins', sans-serif;
        background-color: #f0f2f6;
    }

    /* --- HEADER HERO SECTION --- */
    .hero-section {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        padding: 20px 30px;
        border-radius: 0px 0px 20px 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    .hero-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .hero-subtitle {
        font-size: 14px;
        opacity: 0.9;
        font-weight: 300;
    }

    /* --- SIDEBAR --- */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }
    .sidebar-menu-item {
        padding: 10px 15px;
        margin-bottom: 5px;
        border-radius: 8px;
        color: #4b5563;
        transition: 0.3s;
    }
    .sidebar-menu-item:hover {
        background-color: #eff6ff;
        color: #1e40af;
        font-weight: 500;
    }

    /* --- CHAT CONTAINER --- */
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
        padding-bottom: 80px;
    }

    /* Chat Bubbles */
    .chat-bubble {
        padding: 12px 18px;
        border-radius: 18px;
        font-size: 15px;
        line-height: 1.5;
        max-width: 80%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 10px;
        display: inline-block;
        white-space: pre-wrap;
    }

    /* User Message */
    .user-msg {
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        color: white;
        float: right;
        clear: both;
        border-bottom-right-radius: 4px;
        text-align: right;
    }

    /* Bot Message */
    .bot-msg {
        background: white;
        color: #1f2937;
        float: left;
        clear: both;
        border-bottom-left-radius: 4px;
        border: 1px solid #e5e7eb;
    }

    /* Clearing float */
    .clear-fix {
        clear: both;
        content: "";
        display: table;
    }

    /* --- QUICK BUTTONS --- */
    .quick-btn-container {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
        flex-wrap: wrap;
    }
    .stButton>button {
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        background: white;
        color: #374151;
        transition: all 0.3s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        font-weight: 500;
    }
    .stButton>button:hover {
        border-color: #2563eb;
        color: #2563eb;
        background: #eff6ff;
        transform: translateY(-2px);
    }

    /* --- CHAT INPUT --- */
    .stTextInput>div>div>input {
        border-radius: 20px;
        padding: 10px 20px;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
    }

    /* Footer */
    .footer-custom {
        text-align: center;
        color: #9ca3af;
        font-size: 12px;
        margin-top: 30px;
    }
</style>

<script>
    // Auto-scroll to bottom of chat
    window.scrollTo(0, document.body.scrollHeight);
</script>
""", unsafe_allow_html=True)

# --- FUNGSI RENDER CHAT ---
def render_chat_message(role, content):
    if role == "user":
        st.markdown(f'<div class="chat-bubble user-msg">{content}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble bot-msg">{content}</div>', unsafe_allow_html=True)
    st.markdown('<div class="clear-fix"></div>', unsafe_allow_html=True)

# --- INIT SESSION STATE ---
if "bot" not in st.session_state:
    st.session_state.bot = GovernmentChatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []
    welcome = st.session_state.bot.process("start")
    st.session_state.messages.append({
        "role": "assistant",
        "content": welcome
    })

# --- LAYOUT UTAMA ---
# 1. Hero Header
st.markdown("""
<div class="hero-section">
    <div class="hero-title">🏛️ Smart Public Service</div>
    <div class="hero-subtitle">Sistem Informasi Layanan Publik Berbasis AI</div>
</div>
""", unsafe_allow_html=True)

# Kolom Utama: Main Chat (2/3) dan Sidebar Info (1/3)
col_main, col_side = st.columns([3, 1])

with col_side:
    st.markdown("### 📋 Menu Layanan")
    st.markdown("""
    <div style='text-align: left; line-height: 1.8;'>
    🪪 <b>KTP</b><br>
    👨‍👩‍👧 <b>Kartu Keluarga</b><br>
    📜 <b>Akta Kelahiran</b><br>
    🚗 <b>SIM</b><br>
    🛂 <b>Paspor</b><br>
    🏥 <b>BPJS</b><br>
    💰 <b>Pajak</b><br>
    📢 <b>Pengaduan</b>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    if st.button("🔄 Reset Percakapan"):
        st.session_state.bot = GovernmentChatbot()
        st.session_state.messages = []
        welcome = st.session_state.bot.process("start")
        st.session_state.messages.append({
            "role": "assistant",
            "content": welcome
        })
        st.rerun()

    st.markdown("### 💡 Tips")
    st.info("Ketik angka menu (contoh: 1) untuk memilih layanan. Ketik 0 untuk kembali ke menu utama.")

with col_main:
    # Quick Actions Buttons (Above Chat)
    st.markdown("### ⚡ Layanan Cepat")
    c1, c2, c3, c4 = st.columns(4)
    services = [
        ("1", "🪪 KTP", c1),
        ("2", "👨‍👩‍👧 KK", c2),
        ("4", "🚗 SIM", c3),
        ("6", "🏥 BPJS", c4)
    ]

    for code, label, col in services:
        with col:
            if st.button(label, key=f"btn_{code}"):
                st.session_state.messages.append({"role": "user", "content": code})
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": st.session_state.bot.process(code)
                })
                st.rerun()

    st.markdown("---")

    # Chat Display Area
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages:
            render_chat_message(msg["role"], msg["content"])

    # Input Area
    prompt = st.chat_input("Tulis pesan atau nomor menu...")
    
    if prompt:
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        response = st.session_state.bot.process(prompt)
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
        st.rerun()

# Footer
st.markdown('<div class="footer-custom">© 2026 Smart Public Service Chatbot - Powered by Finite State Machine</div>', unsafe_allow_html=True)