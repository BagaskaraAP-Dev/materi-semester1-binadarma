# ==============================================================
# 05_studi_kasus_menu_interaktif.py
# Studi Kasus: Program Pengecek Hari & Aktivitas Interaktif
# Menggabungkan Semua Fitur: match, default '_', pipe '|', dan guards 'if'
# ==============================================================

print("=" * 50)
print("   SISTEM PENGECEK HARI & JADWAL - CYBORG IT CENTER   ")
print("=" * 50)

try:
    hari = int(input("Masukkan nomor hari (1: Senin s/d 7: Minggu): "))
    bulan = int(input("Masukkan nomor bulan (1 - 12): "))

    print("-" * 50)
    match hari:
        case 1 | 2 | 3 | 4 | 5 if bulan in [6, 7]:
            print("Status: Hari kerja di masa Liburan Semester (Juni/Juli).")
        case 1:
            print("Status: Senin - Upacara & Kuliah Perdana pekan ini.")
        case 2 | 3 | 4:
            print("Status: Hari Kerja Biasa - Kuliah / Praktikum Lab.")
        case 5:
            print("Status: Jumat Berkah - Sholat Jumat & Evaluasi Mingguan.")
        case 6 | 7:
            print("Status: Akhir Pekan (Weekend) - Waktunya istirahat & santai!")
        case _:
            print("Error: Nomor hari tidak valid! Harap masukkan angka antara 1 sampai 7.")
    print("-" * 50)

except ValueError:
    print("Error: Input harus berupa angka bulat!")
