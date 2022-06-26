# To-do List

## Entry Point

Pada entry point terdapat infinite loop untuk meng-input command dari user. Command kemudian diolah menggunakan `shlex.split()` dan dicocokan untuk memanggil fungsi yang bertanggung jawab untuk perintah tersebut.

## Database

```python
database = {}
```

Database dibuat menggunakan struktur data dictionary. Dictionary tersebut memiliki key yang berupa nama dari task dan value yang berupa status dari task tersebut.

## Commands

### `add(task)`

Menambahkan task baru ke dalam database.

### `remove(task)`

Menghapus task dalam database.

### `rename(task, new_name)`

Mengganti nama task pada database.

### `list_tasks(filter='todo')`

Menampilkan semua task pada database sesuai dengan filternya. Filter yang dapat digunakan adalah `todo`, `done`, dan `all`. Filter `todo` hanya menampilkan task yang belum selesai. Filter `done` hanya menampilkan task yang sudah selesai, dan filter `all` menampilkan semua task.

Task yang sudah selesai ditandai dengan `[x]` dan task yang belum selesai ditandai dengan `[ ]`.

### `complete(task)`

Mengubah status task menjadi completed.

### `uncomplete(task)`

Mengubah status task menjadi not completed.

### `toggle(task)`

Mengubah status task menjadi kebalikan dari status semula.

## Error handling

Fungsi error handling dilakukan menggunakan pattern early return, yaitu mengecek error terlebih dahulu dan me-return jika terdapat error. Logic utama pada fungsi ditempatkan di paling akhir. Pattern ini berguna untuk menghindari penggunaan nested-if.
