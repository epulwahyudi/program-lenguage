# Versi 1: Kalkulator menggunakan function (def)
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol"
    return a / b

def kalkulator_sederhana():
    print("=== Kalkulator Sederhana dengan Function ===")
    print("Operasi yang tersedia:")
    print("1. Pertambahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")
    
    while True:
        pilihan = input("\nPilih operasi (1-5): ")
        
        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator!")
            break
            
        if pilihan not in ['1', '2', '3', '4']:
            print("Pilihan tidak valid. Silakan pilih 1-5.")
            continue
            
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        
        if pilihan == '1':
            print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
        elif pilihan == '2':
            print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
        elif pilihan == '3':
            print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
        elif pilihan == '4':
            print(f"Hasil: {angka1} / {angka2} = {bagi(angka1, angka2)}")


# Contoh penggunaan
if __name__ == "__main__":
    # Untuk menjalankan kalkulator dengan function:
    kalkulator_sederhana()
