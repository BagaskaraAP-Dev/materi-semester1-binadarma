"""
Konversi C ke Python — Kasus 7: Seleksi Masuk Wahana
Logika: Pengecekan multi-kondisi (usia minimal 12 tahun dan tinggi badan minimal 140 cm)
"""

usia = int(input("Masukkan usia (tahun): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))

# Periksa usia terlebih dahulu, lalu tinggi badan
if usia < 12:
    print("Usia belum cukup")
elif tinggi < 140:
    print("Tinggi belum cukup")
else:
    print("Boleh naik wahana")
