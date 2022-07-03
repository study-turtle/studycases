# Contact CLI

## Entry Point

Pada entry point terdapat infinite loop untuk meng-input command dari user. Command kemudian diolah menggunakan fungsi input yang menerima input dari user.

## Database

```python
self.contacts = []
```

Database dibuat menggunakan struktur data array (list). List tersebut memiliki dictionary dari atribut ```name``` dan ```number``` yang berisikan nama dan nomor telfon.

## Commands

### `1`

Menambahkan kontak baru.

### `2`

Melihat seluruh kontak pada database.

### `3`

Menghapus kontak pada database

## Functions
```add(name, number)```

Menambahkan kontak baru dengan menerima parameter berupa nama dan nomor telfon.

```view()```

Menampilkan seluruh data pada ```self.contacts```.


```search_by_phone(phone)```

Mencari sebuah kontak berdasarkan nomor telfon dari data ```self.contacts```.

```delete(phone)```

Menghapus sebuah data kontak yang dicocokkan berdasarkan nomor telfon, apabila nomor telfon tidak sama maka data dibuang dari array temporary untuk kembali disimpan pada variabel ```self.contacts```.




## Error handling

Fungsi error handling dilakukan menggunakan kondisi, apabila tidak cocok maka tidak masuk ke dalam kondisi tersebut.
