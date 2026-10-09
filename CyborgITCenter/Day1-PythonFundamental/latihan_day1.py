"""
==========================================================
  CYBORG IT CENTER — Day 1: Latihan Mandiri
  Nama  : Bagaskara Amukti Palapa
  Tanggal: 9 Oktober 2026
  
  Latihan ini berisi soal-soal untuk mengasah pemahaman
  materi Python Fundamental yang sudah dipelajari.
==========================================================
"""

# =====================================================
# LATIHAN 1: Variabel dan Tipe Data
# =====================================================
# Instruksi: Buat variabel untuk data diri kamu,
#            lalu cetak semuanya dengan format yang rapi.

print("=" * 50)
print("LATIHAN 1: Biodata")
print("=" * 50)

nama = "Bagaskara Amukti Palapa"
umur = 19
jurusan = "Teknik Informatika"
universitas = "Universitas Bina Darma"
kota = "Palembang"
hobi = "Coding"

print(f"Nama       : {nama}")
print(f"Umur       : {umur} tahun")
print(f"Jurusan    : {jurusan}")
print(f"Universitas: {universitas}")
print(f"Kota       : {kota}")
print(f"Hobi       : {hobi}")
print(f"Tipe nama  : {type(nama)}")
print(f"Tipe umur  : {type(umur)}")


# =====================================================
# LATIHAN 2: Operasi Aritmatika Lengkap
# =====================================================
# Instruksi: Hitung semua operasi aritmatika dari 2 angka

print("\n" + "=" * 50)
print("LATIHAN 2: Operasi Aritmatika Lengkap")
print("=" * 50)

x = 17
y = 5

print(f"x = {x}, y = {y}")
print(f"Penjumlahan  : {x} + {y} = {x + y}")
print(f"Pengurangan  : {x} - {y} = {x - y}")
print(f"Perkalian    : {x} * {y} = {x * y}")
print(f"Pembagian    : {x} / {y} = {x / y}")
print(f"Modulus       : {x} % {y} = {x % y}")
print(f"Pangkat      : {x} ** {y} = {x ** y}")
print(f"Bagi Bulat   : {x} // {y} = {x // y}")


# =====================================================
# LATIHAN 3: Type Casting
# =====================================================
# Instruksi: Praktekkan konversi tipe data

print("\n" + "=" * 50)
print("LATIHAN 3: Type Casting")
print("=" * 50)

harga_str = "25000"
jumlah_str = "3"

# Tanpa casting (gabungan string)
print(f"Tanpa casting : {harga_str + jumlah_str}")  # "250003"

# Dengan casting (perhitungan matematis)
total = int(harga_str) * int(jumlah_str)
print(f"Dengan casting: {int(harga_str)} x {int(jumlah_str)} = {total}")
print(f"Total (string): Rp {str(total)}")


# =====================================================
# LATIHAN 4: Boolean dan Perbandingan
# =====================================================
# Instruksi: Praktekkan semua operator perbandingan

print("\n" + "=" * 50)
print("LATIHAN 4: Boolean & Perbandingan")
print("=" * 50)

a = 10
b = 7

print(f"a = {a}, b = {b}")
print(f"a == b  : {a == b}")    # False
print(f"a != b  : {a != b}")    # True
print(f"a > b   : {a > b}")     # True
print(f"a < b   : {a < b}")     # False
print(f"a >= b  : {a >= b}")    # True
print(f"a <= b  : {a <= b}")    # False

# Operator logika
print(f"\nTrue and False  = {True and False}")
print(f"True or False   = {True or False}")
print(f"not True        = {not True}")


# =====================================================
# LATIHAN 5: Program Penentuan Grade Nilai
# =====================================================
# Instruksi: Buat program yang menentukan grade berdasarkan nilai
# A = 85-100, B = 70-84, C = 55-69, D = 40-54, E = 0-39

print("\n" + "=" * 50)
print("LATIHAN 5: Penentuan Grade Nilai")
print("=" * 50)

nilai = 82  # Ganti dengan input() untuk interaktif
# nilai = float(input("Masukkan nilai (0-100): "))

if nilai >= 85:
    grade = "A"
    keterangan = "Sangat Baik"
elif nilai >= 70:
    grade = "B"
    keterangan = "Baik"
elif nilai >= 55:
    grade = "C"
    keterangan = "Cukup"
elif nilai >= 40:
    grade = "D"
    keterangan = "Kurang"
else:
    grade = "E"
    keterangan = "Sangat Kurang"

print(f"Nilai      : {nilai}")
print(f"Grade      : {grade}")
print(f"Keterangan : {keterangan}")
if nilai >= 55:
    print("Status     : LULUS [V]")
else:
    print("Status     : TIDAK LULUS [X]")


# =====================================================
# LATIHAN 6: Kalkulator Upgrade (dengan validasi)
# =====================================================
# Instruksi: Kalkulator yang sudah diperbaiki dengan validasi input

print("\n" + "=" * 50)
print("LATIHAN 6: Kalkulator Sederhana (Upgrade)")
print("=" * 50)

# Untuk demo, kita gunakan nilai langsung
# Untuk interaktif, ganti dengan input()
angka1 = 15.5
angka2 = 4.0
operator = "+"

# angka1 = float(input("Masukkan angka pertama: "))
# operator = input("Masukkan operator (+, -, *, /): ")
# angka2 = float(input("Masukkan angka kedua: "))

print(f"\nPerhitungan: {angka1} {operator} {angka2}")

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka1 * angka2
    print(f"Hasil: {hasil}")
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {hasil}")
    else:
        print("[ERROR] Pembagian dengan nol tidak diperbolehkan!")
else:
    print("[ERROR] Operator tidak valid! Gunakan: +, -, *, /")


# =====================================================
# LATIHAN 7: Program Diskon Belanja
# =====================================================
# Instruksi: Hitung total belanja dengan diskon
# Belanja >= 100000 = diskon 10%
# Belanja >= 50000  = diskon 5%
# Belanja < 50000   = tidak ada diskon

print("\n" + "=" * 50)
print("LATIHAN 7: Program Diskon Belanja")
print("=" * 50)

total_belanja = 150000  # Ganti dengan input() untuk interaktif

if total_belanja >= 100000:
    diskon = 0.10
    pesan = "Diskon 10%! Selamat!"
elif total_belanja >= 50000:
    diskon = 0.05
    pesan = "Diskon 5%!"
else:
    diskon = 0
    pesan = "Tidak ada diskon"

potongan = total_belanja * diskon
total_bayar = total_belanja - potongan

print(f"Total Belanja : Rp {total_belanja:,}")
print(f"Diskon        : {pesan}")
print(f"Potongan      : Rp {potongan:,.0f}")
print(f"Total Bayar   : Rp {total_bayar:,.0f}")


print("\n" + "=" * 50)
print(">> Selesai! Semua latihan berhasil dijalankan!")
print("=" * 50)
