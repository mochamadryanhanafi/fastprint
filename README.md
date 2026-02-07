# Fastprint Django Test

Proyek ini adalah aplikasi Django yang dibuat untuk tes rekrutmen. Aplikasi ini mengambil data produk dari API eksternal, menyimpannya di database PostgreSQL, dan menyediakan antarmuka web untuk menampilkan, menambah, mengedit, dan menghapus produk. Aplikasi ini dibangun dengan pendekatan arsitektur bersih dan menggunakan UI modern yang responsif.

## Teknologi yang Digunakan

*   **Backend:**
    *   Python
    *   Django
    *   Django Rest Framework
*   **Frontend:**
    *   HTML
    *   Bootstrap 5
    *   JavaScript
*   **Database:**
    *   PostgreSQL
*   **Kontainerisasi:**
    *   Docker
    *   Docker Compose

## Arsitektur Bersih (Clean Architecture)

Proyek ini mengikuti prinsip-prinsip Arsitektur Bersih untuk menciptakan pemisahan kekhawatiran (separation of concerns) dan membuat codebase lebih mudah dipelihara serta diuji. Kode diorganisir ke dalam lapisan-lapisan berikut:

*   **Lapisan Domain:** Berisi logika bisnis inti dan entitas aplikasi. Ini direpresentasikan oleh model-model Django di file `products/models.py`.
*   **Lapisan Aplikasi:** Berisi aturan bisnis spesifik aplikasi. Ini direpresentasikan oleh layanan dan kasus penggunaan. Dalam proyek ini, file `products/services.py` akan berisi logika untuk berinteraksi dengan API eksternal.
*   **Lapisan Presentasi:** Bertanggung jawab untuk menyajikan data kepada pengguna dan menangani input pengguna. Ini direpresentasikan oleh tampilan (views) dan template Django di direktori `products/views.py` dan `products/templates/`.
*   **Lapisan Infrastruktur:** Berisi detail implementasi layanan eksternal, seperti database dan API eksternal. Ini direpresentasikan oleh pengaturan Django di `fastprint_project/settings.py` dan perintah manajemen di `products/management/commands/populate_products.py`.

## Prasyarat (Prerequisites)

*   **Docker & Docker Compose:** Pastikan Docker Desktop (Windows/Mac) atau Docker Engine (Linux) sudah terinstal dan berjalan.
*   **Make (Opsional untuk Windows):** Pengguna Linux biasanya sudah memiliki `make`. Pengguna Windows bisa menggunakan WSL atau menjalankan perintah docker-compose secara manual.

## Instalasi & Menjalankan (Docker)

Proyek ini telah dikonfigurasi untuk berjalan sepenuhnya di dalam Docker container.

### Linux / Mac (Menggunakan Makefile)

Ketik perintah berikut di terminal:

1.  **Build dan Jalankan Container:**
    ```bash
    make build
    make up
    ```

2.  **Jalankan Migrasi Database:**
    ```bash
    make migrate
    ```

3.  **Populasi Data Awal:**
    ```bash
    make populate
    ```
    *Note: Username & Password API digenerate secara otomatis.*

4.  **Akses Aplikasi:**
    Buka browser dan kunjungi `http://localhost:8000`.

5.  **Hentikan Aplikasi:**
    ```bash
    make down
    ```

### Windows (Tanpa Make)

Jika Anda tidak menggunakan WSL, jalankan perintah manual berikut melalui Command Prompt atau PowerShell:

1.  **Build dan Jalankan:**
    ```bash
    docker-compose build
    docker-compose up -d
    ```

2.  **Migrasi Database:**
    ```bash
    docker-compose exec web python manage.py migrate
    ```

3.  **Populasi Data:**
    ```bash
    docker-compose exec web python manage.py populate_products
    ```

4.  **Akses Aplikasi:**
    Buka `http://localhost:8000`.

## Struktur Proyek & Clean Architecture

Proyek ini diorganisir dengan pendekatan Clean Architecture untuk menjaga kode tetap bersih, teruji, dan mudah dipelihara. Berikut adalah penjelasan struktur utamanya:

*   **`products/models.py` (Domain Layer):**
    Mendefinisikan struktur data (Entitas) seperti `Produk`, `Kategori`, dan `Status`. File ini bersih dari logika bisnis yang kompleks.

*   **`products/services.py` (Service Layer - Baru):**
    Menangani logika bisnis utama, khususnya interaksi dengan API eksternal. Service ini bertugas mengambil data, memvalidasi user/password dinamis, dan menyinkronkan data ke database lokal. Ini memisahkan logika dari View atau Command.

*   **`products/views.py` (Presentation Layer):**
    Bertanggung jawab hanya untuk menerima request HTTP dan mengembalikan response. View menggunakan Serializer untuk format data JSON (API) atau merender Template HTML untuk UI.

*   **`products/serializers.py` (Data Transfer Layer):**
    Mengubah objek model menjadi format JSON dan sebaliknya (Serialization/Deserialization). Juga menangani validasi input form (misal: harga harus angka).

*   **`products/management/commands/populate_products.py` (Infrastructure Layer):**
    Interface command-line (CLI) yang berfungsi sebagai entry point untuk memicu proses sinkronisasi data. Command ini sekarang sangat sederhana karena logika utamanya telah dipindahkan ke `services.py`.

## Endpoint API

*   `GET /api/products/`: Mengembalikan daftar produk yang memiliki status "bisa dijual".

## Fitur Baru (Modern UI)

*   **Desain Modern:** Menggunakan CSS custom dengan variabel warna, glassmorphism, dan transisi halus.
*   **Responsif:** Layout otomatis menyesuaikan diri (Tabel di Desktop, Kartu di Mobile).
*   **Interaktif:** Konfirmasi hapus yang aman dan feedback visual (badges).
