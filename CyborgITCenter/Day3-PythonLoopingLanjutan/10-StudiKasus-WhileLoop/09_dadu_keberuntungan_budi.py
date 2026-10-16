"""
Studi Kasus 9: Dadu Keberuntungan Budi
Konsep       : While Loop Target Match & Break
Deskripsi    : Budi melempar dadu (angka 1 sampai 6) berulang kali
               sampai mendapatkan angka keberuntungan 6.
"""

while True:
    dadu = int(input("Masukkan angka hasil lemparan dadu (1-6): "))
    if dadu == 6:
        break
    print("Belum beruntung, coba lagi!")

print("Hore, dapat 6!")
