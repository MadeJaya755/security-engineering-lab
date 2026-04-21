# Day 3 - File Upload Validator

## 🎯 Tujuan
Membangun sistem upload file dengan validasi keamanan dasar untuk mencegah upload file berbahaya.

---

## 🧠 Konsep Utama

File upload adalah salah satu attack surface paling umum dalam aplikasi web.  
Validasi tidak cukup hanya berdasarkan ekstensi, karena file bisa dengan mudah dimanipulasi.  
Oleh karena itu, diperlukan validasi berlapis:

- Validasi ekstensi file
- Validasi ukuran file
- Validasi tipe file sebenarnya (MIME / magic bytes)

---

## ⚙️ Mekanisme Sistem

1. User upload file melalui endpoint `/upload`
2. Server melakukan validasi:
   - Mengecek ukuran file (maks 2MB)
   - Mengecek ekstensi file
   - Mengecek MIME type menggunakan `python-magic`
3. Jika valid:
   - File disimpan ke folder `uploads/`
   - Nama file di-random menggunakan UUID
4. Jika tidak valid:
   - Request ditolak dengan error message

---

## 🧪 Pengujian

### ✅ File valid
- `.jpg`, `.png`, `.pdf` normal → berhasil upload

### ❌ File tidak valid
- File `.exe` → ditolak
- File rename `.exe` → `.jpg` → ditolak (terdeteksi MIME)
- File > 2MB → ditolak
- Double extension (`.jpg.exe`) → ditolak

---

## 🔐 Keamanan yang Diterapkan

- Extension filtering
- MIME type validation
- File size limiting
- Random filename (UUID)

---

## ⚠️ Kelemahan Sistem

- Belum ada scanning malware (ClamAV)
- Belum ada sanitasi nama file lanjutan
- Belum ada proteksi path traversal
- Belum ada logging aktivitas
- Belum validasi konten file (misalnya PDF dengan script)

---

## 🚀 Pengembangan Selanjutnya

- Integrasi antivirus (ClamAV)
- Logging ke file atau SIEM
- Rate limiting upload
- Authentication sebelum upload
- Penyimpanan file di luar web root

---

## 📌 Insight

Validasi file upload bukan fitur tambahan, tapi kebutuhan dasar dalam aplikasi.  
Kesalahan kecil dalam validasi dapat menyebabkan remote code execution atau kompromi sistem.

---

## 💭 Catatan Pribadi

Project ini memberikan pemahaman bahwa:
- Keamanan tidak hanya soal tools, tapi desain sistem
- Validasi input adalah lapisan pertama pertahanan
- Banyak attack terjadi karena asumsi yang salah terhadap input user