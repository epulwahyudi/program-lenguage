# **operator dalam Python**   

---

## **📌 Hari 3-4: Operator dalam Python**  

### **1. Operator Aritmatika**  
Digunakan untuk operasi matematika dasar.  

| Operator | Nama              | Contoh  | Hasil |
|----------|------------------|---------|-------|
| `+`      | Penjumlahan      | `5 + 3` | `8`   |
| `-`      | Pengurangan      | `5 - 3` | `2`   |
| `*`      | Perkalian        | `5 * 3` | `15`  |
| `/`      | Pembagian        | `5 / 3` | `1.6667` |
| `//`     | Pembagian bulat  | `5 // 3` | `1`   |
| `%`      | Modulus (sisa bagi) | `5 % 3` | `2` |
| `**`     | Pangkat          | `5 ** 3` | `125` |

🔹 **Contoh:**
```python
a = 10
b = 3

print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian Bulat:", a // b)
print("Sisa Bagi:", a % b)
print("Pangkat:", a ** b)
```
📝 **Pemahaman:**  
- Gunakan `//` jika ingin hasil pembagian tanpa desimal.  
- `**` berguna untuk eksponensial (pangkat).  
- `%` sering dipakai untuk mengecek angka genap/ganjil (`x % 2 == 0` → genap).  

---

### **2. Operator Perbandingan**  
Digunakan untuk membandingkan dua nilai dan menghasilkan `True` atau `False`.

| Operator | Arti               | Contoh  | Hasil |
|----------|--------------------|---------|-------|
| `==`     | Sama dengan        | `5 == 3` | `False` |
| `!=`     | Tidak sama dengan  | `5 != 3` | `True`  |
| `>`      | Lebih besar        | `5 > 3` | `True`  |
| `<`      | Lebih kecil        | `5 < 3` | `False` |
| `>=`     | Lebih besar/sama   | `5 >= 3` | `True`  |
| `<=`     | Lebih kecil/sama   | `5 <= 3` | `False` |

🔹 **Contoh:**
```python
x = 7
y = 5

print("Apakah x lebih besar dari y?", x > y)
print("Apakah x lebih kecil dari y?", x < y)
print("Apakah x sama dengan y?", x == y)
print("Apakah x tidak sama dengan y?", x != y)
```
📝 **Pemahaman:**  
- Hasil dari operator perbandingan adalah `True` atau `False`.  
- Sering digunakan dalam percabangan (`if-else`).  

---

### **3. Operator Logika**  
Digunakan untuk menggabungkan ekspresi perbandingan.

| Operator | Arti  | Contoh | Hasil |
|----------|-------|--------|-------|
| `and`    | True jika **semua** benar | `(5 > 3) and (10 > 5)` | `True`  |
| `or`     | True jika **salah satu** benar | `(5 > 3) or (10 < 5)` | `True`  |
| `not`    | Membalik nilai (negasi) | `not(5 > 3)` | `False` |

🔹 **Contoh:**
```python
umur = 20
punya_sim = True

# Cek apakah boleh mengemudi
boleh_mengemudi = (umur >= 18) and punya_sim
print("Boleh mengemudi?", boleh_mengemudi)
```
📝 **Pemahaman:**  
- `and` hanya `True` jika **semua** kondisi benar.  
- `or` cukup satu kondisi `True`, hasilnya tetap `True`.  
- `not` membalik `True` ke `False` dan sebaliknya.  

---

## **📝 Latihan**  
1️⃣ Buat program yang meminta dua angka dari user, lalu tampilkan hasil semua operasi aritmatika di antara keduanya.  
2️⃣ Buat program yang mengecek apakah angka yang diinput adalah **genap atau ganjil**.  

🔹 **Contoh Kode untuk latihan 2:**
```python
angka = int(input("Masukkan angka: "))

if angka % 2 == 0:
    print(f"{angka} adalah angka genap")
else:
    print(f"{angka} adalah angka ganjil")
```
💡 **Hint:**  
- Angka genap adalah angka yang habis dibagi 2 (`x % 2 == 0`).  
- Angka ganjil adalah angka yang tidak habis dibagi 2 (`x % 2 != 0`).  

---
