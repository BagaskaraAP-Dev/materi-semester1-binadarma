# 📘 CYBORG IT CENTER — Day 4: Python Match-Case Statement

> **Platform:** Visual Studio Code / Terminal  
> **Bahasa:** Python 3 (Python 3.10+)  
> **Topik:** Structural Pattern Matching (`match ... case ...`)

---

## 📋 Daftar Materi

| No | File | Topik | Deskripsi |
|:--:|------|-------|-----------|
| 1 | `01_dasar_match_case.py` | **Sintaks Dasar Match** | Menggantikan struktur `if..elif..else` bertingkat dengan `match-case` |
| 2 | `02_nilai_default_underscore.py` | **Nilai Default (`_`)** | Menggunakan wildcard underscore `_` sebagai aksi fallback (seperti `else`) |
| 3 | `03_gabungkan_nilai_or.py` | **Menggabungkan Nilai (`\|`)** | Operator pipe `\|` untuk mencocokkan beberapa nilai dalam satu case |
| 4 | `04_guard_kondisi_if.py` | **Guard Clause (`if`)** | Menambahkan pengaman / kondisi ekstra dengan statemen `if` pada case |
| 5 | `05_studi_kasus_menu_interaktif.py` | **Studi Kasus Interaktif** | Menggabungkan seluruh konsep match-case dengan input dinamis pengguna |

---

## 1. 🔍 Konsep Dasar Pernyataan Match (`match ... case`)

Pernyataan `match` diperkenalkan mulai **Python 3.10**. Fitur ini mengevaluasi sebuah nilai ekspresi sekali, lalu membandingkannya dengan pola di setiap blok `case`. Jika ada yang cocok, blok kode di dalam case tersebut akan langsung dijalankan.

### Sintaks Dasar:
```python
match ekspresi:
    case nilai_1:
        # Blok kode dijalankan jika cocok dengan nilai_1
    case nilai_2:
        # Blok kode dijalankan jika cocok dengan nilai_2
    case _:
        # Blok default jika tidak ada case yang cocok
```

---

## 2. 🛡️ Nilai Default (`case _:`)
- Karakter underscore `_` berfungsi sebagai nilai default (wildcard).
- `case _:` akan selalu cocok dengan nilai apa pun.
- **Penting:** Selalu letakkan `case _:` di baris case paling bawah agar berfungsi layaknya blok `else`.

---

## 3. 🔗 Menggabungkan Nilai dengan Operator Pipe (`|`)
- Karakter pipa `|` berfungsi sebagai operator **OR** di dalam evaluasi case.
- Contoh: `case 1 | 2 | 3 | 4 | 5:` berarti jika nilai adalah 1, 2, 3, 4, ATAU 5.

---

## 4. 🔀 Guard Clause (Statemen `if` dalam Case)
- Anda dapat menyematkan kondisi `if` langsung pada baris `case`.
- Blok kode hanya akan berjalan jika nilainya cocok **DAN** kondisi `if` bernilai `True`.
- Contoh:
  ```python
  case 1 | 2 | 3 | 4 | 5 if bulan == 4:
      print("Hari kerja di bulan April")
  ```

---

## 🚀 Cara Menjalankan di Terminal

Masuk terlebih dahulu ke foldernya:
```powershell
cd "Day4-MATCH,FORLOOPS,LISTS\01-PythonMatch"
```

Lalu jalankan file yang diinginkan menggunakan launcher `py`:
```powershell
py 01_dasar_match_case.py
py 02_nilai_default_underscore.py
py 03_gabungkan_nilai_or.py
py 04_guard_kondisi_if.py
py 05_studi_kasus_menu_interaktif.py
```
