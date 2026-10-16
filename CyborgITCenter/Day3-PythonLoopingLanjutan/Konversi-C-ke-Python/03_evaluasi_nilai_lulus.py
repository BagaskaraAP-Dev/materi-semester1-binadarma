"""
Konversi C ke Python — Kasus 3: Evaluasi Batas Nilai Kelulusan
Logika: Percabangan if-else untuk ambang batas nilai kelulusan minimal 75
"""

nilai = float(input("Masukkan nilai siswa (0-100): "))

# Kelulusan minimal batas 75
if nilai >= 75:
    print("Lulus")
else:
    print("Tidak lulus")
