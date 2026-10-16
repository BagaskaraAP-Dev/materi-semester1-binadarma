"""
==========================================================
  CYBORG IT CENTER — Day 3: Latihan Mandiri & Eksplorasi
  Nama    : Bagaskara Amukti Palapa
  Tanggal : 16 Oktober 2026
  Bahasa  : Python 3

  Menu interaktif pengujian konsep while loop & studi kasus:
  1. Deret Step Increment (+2 dan +100)
  2. Countdown Peluncuran Roket
  3. Simulasi Celengan Doni (Target Rp 5.000)
  4. Game Tebak Angka Rahasia (While Sentinel vs While Break)
  5. Validasi Input Nilai Siswa (0 - 100)
  6. Kasir Toko Donat Bu Ani
  7. Kasir Akumulasi Jajan (Sentinel 0)
==========================================================
"""

def demo_step_increment():
    print("\n--- [Demo 1] Step Increment ---")
    print("Mencetak bilangan genap dari 2 sampai 10:")
    num = 2
    while num <= 10:
        print(num, end=" ")
        num += 2
    print("\n")


def demo_countdown():
    print("\n--- [Demo 2] Countdown Roket ---")
    detik = 5
    while detik >= 1:
        print(f"T-minus: {detik} detik...")
        detik -= 1
    print("🚀 Wush! Roket Berhasil Meluncur!\n")


def demo_celengan():
    print("\n--- [Demo 3] Simulasi Celengan Doni ---")
    celengan = 0
    target = 5000
    hari = 1
    while celengan < target:
        celengan += 1000
        print(f"Hari {hari}: Masuk koin Rp 1.000 | Saldo = Rp {celengan:,}")
        hari += 1
    print("🎉 Target celengan tercapai!\n")


def game_tebak_angka():
    print("\n--- [Demo 4] Game Tebak Angka Rahasia ---")
    sandi = 7
    percobaan = 0
    while True:
        try:
            tebakan = int(input("Tebak angka rahasia (1 - 10): "))
            percobaan += 1
            if tebakan == sandi:
                print(f"✨ Selamat! Tebakanmu benar setelah {percobaan} percobaan!\n")
                break
            else:
                print("❌ Masih salah, coba tebak lagi!")
        except ValueError:
            print("⚠️ Harap masukkan bilangan bulat!")


def demo_validasi_nilai():
    print("\n--- [Demo 5] Validasi Input Nilai (0 - 100) ---")
    while True:
        try:
            nilai = int(input("Masukkan nilai tugas siswa (0 - 100): "))
            if 0 <= nilai <= 100:
                print(f"✅ Nilai {nilai} valid dan berhasil tersimpan!\n")
                break
            else:
                print("❌ Nilai harus berada dalam rentang 0 sampai 100!")
        except ValueError:
            print("⚠️ Harap masukkan angka yang valid!")


def demo_kasir_donat():
    print("\n--- [Demo 6] Kasir Toko Donat Bu Ani ---")
    total_donat = 0
    while True:
        try:
            pesanan = int(input("Masukkan jumlah pesanan donat (0 untuk selesai): "))
            if pesanan == 0:
                break
            if pesanan < 0:
                print("⚠️ Jumlah pesanan tidak boleh negatif!")
                continue
            total_donat += pesanan
            print(f"-> Subtotal sementara: {total_donat} donat")
        except ValueError:
            print("⚠️ Masukkan angka yang valid!")
    print(f"🍩 Total donat yang terjual hari ini: {total_donat} buah.\n")


def main_menu():
    while True:
        print("=" * 55)
        print("   CYBORG IT CENTER - DAY 3: MENU LATIHAN MANDIRI")
        print("=" * 55)
        print("1. Demo Step Increment (+2)")
        print("2. Demo Countdown Peluncuran Roket")
        print("3. Demo Simulasi Celengan Koin Doni")
        print("4. Mainkan Game Tebak Angka Rahasia")
        print("5. Demo Validasi Nilai Tugas Siswa")
        print("6. Demo Kasir Toko Donat Bu Ani")
        print("0. Keluar")
        print("-" * 55)

        pilihan = input("Pilih menu (0-6): ").strip()

        if pilihan == "1":
            demo_step_increment()
        elif pilihan == "2":
            demo_countdown()
        elif pilihan == "3":
            demo_celengan()
        elif pilihan == "4":
            game_tebak_angka()
        elif pilihan == "5":
            demo_validasi_nilai()
        elif pilihan == "6":
            demo_kasir_donat()
        elif pilihan == "0":
            print("Terima kasih! Tetap semangat belajar coding!")
            break
        else:
            print("Pilihan tidak valid, silakan ulangi.\n")


if __name__ == "__main__":
    main_menu()
