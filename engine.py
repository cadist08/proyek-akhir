from FSM import State


class GovernmentChatbot:

    def __init__(self):
        self.state = State.START

    def process(self, message):

        msg = message.lower().strip()

        if self.state == State.START:

            self.state = State.MENU

            return """
Selamat Datang di Chatbot Layanan Publik Indonesia 🇮🇩

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

Ketik angka menu yang diinginkan.
"""

        elif self.state == State.MENU:

            if msg == "1":
                self.state = State.KTP

                return """
Persyaratan Pembuatan KTP:

• Berusia minimal 17 tahun
• Membawa Kartu Keluarga
• Datang ke Disdukcapil setempat

Ketik menu lain untuk melanjutkan.
"""

            elif msg == "2":
                self.state = State.KK

                return """
Persyaratan Pembuatan KK:

• Surat Pengantar RT/RW
• Buku Nikah
• Dokumen pendukung lainnya

Ketik menu lain untuk melanjutkan.
"""

            elif msg == "3":
                self.state = State.AKTA

                return """
Persyaratan Akta Kelahiran:

• Surat Kelahiran
• KTP Orang Tua
• Kartu Keluarga

Ketik menu lain untuk melanjutkan.
"""

            elif msg == "4":
                self.state = State.SIM

                return """
Persyaratan Pembuatan SIM:

• Fotokopi KTP
• Surat Kesehatan
• Lulus Tes Teori dan Praktik

Ketik menu lain untuk melanjutkan.
"""

            elif msg == "5":
                self.state = State.PASPOR

                return """
Persyaratan Paspor:

• E-KTP
• KK
• Akta Kelahiran

Pendaftaran dapat dilakukan melalui aplikasi M-Paspor.

Ketik menu lain untuk melanjutkan.
"""

            elif msg == "6":
                self.state = State.BPJS

                return """
Persyaratan Pendaftaran BPJS:

• KTP
• KK
• Nomor HP Aktif

Ketik menu lain untuk melanjutkan.
"""

            elif msg == "7":
                self.state = State.PAJAK

                return """
Informasi Pajak:

• Memiliki NPWP
• Memiliki EFIN
• Pelaporan melalui DJP Online

Ketik menu lain untuk melanjutkan.
"""

            elif msg == "8":

                self.state = State.PENGADUAN

                return """
Silakan tuliskan pengaduan Anda.
Contoh:

"Jalan rusak di Kecamatan ABC"
"""

            elif msg == "9":

                self.state = State.EXIT

                return "Terima kasih telah menggunakan layanan kami."

            else:

                return """
Pilihan tidak tersedia.

Silakan pilih:

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

        elif self.state == State.PENGADUAN:

            self.state = State.MENU

            return f"""
Pengaduan berhasil diterima:

"{message}"

Laporan akan diteruskan ke instansi terkait.

Silakan pilih layanan kembali:

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
Silakan pilih layanan berikutnya:

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

            return "Program telah selesai."