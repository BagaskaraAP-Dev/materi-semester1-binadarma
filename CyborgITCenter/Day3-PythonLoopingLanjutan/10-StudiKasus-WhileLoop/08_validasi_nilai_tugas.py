"""
Studi Kasus 8: Validasi Nilai Tugas Siswa
Konsep       : Input Validation Loop (Range Check 0 - 100)
Deskripsi    : Memastikan input nilai berada dalam rentang valid (0 hingga 100).
               Jika nilai di luar jangkauan, program mengulang permintaan input.
"""

while True:
    nilai = int(input("Masukkan nilai tugas siswa (0 - 100): "))
    
    if 0 <= nilai <= 100:
        break
    
    print("Nilai tidak sah! Silakan masukkan ulang rentang 0 - 100.")

print(f"Konfirmasi: Nilai {nilai} berhasil disimpan.")
