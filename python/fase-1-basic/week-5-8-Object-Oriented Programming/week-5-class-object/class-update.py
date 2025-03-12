class Anggota:
    def __init__(self, nama, id_anggota, tanggal_bergabung, status="Aktif"):
        self.nama = nama
        self.id_anggota = id_anggota
        self.tanggal_bergabung = tanggal_bergabung
        self.status = status  # Default status: Aktif

    def info(self):
        return f"Nama: {self.nama} | ID: {self.id_anggota} | Bergabung: {self.tanggal_bergabung} | Status: {self.status}"
    
    def perbarui_status(self, status_baru,):
        self.status = status_baru
        print(f"Status {self.nama} diperbarui menjadi {self.status}")

    def perbaharui_tanggal(self, tanggal_baru):  
        self.tanggal_bergabung = tanggal_baru
        print(f"Status {self.tanggal_bergabung} diperbaharui {self.tanggal_bergabung}")

# Contoh penggunaan
anggota1 = Anggota("Epul", "A91", "10 Maret 2025")
print(anggota1.info())

# Mengubah status anggota
anggota1.perbarui_status("Non-Aktif")
print(anggota1.info())
# mengubah tanggal bergabung
anggota1.perbaharui_tanggal("15 Maret 2025")
print(anggota1.info())


## repairing code

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

# Contoh penggunaan
anggota1 = Anggota("Epul", "A91", "10 Maret 2025")
print(anggota1.info())

# Mengubah status anggota
anggota1.perbarui_status("Non-Aktif")
print(anggota1.info())

# Mengubah tanggal bergabung
anggota1.perbarui_tanggal("15 Maret 2025")
print(anggota1.info())
