# ==============================================================
# 03_gabungkan_nilai_or.py
# Materi: Menggabungkan Nilai Case dengan Karakter Pipe '|' (OR)
# ==============================================================

# Gunakan karakter pipa '|' sebagai operator 'or' dalam evaluasi case
# untuk mencocokkan lebih dari satu nilai sekaligus dalam satu blok kode.

hari = 4

print(f"Kategori hari untuk hari ke-{hari}:")

match hari:
    case 1 | 2 | 3 | 4 | 5:
        print("Hari ini adalah hari kerja (Weekday)")
    case 6 | 7:
        print("Hari ini adalah akhir pekan (Weekend)! Selamat berlibur!")
    case _:
        print("Nomor hari tidak valid (harus angka 1 sampai 7)")
