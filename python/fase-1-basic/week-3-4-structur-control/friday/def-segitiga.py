import math
import sys

def kalkulator_segitiga_def():
    # Tampilkan header dan flush output
    print("=" * 40)
    print("KALKULATOR SEGITIGA (FUNCTION)")
    print("=" * 40)
    sys.stdout.flush()  # Memaksa output ditampilkan
    
    while True:
        # Tampilkan menu dan flush output
        print("\nOperasi yang tersedia:")
        print("1. Hitung Luas Segitiga (alas & tinggi)")
        print("2. Hitung Keliling Segitiga (3 sisi)")
        print("3. Hitung Luas Segitiga dengan Rumus Heron (3 sisi)")
        print("4. Hitung Tinggi Segitiga (alas & luas)")
        print("5. Keluar")
        sys.stdout.flush()  # Memaksa output ditampilkan
        
        pilihan = input("\nPilih operasi (1-5): ")
        
        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator segitiga!")
            break
            
        if pilihan not in ['1', '2', '3', '4']:
            print("Pilihan tidak valid. Silakan pilih 1-5.")
            continue
        
        if pilihan == '1':
            alas = float(input("Masukkan panjang alas (satuan): "))
            tinggi = float(input("Masukkan tinggi segitiga (satuan): "))
            luas = 0.5 * alas * tinggi
            print(f"Luas segitiga: {luas} satuan persegi")
            
        elif pilihan == '2':
            sisi1 = float(input("Masukkan panjang sisi pertama (satuan): "))
            sisi2 = float(input("Masukkan panjang sisi kedua (satuan): "))
            sisi3 = float(input("Masukkan panjang sisi ketiga (satuan): "))
            
            # Validasi segitiga
            if sisi1 + sisi2 > sisi3 and sisi1 + sisi3 > sisi2 and sisi2 + sisi3 > sisi1:
                keliling = sisi1 + sisi2 + sisi3
                print(f"Keliling segitiga: {keliling} satuan")
            else:
                print("Input tidak valid! Ketiga sisi tidak membentuk segitiga.")
                
        elif pilihan == '3':
            sisi1 = float(input("Masukkan panjang sisi pertama (satuan): "))
            sisi2 = float(input("Masukkan panjang sisi kedua (satuan): "))
            sisi3 = float(input("Masukkan panjang sisi ketiga (satuan): "))
            
            # Validasi segitiga
            if sisi1 + sisi2 > sisi3 and sisi1 + sisi3 > sisi2 and sisi2 + sisi3 > sisi1:
                s = (sisi1 + sisi2 + sisi3) / 2
                luas = math.sqrt(s * (s - sisi1) * (s - sisi2) * (s - sisi3))
                print(f"Luas segitiga (rumus Heron): {luas:.2f} satuan persegi")
            else:
                print("Input tidak valid! Ketiga sisi tidak membentuk segitiga.")
                
        elif pilihan == '4':
            alas = float(input("Masukkan panjang alas (satuan): "))
            luas = float(input("Masukkan luas segitiga (satuan persegi): "))
            
            if alas > 0 and luas > 0:
                tinggi = (2 * luas) / alas
                print(f"Tinggi segitiga: {tinggi} satuan")
            else:
                print("Input tidak valid! Alas dan luas harus positif.")

# Memastikan output ditampilkan sebelum program dimulai
print("Program kalkulator segitiga dimulai...", flush=True)
kalkulator_segitiga_def()
print("Program selesai.", flush=True)