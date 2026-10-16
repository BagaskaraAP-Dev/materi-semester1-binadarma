"""
Studi Kasus 2: Hitung Mundur Peluncuran Roket
Konsep       : While Loop Decrement (Countdown)
Deskripsi    : Menampilkan hitung mundur dari 5 hingga 1 detik,
               kemudian menampilkan pesan roket siap meluncur.
"""

detik = 5  # Waktu mulai hitung mundur

while detik >= 1:
    print(detik)
    detik -= 1  # Kurangi 1 detik setiap iterasi

print("Roket Meluncur!")
