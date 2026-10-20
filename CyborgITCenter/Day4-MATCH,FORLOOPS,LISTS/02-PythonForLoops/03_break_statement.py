# 03_break_statement.py
# Statemen 'break' pada For Loop

# 'break' berfungsi menghentikan perulangan secara paksa sebelum seluruh elemen selesai dibaca.

buah = ["apel", "pisang", "ceri"]

print("--- Kasus 1: break sesudah print ---")
for item in buah:
    print(item)
    if item == "pisang":
        break
# Output: 'apel', 'pisang' lalu berhenti

print("\n--- Kasus 2: break sebelum print ---")
for item in buah:
    if item == "pisang":
        break
    print(item)
# Output: 'apel' saja (karena saat item 'pisang', loop langsung berhenti sebelum print)
