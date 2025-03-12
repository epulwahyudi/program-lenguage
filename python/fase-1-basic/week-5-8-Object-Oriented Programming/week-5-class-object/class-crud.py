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
            return anggota
    return None

# Fungsi untuk menambahkan anggota baru
def tambah_anggota(daftar_anggota):
    nama = input("Masukkan nama anggota: ")
    id_anggota = input("Masukkan ID anggota: ")
    tanggal_bergabung = input("Masukkan tanggal bergabung (contoh: 10 Maret 2025): ")
    
    anggota_baru = Anggota(nama, id_anggota, tanggal_bergabung)
    daftar_anggota.append(anggota_baru)
    print(f"\nAnggota {nama} berhasil ditambahkan!\n")

# Fungsi untuk menghapus anggota berdasarkan ID
def hapus_anggota(id_anggota, daftar_anggota):
    anggota = cari_anggota(id_anggota, daftar_anggota)
    if anggota:
        daftar_anggota.remove(anggota)
        print(f"\nAnggota dengan ID {id_anggota} telah dihapus.\n")
    else:
        print(f"\nAnggota dengan ID {id_anggota} tidak ditemukan.\n")

# Fungsi untuk memperbarui nama anggota berdasarkan ID
def perbarui_nama(id_anggota, daftar_anggota):
    anggota = cari_anggota(id_anggota, daftar_anggota)
    if anggota:
        nama_baru = input("Masukkan nama baru: ")
        anggota.nama = nama_baru
        print(f"\nNama anggota dengan ID {id_anggota} diperbarui menjadi {nama_baru}.\n")
    else:
        print(f"\nAnggota dengan ID {id_anggota} tidak ditemukan.\n")

# Fungsi untuk menampilkan semua anggota
def tampilkan_anggota(daftar_anggota):
    print("\nDaftar Anggota:")
    if not daftar_anggota:
        print("Belum ada anggota yang terdaftar.\n")
    else:
        for anggota in daftar_anggota:
            print(anggota.info())
    print()

# Data awal daftar anggota
daftar_anggota = [
    Anggota("Epul", "A91", "10 Maret 2025"),
    Anggota("Wahyudi", "A92", "12 Maret 2025"),
    Anggota("Jaka", "A93", "15 Maret 2025")
]

# Program utama dengan menu
while True:
    print("\n=== Sistem Manajemen Anggota ===")
    print("1. Tampilkan daftar anggota")
    print("2. Tambah anggota")
    print("3. Cari anggota")
    print("4. Hapus anggota")
    print("5. Perbarui nama anggota")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_anggota(daftar_anggota)
    elif pilihan == "2":
        tambah_anggota(daftar_anggota)
    elif pilihan == "3":
        id_dicari = input("Masukkan ID anggota yang dicari: ")
        anggota = cari_anggota(id_dicari, daftar_anggota)
        if anggota:
            print("\nAnggota ditemukan:")
            print(anggota.info(), "\n")
        else:
            print(f"\nAnggota dengan ID {id_dicari} tidak ditemukan.\n")
    elif pilihan == "4":
        id_hapus = input("Masukkan ID anggota yang ingin dihapus: ")
        hapus_anggota(id_hapus, daftar_anggota)
    elif pilihan == "5":
        id_perbarui = input("Masukkan ID anggota yang ingin diperbarui: ")
        perbarui_nama(id_perbarui, daftar_anggota)
    elif pilihan == "6":
        print("\nTerima kasih! Program selesai.\n")
        break
    else:
        print("\nPilihan tidak valid! Silakan coba lagi.\n")