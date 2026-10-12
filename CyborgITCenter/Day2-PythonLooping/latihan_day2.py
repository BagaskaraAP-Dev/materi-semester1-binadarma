"""
==========================================================
  CYBORG IT CENTER — Day 2: Latihan Mandiri
  Nama    : Bagaskara Amukti Palapa
  Tanggal : 12 Oktober 2026
  Bahasa  : Python 3
  
  Latihan ini berisi soal-soal implementasi materi:
  1. Variabel Swapping (Manual & Pythonic)
  2. While Loop & Counter
  3. Sentinel Loop & Validasi Input
  4. Random Guess Game dengan Clue & Kesempatan
  5. Mini Project Kasir Menu Warung Kopi
==========================================================
"""

import random

# ========================================================
# LATIHAN 1: Pertukaran Variabel (Swapping)
# ========================================================
print("=" * 55)
print("LATIHAN 1: Teknik Penukaran Variabel")
print("=" * 55)

# Kasus A: Tukar 2 variabel cara manual vs cara Pythonic
x = 100
y = 200
print(f"Nilai mula-mula  : x = {x}, y = {y}")

# 1. Cara klasik (variabel penampung temp)
temp = x
x = y
y = temp
print(f"Hasil tukar klasik (temp) : x = {x}, y = {y}")

# 2. Cara Pythonic (Tuple unpacking)
x, y = y, x
print(f"Hasil tukar pythonic (x,y=y,x): x = {x}, y = {y}")

# Kasus B: Rotasi 3 variabel (a -> b -> c -> a)
p = "Merah"
q = "Kuning"
r = "Hijau"
print(f"\nSebelum rotasi : p={p}, q={q}, r={r}")
p, q, r = r, p, q
print(f"Setelah rotasi : p={p}, q={q}, r={r}\n")


# ========================================================
# LATIHAN 2: Deret Angka & Countdown Menggunakan While
# ========================================================
print("=" * 55)
print("LATIHAN 2: Pola Bilangan & Countdown")
print("=" * 55)

# A. Deret bilangan genap antara 2 sampai 20
print("Deret bilangan genap 2 sampai 20:")
bil = 2
while bil <= 20:
    print(bil, end=" ")
    bil += 2
print("\n")

# B. Countdown peluncuran roket
print("Hitung mundur peluncuran:")
hitung = 5
while hitung > 0:
    print(f"T-minus {hitung} detik...")
    hitung -= 1
print("🚀 BLAST OFF! Meluncur!\n")


# ========================================================
# LATIHAN 3: Akumulasi Total Angka (Sentinel Value)
# ========================================================
print("=" * 55)
print("LATIHAN 3: Akumulator Penjumlahan Bilangan")
print("=" * 55)
print("Program ini menjumlahkan angka yang dimasukkan.")
print("Ketik angka 0 untuk berhenti dan melihat hasil akhir.")

total = 0
banyak_angka = 0

while True:
    try:
        angka_masuk = float(input("Masukkan angka (0 untuk selesai): "))
    except ValueError:
        print("Input harus berupa angka!")
        continue

    if angka_masuk == 0:
        break

    total += angka_masuk
    banyak_angka += 1

rata_rata = (total / banyak_angka) if banyak_angka > 0 else 0
print(f">> Total angka dimasukkan : {banyak_angka}")
print(f">> Jumlah total nilai     : {total}")
print(f">> Rata-rata              : {rata_rata:.2f}\n")


# ========================================================
# LATIHAN 4: Game Tebak Angka dengan Clue & 3 Kesempatan
# ========================================================
print("=" * 55)
print("LATIHAN 4: Game Tebak Angka (Maksimal 3 Kesempatan)")
print("=" * 55)

rahasia = random.randint(1, 20)
maks_nyawa = 3
nyawa = maks_nyawa
menang = False

print(f"Saya menyimpan angka rahasia antara 1 sampai 20.")
print(f"Kamu memiliki {maks_nyawa} kesempatan untuk menebak!\n")

while nyawa > 0:
    try:
        tebak = int(input(f"Sisa nyawa [{nyawa}]. Masukkan tebakan: "))
    except ValueError:
        print("Harap masukkan bilangan bulat!")
        continue

    if tebak == rahasia:
        menang = True
        print(f"🎉 SELAMAT! Kamu berhasil menebak angka {rahasia}!")
        break
    elif tebak < rahasia:
        print("💡 Clue: Angka rahasia LEBIH BESAR.")
    else:
        print("💡 Clue: Angka rahasia LEBIH KECIL.")

    nyawa -= 1

if not menang:
    print(f"❌ Yah, kesempatanmu habis! Angka rahasianya adalah: {rahasia}\n")
else:
    print()


# ========================================================
# LATIHAN 5: Mini Kasir Menu Minuman Interaktif
# ========================================================
print("=" * 55)
print("LATIHAN 5: Aplikasi Kasir Menu Minuman Interaktif")
print("=" * 55)

menu_kopi = {
    1: ("Espresso", 18000),
    2: ("Americano", 20000),
    3: ("Butterscotch Latte", 25000),
    4: ("Caramel Macchiato", 28000)
}

pesanan = []
total_bayar = 0

while True:
    print("\n--- DAFTAR MENU WARUNG KOPI ---")
    for nomor, (nama_menu, harga) in menu_kopi.items():
        print(f"{nomor}. {nama_menu:<20} Rp {harga:>6,}")
    print("5. Selesai Memesan & Cetak Struk")
    print("0. Batal Pesan & Keluar")

    try:
        pilih = int(input("Pilih menu (0-5): "))
    except ValueError:
        print("Input harus angka!")
        continue

    if pilih == 0:
        print("Pesanan dibatalkan. Sampai jumpa!")
        break
    elif pilih == 5:
        if not pesanan:
            print("Anda belum memesan apapun.")
            break
        print("\n" + "=" * 35)
        print("       STRUK PEMBAYARAN")
        print("=" * 35)
        for item, harga, qty in pesanan:
            subtotal = harga * qty
            print(f"{item:<18} x{qty}  Rp {subtotal:>7,}")
        print("-" * 35)
        print(f"TOTAL AKHIR           : Rp {total_bayar:>7,}")
        print("=" * 35)
        print("Terima kasih atas kunjungan Anda!\n")
        break
    elif pilih in menu_kopi:
        nama_item, harga_item = menu_kopi[pilih]
        try:
            qty = int(input(f"Berapa jumlah '{nama_item}' yang ingin dipesan? "))
            if qty <= 0:
                print("Jumlah pesanan harus lebih dari 0!")
                continue
        except ValueError:
            print("Jumlah harus berupa angka!")
            continue

        pesanan.append((nama_item, harga_item, qty))
        total_bayar += harga_item * qty
        print(f"✅ Ditambahkan: {qty}x {nama_item} (Subtotal: Rp {harga_item * qty:,})")
    else:
        print("Menu tidak ditemukan, silakan masukkan nomor 1 - 5.")

print("Program Latihan Mandiri Day 2 selesai.")
