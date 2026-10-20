# ==============================================================
# 01_dasar_match_case.py
# Materi: Sintaks Dasar Pernyataan Match Case di Python
# ==============================================================

# Pernyataan 'match' digunakan untuk menjalankan aksi berbeda berdasarkan kondisi tertentu.
# Alih-alih menulis banyak pernyataan if..elif..else, kita bisa menggunakan 'match'.

hari = 4

print(f"Mengecek hari ke-{hari}:")

match hari:
    case 1:
        print("Senin")
    case 2:
        print("Selasa")
    case 3:
        print("Rabu")
    case 4:
        print("Kamis")
    case 5:
        print("Jumat")
    case 6:
        print("Sabtu")
    case 7:
        print("Minggu")

# Cara Kerja:
# 1. Ekspresi 'match hari' dievaluasi satu kali.
# 2. Nilai ekspresi dibandingkan dengan nilai di setiap 'case'.
# 3. Jika cocok, blok kode yang terkait akan dijalankan.
