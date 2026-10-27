# 05_sorting_manual.py
# Mengurutkan List Secara Manual (Tanpa sort)

# Cara kerja:
# 1. Cari angka terkecil di list nilai
# 2. Pindahkan ke list_urut (append), lalu hapus dari nilai (remove)
# 3. Ulangi sampai semua angka sudah dipindahkan
# Karena yang diambil selalu yang terkecil, list_urut otomatis urut naik.

nilai = []

# for hanya memberi 5 kali kesempatan, jadi data tidak valid
# membuat jumlah data di list berkurang (tidak diminta ulang)
for i in range(5):
    data = int(input("masukkan data: "))
    if data > 0:
        nilai.append(data)
    else:
        print("data tidak valid")

list_urut = []
for i in range(len(nilai)):
    terkecil = nilai[0]
    for j in nilai:
        if j < terkecil:
            terkecil = j
    list_urut.append(terkecil)
    nilai.remove(terkecil)

print(list_urut)

# Untuk urut dari besar ke kecil (seperti reverse=True),
# cukup cari yang TERBESAR: ganti tanda  j < terkecil  menjadi  j > terkecil
# Catatan: setelah loop selesai, list nilai jadi kosong karena isinya
# sudah dipindahkan semua ke list_urut.
