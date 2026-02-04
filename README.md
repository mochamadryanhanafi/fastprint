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

## Menjalankan Proyek

1.  **Mulai database:**
    ```bash
    docker-compose up -d
    ```

2.  **Buat virtual environment dan instal dependensi:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Terapkan migrasi:**
    ```bash
    python manage.py migrate
    ```

4.  **Ambil data dari API:**
    ```bash
    python manage.py populate_products
    ```
    **Catatan:** Username untuk API bersifat sensitif waktu. Jika perintah gagal dengan kesalahan autentikasi, Anda mungkin perlu membuat username baru dan memperbaruinya di file `products/management/commands/populate_products.py`.

5.  **Mulai server pengembangan:**
    ```bash
    python manage.py runserver
    ```

Aplikasi akan tersedia di `http://127.0.0.1:8000/`.

## Endpoint API

*   `GET /api/products/`: Mengembalikan daftar produk yang memiliki status "bisa dijual".

## Operasi CRUD

Aplikasi ini menyediakan operasi CRUD berikut untuk produk:

*   **Buat (Create):** Anda dapat menambahkan produk baru dengan mengklik tombol "Add Product" di halaman daftar produk. Formulir mencakup validasi untuk memastikan nama produk tidak kosong dan harga berupa angka.
*   **Baca (Read):** Halaman daftar produk menampilkan daftar semua produk dengan status "bisa dijual".
*   **Perbarui (Update):** Anda dapat mengedit produk yang sudah ada dengan mengklik tombol "Edit" di halaman daftar produk.
*   **Hapus (Delete):** Anda dapat menghapus produk dengan mengklik tombol "Delete" di halaman daftar produk. Dialog konfirmasi akan ditampilkan sebelum menghapus produk.
