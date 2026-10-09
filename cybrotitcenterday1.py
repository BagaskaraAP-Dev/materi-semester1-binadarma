print("Bagaskara Amukti Palapa")
print("Saya Tinggal Di Palembang")

# variable
nama = "BAGASKARA AMUKTI PALAPA"
umur = 19
tinggi = 170 

print(nama)
print(umur)
print(tinggi)

# tipe data
print(type(nama))
print(type(umur))
print(type(tinggi))

print("====================")
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 % 3)


nama_pertama = input("masukan nama anda : ")
print(nama_pertama)

umur_pertama = input("masukan umur anda : ")
print(type(umur_pertama))

# casting variable
harga_bawang = 15000
harga_tomat = "5000"

print(harga_bawang + int(harga_tomat))

harga_kupas_bawang = 700000
harga_kupas_bawang_str = str(harga_kupas_bawang)
print(type(harga_kupas_bawang_str))

print("=== KALKULATOR SEDERHANA ===")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("Hasil Penjumlahan (+):", angka1 + angka2)
print("Hasil Pengurangan (-):", angka1 - angka2)
print("Hasil Perkalian (*):", angka1 * angka2)
print("Hasil Pembagian (/):", angka1 / angka2)

# string formatting
a = 2
print("nilai a =", a) # cara formating string langsung koma setelah kutip
print(f'nilai a = {a}') # cara formating string dengan f-string

# boolean (tipe data yang hanya menghasilkan nilai true atau false)
islogin = False

if "budi@gmail.com" == "budi@gmail.com" and "12345" == "12345":
    islogin = True
    print(islogin)
else:
    islogin = False
    print(islogin)

cred = "budi@gmail.com" == "budi@gmail.com"
password = "12345" == "12345"
print(cred)
print(password)

angka_lebih = 6 > 5
print(angka_lebih)
angka_kurang = 6 < 5
print(angka_kurang)
angka_sama = 6 == 5
print(angka_sama)

#not equal
angka_tidak_sama = 6 != 5
print(angka_tidak_sama) 

#buatlah program sederhana untuk menghitung nilai kelulusan standart kelulusan 75 lulus jika nilai >= 75 dan tidak lulus jika nilai < 75
# Program Sederhana Menghitung Kelulusan

nilai = float(input("Masukkan nilai siswa: "))

if nilai >= 75:
    print("Selamat! Anda Lulus.")
else:
    print("Anda Tidak Lulus.")

makan = "naspad"
if makan == "sate":
    print("aku beli sate")
elif makan == "naspad":
    print("beli naspad")
elif makan == "soto":
    print("beli soto")
else:
    print("balek rumah")


# tugas update kalkulator agar bisa memilih operator +,-,x,/
print("KALKULATOR SEDERHANA")

angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = int(input("Masukkan angka kedua: "))

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Pembagian dengan nol dak diperbolehkan.")
else:
    print("Operator pacak valid! make +, -, *, atau /.")