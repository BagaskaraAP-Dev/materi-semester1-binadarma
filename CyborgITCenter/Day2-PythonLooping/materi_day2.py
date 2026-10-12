"""
==========================================================
  CYBORG IT CENTER — Day 2: Python Looping & Variable
  Peserta : Bagaskara Amukti Palapa
  Tanggal : 12 Oktober 2026
  Bahasa  : Python 3
==========================================================
"""

import random

# ========================================================
# 1. PERTUKARAN NILAI VARIABEL (SWAPPING)
# ========================================================

# Contoh 1: Menukar 2 variabel menggunakan variabel sementara (temp)
print("=== 1. SWAP 2 VARIABEL ===")
a = 7
b = 8
print(f"Sebelum swap: a = {a}, b = {b}")

c = 0
c = a    # simpan nilai a ke c
a = b    # isi a dengan b
b = c    # isi b dengan c (nilai a awal)

print(f"Setelah swap: a = {a}, b = {b}\n")

# Contoh 2: Masalah Alpro Dasar — Swap 4 Variabel
# Nilai awal : a=8, b=10, c=11, d=5
# Nilai target: a=5, b=8, c=10, d=11
print("=== 2. SWAP 4 VARIABEL (ALPRO DASAR) ===")
a = 8
b = 10
c = 11
d = 5

print(f"Sebelum pergeseran: a = {a}, b = {b}, c = {c}, d = {d}")

# Menggeser nilai dengan menitipkan variabel terakhir ke temp
temp = d   # temp = 5 (nilai d disimpan)
d = c      # d = 11
c = b      # c = 10
b = a      # b = 8
a = temp   # a = 5

print(f"Setelah pergeseran: a = {a}, b = {b}, c = {c}, d = {d}\n")


# ========================================================
# 2. PENGULANGAN (WHILE LOOP) DASAR
# ========================================================

print("=== 3. WHILE LOOP DENGAN COUNTER ===")
# Mengulang selama kondisi angka <= 5 bernilai True
angka = 0
while angka <= 5:
    print(f"Angka ke-{angka}")
    angka += 1  # Increment agar tidak terjadi infinite loop

print("Pengulangan selesai!\n")


# ========================================================
# 3. WHILE LOOP BERBASIS SENTINEL / INPUT USER
# ========================================================

print("=== 4. WHILE LOOP DENGAN EXIT SENTINEL ===")
# Loop terus berjalan sampai pengguna mengetik kata 'exit'
input_user = ""
while input_user.lower() != "exit":
    input_user = input("Ketik sesuatu (ketik 'exit' untuk selesai): ")
    print(f"Menghasilkan: {input_user}")

print("Program sentinel selesai.\n")


# ========================================================
# 4. GAME TEBAK ANGKA RANDOM (WHILE TRUE & BREAK)
# ========================================================

print("=== 5. GAME TEBAK ANGKA SEDERHANA ===")
angka_rahasia = random.randint(1, 10)
percobaan = 0

while True:
    tebakan = int(input("Tebak angka antara 1 sampai 10: "))
    percobaan += 1
    if tebakan == angka_rahasia:
        print(f"Hebat! Tebakan Anda BENAR ({angka_rahasia}) dalam {percobaan} kali coba.")
        break
    else:
        print("Tebakan Anda salah, silakan coba lagi!")

print("Game tebak angka selesai.\n")


# ========================================================
# 5. VALIDASI INPUT DENGAN WHILE LOOP
# ========================================================

print("=== 6. VALIDASI INPUT ANGKA ===")
# Terus meminta input sampai pengguna memasukkan angka 5
input_tebakan = 0
while input_tebakan != 5:
    input_tebakan = int(input("Masukkan angka 5 untuk lanjut: "))
    if input_tebakan != 5:
        print(f"Inputan kamu salah: {input_tebakan}, coba lagi!")

print(f"Inputan kamu benar: {input_tebakan}! Berhasil lanjut.\n")


# ========================================================
# 6. MINI PROJECT: MENU PEMESANAN KOPI INTERAKTIF
# ========================================================

print("=== 7. MENU PEMESANAN KOPI ===")
pilihan = 0

while pilihan != 4:
    print("-" * 30)
    print("   WARUNG KOPI CYBORG")
    print("-" * 30)
    print("1. Espresso       (Rp 18.000)")
    print("2. Americano      (Rp 20.000)")
    print("3. Butterscotch   (Rp 25.000)")
    print("4. Keluar / Exit")
    print("-" * 30)

    try:
        pilihan = int(input("Masukkan pilihan menu (1-4): "))
    except ValueError:
        print("Mohon masukkan angka 1 sampai 4!")
        continue

    if pilihan == 1:
        print(">> Anda memilih: Espresso (Pesanan diproses!)")
    elif pilihan == 2:
        print(">> Anda memilih: Americano (Pesanan diproses!)")
    elif pilihan == 3:
        print(">> Anda memilih: Butterscotch (Pesanan diproses!)")
    elif pilihan == 4:
        print(">> Terima kasih telah berkunjung ke Warung Kopi Cyborg!")
    else:
        print(">> Pilihan tidak tersedia, silakan pilih nomor 1 - 4.")

print("\n=== PROGRAM DAY 2 SELESAI ===")
