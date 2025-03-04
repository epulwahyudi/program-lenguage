# Mini Project: Kalkulator Sederhana
while True: # loop program
    print("\n=== Kalkulator Sederhana ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Mencari Luas Segitiga")
    print("6. Mencari Keliling Segitiga")
    print("7. Mencari Tinggi Segitiga")
    print("8. Keluar")
    #print("9. Mencari Keliling Persgi")
    #print("10. Keluar")

    pilihan = input("Pilih operasi (1/2/3/4/5/6/7/8): ")

    if pilihan == '1':
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        hasil = angka1 + angka2
        operasi = "+"

    elif pilihan == '2':
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        hasil = angka1 - angka2
        operasi = "-"

    elif pilihan == '3':
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        hasil = angka1 * angka2
        operasi = "*"

    elif pilihan == '4':
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        if angka2 != 0:
            hasil = angka1 / angka2
            operasi = "/"
        else:
            print("Error: Pembagian dengan nol!")
            continue  # Kembali ke awal loop

    elif pilihan == "5":
        alas = float(input("Masukan Nilai Alas = "))
        tinggi = float(input("Masukan Nilai Tinggi = "))
        hasil = 0.5 * alas * tinggi
        print(f"Luas Segitiga dengan alas {alas} dan tinggi {tinggi} adalah {hasil:.2f}")
        continue

    elif pilihan == "6":
        sisi1 = float(input("Masukan Nilai Sisi 1 = "))
        sisi2 = float(input("Masukan Nilai Sisi 2 = "))
        sisi3 = float(input("Masukan Nilai Sisi 3 = "))
        hasil = sisi1 + sisi2 + sisi3
        print(f"Keliling Segitiga dengan sisi {sisi1}, {sisi2}, dan {sisi3} adalah {hasil:.2f}")
        continue

    elif pilihan == "7":
        luas = float(input("Masukan Nilai Luas = "))
        alas = float(input("Masukan Nilai Alas = "))

        if alas == 0:
            print("Alas tidak boleh 0!")
            continue
        else:
            hasil = (2 * luas) / alas
            print(f"Tinggi Segitiga dengan luas {luas} dan alas {alas} adalah {hasil:.2f}")
        continue

    elif pilihan == "8":
        print("Terima kasih telah menggunakan kalkulator! 👋")
        break  # Menghentikan loop

    else:
        print("Pilihan tidak valid! Silakan pilih 1-8.")
        continue

    # Menampilkan hasil untuk operasi matematika dasar
    print(f"Hasil: {angka1} {operasi} {angka2} = {hasil:.2f}")

    # Tanya apakah ingin mengulang atau keluar
    ulang = input("\nApakah ingin melakukan perhitungan lagi? (y/n): ").lower()
    if ulang != "y":
        print("Terima kasih telah menggunakan kalkulator! 👋")
        break  # Menghentikan loop
