# Algoritme Aplikasi Toko Buku Sederhana

## 1. Inisialisasi Program
1. Mulai program
2. Buat objek `TokoBuku`
3. Tambahkan beberapa data buku awal ke dalam inventaris
4. Tampilkan menu utama

## 2. Menu Utama
1. Tampilkan pilihan menu:
   - 0: Keluar
   - 1: Tambah Buku
   - 2: Tampilkan Semua Buku
   - 3: Cari Buku
   - 4: Update Buku
   - 5: Hapus Buku
   - 6: Tambah Stok
   - 7: Kurangi Stok
2. Minta input pilihan dari pengguna
3. Proses pilihan berdasarkan input pengguna

## 3. Proses Berdasarkan Pilihan Menu
### **1. Tambah Buku**
1. Minta input data buku (ID, judul, penulis, stok)
2. Validasi input data
3. Tambahkan buku ke dalam inventaris
4. Konfirmasi bahwa buku telah ditambahkan
5. Kembali ke menu utama

### **2. Tampilkan Semua Buku**
1. Periksa apakah ada buku dalam inventaris
2. Jika ada, tampilkan daftar buku
3. Jika tidak, tampilkan pesan "Tidak ada buku dalam inventaris"
4. Kembali ke menu utama

### **3. Cari Buku**
1. Tampilkan pilihan metode pencarian:
   - 1: Cari berdasarkan ID
   - 2: Cari berdasarkan Judul
   - 3: Cari berdasarkan Penulis
2. Minta input berdasarkan pilihan metode pencarian
3. Lakukan pencarian dengan validasi
4. Jika buku ditemukan, tampilkan data buku
5. Jika tidak ditemukan, tampilkan pesan "Buku tidak ditemukan"
6. Kembali ke menu utama

### **4. Update Buku**
1. Minta input ID buku yang ingin diperbarui
2. Cari buku berdasarkan ID
3. Jika ditemukan, tampilkan data saat ini
4. Minta input data baru dan validasi
5. Perbarui data buku
6. Konfirmasi bahwa data telah diperbarui
7. Kembali ke menu utama

### **5. Hapus Buku**
1. Minta input ID buku yang ingin dihapus
2. Cari buku berdasarkan ID
3. Jika ditemukan, minta konfirmasi pengguna
4. Jika dikonfirmasi, hapus buku dari inventaris
5. Tampilkan pesan "Buku berhasil dihapus"
6. Kembali ke menu utama

### **6. Tambah Stok**
1. Minta input ID buku
2. Validasi ID dan periksa keberadaan buku
3. Jika buku ditemukan, minta jumlah stok yang akan ditambahkan
4. Tambahkan stok ke dalam inventaris
5. Tampilkan pesan "Stok berhasil ditambahkan"
6. Kembali ke menu utama

### **7. Kurangi Stok**
1. Minta input ID buku
2. Validasi ID dan periksa keberadaan buku
3. Jika buku ditemukan, minta jumlah stok yang akan dikurangi
4. Periksa apakah stok mencukupi
   - Jika ya, kurangi stok
   - Jika tidak, tampilkan pesan "Stok tidak mencukupi"
5. Tampilkan pesan "Stok berhasil dikurangi"
6. Kembali ke menu utama

## 4. Keluar dari Program
1. Jika pengguna memilih opsi **0 (Keluar)**, tampilkan pesan "Terima kasih telah menggunakan aplikasi toko buku."
2. Program selesai.

