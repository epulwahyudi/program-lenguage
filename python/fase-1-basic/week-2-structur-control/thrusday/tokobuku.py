class Buku:
    def __init__(self, id, judul, penulis, penerbit, tahun, harga, stok):
        self.id = id
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun = tahun
        self.harga = harga
        self.stok = stok
    
    def __str__(self):
        return f"ID: {self.id}\nJudul: {self.judul}\nPenulis: {self.penulis}\nPenerbit: {self.penerbit}\nTahun: {self.tahun}\nHarga: Rp {self.harga}\nStok: {self.stok}\n"

class TokoBuku:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []
        self.id_terakhir = 0
    
    def tambah_buku(self, judul, penulis, penerbit, tahun, harga, stok):
        self.id_terakhir += 1
        buku_baru = Buku(self.id_terakhir, judul, penulis, penerbit, tahun, harga, stok)
        self.daftar_buku.append(buku_baru)
        print(f"Buku '{judul}' berhasil ditambahkan!")
        return buku_baru
    
    def cari_buku_by_id(self, id):
        for buku in self.daftar_buku:
            if buku.id == id:
                return buku
        return None
    
    def cari_buku_by_judul(self, judul):
        hasil = []
        for buku in self.daftar_buku:
            if judul.lower() in buku.judul.lower():
                hasil.append(buku)
        return hasil
    
    def cari_buku_by_penulis(self, penulis):
        hasil = []
        for buku in self.daftar_buku:
            if penulis.lower() in buku.penulis.lower():
                hasil.append(buku)
        return hasil
    
    def tampilkan_semua_buku(self):
        if not self.daftar_buku:
            print("Tidak ada buku dalam daftar.")
        else:
            print(f"\n===== DAFTAR BUKU DI {self.nama.upper()} =====")
            for buku in self.daftar_buku:
                print(buku)
    
    def update_buku(self, id, judul=None, penulis=None, penerbit=None, tahun=None, harga=None, stok=None):
        buku = self.cari_buku_by_id(id)
        if buku:
            if judul:
                buku.judul = judul
            if penulis:
                buku.penulis = penulis
            if penerbit:
                buku.penerbit = penerbit
            if tahun:
                buku.tahun = tahun
            if harga:
                buku.harga = harga
            if stok:
                buku.stok = stok
            print(f"Buku dengan ID {id} berhasil diperbarui!")
            return True
        else:
            print(f"Buku dengan ID {id} tidak ditemukan.")
            return False
    
    def hapus_buku(self, id):
        buku = self.cari_buku_by_id(id)
        if buku:
            self.daftar_buku.remove(buku)
            print(f"Buku '{buku.judul}' berhasil dihapus!")
            return True
        else:
            print(f"Buku dengan ID {id} tidak ditemukan.")
            return False
    
    def tambah_stok(self, id, jumlah):
        buku = self.cari_buku_by_id(id)
        if buku:
            buku.stok += jumlah
            print(f"Stok buku '{buku.judul}' berhasil ditambah {jumlah}. Stok sekarang: {buku.stok}")
            return True
        else:
            print(f"Buku dengan ID {id} tidak ditemukan.")
            return False
    
    def kurangi_stok(self, id, jumlah):
        buku = self.cari_buku_by_id(id)
        if buku:
            if buku.stok >= jumlah:
                buku.stok -= jumlah
                print(f"Stok buku '{buku.judul}' berhasil dikurangi {jumlah}. Stok sekarang: {buku.stok}")
                return True
            else:
                print(f"Stok tidak mencukupi! Stok '{buku.judul}' sekarang: {buku.stok}")
                return False
        else:
            print(f"Buku dengan ID {id} tidak ditemukan.")
            return False

def menu_utama():
    print("\n===== APLIKASI TOKO BUKU SEDERHANA =====")
    print("1. Tambah Buku")
    print("2. Tampilkan Semua Buku")
    print("3. Cari Buku")
    print("4. Update Buku")
    print("5. Hapus Buku")
    print("6. Tambah Stok")
    print("7. Kurangi Stok")
    print("0. Keluar")
    pilihan = input("Pilih menu (0-7): ")
    return pilihan

def menu_cari():
    print("\n===== MENU PENCARIAN =====")
    print("1. Cari berdasarkan ID")
    print("2. Cari berdasarkan Judul")
    print("3. Cari berdasarkan Penulis")
    print("0. Kembali ke Menu Utama")
    pilihan = input("Pilih menu pencarian (0-3): ")
    return pilihan

def main():
    toko = TokoBuku("Toko Buku Makmur")
    
    # Tambah beberapa buku awal untuk contoh
    toko.tambah_buku("Python Programming", "John Smith", "Tech Press", 2022, 150000, 10)
    toko.tambah_buku("Belajar Python untuk Pemula", "Budi Santoso", "Informatika", 2021, 120000, 15)
    toko.tambah_buku("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Bloomsbury", 1997, 200000, 5)
    
    while True:
        pilihan = menu_utama()
        
        if pilihan == "1":
            # Tambah Buku
            print("\n===== TAMBAH BUKU =====")
            judul = input("Judul Buku: ")
            penulis = input("Penulis: ")
            penerbit = input("Penerbit: ")
            
            while True:
                try:
                    tahun = int(input("Tahun Terbit: "))
                    break
                except ValueError:
                    print("Tahun harus berupa angka!")
            
            while True:
                try:
                    harga = float(input("Harga (Rp): "))
                    break
                except ValueError:
                    print("Harga harus berupa angka!")
            
            while True:
                try:
                    stok = int(input("Stok: "))
                    break
                except ValueError:
                    print("Stok harus berupa angka!")
            
            toko.tambah_buku(judul, penulis, penerbit, tahun, harga, stok)
        
        elif pilihan == "2":
            # Tampilkan Semua Buku
            toko.tampilkan_semua_buku()
        
        elif pilihan == "3":
            # Cari Buku
            while True:
                pilihan_cari = menu_cari()
                
                if pilihan_cari == "1":
                    # Cari berdasarkan ID
                    try:
                        id_buku = int(input("Masukkan ID Buku: "))
                        buku = toko.cari_buku_by_id(id_buku)
                        if buku:
                            print("\n===== HASIL PENCARIAN =====")
                            print(buku)
                        else:
                            print(f"Buku dengan ID {id_buku} tidak ditemukan.")
                    except ValueError:
                        print("ID harus berupa angka!")
                
                elif pilihan_cari == "2":
                    # Cari berdasarkan Judul
                    judul = input("Masukkan Judul Buku: ")
                    hasil = toko.cari_buku_by_judul(judul)
                    if hasil:
                        print(f"\n===== HASIL PENCARIAN JUDUL '{judul}' =====")
                        for buku in hasil:
                            print(buku)
                    else:
                        print(f"Tidak ada buku dengan judul yang mengandung '{judul}'.")
                
                elif pilihan_cari == "3":
                    # Cari berdasarkan Penulis
                    penulis = input("Masukkan Nama Penulis: ")
                    hasil = toko.cari_buku_by_penulis(penulis)
                    if hasil:
                        print(f"\n===== HASIL PENCARIAN PENULIS '{penulis}' =====")
                        for buku in hasil:
                            print(buku)
                    else:
                        print(f"Tidak ada buku dengan penulis yang mengandung '{penulis}'.")
                
                elif pilihan_cari == "0":
                    # Kembali ke Menu Utama
                    break
                
                else:
                    print("Pilihan tidak valid!")
        
        elif pilihan == "4":
            # Update Buku
            print("\n===== UPDATE BUKU =====")
            try:
                id_buku = int(input("Masukkan ID Buku yang akan diupdate: "))
                buku = toko.cari_buku_by_id(id_buku)
                if buku:
                    print("Data Buku Saat Ini:")
                    print(buku)
                    print("Masukkan data baru (kosongkan jika tidak ingin mengubah):")
                    
                    judul = input(f"Judul [{buku.judul}]: ")
                    penulis = input(f"Penulis [{buku.penulis}]: ")
                    penerbit = input(f"Penerbit [{buku.penerbit}]: ")
                    
                    tahun_str = input(f"Tahun [{buku.tahun}]: ")
                    tahun = int(tahun_str) if tahun_str else None
                    
                    harga_str = input(f"Harga [{buku.harga}]: ")
                    harga = float(harga_str) if harga_str else None
                    
                    stok_str = input(f"Stok [{buku.stok}]: ")
                    stok = int(stok_str) if stok_str else None
                    
                    toko.update_buku(id_buku, judul or None, penulis or None, penerbit or None, tahun, harga, stok)
                else:
                    print(f"Buku dengan ID {id_buku} tidak ditemukan.")
            except ValueError:
                print("ID/Tahun/Harga/Stok harus berupa angka!")
        
        elif pilihan == "5":
            # Hapus Buku
            print("\n===== HAPUS BUKU =====")
            try:
                id_buku = int(input("Masukkan ID Buku yang akan dihapus: "))
                konfirmasi = input(f"Anda yakin ingin menghapus buku dengan ID {id_buku}? (y/n): ")
                if konfirmasi.lower() == 'y':
                    toko.hapus_buku(id_buku)
            except ValueError:
                print("ID harus berupa angka!")
        
        elif pilihan == "6":
            # Tambah Stok
            print("\n===== TAMBAH STOK =====")
            try:
                id_buku = int(input("Masukkan ID Buku: "))
                jumlah = int(input("Masukkan jumlah stok yang ditambahkan: "))
                toko.tambah_stok(id_buku, jumlah)
            except ValueError:
                print("ID dan jumlah harus berupa angka!")
        
        elif pilihan == "7":
            # Kurangi Stok
            print("\n===== KURANGI STOK =====")
            try:
                id_buku = int(input("Masukkan ID Buku: "))
                jumlah = int(input("Masukkan jumlah stok yang dikurangi: "))
                toko.kurangi_stok(id_buku, jumlah)
            except ValueError:
                print("ID dan jumlah harus berupa angka!")
        
        elif pilihan == "0":
            # Keluar
            print("Terima kasih telah menggunakan Aplikasi Toko Buku!")
            break
        
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()