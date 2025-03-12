import math

# Menyimpan riwayat perhitungan
history = []

def tampilkan_menu():
    print("\n=== KALKULATOR ===")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pembagian Bulat (//)")
    print("6. Modulus (%)")
    print("7. Pangkat (**)")
    print("8. Akar Kuadrat (√)")
    print("9. Lihat Riwayat Perhitungan")
    print("0. Keluar")
    print("==================")

while True:
    tampilkan_menu()
    pilihan = input("Pilih operasi (0-9): ")

    if pilihan == "0":
        print("Kalkulator ditutup. Terima kasih!")
        break
    elif pilihan == "9":
        print("\n=== RIWAYAT PERHITUNGAN ===")
        if not history:
            print("Belum ada perhitungan.")
        else:
            for h in history:
                print(h)
        continue

    if pilihan in ["1", "2", "3", "4", "5", "6", "7"]:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("❌ Input harus berupa angka! Coba lagi.")
            continue

    if pilihan == "1":
        hasil = angka1 + angka2
        operator = "+"
    elif pilihan == "2":
        hasil = angka1 - angka2
        operator = "-"
    elif pilihan == "3":
        hasil = angka1 * angka2
        operator = "*"
    elif pilihan == "4":
        if angka2 == 0:
            hasil = "❌ Error: Tidak bisa membagi dengan nol!"
        else:
            hasil = angka1 / angka2
        operator = "/"
    elif pilihan == "5":
        if angka2 == 0:
            hasil = "❌ Error: Tidak bisa membagi dengan nol!"
        else:
            hasil = angka1 // angka2
        operator = "//"
    elif pilihan == "6":
        hasil = angka1 % angka2
        operator = "%"
    elif pilihan == "7":
        hasil = angka1 ** angka2
        operator = "**"
    elif pilihan == "8":
        try:
            angka = float(input("Masukkan angka untuk akar kuadrat: "))
            if angka < 0:
                hasil = "❌ Error: Tidak bisa menghitung akar negatif!"
            else:
                hasil = math.sqrt(angka)
            history.append(f"√{angka} = {hasil}")
            print(f"Hasil: {hasil}")
        except ValueError:
            print("❌ Input harus berupa angka! Coba lagi.")
        continue
    else:
        print("❌ Pilihan tidak valid! Coba lagi.")
        continue

    history.append(f"{angka1} {operator} {angka2} = {hasil}")
    print(f"Hasil: {hasil}")
