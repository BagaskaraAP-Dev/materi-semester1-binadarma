"""
Studi Kasus 5: Kasir Toko Donat Bu Ani
Konsep       : Sentinel Loop (Berhenti pada input khusus 0) & Akumulator
Deskripsi    : Menghitung total akumulasi penjualan donat pelanggan.
               Kasir terus memasukkan jumlah donat hingga angka 0 dimasukkan.
"""

total = 0
donat = int(input("Masukkan jumlah donat yang dibeli (ketik 0 untuk selesai): "))

while donat != 0:
    total += donat  # Tambahkan ke total akumulasi
    donat = int(input("Masukkan jumlah donat yang dibeli (ketik 0 untuk selesai): "))

print(f"Total donat yang terjual: {total}")
