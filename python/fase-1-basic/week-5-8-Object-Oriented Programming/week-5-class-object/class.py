class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
    
    def deskripsi(self):
        return f"'{self.judul}' oleh {self.penulis} (Terbit: {self.tahun_terbit})"


#create book objects
buku1 = Buku("Python Basics", "Epul", 2020)
buku2 = Buku("Data Science", "Epul", 2021)

#show information of book
print(buku1.deskripsi())
print(buku2.deskripsi())


class Anggota:
    def __init__(self, nama, id_anggota, tanggal_bergabung):
        self.nama = nama
        self.id_anggota = id_anggota
        self.tanggal_bergabung = tanggal_bergabung

    def info(self):
        return f" {self.nama} {self.id_anggota} {self.tanggal_bergabung}"
    
#create a anggota
anggota1 = Anggota("Epul", "A91", 2025)
anggota2 = Anggota("Wahyudi", "A92", 2025)

#show
print(anggota1.info())
print(anggota2.info())


##repairing

class Anggota:
    def __init__(self, nama, id_anggota, tanggal_bergabung):
        self.nama = nama
        self.id_anggota = id_anggota
        self.tanggal_bergabung = str(tanggal_bergabung)  # Konversi ke string

    def info(self):
        return f"Nama: {self.nama} | ID: {self.id_anggota} | Bergabung: {self.tanggal_bergabung}"
    
# Membuat objek anggota
anggota1 = Anggota("Epul", "A91", "10 Maret 2025")
anggota2 = Anggota("Wahyudi", "A92", "12 Maret 2025")

# Menampilkan informasi anggota
print(anggota1.info())
print(anggota2.info())
