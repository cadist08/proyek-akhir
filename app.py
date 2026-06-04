import streamlit as st
from engine import GovernmentChatbot

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Portal Layanan Publik Digital",
    page_icon="🏛️",
    layout="wide"
)

# =========================
# CSS CUSTOM
# =========================
st.markdown("""
<style>

.stApp{
    background-color:#f4f7fc;
}

.hero{
    background: linear-gradient(135deg,#0f172a,#1e40af,#2563eb);
    padding:40px;
    border-radius:20px;
    color:white;
    text-align:center;
    box-shadow:0 4px 20px rgba(0,0,0,0.2);
    margin-bottom:25px;
}

.hero h1{
    font-size:42px;
    margin-bottom:10px;
}

.hero p{
    font-size:18px;
}

.service-card{
    background:white;
    border-radius:15px;
    padding:20px;
    text-align:center;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
    margin-bottom:10px;
}

.footer{
    text-align:center;
    color:#64748b;
    margin-top:30px;
    padding:15px;
}

[data-testid="stSidebar"]{
    background-color:#ffffff;
}

[data-testid="stChatMessage"]{
    border-radius:15px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================
st.markdown("""
<div class="hero">
    <h1>🏛️ Portal Layanan Publik Digital</h1>
    <p>
        Sistem Informasi Pelayanan Administrasi Berbasis
        Finite State Machine (FSM)
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# INISIALISASI BOT
# =========================
if "bot" not in st.session_state:
    st.session_state.bot = GovernmentChatbot()

if "messages" not in st.session_state:

    st.session_state.messages = []

    welcome = st.session_state.bot.process("start")

    st.session_state.messages.append({
        "role": "assistant",
        "content": welcome
    })

# =========================
# SIDEBAR
# =========================
with st.sidebar:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/9f/Coat_of_arms_of_Indonesia_Garuda_Pancasila.svg",
        width=120
    )

    st.header("📋 Layanan")

    st.write("""
    🪪 KTP

    👨‍👩‍👧‍👦 KK

    📄 Akta Kelahiran

    🚗 SIM

    🛂 Paspor

    🏥 BPJS

    💰 Pajak

    📢 Pengaduan
    """)

    st.divider()

    st.header("📊 Statistik")

    st.metric("Jumlah Layanan", "8")
    st.metric("State FSM", "10")
    st.metric("Status Sistem", "Aktif")

    st.divider()

    st.header("🔄 Reset Chat")

    if st.button("Reset Percakapan"):

        st.session_state.bot = GovernmentChatbot()

        st.session_state.messages = []

        welcome = st.session_state.bot.process("start")

        st.session_state.messages.append({
            "role": "assistant",
            "content": welcome
        })

        st.rerun()

    st.divider()

    st.header("📌 Diagram FSM")

    st.code("""
START
   ↓
 MENU
 ├── KTP
 ├── KK
 ├── AKTA
 ├── SIM
 ├── PASPOR
 ├── BPJS
 ├── PAJAK
 ├── PENGADUAN
 └── EXIT
""")

# =========================
# KARTU LAYANAN
# =========================
st.subheader("📌 Layanan Tersedia")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="service-card">
        <h3>🪪 KTP</h3>
        <p>Kartu Tanda Penduduk</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <h3>👨‍👩‍👧‍👦 KK</h3>
        <p>Kartu Keluarga</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="service-card">
        <h3>🚗 SIM</h3>
        <p>Surat Izin Mengemudi</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="service-card">
        <h3>🏥 BPJS</h3>
        <p>Layanan Kesehatan</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# TOMBOL CEPAT
# =========================
st.subheader("⚡ Akses Cepat")

c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("🪪 Informasi KTP"):

        st.session_state.messages.append(
            {"role": "user", "content": "1"}
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": st.session_state.bot.process("1")
            }
        )

        st.rerun()

with c2:
    if st.button("👨‍👩‍👧‍👦 Informasi KK"):

        st.session_state.messages.append(
            {"role": "user", "content": "2"}
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": st.session_state.bot.process("2")
            }
        )

        st.rerun()

with c3:
    if st.button("🚗 Informasi SIM"):

        st.session_state.messages.append(
            {"role": "user", "content": "4"}
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": st.session_state.bot.process("4")
            }
        )

        st.rerun()

with c4:
    if st.button("🏥 Informasi BPJS"):

        st.session_state.messages.append(
            {"role": "user", "content": "6"}
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": st.session_state.bot.process("6")
            }
        )

        st.rerun()

st.divider()

# =========================
# CHAT AREA
# =========================
st.subheader("💬 Chatbot Layanan Publik")

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input(
    "Ketik angka menu atau tulis pengaduan..."
)

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

# =========================
# FOOTER
# =========================
st.markdown("""
<hr>
<div class="footer">
    <b>🏛️ Smart Public Service Chatbot</b><br>
    Sistem Informasi Layanan Publik Berbasis FSM<br>
    © 2026
</div>
""", unsafe_allow_html=True)