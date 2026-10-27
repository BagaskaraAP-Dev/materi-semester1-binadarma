# 04_sort_dan_reverse.py
# Mengurutkan List dengan sort(), sorted(), dan reverse=True

nilai = []

while len(nilai) < 5:
    data = int(input("masukkan data: "))
    if data > 0:
        nilai.append(data)
    else:
        print("data tidak valid")

print(nilai)

# sorted(nilai) membuat list BARU yang sudah urut, list aslinya tidak berubah.
# Kalau hasilnya beda dengan nilai, berarti nilai belum urut.
if nilai != sorted(nilai):
    nilai.sort()
    print("setelah diurutkan:", nilai)

# PERBAIKAN: sebelumnya tertulis print(nilai.sort)
# Tanpa tanda kurung (), yang tercetak adalah objek method-nya:
#   <built-in method sort of list object at 0x...>
# Ditulis print(nilai.sort()) pun hasilnya None, karena sort() mengubah
# list secara langsung dan tidak mengembalikan apa-apa.
# Jadi urutkan dulu, baru cetak list-nya.
print(nilai)

# --- URUT DARI BESAR KE KECIL ---
# reverse=True membuat sort() mengurutkan menurun (descending)
nilai.sort(reverse=True)
print("urut besar ke kecil:", nilai)

# --- PERBANDINGAN CARA MENGURUTKAN & MEMBALIK ---
angka = [3, 1, 4, 1, 5]

# sorted(): hasil list baru, angka tetap seperti semula
print("sorted(angka)              :", sorted(angka))                # [1, 1, 3, 4, 5]
print("sorted(angka, reverse=True):", sorted(angka, reverse=True))  # [5, 4, 3, 1, 1]
print("angka masih asli           :", angka)                        # [3, 1, 4, 1, 5]

# reverse(): hanya membalik posisi item (terakhir jadi pertama), TIDAK mengurutkan
angka.reverse()
print("angka.reverse()            :", angka)                        # [5, 1, 4, 1, 3]

# sort(reverse=True): mengurutkan dari besar ke kecil, mengubah list asli
angka.sort(reverse=True)
print("angka.sort(reverse=True)   :", angka)                        # [5, 4, 3, 1, 1]
