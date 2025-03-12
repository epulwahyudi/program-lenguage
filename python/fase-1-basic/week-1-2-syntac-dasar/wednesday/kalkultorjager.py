import math

def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

def keliling_jajar_genjang(alas, sisi_miring):
    return 2 * (alas + sisi_miring)

def sisi_miring(tinggi, selisih_alas):
    return math.sqrt(tinggi**2 + selisih_alas**2)

def tinggi_jajar_genjang(luas, alas):
    return luas / alas

def diagonal_jajar_genjang(alas, sisi_miring, sudut):
    sudut_radian = math.radians(sudut)
    diagonal1 = math.sqrt(alas**2 + sisi_miring**2 + 2 * alas * sisi_miring * math.cos(sudut_radian))
    diagonal2 = math.sqrt(alas**2 + sisi_miring**2 - 2 * alas * sisi_miring * math.cos(sudut_radian))
    return diagonal1, diagonal2

def kalkulator_jajar_genjang():
    print("\nKalkulator Jajar Genjang")
    print("1. Hitung Luas")
    print("2. Hitung Keliling")
    print("3. Hitung Diagonal")
    pilihan = input("Pilih operasi (1/2/3): ")
    
    if pilihan == "1":
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        print(f"Luas Jajar Genjang: {luas_jajar_genjang(alas, tinggi)}")
    elif pilihan == "2":
        alas = float(input("Masukkan panjang alas: "))
        sisi_miring = float(input("Masukkan panjang sisi miring: "))
        print(f"Keliling Jajar Genjang: {keliling_jajar_genjang(alas, sisi_miring)}")
    elif pilihan == "3":
        alas = float(input("Masukkan panjang alas: "))
        sisi_miring = float(input("Masukkan panjang sisi miring: "))
        sudut = float(input("Masukkan besar sudut antara alas dan sisi miring (derajat): "))
        diagonal1, diagonal2 = diagonal_jajar_genjang(alas, sisi_miring, sudut)
        print(f"Diagonal 1: {diagonal1}")
        print(f"Diagonal 2: {diagonal2}")
    else:
        print("Pilihan tidak valid")

# Menjalankan kalkulator
kalkulator_jajar_genjang()
