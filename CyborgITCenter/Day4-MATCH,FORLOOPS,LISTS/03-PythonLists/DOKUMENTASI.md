# 📘 Materi: Python Lists

List digunakan untuk menyimpan beberapa item sekaligus dalam satu variabel.
List dibuat menggunakan tanda kurung siku `[]`.

---

## 📋 Daftar File

| File | Topik | Ringkasan |
|------|-------|-----------|
| `01_membuat_list.py` | Membuat List | Cara membuat list dan perbedaan 4 tipe koleksi di Python. |
| `02_sifat_list.py` | Sifat List | Tiga sifat utama: berurutan, bisa diubah, boleh duplikat. |
| `03_akses_indeks.py` | Akses Indeks & Slicing | Mengakses item dengan indeks positif, negatif, dan slicing. |
| `04_ubah_tambah_hapus.py` | Ubah, Tambah, Hapus | Operasi `append()`, `insert()`, `remove()`, `pop()`, `del`. |
| `05_panjang_dan_tipe_data.py` | `len()` & Tipe Campuran | Menghitung jumlah item dan menyimpan berbagai tipe data dalam satu list. |

---

## Sifat-Sifat List

### 1. Berurutan (Ordered)
Item di dalam list punya urutan tetap. Item baru yang ditambahkan masuk di posisi paling akhir.

### 2. Bisa Diubah (Changeable)
Kita bisa mengubah, menambah, dan menghapus item setelah list dibuat.

### 3. Boleh Duplikat (Allow Duplicates)
Karena list memakai indeks, list boleh punya item dengan nilai yang sama.

```python
angka = [10, 20, 30, 10, 30]  # angka 10 dan 30 muncul dua kali
```

---

## Indeks List

```
 Indeks positif:  [0]    [1]     [2]
                 "apel" "pisang" "ceri"
 Indeks negatif: [-3]   [-2]    [-1]
```

- Indeks dimulai dari `0` (item pertama).
- Indeks negatif `-1` merujuk ke item terakhir.

---

## 🚀 Eksekusi

```powershell
cd "Day4-MATCH,FORLOOPS,LISTS\03-PythonLists"
py 01_membuat_list.py
py 02_sifat_list.py
py 03_akses_indeks.py
py 04_ubah_tambah_hapus.py
py 05_panjang_dan_tipe_data.py
```
