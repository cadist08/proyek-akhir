import streamlit as st

st.set_page_config(
    page_title="Chatbot Layanan Publik",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Chatbot Layanan Publik")
st.write("Selamat datang di layanan informasi pemerintahan.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ketik pertanyaan...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    if "ktp" in prompt.lower():
        response = """
        Persyaratan KTP:

        - Berusia 17 tahun
        - Membawa KK
        - Datang ke Disdukcapil
        """

    elif "kk" in prompt.lower():
        response = """
        Persyaratan KK:

        - Surat Pengantar RT/RW
        - Buku Nikah
        """

    elif "paspor" in prompt.lower():
        response = """
        Persyaratan Paspor:

        - KTP
        - KK
        - Akta Kelahiran
        """

    elif "bpjs" in prompt.lower():
        response = """
        Persyaratan BPJS:

        - KTP
        - KK
        - Nomor HP Aktif
        """

    elif "sim" in prompt.lower():
        response = """
        Persyaratan SIM:

        - KTP
        - Surat Kesehatan
        - Tes Teori dan Praktik
        """

    else:
        response = """
        Maaf, layanan belum tersedia.

        Kata kunci yang tersedia:
        - KTP
        - KK
        - SIM
        - Paspor
        - BPJS
        """

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )