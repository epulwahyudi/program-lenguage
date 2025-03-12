# Program untuk memahami variabel dan tipe data

# 1. Meminta input dari user
nama = input("Masukkan nama Anda: ")
umur_str = input("Masukkan umur Anda: ")
tinggi_str = input("Masukkan tinggi badan Anda (cm): ")
hobi = input("Masukkan hobi Anda (pisahkan dengan koma jika lebih dari satu): ")
pekerjaan = input("Masukkan Pekerjaan Anda: ")

# 2. Konversi tipe data
umur = int(umur_str)
tinggi = float(tinggi_str)
daftar_hobi = hobi.split(",")  # Mengubah string menjadi list berdasarkan koma

# 3. Membuat dictionary
biodata = {
    "nama": nama,
    "umur": umur,
    "tinggi": tinggi,
    "hobi": daftar_hobi
}

# 4. Menampilkan informasi dan tipe data
print("\n--- Informasi Biodata ---")
print(f"Nama: {biodata['nama']} (Tipe data: {type(biodata['nama'])})")
print(f"Umur: {biodata['umur']} tahun (Tipe data: {type(biodata['umur'])})")
print(f"Tinggi: {biodata['tinggi']} cm (Tipe data: {type(biodata['tinggi'])})")
print(f"Hobi: {', '.join(biodata['hobi'])} (Tipe data: {type(biodata['hobi'])})")

# 5. Operasi matematika sederhana
tahun_lahir = 2024 - umur  # Asumsi tahun sekarang 2024
index_massa_tubuh = tinggi / 100  # Konversi cm ke m
imt = umur / (index_massa_tubuh ** 2)  # Rumus IMT (hanya contoh, bukan rumus IMT sebenarnya)

# 6. Menampilkan hasil operasi
print("\n--- Hasil Operasi ---")
print(f"Tahun lahir (perkiraan): {tahun_lahir} (Tipe data: {type(tahun_lahir)})")
print(f"Tinggi dalam meter: {index_massa_tubuh} m (Tipe data: {type(index_massa_tubuh)})")
print(f"Index Perbandingan Umur-Tinggi: {imt:.2f} (Tipe data: {type(imt)})")

# 7. Boolean check
adalah_dewasa = umur >= 18
nama_panjang = len(nama) > 10

print("\n--- Boolean Check ---")
print(f"Apakah Anda dewasa? {adalah_dewasa} (Tipe data: {type(adalah_dewasa)})")
print(f"Apakah nama Anda panjang? {nama_panjang} (Tipe data: {type(nama_panjang)})")

# 8. Mengakses dan memodifikasi list
print("\n--- Operasi List ---")
if len(daftar_hobi) > 0:
    print(f"Hobi pertama Anda: {daftar_hobi[0]}")
    
    # Menambahkan hobi baru
    daftar_hobi.append("Python programming")
    print(f"Daftar hobi setelah ditambah: {', '.join(daftar_hobi)}")
    
    # Menghitung jumlah hobi
    print(f"Jumlah hobi Anda sekarang: {len(daftar_hobi)}")
