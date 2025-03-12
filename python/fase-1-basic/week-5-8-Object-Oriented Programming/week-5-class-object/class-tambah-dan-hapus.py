class Anggota:
    def __init__(self, nama, id_anggota, tanggal_bergabung, status="Aktif"):
        self.nama = nama
        self.id_anggota = id_anggota
        self.tanggal_bergabung = tanggal_bergabung
        self.status = status  # Default status: Aktif

    def info(self):
        return f"Nama: {self.nama} | ID: {self.id_anggota} | Bergabung: {self.tanggal_bergabung} | Status: {self.status}"
    
# Fungsi untuk mencari anggota berdasarkan ID
def cari_anggota(id_anggota, daftar_anggota):
    for anggota in daftar_anggota:
        if anggota.id_anggota == id_anggota:
            return anggota  # Jika ditemukan, kembalikan objek anggota
    return None  # Jika tidak ditemukan

# Fungsi untuk menghapus anggota berdasarkan ID
def hapus_anggota(id_anggota, daftar_anggota):
    for anggota in daftar_anggota:
        if anggota.id_anggota == id_anggota:
            daftar_anggota.remove(anggota)  # Menghapus anggota dari daftar
            print(f"Anggota dengan ID {id_anggota} telah dihapus.")
            return
    print(f"Anggota dengan ID {id_anggota} tidak ditemukan.")

# Fungsi untuk memperbarui nama anggota berdasarkan ID
def perbarui_nama(id_anggota, nama_baru, daftar_anggota):
    anggota = cari_anggota(id_anggota, daftar_anggota)
    if anggota:
        anggota.nama = nama_baru
        print(f"Nama anggota dengan ID {id_anggota} diperbarui menjadi {nama_baru}.")
    else:
        print(f"Anggota dengan ID {id_anggota} tidak ditemukan.")

# Membuat daftar anggota
daftar_anggota = [
    Anggota("Epul", "A91", "10 Maret 2025"),
    Anggota("Wahyudi", "A92", "12 Maret 2025"),
    Anggota("Jaka", "A93", "15 Maret 2025"),
    Anggota("Juned", "A94", "15 Maret 2025"),
    Anggota("Samsudin", "A95", "15 Maret 2025")
]

# Menampilkan semua anggota sebelum dihapus
print("\nDaftar Anggota Sebelum:")
for anggota in daftar_anggota:
    print(anggota.info())

# Menghapus anggota
hapus_anggota("A92", daftar_anggota)

# Menampilkan semua anggota setelah dihapus
print("\nDaftar Anggota Setelah:")
for anggota in daftar_anggota:
    print(anggota.info())

# Memperbarui nama anggota
perbarui_nama("A91", "Eko", daftar_anggota)

# Menampilkan semua anggota setelah diperbarui
print("\nDaftar Anggota Setelah Perubahan Nama:")
for anggota in daftar_anggota:
    print(anggota.info())
