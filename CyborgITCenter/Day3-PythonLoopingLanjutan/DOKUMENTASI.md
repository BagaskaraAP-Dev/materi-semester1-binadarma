# 📘 CYBORG IT CENTER — Day 3: While Loop Lanjutan & Studi Kasus Algoritma

> **Tanggal:** 16 Oktober 2026  
> **Peserta:** Bagaskara Amukti Palapa  
> **NIM:** 261420008  
> **Platform:** Google Colab / Visual Studio Code  
> **Bahasa:** Python 3  

---

## 📋 Daftar Materi yang Dipelajari

| No | Topik | Deskripsi |
|:--:|-------|-----------|
| 1 | **Step Increment Counter** | Mengubah laju kenaikan perulangan secara custom (`counter += 2` atau `counter += 100`) |
| 2 | **Decrement Loop (Countdown)** | Pola perulangan hitung mundur dari batas atas menuju batas bawah (`detik -= 1`) |
| 3 | **Sentinel / Exit Condition** | Perulangan dinamis berbasis nilai bendera / batas tertentu (`while input != 0`) |
| 4 | **Infinite Loop (`while True`) & `break`** | Pengendalian alur perulangan tak terbatas yang dihentikan oleh kondisi eksplisit |
| 5 | **Validasi Input Pengguna** | Menolak input invalid dan mengulang prompt hingga pengguna memasukkan data sah |
| 6 | **Pola Akumulator (Accumulator Pattern)** | Menjumlahkan total transaksi/data bertahap (`total += harga`) |
| 7 | **10 Studi Kasus While Loop** | Implementasi pemecahan masalah dunia nyata dengan perulangan `while` |
| 8 | **Migrasi Logika C ke Python** | Transisi struktur logika percabangan dan perulangan dari sintaks bahasa C ke Python |

---

## 1. 🔢 Step Increment Counter (Lompatan Pencacah)

Pada perulangan standar, pencacah (*counter*) biasanya bertambah satu (`i += 1`). Namun pada kasus tertentu, kita memerlukan penambahan dengan interval tertentu (*step increment*).

### Implementasi:
```python
# Mencetak deret bilangan mulai 2 melompat 2 angka
counter = 2
while counter <= 10:
    print(counter, end=" ")
    counter += 2

# Output: 2 4 6 8 10
```

---

## 2. ⏳ Decrement Loop (Hitung Mundur / Countdown)

Pola hitung mundur memanfaatkan inisialisasi pada nilai tertinggi, syarat kondisi perulangan `>= batas_bawah`, dan pengurangan nilai pencacah (*decrement*).

### Implementasi:
```python
detik = 5
while detik >= 1:
    print(f"Hitung mundur: {detik} detik")
    detik -= 1

print("Roket Meluncur!")
```

---

## 3. 🚩 Loop Berbasis Nilai Sentinel (Sentinel Condition)

Nilai sentinel adalah nilai khusus yang digunakan sebagai tanda (*flag*) untuk mengakhiri perulangan. Sering digunakan pada aplikasi kasir atau formulir dinamis di mana jumlah data tidak diketahui di awal.

```python
total = 0
donat = int(input("Masukkan jumlah donat (0 untuk selesai): "))

while donat != 0:
    total += donat
    donat = int(input("Masukkan jumlah donat (0 untuk selesai): "))

print(f"Total terjual: {total}")
```

---

## 4. 🔄 Infinite Loop (`while True`) & Statemen `break`

Konstruksi `while True` menciptakan loop yang secara default tidak akan pernah berhenti, kecuali menemui perintah `break` di dalam blok percabangan `if`.

```python
sandi_rahasia = 7

while True:
    tebakan = int(input("Masukkan sandi brankas: "))
    if tebakan == sandi_rahasia:
        print("Sandi Benar! Brankas Terbuka.")
        break
    print("Sandi salah, coba lagi!")
```

---

## 5. 🛡️ Validasi Input Pengguna (Input Validation)

Validasi input mencegah program menerima data yang rusak atau tidak masuk akal (misalnya nilai ujian siswa di luar batas 0–100).

```python
while True:
    nilai = int(input("Masukkan nilai siswa (0 - 100): "))
    if 0 <= nilai <= 100:
        break
    print("Nilai tidak valid! Silakan ulangi.")

print(f"Nilai {nilai} berhasil disimpan.")
```

---

## 6. 💰 Pola Akumulator (Accumulator Pattern)

Pola akumulator menggunakan variabel penampung (misalnya `total = 0`) yang nilainya terus bertambah seiring berjalannya setiap iterasi loop.

```python
total_belanja = 0

while True:
    harga = int(input("Masukkan harga belanja (0 untuk selesai): Rp "))
    if harga == 0:
        break
    total_belanja += harga

print(f"Total akhir: Rp {total_belanja:,}")
```

---

## 📂 7. 10 Studi Kasus While Loop

Berikut adalah ringkasan dari 10 soal studi kasus yang diselesaikan pada sesi latihan:

| No | File Program | Topik Studi Kasus | Pola Algoritma | Kondisi Berhenti |
|:--:|--------------|-------------------|----------------|------------------|
| 1 | `01_celengan_koin_doni.py` | Celengan Koin Doni | Akumulasi tabungan koin (+Rp 1.000) | `tabungan >= 5000` |
| 2 | `02_hitung_mundur_roket.py` | Peluncuran Roket | Countdown decrement (-1) | `detik < 1` |
| 3 | `03_pembagian_permen_sari.py` | Pembagian Permen Genap | Step increment (+2) | `permen > 10` |
| 4 | `04_langkah_kaki_joko.py` | Langkah Kaki Sehat Pak Joko | Step increment (+100) | `langkah > 500` |
| 5 | `05_kasir_donat_bu_ani.py` | Kasir Toko Donat | Sentinel loop | `donat == 0` |
| 6 | `06_konfirmasi_pesan_minum.py` | Pesanan Minum Kantin | `while True` + konfirmasi user | `jawaban != 'y'` |
| 7 | `07_tebak_sandi_brankas.py` | Tebak Angka Sandi Brankas | While loop target matching | `tebakan == 7` |
| 8 | `08_validasi_nilai_tugas.py` | Validasi Rentang Nilai | Boundary checking | `0 <= nilai <= 100` |
| 9 | `09_dadu_keberuntungan_budi.py` | Lemparan Dadu Budi | Event-driven loop | `dadu == 6` |
| 10 | `10_penjumlahan_angka_positif.py` | Kasir Akumulasi Jajan | Sentinel accumulator | `harga == 0` |

---

## 🔁 8. Migrasi Logika Pemrograman: Dari Bahasa C ke Python

Studi komparasi cara mengekspresikan logika algoritma umum dari bahasa C ke dalam sintaks Python yang bersih dan ekspresif:

| No | File Program | Studi Kasus Logika | Logika Algoritma | Perbedaan Karakteristik |
|:--:|--------------|--------------------|------------------|-------------------------|
| 1 | `01_check_bilangan_positif.py` | Cek Positif | `angka > 0` | Tidak butuh tanda kurung `()` pada syarat `if` |
| 2 | `02_bilangan_genap_ganjil.py` | Genap / Ganjil | `angka % 2 == 0` | Menggunakan indentasi sebagai blok eksekusi, tanpa kurung kurawal `{}` |
| 3 | `03_evaluasi_nilai_lulus.py` | Ambang Kelulusan | `nilai >= 75` | Sederhana, pembacaan float langsung via `float(input())` |
| 4 | `04_kategori_nilai_huruf.py` | Kategori Nilai | Cascading `if-elif-else` | Menggantikan sintaks `else if` di bahasa C dengan keyword `elif` |
| 5 | `05_diskon_belanja.py` | Diskon Bertingkat | Ambang batas >= 100.000 | Format angka rapi menggunakan f-string formatting (`:,.0f`) |
| 6 | `06_tarif_parkir.py` | Tarif Parkir Bertingkat | Interval durasi waktu | Tidak memerlukan struktur `switch-case` berbelit |
| 7 | `07_seleksi_wahana.py` | Seleksi Multi-Syarat | Usia & Tinggi badan | Kondisi bertingkat dievaluasi secara sekuensial dan intuitif |
| 8 | `08_autentikasi_login.py` | Login Admin | `username == "..." and password == "..."` | Menggunakan keyword `and` menggantikan operator `&&` pada bahasa C |

---

## 🚀 Cara Menjalankan

### Menjalankan Materi Utama Day 3:
```bash
python CyborgITCenter/Day3-PythonLoopingLanjutan/materi_day3.py
```

### Menjalankan Menu Latihan Interaktif:
```bash
python CyborgITCenter/Day3-PythonLoopingLanjutan/latihan_day3.py
```

### Menjalankan Salah Satu Studi Kasus:
```bash
python CyborgITCenter/Day3-PythonLoopingLanjutan/10-StudiKasus-WhileLoop/01_celengan_koin_doni.py
```

### Menjalankan Program Konversi C ke Python:
```bash
python CyborgITCenter/Day3-PythonLoopingLanjutan/Konversi-C-ke-Python/01_check_bilangan_positif.py
```

---

> 💪 *"Konsistensi dalam belajar logika pemrograman adalah kunci utama menjadi engineer handal."*
