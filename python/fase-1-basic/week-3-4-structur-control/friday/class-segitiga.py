import math

# Kalkulator Segitiga dengan pendekatan CLASS (Object-Oriented)
class KalkulatorSegitiga:
    def __init__(self):
        """Inisialisasi kalkulator segitiga"""
        self.sisi1 = 0
        self.sisi2 = 0
        self.sisi3 = 0
        self.alas = 0
        self.tinggi = 0
        self.luas = 0
        
    def hitung_luas_alas_tinggi(self, alas, tinggi):
        """Menghitung luas segitiga dengan rumus 1/2 * alas * tinggi"""
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi
        return self.luas
    
    def hitung_keliling(self, sisi1, sisi2, sisi3):
        """Menghitung keliling segitiga dengan menjumlahkan ketiga sisinya"""
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        self.sisi3 = sisi3
        return sisi1 + sisi2 + sisi3
    
    def hitung_luas_heron(self, sisi1, sisi2, sisi3):
        """Menghitung luas segitiga dengan rumus Heron"""
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        self.sisi3 = sisi3
        s = (sisi1 + sisi2 + sisi3) / 2  # semi-perimeter
        self.luas = math.sqrt(s * (s - sisi1) * (s - sisi2) * (s - sisi3))
        return self.luas
    
    def hitung_tinggi(self, alas, luas):
        """Menghitung tinggi segitiga jika diketahui alas dan luas"""
        self.alas = alas
        self.luas = luas
        self.tinggi = (2 * luas) / alas
        return self.tinggi
    
    def validasi_segitiga(self, sisi1, sisi2, sisi3):
        """Validasi apakah ketiga sisi dapat membentuk segitiga"""
        return (sisi1 + sisi2 > sisi3 and 
                sisi1 + sisi3 > sisi2 and 
                sisi2 + sisi3 > sisi1)
    
    def jalankan(self):
        """Menjalankan kalkulator segitiga dengan interface konsol"""
        print("=" * 40)
        print("KALKULATOR SEGITIGA (CLASS)")
        print("=" * 40)
        
        while True:
            print("\nOperasi yang tersedia:")
            print("1. Hitung Luas Segitiga (alas & tinggi)")
            print("2. Hitung Keliling Segitiga (3 sisi)")
            print("3. Hitung Luas Segitiga dengan Rumus Heron (3 sisi)")
            print("4. Hitung Tinggi Segitiga (alas & luas)")
            print("5. Keluar")
            
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
                luas = self.hitung_luas_alas_tinggi(alas, tinggi)
                print(f"Luas segitiga: {luas} satuan persegi")
                
            elif pilihan == '2':
                sisi1 = float(input("Masukkan panjang sisi pertama (satuan): "))
                sisi2 = float(input("Masukkan panjang sisi kedua (satuan): "))
                sisi3 = float(input("Masukkan panjang sisi ketiga (satuan): "))
                
                # Validasi segitiga
                if self.validasi_segitiga(sisi1, sisi2, sisi3):
                    keliling = self.hitung_keliling(sisi1, sisi2, sisi3)
                    print(f"Keliling segitiga: {keliling} satuan")
                else:
                    print("Input tidak valid! Ketiga sisi tidak membentuk segitiga.")
                    
            elif pilihan == '3':
                sisi1 = float(input("Masukkan panjang sisi pertama (satuan): "))
                sisi2 = float(input("Masukkan panjang sisi kedua (satuan): "))
                sisi3 = float(input("Masukkan panjang sisi ketiga (satuan): "))
                
                # Validasi segitiga
                if self.validasi_segitiga(sisi1, sisi2, sisi3):
                    luas = self.hitung_luas_heron(sisi1, sisi2, sisi3)
                    print(f"Luas segitiga (rumus Heron): {luas:.2f} satuan persegi")
                else:
                    print("Input tidak valid! Ketiga sisi tidak membentuk segitiga.")
                    
            elif pilihan == '4':
                alas = float(input("Masukkan panjang alas (satuan): "))
                luas = float(input("Masukkan luas segitiga (satuan persegi): "))
                
                if alas > 0 and luas > 0:
                    tinggi = self.hitung_tinggi(alas, luas)
                    print(f"Tinggi segitiga: {tinggi} satuan")
                else:
                    print("Input tidak valid! Alas dan luas harus positif.")

# Untuk menjalankan kalkulator, aktifkan salah satu fungsi berikut:
if __name__ == "__main__":  
    # Untuk menjalankan kalkulator dengan class:
    kalkulator = KalkulatorSegitiga()
    kalkulator.jalankan()