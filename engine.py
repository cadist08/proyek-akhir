from FSM import State


class GovernmentChatbot:

    def __init__(self):
        self.state = State.START

    def process(self, message):

        msg = message.lower()

        if self.state == State.START:
            self.state = State.MENU

            return """
Selamat datang di Chatbot Layanan Publik Indonesia 🇮🇩

Layanan yang tersedia:

1. KTP
2. KK
3. Akta Kelahiran
4. SIM
5. Paspor
6. BPJS
7. Pajak
8. Pengaduan
9. Keluar

Ketik nomor layanan.
"""

        if self.state == State.MENU:

            if msg == "1":
                return """
Persyaratan KTP:

• Berusia 17 tahun
• Membawa KK
• Datang ke Disdukcapil
"""

            elif msg == "2":
                return """
Persyaratan KK:

• Surat pengantar RT/RW
• Buku Nikah
• Dokumen pendukung
"""

            elif msg == "3":
                return """
Persyaratan Akta Kelahiran:

• Surat kelahiran
• KTP orang tua
• KK
"""

            elif msg == "4":
                return """
Informasi SIM:

• Fotokopi KTP
• Surat kesehatan
• Tes teori dan praktik
"""

            elif msg == "5":
                return """
Informasi Paspor:

• E-KTP
• KK
• Akta Kelahiran
• Daftar melalui aplikasi M-Paspor
"""

            elif msg == "6":
                return """
Informasi BPJS:

• KTP
• KK
• Nomor HP aktif
"""

            elif msg == "7":
                return """
Informasi Pajak:

• NPWP
• EFIN
• Lapor melalui DJP Online
"""

            elif msg == "8":
                self.state = State.PENGADUAN

                return """
Silakan tuliskan pengaduan Anda.
"""

            elif msg == "9":
                self.state = State.EXIT

                return "Terima kasih telah menggunakan layanan kami."

            return "Pilihan tidak tersedia."

        if self.state == State.PENGADUAN:

            self.state = State.MENU

            return f"""
Pengaduan diterima:

'{message}'

Laporan akan diteruskan ke instansi terkait.
"""