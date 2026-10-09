# 📘 CYBORG IT CENTER — Day 1: Python Fundamental

> **Tanggal:** 9 Oktober 2026  
> **Peserta:** Bagaskara Amukti Palapa  
> **Platform:** Google Colab (Google Research)  
> **Bahasa:** Python 3  

---

## 📋 Daftar Materi yang Dipelajari

| No | Topik | Deskripsi |
|----|-------|-----------|
| 1 | Print & Output | Menampilkan teks ke layar |
| 2 | Variabel | Menyimpan data dalam variabel |
| 3 | Tipe Data | `str`, `int`, `float`, `bool` |
| 4 | Operasi Aritmatika | `+`, `-`, `*`, `/`, `%` |
| 5 | Input User | Membaca input dari pengguna |
| 6 | Type Casting | Konversi antar tipe data |
| 7 | String Formatting | Cara memformat output string |
| 8 | Boolean & Perbandingan | Operator `==`, `!=`, `>`, `<`, `>=`, `<=` |
| 9 | Percabangan (if/elif/else) | Logika pengambilan keputusan |
| 10 | Mini Project | Kalkulator sederhana dengan pilihan operator |

---

## 1. 🖨️ Print & Output

Fungsi `print()` digunakan untuk menampilkan teks atau nilai ke layar.

```python
print("Bagaskara Amukti Palapa")
print("Saya Tinggal Di Palembang")
```

**Catatan:**
- Teks (string) harus diapit tanda kutip `" "` atau `' '`
- `print()` otomatis menambahkan baris baru di akhir

---

## 2. 📦 Variabel

Variabel adalah tempat menyimpan data. Python tidak perlu deklarasi tipe — langsung assign saja.

```python
nama = "BAGASKARA AMUKTI PALAPA"   # string
umur = 19                           # integer
tinggi = 170                        # integer
```

**Aturan penamaan variabel:**
- Diawali huruf atau underscore (`_`)
- Tidak boleh diawali angka
- Case-sensitive (`Nama` ≠ `nama`)
- Gunakan `snake_case` untuk konvensi Python

---

## 3. 🏷️ Tipe Data

Python memiliki beberapa tipe data dasar:

| Tipe | Contoh | Keterangan |
|------|--------|------------|
| `str` | `"Hello"` | Teks/string |
| `int` | `19` | Bilangan bulat |
| `float` | `3.14` | Bilangan desimal |
| `bool` | `True` / `False` | Nilai kebenaran |

Cek tipe data menggunakan `type()`:

```python
nama = "Bagaskara"
umur = 19
tinggi = 170.5

print(type(nama))    # <class 'str'>
print(type(umur))    # <class 'int'>
print(type(tinggi))  # <class 'float'>
```

---

## 4. ➕ Operasi Aritmatika

| Operator | Nama | Contoh | Hasil |
|----------|------|--------|-------|
| `+` | Penjumlahan | `2 + 3` | `5` |
| `-` | Pengurangan | `2 - 3` | `-1` |
| `*` | Perkalian | `2 * 3` | `6` |
| `/` | Pembagian | `2 / 3` | `0.666...` |
| `%` | Modulus (sisa bagi) | `2 % 3` | `2` |
| `**` | Pangkat | `2 ** 3` | `8` |
| `//` | Pembagian bulat | `7 // 2` | `3` |

```python
print(2 + 3)   # 5
print(2 - 3)   # -1
print(2 * 3)   # 6
print(2 / 3)   # 0.6666...
print(2 % 3)   # 2
```

---

## 5. ⌨️ Input User

Fungsi `input()` membaca input dari pengguna. **Hasilnya selalu bertipe `str`!**

```python
nama = input("Masukkan nama anda: ")
print(nama)

umur = input("Masukkan umur anda: ")
print(type(umur))   # <class 'str'> ← bukan int!
```

> ⚠️ **Penting:** Meskipun user mengetik angka, `input()` tetap mengembalikan string. Gunakan **type casting** untuk mengubahnya.

---

## 6. 🔄 Type Casting

Mengubah tipe data dari satu tipe ke tipe lain.

| Fungsi | Keterangan | Contoh |
|--------|------------|--------|
| `int()` | Konversi ke integer | `int("5000")` → `5000` |
| `float()` | Konversi ke float | `float("3.14")` → `3.14` |
| `str()` | Konversi ke string | `str(700000)` → `"700000"` |

```python
harga_bawang = 15000
harga_tomat = "5000"

# Tanpa casting: ERROR (int + str tidak bisa!)
# Dengan casting: berhasil
print(harga_bawang + int(harga_tomat))   # 20000

harga_kupas = 700000
harga_kupas_str = str(harga_kupas)
print(type(harga_kupas_str))   # <class 'str'>
```

---

## 7. 📝 String Formatting

Dua cara utama memformat string di Python:

### Cara 1: Koma di `print()`
```python
a = 2
print("nilai a =", a)   # nilai a = 2
```

### Cara 2: f-string (Recommended ✅)
```python
a = 2
print(f"nilai a = {a}")   # nilai a = 2
```

> 💡 **Tips:** f-string lebih fleksibel, bisa menyisipkan ekspresi langsung: `f"hasil = {2 + 3}"`

---

## 8. ✅ Boolean & Operator Perbandingan

Boolean hanya memiliki 2 nilai: `True` atau `False`.

### Operator Perbandingan

| Operator | Arti | Contoh | Hasil |
|----------|------|--------|-------|
| `==` | Sama dengan | `6 == 5` | `False` |
| `!=` | Tidak sama | `6 != 5` | `True` |
| `>` | Lebih besar | `6 > 5` | `True` |
| `<` | Lebih kecil | `6 < 5` | `False` |
| `>=` | Lebih besar sama dengan | `6 >= 5` | `True` |
| `<=` | Lebih kecil sama dengan | `6 <= 5` | `False` |

### Operator Logika

| Operator | Arti | Contoh |
|----------|------|--------|
| `and` | DAN (kedua kondisi harus True) | `True and False` → `False` |
| `or` | ATAU (salah satu True sudah cukup) | `True or False` → `True` |
| `not` | NEGASI (kebalikan) | `not True` → `False` |

```python
# Contoh: Simulasi login
email = "budi@gmail.com" == "budi@gmail.com"     # True
password = "12345" == "12345"                      # True
print(email and password)                          # True → Login berhasil!
```

---

## 9. 🔀 Percabangan (if / elif / else)

Percabangan digunakan untuk membuat keputusan berdasarkan kondisi.

### Struktur Dasar

```python
if kondisi:
    # dijalankan jika kondisi True
elif kondisi_lain:
    # dijalankan jika kondisi_lain True
else:
    # dijalankan jika semua kondisi False
```

### Contoh: Program Kelulusan

```python
nilai = float(input("Masukkan nilai siswa: "))

if nilai >= 75:
    print("Selamat! Anda Lulus.")
else:
    print("Anda Tidak Lulus.")
```

### Contoh: Pilihan Menu Makan

```python
makan = "naspad"

if makan == "sate":
    print("aku beli sate")
elif makan == "naspad":
    print("beli naspad")
elif makan == "soto":
    print("beli soto")
else:
    print("balek rumah")
```

---

## 10. 🧮 Mini Project: Kalkulator dengan Pilihan Operator

Program ini menggabungkan semua konsep yang dipelajari:

```python
print("KALKULATOR SEDERHANA")

angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = int(input("Masukkan angka kedua: "))

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
else:
    print("Operator tidak valid! Gunakan +, -, *, atau /.")
```

**Konsep yang digunakan:**
- ✅ `input()` untuk membaca masukan user
- ✅ `float()` dan `int()` untuk type casting
- ✅ `if/elif/else` untuk percabangan
- ✅ f-string untuk formatting output
- ✅ Nested if (if di dalam if) untuk cek pembagian nol

---

## 📊 Alur Belajar Hari Ini

```
Print → Variabel → Tipe Data → Aritmatika → Input
                                                ↓
        Kalkulator ← Percabangan ← Boolean ← Casting
```

---

## 🎯 Key Takeaways

1. **Python itu dinamis** — tidak perlu deklarasi tipe data
2. **`input()` selalu mengembalikan string** — perlu casting ke `int()`/`float()` untuk perhitungan
3. **Indentasi itu penting** — Python menggunakan indentasi untuk blok kode (bukan `{}` seperti Java)
4. **f-string** adalah cara paling modern dan mudah untuk formatting string
5. **Selalu handle edge case** — contoh: cek pembagian dengan nol

---

## 📚 Referensi Tambahan

- [Python Official Docs](https://docs.python.org/3/)
- [W3Schools Python](https://www.w3schools.com/python/)
- [Google Colab](https://colab.research.google.com/) — IDE online yang digunakan saat kelas

---

> 📝 *Dokumentasi ini dibuat sebagai catatan belajar di CYBORG IT CENTER — Python & Machine Learning Track*
