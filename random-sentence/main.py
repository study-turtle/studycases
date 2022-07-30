import random

nama = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'George', 'Harry']
kata_kerja = ['memakan', 'melempar', 'menembak', 'mengubur', 'membakar']
kata_benda = ['apel', 'buku', 'sepeda', 'komputer', 'kulkas', 'mobil']

while True:
    nama_random = random.choice(nama)
    kata_kerja_random = random.choice(kata_kerja)
    kata_benda_random = random.choice(kata_benda)

    print(f'{nama_random} {kata_kerja_random} {kata_benda_random}')
    input()