# 📘 CYBORG IT CENTER — Day 5: Python List (Input, Sort & Reverse)

> **Tanggal:** 27 Oktober 2026  
> **Peserta:** Bagaskara Amukti Palapa  
> **NIM:** 261420008  
> **Bahasa:** Python 3  

---

## 📋 Daftar File

| File | Topik | Ringkasan |
|------|-------|-----------|
| `01_insert_list.py` | `insert()` | Menyisipkan item ke indeks tertentu. |
| `02_input_list_for.py` | `for` + `append()` | Mengisi list dari input sebanyak 5 kali. |
| `03_input_list_while.py` | `while` + validasi | Mengisi list sampai 5 data positif terkumpul. |
| `04_sort_dan_reverse.py` | `sort()`, `sorted()`, `reverse=True` | Mengurutkan naik/turun dan membalik list. Berisi perbaikan bug `print(nilai.sort)`. |
| `05_sorting_manual.py` | Sorting manual | Mengurutkan list tanpa `sort()` dengan mencari angka terkecil berulang kali. |

---

## 1. Menyisipkan Item dengan `insert()`

`insert(indeks, item)` menaruh item di posisi yang diminta. Item yang sudah ada di posisi itu dan sesudahnya bergeser ke kanan.

```python
teks = ['a', 'c', 'd']
teks.insert(1, 'b')
print(teks)  # ['a', 'b', 'c', 'd']
```

| Method | Posisi item baru |
|--------|------------------|
| `append(x)` | Selalu di akhir list |
| `insert(i, x)` | Di indeks `i` |

---

## 2. Mengisi List dari Input: `for` vs `while`

Keduanya mulai dari list kosong `[]` lalu menambah data dengan `append()`. Bedanya ada pada kapan perulangan berhenti.

```python
# for: input diminta TEPAT 5 kali
for i in range(5):
    data = int(input("masukan data : "))
    nilai.append(data)

# while: input diminta TERUS sampai list berisi 5 data
while len(nilai) < 5:
    data = int(input("masukan data : "))
    if data > 0:
        nilai.append(data)
```

| | `for i in range(5)` | `while len(nilai) < 5` |
|---|---|---|
| Jumlah input diminta | Selalu 5 kali | Bisa lebih dari 5 kali |
| Kalau ada data tidak valid | Data dibuang, isi list jadi kurang dari 5 | Data dibuang, pengguna diminta isi ulang |
| Isi list di akhir | 0 sampai 5 data | Pasti 5 data |

Jadi kalau jumlah datanya **harus pas**, pakai `while len(...) < n`.

---

## 3. Mengurutkan: `sort()` vs `sorted()`

```python
angka = [3, 1, 4, 1, 5]

sorted(angka)   # [1, 1, 3, 4, 5]  -> list BARU, angka tetap [3, 1, 4, 1, 5]
angka.sort()    # angka berubah jadi [1, 1, 3, 4, 5], hasilnya None
```

| | `sorted(list)` | `list.sort()` |
|---|---|---|
| List asli | Tidak berubah | Berubah |
| Nilai yang dikembalikan | List baru yang sudah urut | `None` |
| Cocok untuk | Membandingkan / menampilkan tanpa mengubah data | Mengurutkan data itu sendiri |

Karena `sorted()` tidak mengubah list asli, ia bisa dipakai untuk mengecek apakah list sudah urut:

```python
if nilai != sorted(nilai):
    nilai.sort()
    print("setelah diurutkan:", nilai)
```

---

## 4. 🐞 Perbaikan Bug: `print(nilai.sort)`

Kode awal di kelas:

```python
print(nilai.sort)
```

Hasilnya **bukan** isi list, melainkan:

```
<built-in method sort of list object at 0x000001A2B3C4D5E0>
```

**Penyebab:** tanpa tanda kurung `()`, method `sort` tidak dijalankan. Python hanya mencetak "alamat" method-nya.

Ditambah kurung pun masih salah:

```python
print(nilai.sort())   # None
```

Karena `sort()` mengubah list secara langsung dan tidak mengembalikan apa-apa (`None`).

**Perbaikan:** urutkan dulu, baru cetak list-nya.

```python
nilai.sort()
print(nilai)          # [1, 2, 3, 5, 8]
```

Atau kalau ingin dalam satu baris, pakai `sorted()`:

```python
print(sorted(nilai))  # [1, 2, 3, 5, 8]
```

---

## 5. 🔄 Urut Besar ke Kecil dengan `reverse=True`

Secara default `sort()` dan `sorted()` mengurutkan dari kecil ke besar (*ascending*). Tambahkan parameter `reverse=True` untuk mengurutkan dari besar ke kecil (*descending*).

```python
nilai = [5, 2, 8, 1, 3]

nilai.sort(reverse=True)
print(nilai)                          # [8, 5, 3, 2, 1]

print(sorted([5, 2, 8, 1, 3], reverse=True))  # [8, 5, 3, 2, 1]
```

### ⚠️ Jangan tertukar: `reverse=True` vs `reverse()`

| Kode | Yang terjadi | `[3, 1, 4, 1, 5]` menjadi |
|------|--------------|---------------------------|
| `angka.sort(reverse=True)` | **Mengurutkan** dari besar ke kecil | `[5, 4, 3, 1, 1]` |
| `angka.reverse()` | **Membalik posisi** saja (terakhir jadi pertama), tidak mengurutkan | `[5, 1, 4, 1, 3]` |

`reverse()` hanya menghasilkan urutan besar ke kecil kalau list-nya **sudah diurutkan naik** sebelumnya:

```python
angka = [3, 1, 4, 1, 5]
angka.sort()      # [1, 1, 3, 4, 5]
angka.reverse()   # [5, 4, 3, 1, 1]  -> sama dengan sort(reverse=True)
```

---

## 6. Sorting Manual (Tanpa `sort()`)

Idenya: ambil angka **terkecil** satu per satu dan pindahkan ke list baru. Karena yang diambil selalu yang terkecil, list baru otomatis urut.

```python
list_urut = []
for i in range(len(nilai)):
    terkecil = nilai[0]
    for j in nilai:
        if j < terkecil:
            terkecil = j
    list_urut.append(terkecil)
    nilai.remove(terkecil)
```

### Jalannya program dengan input `[5, 2, 8, 1, 3]`

| Putaran `i` | Isi `nilai` sebelum | `terkecil` | Isi `list_urut` sesudah |
|:-----------:|---------------------|:----------:|-------------------------|
| 0 | `[5, 2, 8, 1, 3]` | 1 | `[1]` |
| 1 | `[5, 2, 8, 3]` | 2 | `[1, 2]` |
| 2 | `[5, 8, 3]` | 3 | `[1, 2, 3]` |
| 3 | `[5, 8]` | 5 | `[1, 2, 3, 5]` |
| 4 | `[8]` | 8 | `[1, 2, 3, 5, 8]` |

Catatan:
- `range(len(nilai))` dihitung **sekali** di awal (5 putaran), jadi aman walaupun `nilai` terus mengecil karena `remove()`.
- Setelah selesai, `nilai` menjadi kosong `[]` karena semua isinya sudah dipindah.
- Untuk urut **besar ke kecil** (versi manual dari `reverse=True`), ganti `j < terkecil` menjadi `j > terkecil` agar yang dicari angka terbesar.

---

## 🚀 Eksekusi

```powershell
cd "CyborgITCenter\DAY5-Pyton List"
py 01_insert_list.py
py 02_input_list_for.py
py 03_input_list_while.py
py 04_sort_dan_reverse.py
py 05_sorting_manual.py
```
