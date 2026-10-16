"""
Studi Kasus 4: Langkah Kaki Sehat Pak Joko
Konsep       : While Loop Step Increment (+100)
Deskripsi    : Pak Joko menghitung pencapaian langkah kaki harian
               mulai dari 100 langkah hingga target 500 langkah.
"""

langkah = 100  # Kelipatan 100 pertama

while langkah <= 500:
    print(f"{langkah} langkah tercapai")
    langkah += 100  # Bertambah 100 langkah setiap pencatatan
