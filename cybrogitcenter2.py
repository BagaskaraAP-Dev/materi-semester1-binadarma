a=7
b=8

c=0
c=a
a=b
b=c
print(a)
print(b)

#variabel kelas alpro dasar 
# a=8,b=10,c=11,d=5
# jika ingin a=5,b=8,c=10,d=11 itu bagaimana script

a = 8
b = 10
c = 11
d = 5

print(f"pertama: a = {a}, b = {b}, c = {c}, d = {d}")
temp = d   # 5 dititipakan dulu
d = c      # d = 11
c = b      # c = 10
b = a      # b = 8
a = temp   # a = 5

print(f"kedua: a = {a}, b = {b}, c = {c}, d = {d}")

#pengulangan
angka = 0
while angka <= 5:
    print(angka)
    angka += 1

# ada variable untuk input_user dan while condition menggunakan while != exit selama user tidak ketik exit
# input selalu terjadi

input_user = ""

while input_user != "exit":
    input_user = input("Ketik sesuatu (ketik 'exit' untuk keluar): ")
    print("menghasilkan:", input_user)
print("program finish.")

#membuat game tebak angka sederhana
import random
angka = random.randint(1, 10)
while True:
    tebakan = int(input("Tebak angka antara 1 sampai 10: "))
    if tebakan == angka:
        print("Tebakan Anda benar.")
        break
    else:
        print("Tebakan Anda salah")

# ada variable untuk input_user dan while condition menggunakan while != exit selama user tidak ketik exit
# input selalu terjadi

input_user = 0

while input_user != 5:
    input_user = int(input("masukan tebakan: "))
while input_user != 5:
    input_user = int(input("masukan tebakan: "))
    print(f"inputan kamu salah {input_user}")

print(f"inputan kamu benar {input_user}")

# buat menu menu sederhana untuk membeli minuman kopi
# dan munculkan hasil dari pilihan menu pengguna

# Program menu sederhana untuk membeli minuman kopi sederhana 
print("="*5)
print("1. espresso")
print("2. americano")
print("3. butterscotch")
print("4. exit")
print("="*5)
input_user = 0
input_user = int(input("Masukkan pilihan anda: "))
while input_user != 4:
    if input == 1:
        print("Anda memilih espresso")
    elif input == 2:
        print("Anda memilih americano")
    elif input == 3:
        print("Anda memilih butterscotch")


# ini adalah dokumentasi hari kedua di cybrogitcenter
#next materi
#perulangan for_range 
#kontrol dan nested loop docx
#pengenalan list dan tuple