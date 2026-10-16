"""
Konversi C ke Python — Kasus 5: Perhitungan Diskon Belanja Kasir
Logika: Diskon 10% jika total belanja >= Rp 100.000
"""

total_belanja = float(input("Masukkan total belanja: Rp "))

if total_belanja >= 100000:
    diskon = 0.10 * total_belanja
    total_bayar = total_belanja - diskon
else:
    total_bayar = total_belanja

print(f"Total yang harus dibayar: Rp {total_bayar:,.0f}")
