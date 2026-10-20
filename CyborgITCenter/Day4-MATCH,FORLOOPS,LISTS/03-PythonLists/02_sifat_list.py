# 02_sifat_list.py
# Sifat-Sifat List di Python

# === 1. BERURUTAN (Ordered) ===
# Item di dalam list punya urutan tetap.
# Item baru yang ditambahkan akan masuk di posisi paling akhir.

hewan = ["kucing", "anjing", "kelinci"]
print("Urutan awal:", hewan)

hewan.append("hamster")
print("Setelah ditambah:", hewan)
# 'hamster' masuk di posisi terakhir, urutan lama tidak berubah


# === 2. BISA DIUBAH (Changeable) ===
# Kita bisa mengubah, menambah, dan menghapus item setelah list dibuat.

hewan[0] = "harimau"
print("Setelah elemen pertama diganti:", hewan)


# === 3. BOLEH DUPLIKAT (Allow Duplicates) ===
# Karena list menggunakan indeks, list boleh memiliki item dengan nilai sama.

angka = [10, 20, 30, 10, 30]
print("\nList dengan nilai duplikat:", angka)
print("Angka 10 muncul", angka.count(10), "kali")
