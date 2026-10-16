"""
Studi Kasus 7: Tebak Angka Rahasia Brankas
Konsep       : While Loop Percabangan & Break Statement
Deskripsi    : Pengguna diminta menebak angka sandi rahasia brankas (angka 7).
               Perulangan terus berjalan hingga kombinasi sandi benar dimasukkan.
"""

sandi_rahasia = 7

while True:
    tebakan = int(input("Masukkan tebakan angka rahasia brankas: "))
    if tebakan == sandi_rahasia:
        break
    print("Sandi salah, coba lagi!")

print("Sandi Benar! Brankas Terbuka.")
