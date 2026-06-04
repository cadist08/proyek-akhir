import streamlit as st
from engine import GovernmentChatbot

st.set_page_config(
    page_title="Chatbot Layanan Publik",
    page_icon="🏛️",
    layout="wide"
)

st.markdown("""
<style>

.main-header{
    text-align:center;
    padding:20px;
}

.hero{
    background: linear-gradient(135deg,#1e40af,#2563eb);
    color:white;
    padding:30px;
    border-radius:15px;
    text-align:center;
    margin-bottom:20px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🏛️ Smart Public Service Chatbot</h1>
    <p>Sistem Informasi Layanan Publik Berbasis Finite State Machine (FSM)</p>
</div>
""", unsafe_allow_html=True)

if "bot" not in st.session_state:
    st.session_state.bot = GovernmentChatbot()

if "messages" not in st.session_state:

    st.session_state.messages = []

    welcome = st.session_state.bot.process("start")

    st.session_state.messages.append({
        "role": "assistant",
        "content": welcome
    })

with st.sidebar:

    st.header("📋 Layanan")

    st.write("""
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

    st.header("🔄 Reset")

    if st.button("Reset Chat"):

        st.session_state.bot = GovernmentChatbot()

        st.session_state.messages = []

        welcome = st.session_state.bot.process("start")

        st.session_state.messages.append({
            "role": "assistant",
            "content": welcome
        })

        st.rerun()

    st.divider()

    st.header("📊 Diagram FSM")

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

st.subheader("⚡ Pilih Layanan Cepat")

c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("🪪 KTP"):
        st.session_state.messages.append(
            {"role": "user", "content": "1"}
        )
        st.session_state.messages.append(
            {"role": "assistant",
             "content": st.session_state.bot.process("1")}
        )
        st.rerun()

with c2:
    if st.button("👨‍👩‍👧‍👦 KK"):
        st.session_state.messages.append(
            {"role": "user", "content": "2"}
        )
        st.session_state.messages.append(
            {"role": "assistant",
             "content": st.session_state.bot.process("2")}
        )
        st.rerun()

with c3:
    if st.button("🚗 SIM"):
        st.session_state.messages.append(
            {"role": "user", "content": "4"}
        )
        st.session_state.messages.append(
            {"role": "assistant",
             "content": st.session_state.bot.process("4")}
        )
        st.rerun()

with c4:
    if st.button("🏥 BPJS"):
        st.session_state.messages.append(
            {"role": "user", "content": "6"}
        )
        st.session_state.messages.append(
            {"role": "assistant",
             "content": st.session_state.bot.process("6")}
        )
        st.rerun()

st.divider()

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

st.markdown(
    "<div class='footer'>© 2026 Smart Public Service Chatbot - FSM Project</div>",
    unsafe_allow_html=True
)