"""
Konversi C ke Python — Kasus 4: Penentuan Kategori Nilai Huruf
Logika: Percabangan bertingkat if-elif-else dari nilai batas tertinggi ke terendah
"""

# Menerima input nilai siswa (0-100)
nilai = int(input("Masukkan nilai siswa (0-100): "))

# Urutan pengecekan dimulai dari batas nilai tertinggi
if nilai >= 90:
    print("Kategori A")
elif nilai >= 80:
    print("Kategori B")
elif nilai >= 70:
    print("Kategori C")
else:
    print("Kategori D")
