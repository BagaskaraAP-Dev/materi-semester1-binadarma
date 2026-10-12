# 📘 CYBORG IT CENTER — Day 2: Python Looping & Variable Swapping

> **Tanggal:** 12 Oktober 2026  
> **Peserta:** Bagaskara Amukti Palapa  
> **Platform:** Google Colab / Visual Studio Code  
> **Bahasa:** Python 3  

---

## 📋 Daftar Materi yang Dipelajari

| No | Topik | Deskripsi |
|:--:|-------|-----------|
| 1 | **Pertukaran Nilai Variabel (Swapping)** | Menukar nilai 2 variabel menggunakan variabel penampung (`temp`) dan cara Pythonic |
| 2 | **Studi Kasus Alpro Dasar: Swap 4 Variabel** | Menggeser posisi urutan 4 nilai variabel (`a`, `b`, `c`, `d`) secara siklik |
| 3 | **Perulangan `while` (While Loop)** | Konsep perulangan berbasis kondisi logika (syarat berhenti) |
| 4 | **Loop Berbasis Sentinel (Exit Condition)** | Mengulang program input pengguna secara dinamis hingga diketik `"exit"` |
| 5 | **Modul `random` & Game Tebak Angka** | Penggunaan `random.randint()`, `while True`, dan statemen `break` |
| 6 | **Validasi Input Pengguna** | Memaksa pengguna memasukkan input yang benar sebelum melanjutkan eksekusi |
| 7 | **Mini Project: Menu Pemesanan Kopi CLI** | Pembuatan menu interaktif konsol dengan while loop dan branching `if/elif/else` |
| 8 | **Troubleshooting & Infinite Loop Prevention** | Memahami penyebab perulangan tanpa henti dan teknik update variabel di dalam loop |

---

## 1. 🔄 Pertukaran Nilai Variabel (Variable Swapping)

Dalam algoritma dasar, jika kita ingin menukar isi dua variabel, kita tidak bisa langsung menugaskannya satu sama lain tanpa kehilangan salah satu nilainya.

### A. Metode Klasik: Menggunakan Variabel Sementara (`temp`)

```python
a = 7
b = 8

# Menukar nilai
temp = a   # temp = 7 (nilai a diamankan)
a = b      # a = 8
b = temp   # b = 7

print(f"a = {a}, b = {b}")  # a = 8, b = 7
```

### B. Metode Pythonic: Tuple Unpacking

Python mendukung sintaks khusus yang lebih ringkas dan elegan:

```python
a, b = b, a
```

---

## 2. 🧩 Studi Kasus Alpro: Pergeseran Siklik 4 Variabel

**Soal Logika:**
Diberikan 4 variabel dengan nilai mula-mula:
- `a = 8`, `b = 10`, `c = 11`, `d = 5`

Ingin diubah menjadi:
- `a = 5`, `b = 8`, `c = 10`, `d = 11`

### Analisis Logika:
Nilai `d` (5) harus dipindahkan ke `a`, sedangkan nilai `c` ke `d`, `b` ke `c`, dan `a` ke `b`.  
Jika kita ubah dari depan langsung tanpa menampung nilai `d`, maka nilai `5` akan hilang tertimpa.

### Implementasi Kode:

```python
a = 8
b = 10
c = 11
d = 5

print(f"Mula-mula : a={a}, b={b}, c={c}, d={d}")

temp = d   # Amankan nilai d (5)
d = c      # d mengambil nilai c (11)
c = b      # c mengambil nilai b (10)
b = a      # b mengambil nilai a (8)
a = temp   # a mengambil nilai temp (5)

print(f"Hasil akhir: a={a}, b={b}, c={c}, d={d}")
# Output: a = 5, b = 8, c = 10, d = 11
```

---

## 3. 🔁 Perulangan `while` (While Loop)

Perulangan `while` mengeksekusi blok kode berulang kali **selama kondisi yang diperiksa bernilai `True`**.

### Struktur Anatomi While Loop:

```python
# 1. Inisialisasi variabel pencacah (counter)
angka = 0

# 2. Pemeriksaan kondisi
while angka <= 5:
    print(angka)
    # 3. Pembaruan/Increment (WAJIB agar tidak loop selamanya!)
    angka += 1

print("Loop selesai")
```

> ⚠️ **Catatan Penting:**  
> Jika langkah ke-3 (`angka += 1`) lupa ditulis, variabel `angka` akan selamanya bernilai `0`, menyebabkan **Infinite Loop** (program macet dan berjalan tanpa henti).

---

## 4. 🛑 Sentinel Value & Loop Berbasis Input Pengguna

Perulangan tidak hanya menggunakan angka hitungan, tetapi juga bisa menunggu kata kunci tertentu dari pengguna (dikenal sebagai **Sentinel Loop**).

```python
input_user = ""

while input_user.lower() != "exit":
    input_user = input("Ketik sesuatu (ketik 'exit' untuk keluar): ")
    print("Menghasilkan:", input_user)

print("Program finish.")
```

**Karakteristik Sentinel Loop:**
- Variabel inisialisasi diatur agar pertama kali masuk loop (`input_user = ""`).
- Setiap putaran loop meminta input baru.
- Saat pengguna mengetik `'exit'`, kondisi `input_user != "exit"` menjadi `False` dan perulangan berhenti.

---

## 5. 🎲 Modul `random` & Game Tebak Angka

Kita menggabungkan pustaka standar Python `random` dengan perulangan tak hingga `while True` dan pernyataan keluar `break`.

```python
import random

angka_rahasia = random.randint(1, 10)  # Memilih angka acak 1 sampai 10

while True:
    tebakan = int(input("Tebak angka antara 1 sampai 10: "))
    if tebakan == angka_rahasia:
        print("Tebakan Anda benar!")
        break  # Menghentikan loop secara langsung
    else:
        print("Tebakan Anda salah, coba lagi!")
```

### Konsep Baru:
- `random.randint(a, b)`: Menghasilkan bilangan bulat acak inclusive antara `a` dan `b`.
- `while True`: Membuka perulangan tanpa batas.
- `break`: Statemen darurat untuk langsung keluar dari blok perulangan terdekat.

---

## 6. 🔒 Validasi Input Pengguna

Seringkali program memerlukan masukan tertentu agar bisa melanjutkan proses. Kita dapat memanfaatkan `while` loop sebagai gerbang validasi:

```python
input_user = 0

while input_user != 5:
    input_user = int(input("Masukkan angka 5 untuk membuka kunci: "))
    if input_user != 5:
        print(f"Inputan kamu salah ({input_user}), coba lagi!")

print("Kunci terbuka! Inputan kamu benar.")
```

---

## 7. ☕ Mini Project: Menu Pemesanan Kopi Interaktif

Membuat antarmuka konsol menu pemesanan minuman yang terus muncul sampai pengguna memilih nomor 4 (Exit).

```python
pilihan = 0

while pilihan != 4:
    print("=" * 25)
    print("   WARUNG KOPI CYBORG")
    print("=" * 25)
    print("1. Espresso")
    print("2. Americano")
    print("3. Butterscotch")
    print("4. Keluar / Exit")
    print("=" * 25)
    
    pilihan = int(input("Masukkan pilihan anda (1-4): "))
    
    if pilihan == 1:
        print(">> Anda memilih espresso\n")
    elif pilihan == 2:
        print(">> Anda memilih americano\n")
    elif pilihan == 3:
        print(">> Anda memilih butterscotch\n")
    elif pilihan == 4:
        print(">> Terima kasih telah berbelanja!\n")
    else:
        print(">> Menu tidak valid!\n")
```

---

## 🛠️ Catatan Refleksi & Troubleshooting (Bug Fix)

Pada berkas sesi latihan `cybrogitcenter2.py`, terdapat potongan kode awal:

```python
# KODE SEBELUMNYA:
input_user = 0
input_user = int(input("Masukkan pilihan anda: "))
while input_user != 4:
    if input == 1:
        print("Anda memilih espresso")
    elif input == 2:
        print("Anda memilih americano")
    ...
```

### Masalah yang Ditemukan:
1. **Nama Variabel Salah**: Mengecek `if input == 1` padahal variabel yang menyimpan angka adalah `input_user`. `input` adalah fungsi bawaan Python.
2. **Infinite Loop**: Pemanggilan `input()` berada di **luar** `while loop`, sehingga ketika pengguna memilih angka `1`, kondisi `input_user != 4` akan selalu `True` dan mencetak teks tanpa henti.
3. **Solusi**: Pindahkan `input_user = int(input(...))` ke **dalam badan loop** agar dievaluasi ulang pada setiap putaran.

---

## 📊 Alur Logika Perulangan (Flowchart)

```
        +-----------------------+
        |   Inisialisasi Nilai  |
        +-----------------------+
                    |
                    v
          /-------------------\
         /   Kondisi Benar?    \  ---(TIDAK)---> [ Keluar / Selesai ]
         \     (True / False)  /
          \-------------------/
                    | (YA)
                    v
        +-----------------------+
        |  Jalankan Statemen    |
        +-----------------------+
                    |
                    v
        +-----------------------+
        |  Update Nilai/Input   |
        +-----------------------+
                    |
                    +-----> (Kembali ke evaluasi kondisi)
```

---

## 🎯 Key Takeaways Day 2

1. **Prinsip Swap**: Menukar variabel selalu butuh wadah penampung sementara (`temp`) kecuali menggunakan fitur unpacking Python.
2. **Struktur 3 Bagian While**: Selalu pastikan ada *Inisialisasi*, *Kondisi*, dan *Update*.
3. **Pencegahan Infinite Loop**: Selalu periksa apakah ada kondisi yang pasti menghentikan loop (`break` atau perubahan nilai kondisi).
4. **Interactive CLI Menu**: Kombinasi `while != exit_code` dan `if/elif/else` adalah fondasi dasar semua aplikasi berbasis terminal.

---

## 🚀 Rencana Materi Selanjutnya (Next Topics)

- [ ] Perulangan `for` dan fungsi rentang `range()`
- [ ] Kontrol perulangan mendalam (`break`, `continue`, `pass`)
- [ ] Perulangan bersarang (*Nested Loop*)
- [ ] Pengenalan Koleksi Data: **List** dan **Tuple**

---

> 📝 *Dokumentasi ini disusun sebagai rangkuman resmi materi CYBORG IT CENTER — Python & Machine Learning Track Day 2.*
