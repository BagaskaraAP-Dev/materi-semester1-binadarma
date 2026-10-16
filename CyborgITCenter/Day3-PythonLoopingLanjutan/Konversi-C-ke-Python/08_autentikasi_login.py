"""
Konversi C ke Python — Kasus 8: Autentikasi Pengguna & Sistem Login Sederhana
Logika: Pengecekan multi-kondisi simultan menggunakan operator logika 'and'
"""

username = input("Username: ")
password = input("Password: ")

# Pengecekan username dan password dalam kondisi logika yang sama
if username == "admin" and password == "12345":
    print("Login berhasil! Selamat datang Admin.")
else:
    print("Username atau password salah!")
