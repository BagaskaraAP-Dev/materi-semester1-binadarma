"""
Studi Kasus 10: Penjumlahan Angka Positif / Akumulasi Jajan
Konsep        : Sentinel Akumulator (Exit saat 0)
Deskripsi     : Menghitung total belanja jajan yang diinput pengguna secara bertahap.
                Program berhenti dan menampilkan total belanja saat diinput angka 0.
"""

total = 0

while True:
    harga = int(input("Masukkan harga jajan (ketik 0 untuk selesai): Rp "))
    
    if harga == 0:
        break
    
    total += harga  # Akumulasi harga ke dalam total

print(f"Total belanja akhir: Rp {total}")
