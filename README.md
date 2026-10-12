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
│   └── 📂 Day2-PythonLooping/                # Day 2: While Loop & Variable Swapping
│       ├── 📄 materi_day2.py                 # Kode materi saat kelas (refactored)
│       ├── 📄 latihan_day2.py                # Latihan mandiri terstruktur
│       └── 📝 DOKUMENTASI.md                 # Dokumentasi lengkap materi Day 2
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
- [x] Konversi Sistem Bilangan (Desimal, Biner, Oktal, Heksa - Bulat & Pecahan)
- [ ] Looping `for` & `range()`
- [ ] Fungsi (*Function* & *Parameter*)
- [ ] Struktur Data (List, Tuple, Dictionary, Set)
- [ ] Pengolahan File (*File Handling*)
- [ ] Pemrograman Berorientasi Objek (*OOP*)
- [ ] Pengenalan *Machine Learning*

---

> 💪 *"Belajar coding itu marathon, bukan sprint. Tetap konsisten!"*
