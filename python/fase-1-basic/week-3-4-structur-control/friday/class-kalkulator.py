# Versi 2: Kalkulator menggunakan class
class Kalkulator:
    def __init__(self):
        self.hasil = 0
    
    def tambah(self, a, b):
        self.hasil = a + b
        return self.hasil
    
    def kurang(self, a, b):
        self.hasil = a - b
        return self.hasil
    
    def kali(self, a, b):
        self.hasil = a * b
        return self.hasil
    
    def bagi(self, a, b):
        if b == 0:
            self.hasil = "Error: Pembagian dengan nol"
        else:
            self.hasil = a / b
        return self.hasil
    
    def jalankan(self):
        print("=== Kalkulator Sederhana dengan Class ===")
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
                print(f"Hasil: {angka1} + {angka2} = {self.tambah(angka1, angka2)}")
            elif pilihan == '2':
                print(f"Hasil: {angka1} - {angka2} = {self.kurang(angka1, angka2)}")
            elif pilihan == '3':
                print(f"Hasil: {angka1} * {angka2} = {self.kali(angka1, angka2)}")
            elif pilihan == '4':
                print(f"Hasil: {angka1} / {angka2} = {self.bagi(angka1, angka2)}")

# Contoh penggunaan
if __name__ == "__main__":
  
    # Untuk menjalankan kalkulator dengan class:
    kalk = Kalkulator()
    kalk.jalankan()
    