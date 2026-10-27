# 01_insert_list.py
# Menyisipkan Item ke Posisi Tertentu dengan insert()

# insert(indeks, item) menaruh item di indeks yang diminta,
# item yang sudah ada di posisi itu dan sesudahnya bergeser ke kanan.

teks = ['a', 'c', 'd']

# 'b' disisipkan di indeks 1, sehingga 'c' dan 'd' bergeser
teks.insert(1, 'b')
print(teks)  # ['a', 'b', 'c', 'd']
