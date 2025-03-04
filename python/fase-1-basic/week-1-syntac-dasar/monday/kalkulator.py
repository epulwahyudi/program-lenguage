# Mini Project: Kalkulator Sederhana
print("\n=== Kalkulator Sederhana ===")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Mencari Luas Segitiga")
print("6. Mencari Keliling Segitiga")
print("7. Mencari Tinggi Segitiga")

pilihan = input("Pilih operasi (1/2/3/4/5/6/7): ")

if pilihan in ['1', '2', '3', '4']:  # Operasi matematika dasar
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        hasil = angka1 + angka2
        operasi = "+"
    elif pilihan == '2':
        hasil = angka1 - angka2
        operasi = "-"
    elif pilihan == '3':
        hasil = angka1 * angka2
        operasi = "*"
    elif pilihan == '4':
        if angka2 != 0:
            hasil = angka1 / angka2
            operasi = "/"
        else:
            print("Error: Pembagian dengan nol!")
            hasil = None  # Hindari error saat mencetak hasil

    if hasil is not None:
        print(f"Hasil: {angka1} {operasi} {angka2} = {hasil}")

elif pilihan == "5":  # Luas segitiga
    alas = float(input("Masukan Nilai Alas = "))
    tinggi = float(input("Masukan Nilai Tinggi = "))
    hasil = 0.5 * alas * tinggi
    print(f"Luas Segitiga dengan alas {alas} dan tinggi {tinggi} adalah {hasil}")

elif pilihan == "6":  # Keliling segitiga
    sisi1 = float(input("Masukan Nilai Sisi 1 = "))
    sisi2 = float(input("Masukan Nilai Sisi 2 = "))
    sisi3 = float(input("Masukan Nilai Sisi 3 = "))
    hasil = sisi1 + sisi2 + sisi3
    print(f"Keliling Segitiga dengan sisi {sisi1}, {sisi2}, dan {sisi3} adalah {hasil}")

elif pilihan == "7":  # Tinggi segitiga
    luas = float(input("Masukan Nilai Luas = "))
    alas = float(input("Masukan Nilai Alas = "))
    if alas == 0:
        print("Error: Alas tidak boleh 0!")
    else:
        hasil = (2 * luas) / alas
        print(f"Tinggi Segitiga dengan luas {luas} dan alas {alas} adalah {hasil}")

else:
    print("Pilihan tidak valid! Silakan pilih 1-7.")
