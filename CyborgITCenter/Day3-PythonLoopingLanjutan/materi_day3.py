"""
==========================================================
  CYBORG IT CENTER — Day 3: While Loop Lanjutan & Logika
  Peserta : Bagaskara Amukti Palapa
  Tanggal : 16 Oktober 2026
  Bahasa  : Python 3
==========================================================
"""

# ========================================================
# 1. PERULANGAN WHILE DENGAN PENCACAH STANDAR (INCREMENT 1)
# ========================================================
print("=== 1. WHILE LOOP DASAR (INCREMENT 1) ===")
i = 0
while i <= 5:
    print(f"Iterasi ke-{i}")
    i = i + 1

print()

# ========================================================
# 2. WHILE LOOP DENGAN KELIPATAN TERTENTU (STEP INCREMENT)
# ========================================================
print("=== 2. WHILE LOOP STEP INCREMENT (+2) ===")
# Kasus A: Mencetak bilangan dari 2 hingga 5 dengan kenaikan 2 angka
counter = 2
while counter <= 5:
    print(f"Counter: {counter}")
    counter = counter + 2

print()

# Kasus B: Mencetak deret bilangan mulai dari 7 hingga 20 bertambah 2
print("=== Deret Bilangan Ganjil (7 - 20) ===")
j = 7
while j <= 20:
    print(f"Nilai j: {j}")
    j = j + 2

print()

# ========================================================
# 3. WHILE LOOP HITUNG MUNDUR (DECREMENT / COUNTDOWN)
# ========================================================
print("=== 3. WHILE LOOP COUNTDOWN ===")
detik = 5
while detik >= 1:
    print(f"Hitung mundur: {detik} detik...")
    detik -= 1

print("Roket Berhasil Meluncur!\n")

# ========================================================
# 4. GAME TEBAK ANGKA: SENTINEL WHILE LOOP
# ========================================================
print("=== 4. TEBAK ANGKA DENGAN SENTINEL CONDITION ===")
angka_rahasia = 7
tebakan = 0

print("Petunjuk: Angka rahasia antara 1 sampai 10.")
# Perulangan berjalan selama tebakan belum sama dengan rahasia
# Catatan: Bagian ini di-comment agar script dapat dieksekusi non-interaktif
"""
while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka: "))
    if tebakan != angka_rahasia:
        print("Tebakan salah, ayo coba lagi!")

print("Tebakan benar! Angka rahasia adalah 7.\n")
"""

# ========================================================
# 5. GAME TEBAK ANGKA: WHILE TRUE & BREAK STATEMENT
# ========================================================
print("=== 5. TEBAK ANGKA DENGAN WHILE TRUE & BREAK ===")
"""
rahasia = 7
while True:
    tebakan = int(input("Masukkan tebakanmu: "))
    if tebakan == rahasia:
        print("Selamat! Tebakanmu tepat sekali.")
        break
    else:
        print("Masih belum tepat. Coba lagi!")
"""

# ========================================================
# 6. AKUMULATOR DENGAN WHILE LOOP
# ========================================================
print("=== 6. AKUMULATOR PENJUMLAHAN DERET ===")
total = 0
k = 1
while k <= 5:
    total += k
    print(f"Menambahkan {k}, subtotal = {total}")
    k += 1

print(f"Total akhir penjumlahan 1 sampai 5: {total}\n")
print("Sesi materi Day 3 selesai dengan sukses!")
