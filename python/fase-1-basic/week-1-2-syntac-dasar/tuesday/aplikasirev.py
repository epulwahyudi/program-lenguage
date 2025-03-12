# Program untuk memahami variabel dan tipe data termasuk tuple

# 1. Meminta input dari user
nama = input("Masukkan nama Anda: ")
umur_str = input("Masukkan umur Anda: ")
tinggi_str = input("Masukkan tinggi badan Anda (cm): ")
hobi = input("Masukkan hobi Anda (pisahkan dengan koma jika lebih dari satu): ")

# Mengumpulkan informasi lokasi dengan tuple
print("\nMasukkan informasi lokasi Anda:")
kota = input("Masukkan kota: ")
provinsi = input("Masukkan provinsi: ")
kode_pos = input("Masukkan kode pos: ")

# 2. Konversi tipe data
umur = int(umur_str)
tinggi = float(tinggi_str)
daftar_hobi = hobi.split(",")  # Mengubah string menjadi list berdasarkan koma

# 3. Membuat tuple
# Tuple untuk informasi lokasi (immutable - tidak dapat diubah)
lokasi = (kota, provinsi, kode_pos)

# Tuple untuk informasi pribadi
tanggal_lahir = (2024 - umur, "Januari", 1)  # Asumsi tanggal 1 Januari

# 4. Membuat dictionary
biodata = {
    "nama": nama,
    "umur": umur,
    "tinggi": tinggi,
    "hobi": daftar_hobi,
    "lokasi": lokasi,
    "tanggal_lahir": tanggal_lahir
}

# 5. Menampilkan informasi dan tipe data
print("\n--- Informasi Biodata ---")
print(f"Nama: {biodata['nama']} (Tipe data: {type(biodata['nama'])})")
print(f"Umur: {biodata['umur']} tahun (Tipe data: {type(biodata['umur'])})")
print(f"Tinggi: {biodata['tinggi']} cm (Tipe data: {type(biodata['tinggi'])})")
print(f"Hobi: {', '.join(biodata['hobi'])} (Tipe data: {type(biodata['hobi'])})")

# Mengakses dan menampilkan data dari tuple
print("\n--- Informasi dari Tuple ---")
print(f"Lokasi: {biodata['lokasi']} (Tipe data: {type(biodata['lokasi'])})")
print(f"Kota: {biodata['lokasi'][0]}")
print(f"Provinsi: {biodata['lokasi'][1]}")
print(f"Kode Pos: {biodata['lokasi'][2]}")

# Unpacking tuple
tahun, bulan, tanggal = biodata['tanggal_lahir']
print(f"\nTanggal Lahir (perkiraan): {tanggal} {bulan} {tahun}")
print(f"Tipe data tanggal lahir: {type(biodata['tanggal_lahir'])}")

# 6. Operasi matematika sederhana
tahun_lahir = 2024 - umur  # Asumsi tahun sekarang 2024
index_massa_tubuh = tinggi / 100  # Konversi cm ke m
imt = umur / (index_massa_tubuh ** 2)  # Rumus IMT (contoh saja)

# 7. Menampilkan hasil operasi
print("\n--- Hasil Operasi ---")
print(f"Tahun lahir (perkiraan): {tahun_lahir} (Tipe data: {type(tahun_lahir)})")
print(f"Tinggi dalam meter: {index_massa_tubuh} m (Tipe data: {type(index_massa_tubuh)})")
print(f"Index Perbandingan Umur-Tinggi: {imt:.2f} (Tipe data: {type(imt)})")

# 8. Boolean check
adalah_dewasa = umur >= 18
nama_panjang = len(nama) > 10

print("\n--- Boolean Check ---")
print(f"Apakah Anda dewasa? {adalah_dewasa} (Tipe data: {type(adalah_dewasa)})")
print(f"Apakah nama Anda panjang? {nama_panjang} (Tipe data: {type(nama_panjang)})")

# 9. Perbedaan list dan tuple
print("\n--- Perbedaan List dan Tuple ---")
print("List (Hobi) dapat dimodifikasi:")
daftar_hobi.append("Python programming")
print(f"Daftar hobi setelah ditambah: {', '.join(daftar_hobi)}")

print("\nTuple (Lokasi) tidak dapat dimodifikasi:")
print("lokasi[0] = 'Jakarta' # Ini akan error jika dijalankan")
print("Harus membuat tuple baru jika ingin mengubah data")
lokasi_baru = ("Jakarta", lokasi[1], lokasi[2])
print(f"Lokasi baru: {lokasi_baru}")

# 10. Konversi antara list dan tuple
print("\n--- Konversi List dan Tuple ---")
# List ke Tuple
hobi_tuple = tuple(daftar_hobi)
print(f"Hobi sebagai tuple: {hobi_tuple} (Tipe data: {type(hobi_tuple)})")

# Tuple ke List
lokasi_list = list(lokasi)
print(f"Lokasi sebagai list: {lokasi_list} (Tipe data: {type(lokasi_list)})")
print("Sekarang lokasi_list dapat dimodifikasi")
lokasi_list[0] = "Jakarta"
print(f"Lokasi list setelah dimodifikasi: {lokasi_list}")