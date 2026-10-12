# ☕ Dokumentasi Tugas 1: Program Konversi Sistem Bilangan

> **Mata Kuliah:** Sistem Komputer / Sistem Bilangan  
> **Nama:** Bagaskara Amukti Palapa  
> **NIM:** 261420008  
> **Jurusan:** Teknik Informatika — Universitas Bina Darma  
> **Bahasa:** Java  
> **Berkas:** [`KonversiBilangan.java`](./KonversiBilangan.java)  

---

## 📌 Deskripsi Program

Program ini merupakan implementasi manual untuk konversi sistem bilangan antara **Desimal (10)**, **Biner (2)**, **Oktal (8)**, dan **Heksadesimal (16)** berdasarkan algoritma Soal 17.

Program ini dibuat secara murni menggunakan logika algoritma matematika manual, **tanpa menggunakan fungsi instan bawaan Java** seperti:
- ❌ `Integer.toBinaryString()`
- ❌ `Integer.toHexString()`
- ❌ `Integer.toOctalString()`
- ❌ `Integer.parseInt(s, radix)`

---

## 🌟 Keunggulan Fitur

1. **Mendukung Bilangan Pecahan (Koma)**  
   Mampu mengonversi bilangan bulat maupun bilangan dengan pecahan desimal (contoh: `25,625` atau `1101,101`).
2. **Presisi Pecahan Tanpa Floating-Point Error**  
   Bagian pecahan dihitung menggunakan representasi pembilang/penyebut rasional sehingga hasil konversi pecahan tidak terdistorsi oleh galat desimal floating-point.
3. **Trace Langkah Perhitungan Lengkap (Step-by-Step)**  
   Program menampilkan proses matematis:
   - Pembagian berulang beserta sisa bagi (Desimal ke basis lain)
   - Perkalian berulang untuk bagian pecahan
   - Penjumlahan bobot suku perpangkatan $B^i$ dan $B^{-j}$ (Basis lain ke Desimal)
   - Pengelompokan bit 3-bit / 4-bit (Biner <-> Oktal/Heksa)

---

## 🧮 4 Algoritma yang Diimplementasikan

### 1. Algoritma A: Desimal ke Basis Lain (Biner, Oktal, Heksa)
- **Bagian Bulat:** Dibagi berulang dengan basis $B$. Sisa pembagian dicatat dari bawah ke atas.
- **Bagian Pecahan:** Dikalikan berulang dengan basis $B$. Bagian bulat hasil kali dicatat dari atas ke bawah hingga maksimal 8 digit pecahan.

### 2. Algoritma B: Biner ke Basis Lain
- **Biner ke Desimal:** Menjumlahkan tiap digit bit dikalikan dengan $2^n$ (bulat) dan $2^{-m}$ (pecahan).
- **Biner ke Oktal:** Mengelompokkan tiap 3 bit dari koma (ke kiri untuk bulat, ke kanan untuk pecahan).
- **Biner ke Heksadesimal:** Mengelompokkan tiap 4 bit dari koma.

### 3. Algoritma C: Oktal ke Basis Lain
- **Oktal ke Desimal:** Menjumlahkan tiap digit dikalikan dengan $8^n$ dan $8^{-m}$.
- **Oktal ke Biner:** Setiap digit oktal diubah menjadi 3 bit biner.
- **Oktal ke Heksadesimal:** Dikonversi terlebih dahulu ke biner (3-bit per digit), lalu biner dikelompokkan menjadi 4-bit heksadesimal.

### 4. Algoritma D: Heksadesimal ke Basis Lain
- **Heksa ke Desimal:** Menjumlahkan tiap digit dikalikan dengan $16^n$ dan $16^{-m}$.
- **Heksa ke Biner:** Setiap digit heksadesimal diubah menjadi 4 bit biner.
- **Heksa ke Oktal:** Dikonversi terlebih dahulu ke biner (4-bit per digit), lalu biner dikelompokkan menjadi 3-bit oktal.

---

## 💻 Cara Menjalankan Program

### 1. Kompilasi:
```bash
javac Kuliah/KonversiBilangan.java
```

### 2. Eksekusi:
```bash
java -cp Kuliah KonversiBilangan
```

Atau jika dijalankan langsung dari direktori `Kuliah/`:
```bash
cd Kuliah
javac KonversiBilangan.java
java KonversiBilangan
```

---

## 🖥️ Contoh Penggunaan & Tampilan Menu

```text
==============================================
   PROGRAM KONVERSI BILANGAN
   Bagaskara Amukti Palapa - 261420008
==============================================
1. Desimal -> Biner, Oktal, Heksa      (17a)
2. Biner   -> Desimal, Oktal, Heksa    (17b)
3. Oktal   -> Desimal, Biner, Heksa    (17c)
4. Heksa   -> Desimal, Biner, Oktal    (17d)
0. Keluar
Pilih menu: 1
Masukkan bilangan Desimal (pecahan pakai koma): 25,625

[Desimal ke Biner]
  Bagian bulat 25 dibagi 2 berulang:
    25 : 2 = 12  sisa 1
    12 : 2 = 6  sisa 0
    6 : 2 = 3  sisa 0
    3 : 2 = 1  sisa 1
    1 : 2 = 0  sisa 1
  Bagian pecahan 0,625 dikali 2 berulang:
    0,625 x 2 = 1,250  -> 1
    0,25 x 2 = 0,50  -> 0
    0,5 x 2 = 1,0  -> 1
  >> 25,625 (10) = 11001,101 (2)
```
