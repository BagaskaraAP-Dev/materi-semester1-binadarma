# 04_continue_statement.py
# Statemen 'continue' pada For Loop

# 'continue' menghentikan iterasi yang sedang berjalan dan langsung melompat
# ke iterasi elemen berikutnya. Elemen saat kondisi bernilai True akan dilewati (di-skip).

buah = ["apel", "pisang", "ceri"]

print("Lewati 'pisang' menggunakan continue:")
for item in buah:
    if item == "pisang":
        continue
    print(item)

# Output: 'apel' dan 'ceri' ('pisang' dilewati)
