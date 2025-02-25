#Kalkulator persegi
while True:
    print("===Kalkulator Persegi===")

    print("1. Mencari Luas Persegi")
    print("2. Mecari Keliling Persegi ")
    print("3. Keluar")

    pilihan=input("Pilih Operasi (1/2/3) : ")

    if pilihan =='1':
        #menghitung luas persegi
        sisi1 =float(input("Masukan Nilai Sisi 1 = "))
        sisi2 =float(input("Masukan Nilai Sisi 2 = "))

        luas = sisi1 * sisi2

        print(f"Luas persegi dari {sisi1}, dan {sisi2}, adalah = {luas} ")
        continue

    elif pilihan =='2':
        #menghitung keliling
        sisi1 = float(input("Masukan Nilai Sisi 1 = "))
        sisi2 = float(input("Masukan Nilai Sisi 2 = "))
        sisi3 = float(input("Masukan Nilai Sisi 3 = "))
        sisi4 = float(input("Masukan Nilai Sisi 4 = "))

        keliling = 4 * (sisi1 + sisi2 + sisi3 + sisi4 )

        print(f"Keliling persegi dari {sisi1}, {sisi2}, {sisi3}, dan {sisi4} adalah = {keliling}")
        continue
    
    elif pilihan =='3':
        print("Terimakasih telah menggunakan kalkulator persegi")
        break
    else:
        print("Pilihan Tidak Valid ! Silahakan pilih 1-3")
