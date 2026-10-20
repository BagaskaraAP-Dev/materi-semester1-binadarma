# 05_panjang_dan_tipe_data.py
# Menghitung Panjang List dan Tipe Data Campuran

# --- Panjang list menggunakan len() ---
mahasiswa = ["Andi", "Budi", "Citra", "Dewi"]
print("Jumlah mahasiswa:", len(mahasiswa))

# --- List bisa berisi tipe data campuran ---
# Dalam satu list, item boleh berisi string, angka, boolean sekaligus.
campuran = ["Bagaskara", 19, True, 3.14, "Informatika"]
print("Isi list campuran:", campuran)

for item in campuran:
    print(f"  {item} -> tipe: {type(item).__name__}")
