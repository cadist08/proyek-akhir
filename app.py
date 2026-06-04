import streamlit as st
from engine import GovernmentChatbot

st.set_page_config(
    page_title="Chatbot Layanan Publik",
    page_icon="🏛️",
    layout="wide"
)

st.markdown("""
<style>
.main-title{
    text-align:center;
    color:#1f77b4;
}
.card{
    background:#f8f9fa;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 class='main-title'>🏛️ Chatbot Layanan Publik Indonesia</h1>",
    unsafe_allow_html=True
)

st.write("Sistem Informasi Pemerintahan Berbasis Finite State Machine (FSM)")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🪪 KTP")
    st.info("👨‍👩‍👧‍👦 KK")

with col2:
    st.info("📄 Akta Kelahiran")
    st.info("🚗 SIM")

with col3:
    st.info("🛂 Paspor")
    st.info("🏥 BPJS")

st.divider()

if "bot" not in st.session_state:
    st.session_state.bot = GovernmentChatbot()

if "messages" not in st.session_state:

    st.session_state.messages = []

    welcome = st.session_state.bot.process("start")

    st.session_state.messages.append({
        "role": "assistant",
        "content": welcome
    })

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Masukkan pilihan layanan...")

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

with st.sidebar:

    st.header("Tentang Sistem")

    st.write("""
    Chatbot ini menyediakan informasi:

    • KTP
    • KK
    • Akta Kelahiran
    • SIM
    • Paspor
    • BPJS
    • Pajak
    • Pengaduan
    """)

    st.divider()

    st.write("State FSM")

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
""")