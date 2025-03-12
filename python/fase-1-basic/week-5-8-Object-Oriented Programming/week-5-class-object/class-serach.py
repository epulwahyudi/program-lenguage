class Anggota:
    def __init__(self, nama, id_anggota, tanggal_bergabung, status="Aktif"):
        self.nama = nama
        self.id_anggota = id_anggota
        self.tanggal_bergabung = tanggal_bergabung
        self.status = status  # Default status: Aktif

    def info(self):
        return f"Nama: {self.nama} | ID: {self.id_anggota} | Bergabung: {self.tanggal_bergabung} | Status: {self.status}"
    
    def perbarui_status(self, status_baru):
        self.status = status_baru
        print(f"Status {self.nama} diperbarui menjadi {self.status}")

    def perbarui_tanggal(self, tanggal_baru):  
        self.tanggal_bergabung = tanggal_baru
        print(f"Tanggal bergabung {self.nama} diperbarui menjadi {self.tanggal_bergabung}")

# Fungsi untuk mencari anggota berdasarkan ID
def cari_anggota(id_anggota, daftar_anggota):
    for anggota in daftar_anggota:
        if anggota.id_anggota == id_anggota:
            return anggota  # Mengembalikan objek anggota jika ditemukan
    return None  # Jika tidak ditemukan

# Membuat daftar anggota
daftar_anggota = [
    Anggota("Epul", "A91", "10 Maret 2025"),
    Anggota("Wahyudi", "A92", "12 Maret 2025"),
    Anggota("Jaka", "A93", "15 Maret 2025")
]

# Mencari anggota dengan ID tertentu
id_dicari = "A92"

# Mencari Anggota dengan Input
id_dicari =  input("Masukan ID Anggota yang dicari: ")
anggota_ditemukan = cari_anggota(id_dicari, daftar_anggota)

if anggota_ditemukan:
    print("Anggota ditemukan:")
    print(anggota_ditemukan.info())
else:
    print(f"Anggota dengan ID {id_dicari} tidak ditemukan.")

#


