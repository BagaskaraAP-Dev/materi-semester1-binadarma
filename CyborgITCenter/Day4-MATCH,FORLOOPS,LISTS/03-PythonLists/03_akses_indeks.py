# 03_akses_indeks.py
# Mengakses Item List dengan Indeks

# Item pertama punya indeks [0], item kedua [1], dst.
# Indeks negatif dimulai dari belakang: [-1] = item terakhir.

warna = ["merah", "hijau", "biru", "kuning", "ungu"]

print("Item pertama  (indeks 0) :", warna[0])
print("Item kedua    (indeks 1) :", warna[1])
print("Item ketiga   (indeks 2) :", warna[2])
print("Item terakhir (indeks -1):", warna[-1])

# Slicing: mengambil potongan list dari indeks tertentu
# Formatnya: list[mulai : sebelum]
print("\nSlicing [1:4]:", warna[1:4])   # indeks 1, 2, 3
print("Slicing [:3] :", warna[:3])      # indeks 0, 1, 2
print("Slicing [2:] :", warna[2:])      # indeks 2 sampai akhir
