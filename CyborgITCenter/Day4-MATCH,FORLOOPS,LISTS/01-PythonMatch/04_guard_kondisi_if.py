# ==============================================================
# 04_guard_kondisi_if.py
# Materi: Pernyataan 'if' sebagai Penjaga (Guards) pada Case
# ==============================================================

# Anda dapat menambahkan pernyataan 'if' pada evaluasi case sebagai
# pengecekan kondisi tambahan (Guard Clause). Blok case hanya akan dieksekusi
# jika nilai cocok DAN kondisi 'if' bernilai True.

bulan = 5  # Bulan Mei
hari = 4   # Hari ke-4 (Kamis)

nama_bulan = "April" if bulan == 4 else ("Mei" if bulan == 5 else f"Bulan ke-{bulan}")
print(f"Pengecekan: Hari ke-{hari}, {nama_bulan}")

match hari:
    case 1 | 2 | 3 | 4 | 5 if bulan == 4:
        print("Hari kerja di bulan April")
    case 1 | 2 | 3 | 4 | 5 if bulan == 5:
        print("Hari kerja di bulan Mei")
    case 6 | 7:
        print("Hari akhir pekan (Weekend)")
    case _:
        print("Tidak ada kondisi yang cocok")
