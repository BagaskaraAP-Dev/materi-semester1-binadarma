# 📘 Materi: Python For Loops

Perulangan `for` di Python digunakan untuk melakukan iterasi pada objek *sequence* (seperti `list`, `string`, `tuple`, `dictionary`, `set`, atau objek `range`).

---

## 📋 Daftar File

| File | Topik | Ringkasan |
|------|-------|-----------|
| `01_dasar_for_list.py` | Iterasi List | Membaca tiap elemen dari list tanpa variabel counter indeks manual. |
| `02_loop_string.py` | Iterasi String | Menelusuri setiap karakter huruf dalam teks string. |
| `03_break_statement.py` | Statemen `break` | Menghentikan loop secara paksa sebelum daftar elemen habis. |
| `04_continue_statement.py` | Statemen `continue` | Melewati (*skip*) iterasi saat ini dan lanjut ke elemen berikutnya. |
| `05_fungsi_range.py` | Fungsi `range()` | Membuat deret angka numerik dengan kontrol `start`, `stop`, dan `step`. |

---

## 1. Iterasi Koleksi (Sequence)

Python tidak membutuhkan deklarasi indeks awal (seperti `int i = 0` di C/Java). Variabel loop langsung menampung nilai elemen yang sedang diproses.

```python
buah = ["apel", "pisang", "ceri"]
for item in buah:
    print(item)
```

---

## 2. Iterasi String

String diperlakukan sebagai urutan karakter:

```python
for huruf in "pisang":
    print(huruf)
```

---

## 3. Kontrol Loop: `break` vs `continue`

- **`break`**: Keluar total dari perulangan.
- **`continue`**: Menghentikan putaran saat ini dan langsung melompat ke putaran berikutnya.

```python
# break: berhenti total ketika ketemu "pisang"
for x in fruits:
    if x == "pisang":
        break
    print(x)

# continue: lewati "pisang", lanjutkan item setelahnya
for x in fruits:
    if x == "pisang":
        continue
    print(x)
```

---

## 4. Fungsi `range()`

Digunakan untuk menentukan berapa kali blok kode dieksekusi berdasarkan deret angka.

- `range(stop)`: Mulai dari `0` sampai `stop - 1`.
- `range(start, stop)`: Mulai dari `start` sampai `stop - 1`.
- `range(start, stop, step)`: Kenaikan nilai sebesar `step`.

```python
for i in range(6):       # 0, 1, 2, 3, 4, 5
    print(i)

for i in range(2, 6):    # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):# 0, 2, 4, 6, 8
    print(i)
```

---

## 🚀 Eksekusi

```powershell
cd "Day4-MATCH,FORLOOPS,LISTS\02-PythonForLoops"
py 01_dasar_for_list.py
py 02_loop_string.py
py 03_break_statement.py
py 04_continue_statement.py
py 05_fungsi_range.py
```
