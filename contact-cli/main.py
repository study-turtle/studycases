class Contact:
    def __init__(self):
        self.contacts = []

    def add(self, name, number):
        queues = {
            "name": name,
            "number": number
        }

        self.contacts.append(queues)

    def view(self):
        for item in self.contacts:
            print("-----")
            print(f"Name: {item['name']}")
            print(f"Number: {item['number']}")

    def search_by_phone(self, phone):
        contact = None  # Nilai null sebagai default
        for item in self.contacts:
            if item['number'] == phone:
                contact = item
                break

        return contact

    def delete(self, phone):
        contact = []

        for item in self.contacts:
            if item['number'] != phone:
                contact.append(item)

        self.contacts = contact


ct = Contact()
while True:
    print("\n\n")
    
    print("Selamat Datang di Penyimpanan Kotak Afiani")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Delete Contact")

    menu = input("Pilih Menu Anda : ")

    if menu == "1":
        
        name = input("Masukkan nama: ")
        number = input("Masukkan nomor: ")
        ct.add(name, number)

        print(f"Selamat, kamu berhasil menambahkan kontak {name}")

    elif menu == "2":
        ct.view()
    else:
        phone = input("Masukkan nomor yang ingin dihapus: ")

        contact = ct.search_by_phone(phone)

        if not contact:
            print("Kontak tidak ditemukan")
        else:
            print("Kontak ditemukan!")
            print("-----")
            print(f"Name: {contact['name']}")
            print(f"Number: {contact['number']}")
            print("-----")
            print("\n")
            
            opsi = input("Apakah kamu benar ingin menghapus kontak? (y/n) : ")
            opsi = opsi.lower()  # Buat seluruh karakter yang dimasukkan menjadi huruf kecil
            
            if opsi == "y":
                ct.delete(phone)
                print(f"Kontak yang dihapus adalah {contact['name']}")
            else:
                print("Kontak tidak jadi dihapus")
