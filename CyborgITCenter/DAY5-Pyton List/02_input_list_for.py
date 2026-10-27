# 02_input_list_for.py
# Mengisi List dari Input Pengguna dengan for + append()

# Mulai dari list kosong, lalu tiap input ditambahkan ke akhir list.
# for i in range(5) berarti input diminta tepat 5 kali.

nilai = []

for i in range(5):
    data = int(input("masukan data : "))
    nilai.append(data)

print(nilai)
