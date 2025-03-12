# **📌 Hari 7-8: Praktik Program Sederhana & Mini Project Kalkulator**  

## **1. Praktik Program Sederhana (3-4 per minggu)**  
Kita akan buat beberapa program sederhana berdasarkan materi sebelumnya.  

---

### **1.1. Program 1: Menentukan Bilangan Ganjil atau Genap**  
🔹 **Konsep:**  
- User memasukkan angka.  
- Program menentukan apakah angka itu ganjil atau genap.  

🔹 **Kode:**
```python
angka = int(input("Masukkan angka: "))

if angka % 2 == 0:
    print(f"{angka} adalah bilangan GENAP.")
else:
    print(f"{angka} adalah bilangan GANJIL.")
```
📌 **Contoh Output:**  
```
Masukkan angka: 7  
7 adalah bilangan GANJIL.  
```

---

### **1.2. Program 2: Konversi Suhu (Celsius ke Fahrenheit)**  
🔹 **Konsep:**  
- User memasukkan suhu dalam Celsius.  
- Program mengonversinya ke Fahrenheit dengan rumus:  
  \[
  F = (C \times 9/5) + 32
  \]  

🔹 **Kode:**
```python
celsius = float(input("Masukkan suhu dalam Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")
```
📌 **Contoh Output:**  
```
Masukkan suhu dalam Celsius: 30  
30.0°C = 86.0°F  
```

---

### **1.3. Program 3: Hitung Luas & Keliling Lingkaran**  
🔹 **Konsep:**  
- User memasukkan jari-jari lingkaran.  
- Program menghitung **luas** dan **keliling** lingkaran.  
- Rumus:  
  \[
  \text{Luas} = \pi \times r^2
  \]  
  \[
  \text{Keliling} = 2 \times \pi \times r
  \]  
- Gunakan `math.pi` untuk nilai **π (3.14159)**.

🔹 **Kode:**
```python
import math

r = float(input("Masukkan jari-jari lingkaran: "))

luas = math.pi * (r ** 2)
keliling = 2 * math.pi * r

print(f"Luas Lingkaran: {luas:.2f}")
print(f"Keliling Lingkaran: {keliling:.2f}")
```
📌 **Contoh Output:**  
```
Masukkan jari-jari lingkaran: 10  
Luas Lingkaran: 314.16  
Keliling Lingkaran: 62.83  
```

---

### **1.4. Program 4: Kalkulator Sederhana**  
🔹 **Konsep:**  
- User memasukkan dua angka dan operasi (`+, -, *, /`).  
- Program melakukan perhitungan sesuai operasi yang dipilih.  

🔹 **Kode:**
```python
angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    hasil = angka1 / angka2
else:
    hasil = "Operator tidak valid"

print(f"Hasil: {hasil}")
```
📌 **Contoh Output:**  
```
Masukkan angka pertama: 10  
Masukkan operator (+, -, *, /): *  
Masukkan angka kedua: 5  
Hasil: 50  
```

---

## **2. Mini Project: Kalkulator Sederhana**
Sekarang, kita buat **versi lebih lengkap** dari kalkulator sebelumnya.  
✅ **Bisa digunakan terus-menerus tanpa harus restart**  
✅ **Bisa menangani pembagian oleh nol**  

🔹 **Kode:**
```python
while True:
    angka1 = float(input("Masukkan angka pertama: "))
    operator = input("Masukkan operator (+, -, *, /) atau ketik 'exit' untuk keluar: ")

    if operator.lower() == "exit":
        print("Kalkulator ditutup. Terima kasih!")
        break

    angka2 = float(input("Masukkan angka kedua: "))

    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        if angka2 == 0:
            hasil = "Error: Tidak bisa membagi dengan nol!"
        else:
            hasil = angka1 / angka2
    else:
        hasil = "Operator tidak valid"

    print(f"Hasil: {hasil}")
    print("-" * 30)
```
📌 **Contoh Interaksi:**
```
Masukkan angka pertama: 15  
Masukkan operator (+, -, *, /) atau ketik 'exit' untuk keluar: /  
Masukkan angka kedua: 3  
Hasil: 5.0  
------------------------------
Masukkan angka pertama: 10  
Masukkan operator (+, -, *, /) atau ketik 'exit' untuk keluar: exit  
Kalkulator ditutup. Terima kasih!  
```

---

## **📌 Kesimpulan Hari 7-8**
✅ Kita telah membuat **beberapa program sederhana** seperti:  
- Menentukan bilangan **ganjil/genap**  
- Konversi **Celsius ke Fahrenheit**  
- Menghitung **luas & keliling lingkaran**  
- Kalkulator sederhana  

✅ Kita juga telah membuat **Mini Project Kalkulator** dengan fitur:  
- Bisa **terus berjalan** tanpa restart  
- Bisa menangani **pembagian oleh nol**  
- Bisa **keluar dari program** dengan mengetik `exit`  

---

Sekarang, kamu bisa mulai bereksperimen dengan **mengembangkan program ini**! Misalnya:  
- Tambahkan **operasi pangkat (`**`) atau modulus (`%`)** pada kalkulator.  
- Tambahkan **menu pilihan** sebelum memasukkan angka agar lebih rapi.  

