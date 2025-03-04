#definis funtion dasar

def sapa(nama):
    """Fungsi sederhana untuk menyapa seseorang"""
    return f"Halo, {nama}!"

#memanggil function
pesan = sapa("Epul")
print(pesan)

# function dengan multiple parameters
def hitung_luas_persegi_panjang(pajang, lebar):
    luas = pajang * lebar
    return luas

# function dengan default parameter
def daftar_siswa(nama, kelas="11A", jurusan="APA"):
    return f"Nama: {nama}, Kelas: {kelas}, Jurusan: {jurusan}"

print(daftar_siswa("Epul"))
print(daftar_siswa("EP", "12B"))
print(daftar_siswa("Yudi", "13A", "IPA"))


#Funtion dengan arbitrary argument (*args)
def jumlahkan(*angka):
    total = 0
    for num in angka:
        total += num
    return total

print(jumlahkan(1,2,3))
print(jumlahkan(5,10,15,20))


#funtion dengan keyword arguments (**kwargs)
def cetak_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

cetak_info(nama="Epul", umur=28, hobi="membaca")


#module
import math
import random
from datetime import datetime

#menggunakan function dari module
print(f"Pi: {math.pi}")
print(f"Random number: {random.randint(1,100)}")
print(f"Current date: {datetime.now().date()}")