# Random Sentence Generator

## Database

```python
nama = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'George', 'Harry']
kata_kerja = ['memakan', 'melempar', 'menembak', 'mengubur', 'membakar']
kata_benda = ['apel', 'buku', 'sepeda', 'komputer', 'kulkas', 'mobil']
```

Database dibuat menggunakan struktur data list. Program memuat tiga list, yaitu list nama, kata kerja, dan kata benda.

## Main Loop

```python
while True:
    nama_random = random.choice(nama)
    kata_kerja_random = random.choice(kata_kerja)
    kata_benda_random = random.choice(kata_benda)

    print(f'{nama_random} {kata_kerja_random} {kata_benda_random}')
    input()
```

Dalap setiap loop, kita mengambil satu kata dari masing-masing list menggunakan fungsi `random.choice`. Kemudian, kalimat tersebut dicetak ke layar, dan program menunggu user untuk menekan enter untuk mencetak kalimat selanjutnya.