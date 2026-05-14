# Web-Based Digital Signature System

Sebuah sistem simulasi __Digital Signature__ berbasis web untuk mendemonstrasikan konsep autentikasi data menggunakan kriptografi. 

Proyek ini dibangun menggunakan **Flask** di sisi *backend* untuk pemrosesan kriptografi yang aman, dan **HTML/JS** murni di sisi *frontend*.

## 🚀 Fitur Utama
*   **RSA Key Generation:** Menghasilkan __Public & Private Key__ menggunakan algoritma RSA-PSS secara otomatis di sisi server.
*   **File Signing:** Membaca data biner dari file fisik (PDF, TXT, Gambar, dll), melakukan *hashing* dengan SHA-256, dan menandatanganinya menggunakan *Private Key*.
*   **File Verification:** Memverifikasi integritas file asli terhadap *Digital Signature* (format Base64) menggunakan *Public Key*.

## 📂 Struktur Proyek

```text
digital-signature/
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

## 🛠️ Prasyarat
*   Python 3.12 atau lebih baru
*   `pip` (Python Package Installer)

## ⚙️ Instalasi dan Menjalankan Server

**1. Clone Repository**
```bash
git clone https://github.com/Rifanism/digital-signature.git
```

**2. Buat Virtual Environment (Optional)**
```bash
python -m venv venv
source venv/bin/activate
```

**3. Install Dependensi**
```bash
pip install -r requirements.txt
```

**4. Run**
```bash
python app.py
```

**5. Akses Melalui Browser**
Buka web browser dan kunjungi: `http://127.0.0.1:5000`

## 📖 Panduan Penggunaan
1.  **Inisialisasi:** Klik tombol **"Generate RSA Keys"** terlebih dahulu untuk membuat identitas kriptografi di memori server.
2.  **Signing:** Pada bagian `[02] Sign File`, pilih file apa saja dari komputermu, lalu klik **"Sign Document"**. Salin teks Base64 yang muncul di layar.
3.  **Verifikasi:** Pada bagian `[03] Verify File`, pilih file yang sama, tempel teks Base64 tadi ke dalam kotak *signature*, lalu klik **"Verify File Integrity"**. Coba ubah isi file asli sedikit saja untuk melihat sistem menolak file yang sudah dimodifikasi (INVALID).

## 💻 Git Workflow
Untuk menyimpan proyek ini ke repositori Git, jalankan urutan perintah berikut di terminal:

```bash
git init
git add .
git commit -m "feat: initial commit for digital signature system"
git branch -M main
git remote add origin <URL_REPOSITORI_KAMU>
git push -u origin main
```

---
*Dibuat oleh Rif'an Habibi (Rifanism) untuk keperluan tugas Keamanan Jaringan.*
```
