# Day 04 - Secure Config Loader (Environment Variables)

## Overview
Pada hari ke-4, project berfokus pada implementasi **secure configuration loader** menggunakan environment variables. Tujuannya adalah memisahkan data sensitif (seperti password dan API key) dari source code untuk mengurangi risiko kebocoran.

---

## Problem
Banyak aplikasi menyimpan credential langsung di dalam kode, contohnya:
- Database password
- API key
- Secret token

Hal ini berbahaya karena:
- Bisa ter-push ke GitHub
- Mudah diakses jika repository bocor
- Sulit dikelola di environment berbeda (dev, staging, production)

---

## Solution
Menggunakan `.env` file dan library `python-dotenv` untuk:
- Load konfigurasi dari environment
- Validasi config wajib
- Menyembunyikan data sensitif saat ditampilkan

---

## Implementation

### 1. Environment File

`.env` (tidak boleh di-commit):
```env
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=supersecret
API_KEY=123456