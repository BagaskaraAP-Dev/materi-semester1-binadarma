# 📂 Materi Semester 1 — Universitas Bina Darma

> Repository ini berisi kumpulan materi, catatan, tugas perkuliahan, dan latihan pemrograman selama Semester 1 di **Universitas Bina Darma, Palembang**.

**Nama:** Bagaskara Amukti Palapa  
**NIM:** 261420008  
**Jurusan:** Teknik Informatika  
**Universitas:** Universitas Bina Darma  

---

## 📁 Struktur Repository

```
MateriSemester1/
├── 📂 CyborgITCenter/                        # Pelatihan CYBORG IT CENTER (Python & ML)
│   ├── 📂 Day1-PythonFundamental/            # Day 1: Python Fundamental
│   │   ├── 📄 materi_day1.py                 # Kode materi saat kelas
│   │   ├── 📄 latihan_day1.py                # Latihan mandiri
│   │   └── 📝 DOKUMENTASI.md                 # Dokumentasi lengkap materi Day 1
│   │
│   ├── 📂 Day2-PythonLooping/                # Day 2: While Loop & Variable Swapping
│   │   ├── 📄 materi_day2.py                 # Kode materi saat kelas (refactored)
│   │   ├── 📄 latihan_day2.py                # Latihan mandiri terstruktur
│   │   └── 📝 DOKUMENTASI.md                 # Dokumentasi lengkap materi Day 2
│   │
│   ├── 📂 Day3-PythonLoopingLanjutan/        # Day 3: While Loop Lanjutan & Studi Kasus Algoritma
│   │   ├── 📄 materi_day3.py                 # Kode materi sesi kelas
│   │   ├── 📄 latihan_day3.py                # Latihan mandiri & menu CLI interaktif
│   │   ├── 📝 DOKUMENTASI.md                 # Dokumentasi komprehensif Day 3
│   │   ├── 📂 10-StudiKasus-WhileLoop/       # 10 Studi Kasus Perulangan While
│   │   │   ├── 📄 01_celengan_koin_doni.py
│   │   │   ├── 📄 02_hitung_mundur_roket.py
│   │   │   ├── 📄 03_pembagian_permen_sari.py
│   │   │   ├── 📄 04_langkah_kaki_joko.py
│   │   │   ├── 📄 05_kasir_donat_bu_ani.py
│   │   │   ├── 📄 06_konfirmasi_pesan_minum.py
│   │   │   ├── 📄 07_tebak_sandi_brankas.py
│   │   │   ├── 📄 08_validasi_nilai_tugas.py
│   │   │   ├── 📄 09_dadu_keberuntungan_budi.py
│   │   │   ├── 📄 10_penjumlahan_angka_positif.py
│   │   │   └── 📄 soal_studi_kasus.txt
│   │   └── 📂 Konversi-C-ke-Python/          # 8 Program Migrasi Logika Algoritma C ke Python
│   │       ├── 📄 01_check_bilangan_positif.py
│   │       ├── 📄 02_bilangan_genap_ganjil.py
│   │       ├── 📄 03_evaluasi_nilai_lulus.py
│   │       ├── 📄 04_kategori_nilai_huruf.py
│   │       ├── 📄 05_diskon_belanja.py
│   │       ├── 📄 06_tarif_parkir.py
│   │       ├── 📄 07_seleksi_wahana.py
│   │       └── 📄 08_autentikasi_login.py
│   │
│   └── 📂 DAY5-Pyton List/                   # Day 5: Python List (Input, Sort & Reverse)
│       ├── 📄 01_insert_list.py
│       ├── 📄 02_input_list_for.py
│       ├── 📄 03_input_list_while.py
│       ├── 📄 04_sort_dan_reverse.py
│       ├── 📄 05_sorting_manual.py
│       └── 📝 DOKUMENTASI.md                 # Dokumentasi lengkap Day 5
│
├── 📂 Kuliah/                                # Materi & Tugas Perkuliahan
│   ├── 📄 belajar.py                         # Latihan Python dasar kuliah
│   ├── 📄 belajar.java                       # Latihan Java operasi aritmatika
│   ├── ☕ KonversiBilangan.java               # Tugas 1 Sistem Bilangan (Manual Multi-Basis)
│   └── 📝 DOKUMENTASI_KONVERSI_BILANGAN.md   # Dokumentasi lengkap Tugas 1
│
├── 📄 cybrotitcenterday1.py                  # (Original) Sesi kelas CYBORG Day 1
├── 📄 cybrogitcenter2.py                     # (Original) Sesi kelas CYBORG Day 2
├── 📄 belajar.py                             # (Original) Python kuliah
├── 📄 belajar.java                           # (Original) Java kuliah
├── 📄 KonversiBilangan.java                  # (Original) Tugas sistem bilangan
└── 📝 README.md                              # Dokumentasi utama repository
```

---

## 🏫 CYBORG IT CENTER — Python & Machine Learning Track

### Day 1: Python Fundamental (9 Oktober 2026)
📂 [`CyborgITCenter/Day1-PythonFundamental/`](./CyborgITCenter/Day1-PythonFundamental/)

| Materi | Deskripsi |
|--------|-----------|
| Print & Output | Menampilkan teks ke layar |
| Variabel | Menyimpan data dalam variabel |
| Tipe Data | `str`, `int`, `float`, `bool` |
| Operasi Aritmatika | `+`, `-`, `*`, `/`, `%`, `**`, `//` |
| Input User | Membaca input dari pengguna via konsol |
| Type Casting | Konversi antar tipe data (`int()`, `float()`, `str()`) |
| String Formatting | f-string dan formatting string |
| Boolean & Perbandingan | Operator logika dan perbandingan |
| Percabangan | `if`, `elif`, `else` |
| Mini Project | Kalkulator sederhana dengan operator aritmatika |

📖 **Dokumentasi lengkap:** [`Day1 DOKUMENTASI.md`](./CyborgITCenter/Day1-PythonFundamental/DOKUMENTASI.md)

---

### Day 2: Python While Loop & Variable Swapping (12 Oktober 2026)
📂 [`CyborgITCenter/Day2-PythonLooping/`](./CyborgITCenter/Day2-PythonLooping/)

| Materi | Deskripsi |
|--------|-----------|
| Pertukaran Variabel (Swap) | Teknik variabel sementara (`temp`) & Pythonic unpacking |
| Studi Kasus Alpro (4 Variabel) | Pergeseran siklik urutan `a`, `b`, `c`, `d` |
| Perulangan While (Counter) | Loop dengan kondisi cacah (`angka <= 5`) |
| Sentinel / Exit Condition | Loop dinamis berbasis input pengguna (`while != "exit"`) |
| Modul `random` & Tebak Angka | Pemanfaatan `random.randint()`, `while True`, dan `break` |
| Validasi Input Pengguna | Mengulang prompt hingga input memenuhi syarat |
| Mini Project: Menu Kopi CLI | Antarmuka konsol menu pemesanan minuman warung kopi |
| Bug Fix & Analysis | Solusi pencegahan infinite loop dan perbaikan scope variabel |

📖 **Dokumentasi lengkap:** [`Day2 DOKUMENTASI.md`](./CyborgITCenter/Day2-PythonLooping/DOKUMENTASI.md)

---

### Day 3: While Loop Lanjutan & Studi Kasus Algoritma (16 Oktober 2026)
📂 [`CyborgITCenter/Day3-PythonLoopingLanjutan/`](./CyborgITCenter/Day3-PythonLoopingLanjutan/)

| Materi | Deskripsi |
|--------|-----------|
| Step Increment Counter | Pola lompatan pencacah (`counter += 2`, `langkah += 100`) |
| Decrement Loop (Countdown) | Hitung mundur waktu peluncuran roket (`detik -= 1`) |
| Sentinel / Exit Condition | Terminasi loop berbasis input spesifik (`while donat != 0`) |
| Infinite Loop & `break` | Perulangan `while True` dengan terminasi kondisi khusus |
| Validasi Input Pengguna | Boundary checking nilai siswa rentang 0–100 |
| Akumulator Transaksi | Akumulasi total belanja jajan kasir bertahap |
| 10 Studi Kasus While | Pemecahan 10 variasi masalah logika perulangan dunia nyata |
| Konversi Logika C ke Python | Transisi sintaks kontrol alur, percabangan, dan operator dari C ke Python |

📖 **Dokumentasi lengkap:** [`Day3 DOKUMENTASI.md`](./CyborgITCenter/Day3-PythonLoopingLanjutan/DOKUMENTASI.md)

---

### Day 5: Python List — Input, Sort & Reverse (27 Oktober 2026)
📂 [`CyborgITCenter/DAY5-Pyton List/`](./CyborgITCenter/DAY5-Pyton%20List/)

| Materi | Deskripsi |
|--------|-----------|
| `insert()` | Menyisipkan item ke indeks tertentu |
| Input ke List (`for` + `append()`) | Mengisi list dari input pengguna sebanyak 5 kali |
| Input ke List (`while` + validasi) | Mengisi list sampai 5 data positif terkumpul |
| `sort()` vs `sorted()` | Mengurutkan list asli vs membuat list baru yang urut |
| `reverse=True` vs `reverse()` | Urut besar ke kecil vs sekadar membalik posisi item |
| Bug Fix `print(nilai.sort)` | Kenapa yang tercetak objek method / `None`, dan cara benarnya |
| Sorting Manual | Mengurutkan tanpa `sort()` dengan mencari nilai terkecil berulang |

📖 **Dokumentasi lengkap:** [`Day5 DOKUMENTASI.md`](./CyborgITCenter/DAY5-Pyton%20List/DOKUMENTASI.md)

---

## 🎓 Materi Perkuliahan Universitas Bina Darma

### 1. Tugas 1: Program Konversi Sistem Bilangan (Java)
- **File Kode:** [`Kuliah/KonversiBilangan.java`](./Kuliah/KonversiBilangan.java)
- **Dokumentasi:** [`Kuliah/DOKUMENTASI_KONVERSI_BILANGAN.md`](./Kuliah/DOKUMENTASI_KONVERSI_BILANGAN.md)
- **Deskripsi:** Implementasi manual konversi bilangan antar basis (Desimal, Biner, Oktal, Heksadesimal) tanpa menggunakan fungsi bawaan sistem. Mendukung bilangan pecahan/koma dengan presisi rasional serta menampilkan langkah-langkah perhitungannya secara terperinci.

### 2. Dasar Pemrograman (Python & Java)
- **Python:** [`Kuliah/belajar.py`](./Kuliah/belajar.py) — Program kalkulator sederhana interaktif
- **Java:** [`Kuliah/belajar.java`](./Kuliah/belajar.java) — Program kalkulator aritmatika menggunakan `Scanner`

---

## 🛠️ Tools yang Digunakan

| Tool | Kegunaan |
|------|----------|
| [Google Colab](https://colab.research.google.com/) | Cloud notebook untuk Python & Machine Learning |
| [VS Code](https://code.visualstudio.com/) | Editor kode dan environment lokal |
| Python 3 | Bahasa pemrograman utama |
| Java (JDK 21) | Bahasa pemrograman mata kuliah algoritma |
| Git & GitHub | Sistem version control dan portofolio kode |

---

## 🚀 Cara Menjalankan

### Python (CYBORG IT CENTER Day 1)
```bash
python CyborgITCenter/Day1-PythonFundamental/latihan_day1.py
```

### Python (CYBORG IT CENTER Day 2)
```bash
python CyborgITCenter/Day2-PythonLooping/latihan_day2.py
```

### Python (CYBORG IT CENTER Day 3)
```bash
# Menjalankan Materi Kelas Day 3
python CyborgITCenter/Day3-PythonLoopingLanjutan/materi_day3.py

# Menjalankan Menu Latihan Interaktif Day 3
python CyborgITCenter/Day3-PythonLoopingLanjutan/latihan_day3.py

# Menjalankan Salah Satu Studi Kasus
python CyborgITCenter/Day3-PythonLoopingLanjutan/10-StudiKasus-WhileLoop/01_celengan_koin_doni.py

# Menjalankan Program Migrasi C ke Python
python CyborgITCenter/Day3-PythonLoopingLanjutan/Konversi-C-ke-Python/01_check_bilangan_positif.py
```

### Python (CYBORG IT CENTER Day 5)
```bash
python "CyborgITCenter/DAY5-Pyton List/04_sort_dan_reverse.py"
python "CyborgITCenter/DAY5-Pyton List/05_sorting_manual.py"
```

### Java (Tugas 1 Konversi Bilangan)
```bash
javac Kuliah/KonversiBilangan.java
java -cp Kuliah KonversiBilangan
```

### Java (Program Belajar Aritmatika)
```bash
javac Kuliah/belajar.java
java -cp Kuliah belajar
```

---

## 📈 Progress Belajar

- [x] Python Fundamental (Variable, Tipe Data, Input/Output)
- [x] Operasi Aritmatika & Type Casting
- [x] Percabangan (`if` / `elif` / `else`)
- [x] Mini Project: Kalkulator Sederhana
- [x] Pertukaran Nilai Variabel (Swapping 2 & 4 variabel)
- [x] Perulangan While (Counter, Sentinel, Validation)
- [x] Random Module & Game Tebak Angka
- [x] Interactive Console Menu System
- [x] While Loop Step Increment & Countdown
- [x] 10 Studi Kasus Perulangan & Akumulator
- [x] Migrasi & Penerapan Logika Pemrograman (C ke Python)
- [x] Konversi Sistem Bilangan (Desimal, Biner, Oktal, Heksa - Bulat & Pecahan)
- [x] List: `insert()`, `append()`, `sort()`, `sorted()`, `reverse=True` & Sorting Manual
- [ ] Looping `for` & `range()`
- [ ] Fungsi (*Function* & *Parameter*)
- [ ] Struktur Data (List, Tuple, Dictionary, Set)
- [ ] Pengolahan File (*File Handling*)
- [ ] Pemrograman Berorientasi Objek (*OOP*)
- [ ] Pengenalan *Machine Learning*

---

> 💪 *"Belajar coding itu marathon, bukan sprint. Tetap konsisten!"*
