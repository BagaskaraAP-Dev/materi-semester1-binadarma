"""
Studi Kasus 6: Konfirmasi Pesan Minum Kantin
Konsep       : Infinite While Loop (while True) & Kondisi Terminasi String
Deskripsi    : Pencatatan jumlah pesanan es teh manis kantin.
               Program terus berjalan dan berhenti jika pengguna tidak mengetik 'y'/'Y'.
"""

jumlah_gelas = 0

while True:
    jumlah_gelas += 1
    print(f"Pesanan teh manis ke-{jumlah_gelas} berhasil dicatat.")
    
    jawaban = input("Apakah ingin memesan lagi? (y/t): ")
    if jawaban.lower() != 'y':
        break

print(f"Terima kasih! Total pesanan Anda: {jumlah_gelas} gelas.")
