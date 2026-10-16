"""
Konversi C ke Python — Kasus 2: Klasifikasi Bilangan Genap & Ganjil
Logika: Pengecekan sisa bagi menggunakan operator modulo % (angka % 2 == 0)
"""

angka = int(input("Masukkan sebuah bilangan bulat: "))

if angka % 2 == 0:
    print("Genap")
else:
    print("Ganjil")
