# FastPrint - Sistem Manajemen Produk

Aplikasi web modern untuk manajemen produk dengan UI yang responsif dan estetis. Dibangun dengan Django, PostgreSQL, dan Docker menggunakan prinsip Clean Architecture.

##  Fitur Utama

### 1. **Dashboard Statistik**
- **Total Produk**: Menampilkan jumlah total produk
- **Produk Siap Dijual**: Tracking produk dengan status "Bisa dijual"
- **Total Kategori**: Jumlah kategori produk
- **Update Terakhir**: Timestamp update data terbaru

### 2. **Manajemen Produk (CRUD)**
-  **Create**: Tambah produk baru dengan validasi real-time
-  **Read**: Tampilan tabel (desktop) dan card (mobile)
-  **Update**: Edit produk dengan konfirmasi modal
-  **Delete**: Hapus produk dengan konfirmasi modal modern

### 3. **Sistem Filter & Pencarian**
-  **Search**: Pencarian produk berdasarkan nama
-  **Filter Kategori**: Filter berdasarkan kategori produk
-  **Filter Status**: Filter berdasarkan status produk
-  **Reset Filter**: Tombol reset untuk menghapus semua filter

### 4. **UI/UX Modern**
-  **Soft Color Palette**: Warna lembut (soft blue & cream)
-  **Glassmorphism**: Efek kaca frosted pada card
-  **Responsive Design**: Otomatis menyesuaikan desktop/mobile
-  **Smooth Animations**: Transisi dan animasi halus
-  **Toast Notifications**: Feedback visual untuk setiap aksi
-  **Icon-Only Actions**: Tombol aksi dengan icon saja (lebih compact)

### 5. **Konfirmasi Modal**
-  **Save Confirmation**: Popup konfirmasi sebelum menyimpan
-  **Edit Confirmation**: Popup konfirmasi sebelum update
-  **Delete Confirmation**: Popup konfirmasi sebelum hapus
- Modern Bootstrap 5 modals dengan animasi fade

### 6. **Validasi Form**
- Client-side validation dengan feedback real-time
- Visual indicators (green/red borders)
- Error messages yang jelas
- Loading state saat submit

## Teknologi yang Digunakan

### Backend
- **Python 3.11**
- **Django 4.2.1** - Web framework
- **Django REST Framework** - API endpoints
- **pg8000** - PostgreSQL adapter

### Frontend
- **HTML5** - Struktur
- **CSS3** - Styling dengan custom variables
- **JavaScript (Vanilla)** - Interaktivitas
- **Bootstrap 5.3.3** - UI framework
- **Bootstrap Icons** - Icon library
- **Google Fonts (Inter)** - Typography

### Database
- **PostgreSQL 13** - Relational database

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration

##  Arsitektur Sistem

### Clean Architecture Layers

```
┌─────────────────────────────────────────┐
│     Presentation Layer (Views)          │
│  - product_list.html                    │
│  - product_form.html                    │
│  - views.py (HTTP handlers)             │
├─────────────────────────────────────────┤
│     Application Layer (Services)        │
│  - services.py (Business logic)         │
│  - serializers.py (Data validation)     │
├─────────────────────────────────────────┤
│     Domain Layer (Models)               │
│  - models.py (Entities)                 │
│    • Produk                             │
│    • Kategori                           │
│    • Status                             │
├─────────────────────────────────────────┤
│     Infrastructure Layer                │
│  - Database (PostgreSQL)                │
│  - External API integration             │
│  - Management commands                  │
└─────────────────────────────────────────┘
```

### Database Schema

**Tabel: Produk**
- `id_produk` (PK) - Integer
- `nama_produk` - String
- `harga` - Decimal
- `kategori` (FK) - Foreign Key ke Kategori
- `status` (FK) - Foreign Key ke Status

**Tabel: Kategori**
- `id_kategori` (PK) - Integer
- `nama_kategori` - String

**Tabel: Status**
- `id_status` (PK) - Integer
- `nama_status` - String

##  Instalasi & Setup

### Prasyarat
- Docker Desktop (Windows/Mac) atau Docker Engine (Linux)
- Docker Compose
- Make (opsional untuk Linux/Mac)

### Linux / Mac (dengan Makefile)

```bash
# 1. Build container
make build

# 2. Jalankan aplikasi
make up

# 3. Migrasi database
make migrate

# 4. Populasi data awal
make populate

# 5. Akses aplikasi
# Buka browser: http://localhost:8001
```

**Perintah tambahan:**
```bash
make down      # Stop container
make logs      # Lihat logs
make shell     # Masuk ke shell container
make restart   # Restart container
```

### Windows (tanpa Make)

```bash
# 1. Build dan jalankan
docker-compose build
docker-compose up -d

# 2. Migrasi database
docker-compose exec web python manage.py migrate

# 3. Populasi data
docker-compose exec web python manage.py populate_products

# 4. Akses aplikasi
# Buka browser: http://localhost:8001
```

**Perintah tambahan:**
```bash
docker-compose down                    # Stop container
docker-compose logs -f web            # Lihat logs
docker-compose exec web bash          # Masuk ke shell
docker-compose restart web            # Restart
```

##  API Endpoints

### REST API
- `GET /api/products/` - List semua produk dengan status "Bisa dijual"
  - Response: JSON array of products
  - Filter otomatis: hanya produk yang bisa dijual

### Web Pages
- `GET /products/` - Halaman list produk (dengan filter & search)
- `GET /products/create/` - Form tambah produk baru
- `GET /products/<id>/update/` - Form edit produk
- `POST /products/<id>/delete/` - Hapus produk

##  Desain UI

### Color Palette
```css
--primary: #7BA3C5        /* Soft Blue */
--secondary: #E8D5C4      /* Warm Cream */
--success: #81B29A        /* Mint Green */
--danger: #E07A5F         /* Soft Terracotta */
--background: #F8F9FA     /* Light Gray */
```

### Design Principles
1. **Minimalist**: Clean dan tidak berlebihan
2. **Soft Colors**: Warna lembut untuk mata
3. **Consistent Spacing**: Padding dan margin yang konsisten
4. **Clear Hierarchy**: Typography yang jelas
5. **Responsive First**: Mobile-friendly dari awal

##  Struktur Proyek

```
fastprint/
├── docker-compose.yml          # Docker orchestration
├── Dockerfile                  # Container definition
├── Makefile                    # Shortcut commands
├── requirements.txt            # Python dependencies
├── manage.py                   # Django CLI
├── fastprint_project/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── products/                   # Main app
    ├── models.py              # Domain entities
    ├── views.py               # HTTP handlers
    ├── serializers.py         # Data validation
    ├── services.py            # Business logic
    ├── urls.py                # URL routing
    ├── static/
    │   └── products/
    │       └── style.css      # Custom styles
    ├── templates/
    │   └── products/
    │       ├── base.html      # Base template
    │       ├── product_list.html
    │       └── product_form.html
    └── management/
        └── commands/
            └── populate_products.py
```

##  Konfigurasi

### Environment Variables
File `docker-compose.yml` sudah dikonfigurasi dengan:
- `POSTGRES_DB=fastprint_db`
- `POSTGRES_USER=fastprint_user`
- `POSTGRES_PASSWORD=fastprint_password`
- Port mapping: `8001:8000` (untuk menghindari konflik)

### Django Settings
- `DEBUG=True` (development)
- `ALLOWED_HOSTS=['*']`
- Database: PostgreSQL dengan pg8000
- Static files: `/static/`
- Media files: `/media/`

##  Testing

### Manual Testing Checklist
- [ ] Create produk baru dengan validasi
- [ ] Edit produk existing
- [ ] Delete produk dengan konfirmasi
- [ ] Filter by kategori
- [ ] Filter by status
- [ ] Search by nama produk
- [ ] Reset filters
- [ ] Responsive di mobile
- [ ] Toast notifications muncul
- [ ] Modal confirmations bekerja

##  Troubleshooting

### Port sudah digunakan
```bash
# Ubah port di docker-compose.yml
ports:
  - "8002:8000"  # Ganti 8001 ke 8002
```

### Database connection error
```bash
# Restart database container
docker-compose restart db
docker-compose restart web
```

### Static files tidak muncul
```bash
# Collect static files
docker-compose exec web python manage.py collectstatic --noinput
```

### Template syntax error
```bash
# Pastikan spacing di template benar
# Contoh: {% if form.kategori.value == k.pk %}
# BUKAN: {% if form.kategori.value==k.pk %}
```

##  Catatan Penting

1. **Port**: Aplikasi berjalan di `http://localhost:8001` (bukan 8000)
2. **Auto-reload**: Django development server auto-reload saat file berubah
3. **Data Persistence**: Data PostgreSQL tersimpan di Docker volume
4. **API Credentials**: Username dan password API di-generate otomatis

##  Developer

- **Project**: FastPrint Product Management System
- **Framework**: Django 4.2.1
- **Architecture**: Clean Architecture
- **UI/UX**: Modern, Responsive, User-Friendly

##  License

This project is created for recruitment test purposes.

---

**Warm Regards Ryan hanafi**
