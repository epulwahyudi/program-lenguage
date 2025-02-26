#kalkulator jajar genjang
print("\nKalkulator Jajar Genjang")

print("1. Mencari Luas")
print("2. Mencari Keliling")
print("3. Mencari Tinggi")

pilihan = input("Pilih Operasi (1/2/3) : ")
if pilihan == '1':
    #mencari luas
    alas = float(input("Masukan Nilai Alas : "))
    tinggi = float(input("Masukan Nilai Tinggi : "))

    luas = alas * tinggi

    print(f"Luas Jajar Genjang dari {alas},dan {tinggi}, adalah {luas}")
elif pilihan == '2':
    #mencari keliling
    alas = float(input("Masukan Nilai Alas : "))
    sisi_miring = float(input("Masukan Nilai Panjang Sisi Miring : "))

    keliling = 2 * (alas + sisi_miring)

    print(f"Keliling Jajar Genjang dari {alas}, dan {sisi_miring}, adalah {keliling}")
elif pilihan == '3':
    #mencari tinggi
    luas = float(input("Masukan Nilai Luas : "))
    alas = float(input("Masukan Nilai Alas : "))

    tinggi = luas / alas

    print(f"Tinggi Jajar Genjang dari {luas}, dan {alas}, adalah {tinggi}")
else:
    print("Pilihan tidak Valid ! Silahkan pilih 1-3")