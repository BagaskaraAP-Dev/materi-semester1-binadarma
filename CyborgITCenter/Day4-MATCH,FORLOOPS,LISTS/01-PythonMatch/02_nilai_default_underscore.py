# ==============================================================
# 02_nilai_default_underscore.py
# Materi: Nilai Default (Wildcard '_') pada Match Case
# ==============================================================

# Gunakan karakter underscore '_' sebagai case terakhir jika Anda ingin
# menjalankan blok kode saat tidak ada case lain yang cocok (mirip fungsi 'else').
# Nilai '_' akan SELALU cocok dengan nilai apa pun, sehingga penting untuk
# meletakkannya di posisi case paling akhir.

hari = 4

print(f"Mengecek status akhir pekan untuk hari ke-{hari}:")

match hari:
    case 6:
        print("Hari ini adalah hari Sabtu")
    case 7:
        print("Hari ini adalah hari Minggu")
    case _:
        print("Bukan akhir pekan, tetap semangat menantikan akhir pekan!")
