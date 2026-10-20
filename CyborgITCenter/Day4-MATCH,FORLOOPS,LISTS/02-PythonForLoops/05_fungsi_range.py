# 05_fungsi_range.py
# Fungsi range() pada For Loop

# range() menghasilkan sequence angka numerik integer.
# Karakteristik bawaan:
# - Mulai dari 0 (default)
# - Bertambah 1 setiap langkah (default)
# - Berhenti sebelum nilai batas akhir (eksklusif)

print("--- 1. range(stop): range(6) -> 0 sampai 5 ---")
for x in range(6):
    print(x)

print("\n--- 2. range(start, stop): range(2, 6) -> 2 sampai 5 ---")
for x in range(2, 6):
    print(x)

print("\n--- 3. range(start, stop, step): range(1, 10, 2) -> angka ganjil 1 sampai 9 ---")
for x in range(1, 10, 2):
    print(x)
