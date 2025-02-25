#kalkulator persegi panjang

while True: # loop program
    print("====Kalkulator Persegi Panjang")
    print("1. Mencari Luas ")
    print("2. Mencari Keliling")
    print("3. Keluar")

    pilihan = (input("Pilihlah Operasi (1/2/3)"))

    if pilihan == '1':
        #mencari luas
        panjang=float(input("Masukan Nilai Panjang = "))
        lebar=float(input("Masukan Nilai Lebar = "))

        hasil = panjang * lebar

        print(f"Luas dari {panjang} dan {lebar} adalah {hasil}")
        continue
    elif pilihan == '2':
        #mencari keliling
        panjang=float(input("Masukan Nilai Panjang = "))
        lebar=float(input("Masukan Nilai Lebar = "))

        hasil = ( 2 * panjang ) + ( 2 * lebar )

        print(f"Keliling dari {panjang} dan {lebar} adalah {hasil}")
        continue
    elif pilihan == '3':
        print("Terimakasih telah menggunakan kalkulator persegi panjang")
        break
    else:
        print("Pilihan tidak valid ! Silahkan1pilih 1-3")

