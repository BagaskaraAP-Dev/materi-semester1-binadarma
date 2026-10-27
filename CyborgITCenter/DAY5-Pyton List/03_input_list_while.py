# 03_input_list_while.py
# Mengisi List dengan while + Validasi Data Positif

# Bedanya dengan for: while terus meminta input sampai list berisi 5 data.
# Data yang tidak lolos validasi (<= 0) tidak dimasukkan, jadi
# pengguna diminta mengisi ulang sampai jumlahnya pas 5.

nilai = []

while len(nilai) < 5:
    data = int(input("masukan data : "))
    if data > 0:
        nilai.append(data)

print(nilai)
