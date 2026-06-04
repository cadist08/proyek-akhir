from FSM import State


class GovernmentChatbot:

    def __init__(self):
        self.state = State.START

    def process(self, message):

        msg = message.lower().strip()

        if self.state == State.START:

            self.state = State.MENU

            return """
👋 Selamat Datang di Smart Public Service Chatbot

Silakan pilih layanan:

1. KTP
2. KK
3. Akta Kelahiran
4. SIM
5. Paspor
6. BPJS
7. Pajak
8. Pengaduan
9. Keluar
"""

        elif self.state == State.MENU:

            if msg == "1":
                self.state = State.KTP

                return """
🪪 Persyaratan KTP

• Berusia minimal 17 tahun
• Membawa Kartu Keluarga
• Datang ke Disdukcapil

Ketik apa saja untuk kembali ke menu.
"""

            elif msg == "2":
                self.state = State.KK

                return """
👨‍👩‍👧‍👦 Persyaratan KK

• Surat Pengantar RT/RW
• Buku Nikah
• Dokumen pendukung

Ketik apa saja untuk kembali ke menu.
"""

            elif msg == "3":
                self.state = State.AKTA

                return """
📄 Persyaratan Akta Kelahiran

• Surat Kelahiran
• KTP Orang Tua
• Kartu Keluarga

Ketik apa saja untuk kembali ke menu.
"""

            elif msg == "4":
                self.state = State.SIM

                return """
🚗 Persyaratan SIM

• Fotokopi KTP
• Surat Kesehatan
• Lulus Tes Teori dan Praktik

Ketik apa saja untuk kembali ke menu.
"""

            elif msg == "5":
                self.state = State.PASPOR

                return """
🛂 Persyaratan Paspor

• E-KTP
• Kartu Keluarga
• Akta Kelahiran

Pendaftaran melalui aplikasi M-Paspor.

Ketik apa saja untuk kembali ke menu.
"""

            elif msg == "6":
                self.state = State.BPJS

                return """
🏥 Persyaratan BPJS

• KTP
• KK
• Nomor HP Aktif

Ketik apa saja untuk kembali ke menu.
"""

            elif msg == "7":
                self.state = State.PAJAK

                return """
💰 Informasi Pajak

• Memiliki NPWP
• Memiliki EFIN
• Lapor melalui DJP Online

Ketik apa saja untuk kembali ke menu.
"""

            elif msg == "8":
                self.state = State.PENGADUAN

                return """
📢 Silakan tuliskan pengaduan Anda.

Contoh:
Jalan rusak di Kecamatan ABC
"""

            elif msg == "9":
                self.state = State.EXIT

                return "🙏 Terima kasih telah menggunakan layanan kami."

            else:
                return "Silakan pilih menu 1 sampai 9."

        elif self.state == State.PENGADUAN:

            self.state = State.MENU

            return f"""
✅ Pengaduan berhasil diterima

"{message}"

Terima kasih atas laporan Anda.

Silakan pilih menu kembali.
"""

        elif self.state in [
            State.KTP,
            State.KK,
            State.AKTA,
            State.SIM,
            State.PASPOR,
            State.BPJS,
            State.PAJAK
        ]:

            self.state = State.MENU

            return """
🏠 Kembali ke Menu

1. KTP
2. KK
3. Akta Kelahiran
4. SIM
5. Paspor
6. BPJS
7. Pajak
8. Pengaduan
9. Keluar
"""

        elif self.state == State.EXIT:
            return "Program selesai."