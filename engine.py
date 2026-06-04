import random
import string
from datetime import datetime, timedelta
from FSM import State


MENU_TEXT = """
📋 **MENU UTAMA**

**📄 Layanan Dokumen**
`1` · 🪪 KTP
`2` · 👨‍👩‍👧 Kartu Keluarga
`3` · 📜 Akta Kelahiran
`4` · 🚗 SIM
`5` · 🛂 Paspor
`6` · 🏥 BPJS Kesehatan
`7` · 💰 Pajak (NPWP/SPT)

**🔧 Layanan Lainnya**
`8` · 📢 Buat Pengaduan
`9` · 🎫 Ambil Nomor Antrian
`10` · 🔍 Cek Status Pengaduan
`11` · ❓ FAQ / Pertanyaan Umum
`12` · 📅 Jadwal Pelayanan
`0` · 🚪 Keluar

"""


class GovernmentChatbot:

    def __init__(self):
        self.state = State.START
        self.antrian_counter = {"KTP": 45, "KK": 23, "AKTA": 12, "SIM": 67, "PASPOR": 8, "BPJS": 34, "PAJAK": 19}
        self.pengaduan_log = {}
        self.pending_kategori = None

    def _generate_nomor(self, prefix="ADU"):
        suffix = ''.join(random.choices(string.digits, k=6))
        return f"{prefix}-{datetime.now().strftime('%d%m%y')}-{suffix}"

    def _generate_antrian(self, jenis):
        self.antrian_counter[jenis] = self.antrian_counter.get(jenis, 0) + 1
        num = self.antrian_counter[jenis]
        prefix_map = {"KTP": "A", "KK": "B", "AKTA": "C", "SIM": "D", "PASPOR": "E", "BPJS": "F", "PAJAK": "G"}
        prefix = prefix_map.get(jenis, "Z")
        waktu_estimasi = datetime.now() + timedelta(minutes=num * 7)
        return f"{prefix}{num:03d}", waktu_estimasi.strftime("%H:%M")

    def process(self, message):
        msg = message.strip()
        msg_lower = msg.lower()

        # START
        if self.state == State.START:
            self.state = State.MENU
            now = datetime.now()
            greeting = "Selamat Pagi" if now.hour < 12 else ("Selamat Siang" if now.hour < 15 else ("Selamat Sore" if now.hour < 18 else "Selamat Malam"))
            return f"""
👋 **{greeting}! Selamat Datang di**
# 🏛️ Portal Layanan Publik Digital
**Pemerintah Kota — Sistem Terpadu Pelayanan Masyarakat**

---
Saya **SIPA** *(Sistem Informasi Pelayanan Administrasi)*, siap membantu Anda mengurus berbagai keperluan administrasi kependudukan.

🕐 Hari ini: **{now.strftime("%A, %d %B %Y · %H:%M")} WIB**
🟢 Status Sistem: **Online & Siap Melayani**

---
{MENU_TEXT}
💡 *Ketik nomor menu untuk memilih layanan*
"""

        # MENU
        elif self.state == State.MENU:

            if msg == "1":
                self.state = State.KTP
                return """
🪪 **LAYANAN KTP ELEKTRONIK**

**Pilih jenis layanan KTP:**

`A` · 📝 Pembuatan KTP Baru (usia 17 tahun)
`B` · 🔄 Perpanjangan / Penggantian KTP
`C` · ❌ KTP Hilang / Rusak
`D` · 📋 Cek Persyaratan Lengkap

`0` · 🔙 Kembali ke Menu
"""

            elif msg == "2":
                self.state = State.KK
                return """
👨‍👩‍👧 **LAYANAN KARTU KELUARGA**

**📋 Persyaratan Umum:**
✅ Surat Pengantar RT → RW → Kelurahan
✅ KTP semua anggota keluarga
✅ Buku Nikah / Akta Perkawinan
✅ Akta Kelahiran anak (jika ada)
✅ Dokumen pendukung lainnya

**📍 Tempat Pengajuan:**
Kantor Kelurahan setempat → Kecamatan → Disdukcapil

**⏱️ Estimasi Waktu:**
• Kelurahan: 1–2 hari kerja
• Kecamatan: 2–3 hari kerja
• Disdukcapil: 3–5 hari kerja

**💡 Tips:**
> Pastikan data yang diisikan sudah benar sebelum diserahkan untuk menghindari revisi

`9` · 🎫 Ambil Antrian KK Sekarang
`0` · 🔙 Kembali ke Menu

Ketik **`0`** untuk menu atau **`9`** untuk ambil antrian.
"""

            elif msg == "3":
                self.state = State.AKTA
                return """
📜 **LAYANAN AKTA KELAHIRAN**

**📋 Persyaratan:**
✅ Surat Keterangan Lahir dari RS/Bidan/Puskesmas
✅ KTP kedua orang tua
✅ Kartu Keluarga
✅ Buku Nikah / Akta Perkawinan orang tua

**⏱️ Estimasi Waktu:** 3–5 hari kerja

**⚠️ Penting:**
> Akta kelahiran wajib dibuat **≤ 60 hari** setelah kelahiran.
> Melewati 60 hari diperlukan penetapan pengadilan.

**🌐 Bisa Online via:**
Aplikasi **Dukcapil Go Digital** atau website resmi Disdukcapil

`0` · 🔙 Kembali ke Menu
"""

            elif msg == "4":
                self.state = State.SIM
                return """
🚗 **LAYANAN SIM (SATLANTAS)**

**Pilih jenis layanan SIM:**

`A` · 🆕 SIM Baru (A / B1 / B2 / C / D)
`B` · 🔄 Perpanjangan SIM
`C` · ❌ SIM Hilang / Rusak
`D` · 🔃 Peningkatan Golongan SIM

`0` · 🔙 Kembali ke Menu
"""

            elif msg == "5":
                self.state = State.PASPOR
                return """
🛂 **LAYANAN PASPOR (IMIGRASI)**

**📋 Persyaratan Dasar:**
✅ E-KTP asli + fotokopi
✅ Kartu Keluarga asli + fotokopi
✅ Akta Kelahiran / Ijazah / Surat Nikah
✅ Materai Rp 10.000 (2 lembar)

**📱 Pendaftaran Wajib via Aplikasi:**
> **M-Paspor** (App Store / Play Store)
> Daftar → Pilih jadwal → Datang ke Imigrasi

**💰 Biaya:**
| Jenis | Tarif |
|-------|-------|
| Paspor Biasa 48 hal | Rp 350.000 |
| Paspor Elektronik | Rp 650.000 |
| Percepatan (+1 hari) | +Rp 1.000.000 |

**⏱️ Proses:** 4 hari kerja (reguler)

`0` · 🔙 Kembali ke Menu
"""

            elif msg == "6":
                self.state = State.BPJS
                return """
🏥 **LAYANAN BPJS KESEHATAN**

**Pilih layanan BPJS:**

`A` · 🆕 Pendaftaran Peserta Baru
`B` · 🔄 Perubahan Data / Pindah Faskes
`C` · 💳 Cek Iuran & Tunggakan
`D` · 🏥 Cari Fasilitas Kesehatan

`0` · 🔙 Kembali ke Menu
"""

            elif msg == "7":
                self.state = State.PAJAK
                return """
💰 **LAYANAN PAJAK (DJP)**

**Pilih layanan pajak:**

`A` · 🪪 Daftar NPWP Baru
`B` · 📊 Lapor SPT Tahunan
`C` · 🔑 Aktivasi EFIN
`D` · ❓ Info Tarif & Ketentuan

`0` · 🔙 Kembali ke Menu
"""

            elif msg == "8":
                self.state = State.PENGADUAN_KATEGORI
                return """
📢 **LAYANAN PENGADUAN MASYARAKAT**

Pilih **kategori pengaduan** Anda:

`A` · 🛣️ Infrastruktur (Jalan, Jembatan, Drainase)
`B` · 🗑️ Kebersihan & Sampah
`C` · 💡 Penerangan Jalan
`D` · 🌊 Banjir & Lingkungan
`E` · 🏥 Layanan Kesehatan
`F` · 🎓 Layanan Pendidikan
`G` · 👮 Keamanan & Ketertiban
`H` · 📋 Layanan Administrasi
`I` · 📝 Lainnya

`0` · 🔙 Kembali ke Menu
"""

            elif msg == "9":
                self.state = State.ANTRIAN_PILIH
                return """
🎫 **AMBIL NOMOR ANTRIAN**

Pilih layanan untuk ambil antrian:

`1` · 🪪 KTP        (Antrean: ~{} orang)
`2` · 👨‍👩‍👧 KK         (Antrean: ~{} orang)
`3` · 📜 Akta        (Antrean: ~{} orang)
`4` · 🚗 SIM         (Antrean: ~{} orang)
`5` · 🛂 Paspor      (Antrean: ~{} orang)
`6` · 🏥 BPJS        (Antrean: ~{} orang)
`7` · 💰 Pajak       (Antrean: ~{} orang)

`0` · 🔙 Kembali ke Menu
""".format(
                    self.antrian_counter["KTP"],
                    self.antrian_counter["KK"],
                    self.antrian_counter["AKTA"],
                    self.antrian_counter["SIM"],
                    self.antrian_counter["PASPOR"],
                    self.antrian_counter["BPJS"],
                    self.antrian_counter["PAJAK"],
                )

            elif msg == "10":
                self.state = State.STATUS
                return """
🔍 **CEK STATUS PENGADUAN**

Masukkan **Nomor Tiket Pengaduan** Anda.

Format: `ADU-DDMMYY-XXXXXX`
Contoh: `ADU-040626-123456`

*Nomor tiket diberikan saat Anda membuat pengaduan.*

`0` · 🔙 Kembali ke Menu
"""

            elif msg == "11":
                self.state = State.FAQ
                return """
❓ **FAQ — PERTANYAAN UMUM**

Pilih topik pertanyaan:

`1` · 🕐 Jam & Hari Operasional Pelayanan
`2` · 💳 Biaya Pembuatan Dokumen
`3` · ⏱️ Berapa Lama Proses Pengurusan?
`4` · 📱 Layanan Online Tersedia
`5` · 🆘 Dokumen Hilang, Apa yang Harus Dilakukan?
`6` · 👶 Persyaratan untuk Anak di Bawah Umur
`7` · 🔄 Cara Mengurus Dokumen Hilang Akibat Bencana

`0` · 🔙 Kembali ke Menu
"""

            elif msg == "12":
                self.state = State.JADWAL
                return self._get_jadwal()

            elif msg == "0":
                self.state = State.EXIT
                return "🙏 **Terima kasih** telah menggunakan Portal Layanan Publik Digital.\n\nSemoga urusan Anda lancar! 🌟"

            else:
                return f"⚠️ Pilihan **\"{msg}\"** tidak tersedia.\n\nSilakan ketik angka **1–12** atau **0** untuk keluar.\n{MENU_TEXT}"

        #  KTP Sub-Menu 
        elif self.state == State.KTP:
            opt = msg.upper()
            if opt == "A":
                resp = """
**🆕 KTP BARU — Persyaratan:**
✅ Berusia minimal **17 tahun** atau sudah menikah
✅ Surat Pengantar RT/RW (beberapa daerah tidak perlu)
✅ Kartu Keluarga asli
✅ Pas foto 3×4 (2 lembar) — *opsional, tergantung daerah*

**📍 Alur Proses:**
1. Datang ke **Kelurahan** → Ambil formulir F-1.01
2. Isi formulir → Bawa ke **Disdukcapil**
3. Perekaman biometrik (sidik jari, retina, tanda tangan)
4. KTP dicetak dalam **1–14 hari kerja**

> 💡 **Gratis!** Tidak ada biaya resmi pembuatan KTP.
"""
            elif opt == "B":
                resp = """
**🔄 PERPANJANGAN / PENGGANTIAN KTP:**
✅ KTP lama yang sudah habis masa berlaku
✅ Kartu Keluarga
✅ Surat Pengantar (jika diperlukan)

> ⚠️ KTP Elektronik berlaku **seumur hidup** — tidak perlu diperpanjang kecuali ada perubahan data.
"""
            elif opt == "C":
                resp = """
**❌ KTP HILANG / RUSAK:**
✅ Surat Keterangan Kehilangan dari **Kepolisian**
✅ Fotokopi KTP (jika ada)
✅ Kartu Keluarga
✅ Surat Pengantar RT/RW

> 📞 Laporkan dulu ke Polsek/Polres terdekat sebelum ke Disdukcapil.
"""
            elif opt == "D":
                resp = """
**📋 PERSYARATAN LENGKAP KTP:**

| Jenis | Dokumen Utama |
|-------|--------------|
| KTP Baru | KK + Surat Pengantar |
| Perpanjangan | KTP Lama + KK |
| Hilang | Laporan Polisi + KK |
| Rusak | KTP Rusak + KK |
| Pindah Domisili | Surat Pindah + KK Baru |
"""
            elif opt == "0":
                self.state = State.MENU
                return MENU_TEXT
            else:
                return "⚠️ Pilih **A**, **B**, **C**, **D**, atau **0** untuk kembali."

            self.state = State.MENU
            return resp + "\n\n`0` · 🔙 Ketik **0** untuk Menu Utama"

        #  SIM Sub-Menu 
        elif self.state == State.SIM:
            opt = msg.upper()
            if opt == "A":
                resp = """
**🆕 SIM BARU — Persyaratan:**
✅ KTP asli + fotokopi
✅ Surat Keterangan Sehat jasmani dari dokter
✅ Surat Keterangan Sehat rohani (psikologi)
✅ Usia minimal: SIM A = 17th | SIM B = 20th | SIM C = 17th

**📋 Tahapan:**
1. Registrasi online di **sim.korlantas.polri.go.id**
2. Datang ke Satpas/Polres sesuai jadwal
3. Tes Teori (40 soal, passing grade 70%)
4. Tes Praktik Mengemudi
5. Foto & Sidik Jari → SIM dicetak

**💰 Biaya PNBP:**
| SIM | Tarif |
|-----|-------|
| SIM A | Rp 120.000 |
| SIM B1/B2 | Rp 120.000 |
| SIM C | Rp 100.000 |
| SIM D | Rp 50.000 |
"""
            elif opt == "B":
                resp = """
**🔄 PERPANJANGAN SIM:**
✅ SIM lama (masih berlaku / habis maks. 1 hari)
✅ KTP asli + fotokopi
✅ Surat Keterangan Sehat dari dokter
✅ Tes psikologi (di lokasi Satpas)

> ⚠️ SIM yang sudah **expired > 1 hari** harus buat baru!

**💰 Biaya:** Sama dengan SIM baru (PNBP)
"""
            elif opt == "C":
                resp = """
**❌ SIM HILANG / RUSAK:**
✅ Surat Keterangan Kehilangan dari Kepolisian
✅ KTP asli + fotokopi
✅ Surat Keterangan Sehat

> Prosesnya sama dengan perpanjangan SIM.
"""
            elif opt == "D":
                resp = """
**🔃 PENINGKATAN GOLONGAN SIM:**

| Dari | Ke | Syarat Usia |
|------|-----|------------|
| SIM A | SIM B1 | Min. 20 tahun |
| SIM B1 | SIM B2 | Min. 21 tahun |
| SIM C | SIM C1 | Min. 18 tahun |

✅ SIM lama aktif (min. 12 bulan)
✅ Tes teori & praktik ulang untuk golongan baru
"""
            elif opt == "0":
                self.state = State.MENU
                return MENU_TEXT
            else:
                return "⚠️ Pilih **A**, **B**, **C**, **D**, atau **0** untuk kembali."

            self.state = State.MENU
            return resp + "\n\n`0` · 🔙 Ketik **0** untuk Menu Utama"

        #  BPJS Sub-Menu 
        elif self.state == State.BPJS:
            opt = msg.upper()
            if opt == "A":
                resp = """
**🆕 PENDAFTARAN BPJS KESEHATAN BARU:**
✅ KTP / NIK
✅ Kartu Keluarga
✅ Nomor HP aktif
✅ Nomor Rekening Bank (untuk autodebet)

**Cara Daftar:**
1. 🌐 Online: **bpjs-kesehatan.go.id** atau **Aplikasi Mobile JKN**
2. 🏥 Datang langsung ke kantor BPJS terdekat
3. 🏦 Melalui bank mitra (BRI, BNI, Mandiri, BTN)

**💰 Iuran 2026:**
| Kelas | Iuran/Bulan |
|-------|------------|
| Kelas III | Rp 42.000 |
| Kelas II | Rp 100.000 |
| Kelas I | Rp 150.000 |
"""
            elif opt == "B":
                resp = """
**🔄 PERUBAHAN DATA / PINDAH FASKES:**
✅ KTP dan Kartu BPJS
✅ Menggunakan aplikasi **Mobile JKN**
✅ Atau datang ke kantor BPJS dengan membawa dokumen

> Pindah Faskes bisa dilakukan **1× per bulan** melalui Mobile JKN.
"""
            elif opt == "C":
                resp = """
**💳 CEK IURAN & TUNGGAKAN:**
📱 Via **Aplikasi Mobile JKN** — menu "Info Iuran"
🌐 Via **bpjs-kesehatan.go.id**
📞 Call Center: **1500-400**
💬 WhatsApp: **08118750400**

> Segera lunasi tunggakan agar layanan tidak diblokir.
"""
            elif opt == "D":
                resp = """
**🏥 CARI FASILITAS KESEHATAN:**
📱 Buka **Aplikasi Mobile JKN** → menu "Fasilitas Kesehatan"
🌐 **faskes.bpjs-kesehatan.go.id**

Masukkan kode pos atau nama kota untuk menemukan:
• Puskesmas & Klinik (Faskes Tingkat 1)
• Rumah Sakit (Faskes Tingkat 2 & 3)
"""
            elif opt == "0":
                self.state = State.MENU
                return MENU_TEXT
            else:
                return "⚠️ Pilih **A**, **B**, **C**, **D**, atau **0** untuk kembali."

            self.state = State.MENU
            return resp + "\n\n`0` · 🔙 Ketik **0** untuk Menu Utama"

        #  PAJAK Sub-Menu 
        elif self.state == State.PAJAK:
            opt = msg.upper()
            if opt == "A":
                resp = """
**🪪 DAFTAR NPWP BARU:**
Syarat: WNI dengan penghasilan di atas PTKP (Rp 4.500.000/bln)

**Cara Daftar Online (Disarankan):**
1. Buka **ereg.pajak.go.id**
2. Daftar akun → Isi formulir pendaftaran
3. Upload foto KTP + selfie
4. Kartu NPWP dikirim ke alamat **atau** bisa diambil di KPP

> 💡 NPWP sekarang terintegrasi dengan NIK KTP sejak 2024!
"""
            elif opt == "B":
                resp = """
**📊 LAPOR SPT TAHUNAN:**
Batas waktu: **31 Maret** (pribadi) | **30 April** (badan)

**Cara Lapor Online:**
1. Buka **djponline.pajak.go.id**
2. Login dengan NPWP + EFIN
3. Pilih e-Filing → Isi SPT
4. Submit → Simpan BPE (Bukti Penerimaan Elektronik)

> ⚠️ Telat lapor = denda **Rp 100.000** (pribadi) / **Rp 1.000.000** (badan)
"""
            elif opt == "C":
                resp = """
**🔑 AKTIVASI EFIN:**
EFIN (Electronic Filing Identification Number) diperlukan untuk lapor SPT online.

**Cara aktivasi:**
1. Datang ke **KPP** (Kantor Pelayanan Pajak) terdekat
2. Bawa KTP + NPWP asli
3. Isi formulir permohonan EFIN
4. EFIN dikirim ke email yang terdaftar

> ℹ️ EFIN hanya perlu diaktifkan **sekali** seumur hidup.
"""
            elif opt == "D":
                resp = """
**❓ INFO TARIF & KETENTUAN PAJAK:**

| Penghasilan/Tahun | Tarif PPh |
|-------------------|-----------|
| ≤ Rp 60 juta | 5% |
| Rp 60–250 juta | 15% |
| Rp 250–500 juta | 25% |
| Rp 500 juta–5 M | 30% |
| > Rp 5 miliar | 35% |

**PTKP 2026:**
• Lajang: Rp 54.000.000/tahun
• Menikah: Rp 58.500.000/tahun
• Per tanggungan: +Rp 4.500.000/tahun (maks. 3)
"""
            elif opt == "0":
                self.state = State.MENU
                return MENU_TEXT
            else:
                return "⚠️ Pilih **A**, **B**, **C**, **D**, atau **0** untuk kembali."

            self.state = State.MENU
            return resp + "\n\n`0` · 🔙 Ketik **0** untuk Menu Utama"

        #  PENGADUAN — Pilih Kategori 
        elif self.state == State.PENGADUAN_KATEGORI:
            opt = msg.upper()
            kategori_map = {
                "A": "🛣️ Infrastruktur",
                "B": "🗑️ Kebersihan & Sampah",
                "C": "💡 Penerangan Jalan",
                "D": "🌊 Banjir & Lingkungan",
                "E": "🏥 Layanan Kesehatan",
                "F": "🎓 Layanan Pendidikan",
                "G": "👮 Keamanan & Ketertiban",
                "H": "📋 Layanan Administrasi",
                "I": "📝 Lainnya",
            }
            if opt in kategori_map:
                self.pending_kategori = kategori_map[opt]
                self.state = State.PENGADUAN_TULIS
                return f"""
📢 **PENGADUAN — {kategori_map[opt]}**

✏️ Silakan **tuliskan pengaduan Anda secara lengkap:**

Sertakan informasi:
• 📍 Lokasi kejadian (nama jalan, kelurahan, kecamatan)
• 📅 Waktu kejadian
• 📝 Deskripsi masalah yang jelas

*Contoh: "Jalan berlubang besar di Jl. Merdeka No. 5, Kel. Sukamaju, sudah 3 bulan belum diperbaiki"*
"""
            elif opt == "0":
                self.state = State.MENU
                return MENU_TEXT
            else:
                return "⚠️ Pilih kategori **A** hingga **I**, atau **0** untuk kembali."

        #  PENGADUAN — Tulis Isi 
        elif self.state == State.PENGADUAN_TULIS:
            if msg == "0":
                self.state = State.MENU
                return MENU_TEXT

            nomor = self._generate_nomor("ADU")
            kategori = self.pending_kategori or "Umum"
            self.pengaduan_log[nomor] = {
                "kategori": kategori,
                "isi": message,
                "status": "Diterima",
                "waktu": datetime.now().strftime("%d/%m/%Y %H:%M"),
            }
            self.pending_kategori = None
            self.state = State.MENU
            return f"""
✅ **PENGADUAN BERHASIL DITERIMA**

📌 **Nomor Tiket:** `{nomor}`
🗂️ **Kategori:** {kategori}
🕐 **Waktu:** {datetime.now().strftime("%d/%m/%Y %H:%M")} WIB
📊 **Status:** 🟡 Diterima — Menunggu Verifikasi

---
**Isi Pengaduan:**
> *{message}*

---
**Alur Tindak Lanjut:**
1. 🟡 **Diterima** ← *Anda di sini*
2. 🔵 Verifikasi oleh petugas (1–2 hari kerja)
3. 🟠 Diteruskan ke dinas terkait
4. 🟢 Dalam Penanganan
5. ✅ Selesai

---
💾 **Simpan nomor tiket Anda!**
Gunakan menu `10` untuk mengecek status pengaduan.

{MENU_TEXT}"""

        #  STATUS PENGADUAN 
        elif self.state == State.STATUS:
            if msg == "0":
                self.state = State.MENU
                return MENU_TEXT

            if msg.upper() in self.pengaduan_log:
                data = self.pengaduan_log[msg.upper()]
                status_icon = {"Diterima": "🟡", "Diverifikasi": "🔵", "Diproses": "🟠", "Selesai": "🟢"}.get(data["status"], "⚪")
                self.state = State.MENU
                return f"""
🔍 **STATUS PENGADUAN DITEMUKAN**

📌 **Nomor:** `{msg.upper()}`
🗂️ **Kategori:** {data["kategori"]}
🕐 **Dibuat:** {data["waktu"]}
📊 **Status:** {status_icon} **{data["status"]}**

**Isi Pengaduan:**
> *{data["isi"]}*

Ketik **0** untuk Menu Utama.
"""
            else:
                # Simulasi tiket tidak ditemukan
                self.state = State.MENU
                return f"""
⚠️ **Nomor tiket `{msg}` tidak ditemukan.**

Kemungkinan penyebab:
• Nomor tiket salah atau tidak lengkap
• Pengaduan dibuat di sesi yang berbeda

💡 Format yang benar: `ADU-DDMMYY-XXXXXX`

{MENU_TEXT}"""

        #  AMBIL ANTRIAN 
        elif self.state == State.ANTRIAN_PILIH:
            antrian_map = {
                "1": "KTP", "2": "KK", "3": "AKTA",
                "4": "SIM", "5": "PASPOR", "6": "BPJS", "7": "PAJAK"
            }
            emoji_map = {
                "KTP": "🪪", "KK": "👨‍👩‍👧", "AKTA": "📜",
                "SIM": "🚗", "PASPOR": "🛂", "BPJS": "🏥", "PAJAK": "💰"
            }
            if msg == "0":
                self.state = State.MENU
                return MENU_TEXT
            elif msg in antrian_map:
                jenis = antrian_map[msg]
                nomor_antrian, est_waktu = self._generate_antrian(jenis)
                self.state = State.MENU
                return f"""
🎫 **NOMOR ANTRIAN BERHASIL**

{emoji_map[jenis]} **Layanan:** {jenis}
🔢 **Nomor Antrian Anda:**

# `{nomor_antrian}`

⏰ **Estimasi Dipanggil:** ~{est_waktu} WIB
📍 **Loket:** Gedung Pelayanan Lt. 1 — Loket {jenis}

---
📸 *Harap screenshot / catat nomor antrian ini*
⚠️ *Jika tidak hadir saat dipanggil, antrian hangus*

{MENU_TEXT}"""
            else:
                return "⚠️ Pilih layanan **1–7** atau **0** untuk kembali."

        #  FAQ 
        elif self.state == State.FAQ:
            faq_answers = {
                "1": """
**🕐 JAM & HARI OPERASIONAL:**

| Instansi | Hari | Jam |
|---------|------|-----|
| Disdukcapil | Senin–Jumat | 08:00–15:00 |
| Satpas SIM | Senin–Jumat | 08:00–14:00 |
| Imigrasi | Senin–Jumat | 08:00–15:00 |
| KPP Pajak | Senin–Jumat | 08:00–16:00 |
| BPJS | Senin–Jumat | 08:00–15:30 |
| Kelurahan | Senin–Jumat | 08:00–15:00 |

> ⚠️ Tutup pada hari libur nasional & cuti bersama
""",
                "2": """
**💳 BIAYA RESMI PEMBUATAN DOKUMEN:**

| Dokumen | Biaya |
|---------|-------|
| KTP / KK / Akta | **GRATIS** |
| SIM A/B | Rp 120.000 |
| SIM C | Rp 100.000 |
| Paspor Biasa | Rp 350.000 |
| Paspor Elektronik | Rp 650.000 |
| NPWP | **GRATIS** |

> ⚠️ Waspada pungli! Tidak ada biaya tambahan resmi.
""",
                "3": """
**⏱️ ESTIMASI WAKTU PROSES:**

| Layanan | Waktu |
|---------|-------|
| KTP (perekaman) | 1–14 hari kerja |
| Kartu Keluarga | 3–5 hari kerja |
| Akta Kelahiran | 3–5 hari kerja |
| SIM Baru | 1 hari (lulus tes) |
| Paspor | 4 hari kerja |
| NPWP | 1 hari (online) |
| Daftar BPJS | Langsung aktif |
""",
                "4": """
**📱 LAYANAN ONLINE TERSEDIA:**

| Layanan | Platform |
|---------|---------|
| Paspor | Aplikasi M-Paspor |
| SIM | sim.korlantas.polri.go.id |
| BPJS | Aplikasi Mobile JKN |
| Pajak SPT | djponline.pajak.go.id |
| NPWP | ereg.pajak.go.id |
| Dukcapil | Aplikasi Dukcapil Go Digital |
| Pengaduan | lapor.go.id |
""",
                "5": """
**🆘 DOKUMEN HILANG — LANGKAH DARURAT:**

1. **Laporkan ke Polsek/Polres** setempat
   → Dapatkan Surat Keterangan Kehilangan
2. **Bawa ke instansi terkait** dengan surat kehilangan + KK
3. Isi formulir penggantian
4. Tunggu dokumen baru diterbitkan

> 💡 Untuk keamanan, foto/scan semua dokumen penting dan simpan di cloud!
""",
                "6": """
**👶 DOKUMEN UNTUK ANAK DI BAWAH UMUR:**

Semua pengurusan dokumen anak **wajib didampingi orang tua/wali**.

| Dokumen | Syarat Tambahan |
|---------|----------------|
| Akta Kelahiran | Surat Lahir RS + KTP+KK Ortu |
| KK (tambah anak) | Akta Kelahiran |
| Paspor Anak | Akta + KTP+KK+Paspor Ortu |
| BPJS Anak | KK + Akta Kelahiran |
""",
                "7": """
**🔄 DOKUMEN HILANG AKIBAT BENCANA:**

Pemerintah menyediakan layanan **penerbitan dokumen darurat** bagi korban bencana:

✅ Tidak dipungut biaya apapun
✅ Proses dipercepat (1–3 hari)
✅ Bisa dilakukan secara kolektif melalui Kelurahan/Kecamatan

Hubungi **Posko BPBD** atau Kelurahan setempat untuk koordinasi.
""",
            }
            if msg in faq_answers:
                self.state = State.MENU
                return faq_answers[msg] + "\n\nKetik **0** untuk Menu Utama."
            elif msg == "0":
                self.state = State.MENU
                return MENU_TEXT
            else:
                return "⚠️ Pilih nomor **1–7** atau **0** untuk kembali ke Menu."

        #  JADWAL 
        elif self.state == State.JADWAL:
            self.state = State.MENU
            return MENU_TEXT

        #  AKTA, KK (simple) 
        elif self.state in [State.AKTA]:
            self.state = State.MENU
            return MENU_TEXT

        #  EXIT 
        elif self.state == State.EXIT:
            return "🙏 Sesi telah berakhir. Refresh halaman untuk memulai kembali."

        return "Maaf, terjadi kesalahan. Ketik **0** untuk kembali ke Menu."

    def _get_jadwal(self):
        now = datetime.now()
        hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        hari_ini = hari[now.weekday()]
        buka = now.weekday() < 5 and 8 <= now.hour < 15
        status = "🟢 **BUKA**" if buka else "🔴 **TUTUP**"

        return f"""
📅 **JADWAL PELAYANAN**

🗓️ Hari ini: **{hari_ini}, {now.strftime("%d %B %Y")}**
🕐 Pukul: **{now.strftime("%H:%M")} WIB**
Status: {status}

---
**🏛️ DISDUKCAPIL (KTP, KK, Akta)**
📅 Senin–Jumat · ⏰ 08:00–15:00 WIB
📍 Jl. Ahmad Yani No. 1, Gedung Pelayanan Lt. 1

**🚔 SATPAS SIM (Kepolisian)**
📅 Senin–Jumat · ⏰ 08:00–14:00 WIB
📍 Polres Kota — Gedung Layanan SIM

**🛂 KANTOR IMIGRASI (Paspor)**
📅 Senin–Jumat · ⏰ 08:00–15:00 WIB
📍 Jl. Diponegoro No. 55
📱 Daftar via aplikasi **M-Paspor**

**🏥 BPJS KESEHATAN**
📅 Senin–Jumat · ⏰ 08:00–15:30 WIB
📅 Sabtu · ⏰ 08:00–11:00 WIB
📍 Jl. Gatot Subroto No. 10

**💰 KPP PRATAMA (Pajak)**
📅 Senin–Jumat · ⏰ 08:00–16:00 WIB
📍 Jl. Sudirman No. 23

---
📞 **Hotline:** 1500-XXX
📧 **Email:** layanan@pemkot.go.id

{MENU_TEXT}"""