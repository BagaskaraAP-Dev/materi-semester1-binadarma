"""
Studi Kasus 1: Celengan Koin Doni
Konsep       : While Loop Counter & Akumulasi Nilai
Deskripsi    : Doni menabung koin Rp 1.000 setiap kali menabung ke celengan.
               Program berhenti jika celengan mencapai atau melampaui Rp 5.000.
"""

tabungan = 0  # Inisialisasi celengan kosong

while tabungan < 5000:
    tabungan += 1000  # Menabung Rp 1.000 per putaran
    print(f"Tabungan: Rp {tabungan}")

print("Target tercapai!")
