# Program Management Kontak

# Database kontak (menggunakan dictionary dalam list)
daftar_kontak = [
    {"nama": "Andi", "telepon": "081234567890", "email": "andi@example.com"},
    {"nama": "Budi", "telepon": "089876543210", "email": "budi@example.com"}
]

def tampilkan_menu():
    """Menampilkan menu program"""
    print("\n=== PROGRAM MANAGEMENT KONTAK ===")
    print("[1] Tampilkan Semua Kontak")
    print("[2] Tambah Kontak Baru")
    print("[3] Cari Kontak")
    print("[4] Edit Kontak")
    print("[5] Hapus Kontak")
    print("[0] Keluar")
    
def tampilkan_kontak(kontak):
    """Menampilkan informasi satu kontak"""
    print(f"Nama: {kontak['nama']}")
    print(f"Telepon: {kontak['telepon']}")
    print(f"Email: {kontak['email']}")
    
def tampilkan_semua_kontak():
    """Menampilkan semua kontak"""
    print("\n=== DAFTAR KONTAK ===")
    if len(daftar_kontak) == 0:
        print("Tidak ada kontak tersimpan")
    else:
        for i, kontak in enumerate(daftar_kontak, 1):
            print(f"\nKontak #{i}")
            tampilkan_kontak(kontak)
            
def tambah_kontak():
    """Menambahkan kontak baru"""
    print("\n=== TAMBAH KONTAK BARU ===")
    nama = input("Masukkan nama: ")
    telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")
    
    # Membuat dictionary kontak baru
    kontak_baru = {
        "nama": nama,
        "telepon": telepon,
        "email": email
    }
    
    # Menambahkan ke daftar kontak
    daftar_kontak.append(kontak_baru)
    print("Kontak berhasil ditambahkan!")
    
def cari_kontak():
    """Mencari kontak berdasarkan nama"""
    print("\n=== CARI KONTAK ===")
    keyword = input("Masukkan nama yang dicari: ").lower()
    
    # List untuk menyimpan hasil pencarian
    hasil_pencarian = []
    
    # Mencari di semua kontak
    for kontak in daftar_kontak:
        if keyword in kontak["nama"].lower():
            hasil_pencarian.append(kontak)
    
    # Menampilkan hasil
    if len(hasil_pencarian) == 0:
        print("Kontak tidak ditemukan")
    else:
        print(f"\nDitemukan {len(hasil_pencarian)} kontak:")
        for i, kontak in enumerate(hasil_pencarian, 1):
            print(f"\nHasil #{i}")
            tampilkan_kontak(kontak)
    
def edit_kontak():
    """Mengedit kontak yang ada"""
    print("\n=== EDIT KONTAK ===")
    
    # Menampilkan semua kontak dulu
    tampilkan_semua_kontak()
    
    # Meminta input indeks kontak yang akan diedit
    try:
        indeks = int(input("\nMasukkan nomor kontak yang akan diedit: ")) - 1
        
        if 0 <= indeks < len(daftar_kontak):
            # Menampilkan data saat ini
            print("\nData saat ini:")
            tampilkan_kontak(daftar_kontak[indeks])
            
            # Meminta data baru
            print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
            nama_baru = input("Nama baru: ")
            telepon_baru = input("Telepon baru: ")
            email_baru = input("Email baru: ")
            
            # Update data jika input tidak kosong
            if nama_baru:
                daftar_kontak[indeks]["nama"] = nama_baru
            if telepon_baru:
                daftar_kontak[indeks]["telepon"] = telepon_baru
            if email_baru:
                daftar_kontak[indeks]["email"] = email_baru
                
            print("Kontak berhasil diperbarui!")
        else:
            print("Nomor kontak tidak valid!")
            
    except ValueError:
        print("Input harus berupa angka!")
    
def hapus_kontak():
    """Menghapus kontak"""
    print("\n=== HAPUS KONTAK ===")
    
    # Menampilkan semua kontak dulu
    tampilkan_semua_kontak()
    
    # Meminta input indeks kontak yang akan dihapus
    try:
        indeks = int(input("\nMasukkan nomor kontak yang akan dihapus: ")) - 1
        
        if 0 <= indeks < len(daftar_kontak):
            # Konfirmasi penghapusan
            nama = daftar_kontak[indeks]["nama"]
            konfirmasi = input(f"Anda yakin ingin menghapus kontak {nama}? (y/n): ")
            
            if konfirmasi.lower() == 'y':
                del daftar_kontak[indeks]
                print("Kontak berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan")
        else:
            print("Nomor kontak tidak valid!")
            
    except ValueError:
        print("Input harus berupa angka!")

# Program utama
def main():
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (0-5): ")
        
        if pilihan == '1':
            tampilkan_semua_kontak()
        elif pilihan == '2':
            tambah_kontak()
        elif pilihan == '3':
            cari_kontak()
        elif pilihan == '4':
            edit_kontak()
        elif pilihan == '5':
            hapus_kontak()
        elif pilihan == '0':
            print("\nTerima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi")

# Menjalankan program
if __name__ == "__main__":
    main()