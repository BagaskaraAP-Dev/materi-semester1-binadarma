# 04_ubah_tambah_hapus.py
# Mengubah, Menambah, dan Menghapus Item pada List

kota = ["Jakarta", "Bandung", "Surabaya"]
print("Awal:", kota)

# --- MENGUBAH item ---
kota[1] = "Yogyakarta"
print("Setelah ubah indeks 1:", kota)

# --- MENAMBAH item ---
# append(): tambah di akhir
kota.append("Semarang")
print("Setelah append:", kota)

# insert(): sisipkan di posisi tertentu
kota.insert(1, "Medan")
print("Setelah insert di indeks 1:", kota)

# --- MENGHAPUS item ---
# remove(): hapus berdasarkan nilai
kota.remove("Surabaya")
print("Setelah remove 'Surabaya':", kota)

# pop(): hapus berdasarkan indeks (default: indeks terakhir)
item_dihapus = kota.pop()
print(f"Setelah pop (yang dihapus: '{item_dihapus}'):", kota)

# del: hapus berdasarkan indeks atau hapus seluruh list
del kota[0]
print("Setelah del indeks 0:", kota)
