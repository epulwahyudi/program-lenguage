# Kalkulator Segitiga

while True:
    print("=====Kalkulator Segitiga=====")
    print("1. Mencari Luas Segitiga")
    print("2. Mencari Keliling Segitiga")
    print("3. Mencari Tinggi Segitiga dari Luas")
    print("4. Keluar")

    # Memilih operasi
    pilihan = input("Pilih Operasi (1/2/3/4) : ")

    if pilihan == "1":
        # Menghitung Luas Segitiga
        alas = float(input("Masukan Nilai Alas = "))
        tinggi = float(input("Masukan Nilai Tinggi = "))
        
        luas = 0.5 * alas * tinggi
        print(f"Luas Segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas:.2f}")
        continue

    elif pilihan == "2":
        # Menghitung Keliling Segitiga
        sisi1 = float(input("Masukan Nilai Sisi 1 = "))
        sisi2 = float(input("Masukan Nilai Sisi 2 = "))
        sisi3 = float(input("Masukan Nilai Sisi 3 = "))

        keliling = sisi1 + sisi2 + sisi3
        print(f"Keliling Segitiga dengan sisi {sisi1}, {sisi2}, dan {sisi3} adalah {keliling:.2f}")
        continue

    elif pilihan == "3":
        # Mencari Tinggi Segitiga dari Luas dan Alas
        luas = float(input("Masukan Nilai Luas = "))
        alas = float(input("Masukan Nilai Alas = "))

        if alas == 0:
            print("Alas tidak boleh 0!")
        else:
            tinggi = (2 * luas) / alas
            print(f"Tinggi Segitiga dengan luas {luas} dan alas {alas} adalah {tinggi:.2f}")
        continue
    elif pilihan == "4":
        print("Terima kasih telah menggunakan kalkulator segitiga! 👋")
        break  # Menghentikan loop
    else:
        print("Pilihan tidak valid! Silakan pilih 1-3.")
