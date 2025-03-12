# **Hari 5-6: Input/Output & Manipulasi String** 

---

## **📌 Hari 5-6: Input, Output, dan Manipulasi String di Python**  

### **1. Input & Output di Python**  
✅ **Input (`input()`)** digunakan untuk menerima data dari pengguna.  
✅ **Output (`print()`)** digunakan untuk menampilkan data ke layar.  

---

### **1.1. Mengambil Input dari Pengguna**
Fungsi `input()` selalu mengembalikan data dalam bentuk **string**.  
Jika ingin angka, kita harus mengubahnya ke `int` atau `float`.  

🔹 **Contoh Input:**
```python
nama = input("Masukkan nama Anda: ")
usia = input("Masukkan usia Anda: ")

print("Halo", nama, "! Usia Anda adalah", usia)
```
📌 **Contoh Input & Output:**  
```
Masukkan nama Anda: Budi
Masukkan usia Anda: 25
Halo Budi! Usia Anda adalah 25
```

🔹 **Konversi Input ke Angka:**  
```python
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

hasil = angka1 + angka2
print("Hasil penjumlahan:", hasil)
```
📌 **Jika input `"5"` dan `"3"`, maka output = `8`**  

---

### **1.2. Menampilkan Output dengan `print()`**
🔹 **Penggunaan print dengan berbagai cara:**
```python
nama = "Andi"
usia = 30

# Cara 1: Menggunakan koma
print("Nama saya", nama, "dan usia saya", usia)

# Cara 2: Menggunakan string format lama (%)
print("Nama saya %s dan usia saya %d" % (nama, usia))

# Cara 3: Menggunakan format() (Python 3)
print("Nama saya {} dan usia saya {}".format(nama, usia))

# Cara 4: Menggunakan f-string (Python 3.6+)
print(f"Nama saya {nama} dan usia saya {usia}")
```
📌 **Output Semua Cara:**  
```
Nama saya Andi dan usia saya 30
```

**📌 Rekomendasi:** Gunakan **f-string** karena lebih mudah dibaca.

---

## **2. Manipulasi String**
Python menyediakan banyak fungsi untuk **mengolah teks**.

### **2.1. Mengubah Huruf Besar/Kecil**  
```python
teks = "Belajar Python"

print(teks.upper())  # BELAJAR PYTHON
print(teks.lower())  # belajar python
print(teks.title())  # Belajar Python
print(teks.capitalize())  # Belajar python
```

---

### **2.2. Menghitung Panjang String**  
```python
kalimat = "Python mudah!"
print(len(kalimat))  # Output: 13
```

---

### **2.3. Menghapus Spasi di Awal/Akhir**  
```python
kata = "  Python  "
print(kata.strip())  # "Python"
print(kata.lstrip())  # "Python  "
print(kata.rstrip())  # "  Python"
```

---

### **2.4. Mengambil Sebagian String (Slicing)**  
```python
teks = "Hello Python"
print(teks[0:5])  # "Hello"
print(teks[:5])   # "Hello" (dari awal sampai index ke-4)
print(teks[6:])   # "Python" (mulai dari index ke-6 sampai akhir)
print(teks[-6:])  # "Python" (ambil dari belakang)
```

---

### **2.5. Mengganti Kata dalam String**
```python
kalimat = "Saya suka apel"
kalimat_baru = kalimat.replace("apel", "jeruk")
print(kalimat_baru)  # Output: "Saya suka jeruk"
```

---

### **2.6. Memisahkan String (`split()`) dan Menggabungkan (`join()`)**
```python
data = "apel,jeruk,mangga"
list_buah = data.split(",")  # Pisahkan berdasarkan koma
print(list_buah)  # ['apel', 'jeruk', 'mangga']

gabung = "-".join(list_buah)
print(gabung)  # "apel-jeruk-mangga"
```

---

## **📝 Latihan Hari 5-6**
1️⃣ **Program Input-Output Sederhana**  
Buat program yang meminta nama dan kota asal pengguna, lalu tampilkan dengan format:  
_"Halo, [Nama]! Kamu berasal dari [Kota]."_  
```python
nama = input("Masukkan nama: ")
kota = input("Masukkan kota asal: ")

print(f"Halo, {nama}! Kamu berasal dari {kota}.")
```

---

2️⃣ **Membalik String**  
Buat program yang menerima input teks dari pengguna, lalu membaliknya.  
```python
teks = input("Masukkan teks: ")
print("Hasil balik:", teks[::-1])
```
📌 **Input:** `Python`  
📌 **Output:** `nohtyP`  

---

3️⃣ **Menghitung Jumlah Huruf dalam Kalimat**  
Buat program yang meminta pengguna memasukkan kalimat, lalu hitung jumlah hurufnya.  
```python
kalimat = input("Masukkan kalimat: ")
jumlah_huruf = len(kalimat.replace(" ", ""))  # Hapus spasi sebelum menghitung
print(f"Jumlah huruf dalam kalimat: {jumlah_huruf}")
```

---

4️⃣ **Mengganti Huruf Vokal dalam String**  
Buat program yang mengganti semua huruf vokal (`a, e, i, o, u`) dalam sebuah string dengan `*`.  
```python
teks = input("Masukkan teks: ")

# Ganti vokal dengan "*"
hasil = teks
for vokal in "aeiouAEIOU":
    hasil = hasil.replace(vokal, "*")

print("Hasil:", hasil)
```
📌 **Input:** `"Belajar Python"`  
📌 **Output:** `"B*l*j*r Pyth*n"`

---

### **📌 Kesimpulan Hari 5-6**
✅ **`input()`** untuk mengambil data dari pengguna  
✅ **`print()`** untuk menampilkan output  
✅ String dapat dimanipulasi dengan berbagai metode (`upper()`, `lower()`, `replace()`, dll.)  
✅ Bisa mengambil sebagian teks dengan slicing `[start:end]`  
✅ Bisa mengganti, membalik, atau menghitung jumlah huruf dalam string  

