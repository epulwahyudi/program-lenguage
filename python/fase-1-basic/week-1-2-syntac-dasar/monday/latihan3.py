# Mengambil input dari user
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))  # mengubah string ke integer
sekolah = input("Masukan nama sekolah: ")

# Output dengan format
print(f"Halo {nama}, umur Anda {umur}, tahun dan sekolah anda {sekolah}")

# Output tanpa f-string 
print("Halo", nama, ", umur Anda", umur, ", tahun dan sekolah Anda", sekolah)
