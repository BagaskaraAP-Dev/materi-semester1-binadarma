"""
Konversi C ke Python — Kasus 6: Tarif Parkir Bertingkat
Logika: Pengecekan interval durasi jam parkir bertingkat
        - <= 2 jam  : Rp 5.000
        - <= 5 jam  : Rp 10.000
        - > 5 jam   : Rp 15.000
"""

jam = float(input("Masukkan jumlah jam parkir: "))

# Pengecekan durasi parkir
if jam <= 2:
    tarif = 5000
elif jam <= 5:
    tarif = 10000
else:
    tarif = 15000

print(f"Tarif parkir yang harus dibayar: Rp {tarif:,}")
