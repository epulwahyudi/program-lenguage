# **variabel dan tipe data**

---

## **📌 Hari 1-2: Variabel dan Tipe Data dalam Python**  

### **1. Apa itu Variabel?**  
Variabel adalah wadah untuk menyimpan nilai atau data di dalam program.  
- Bisa diisi dengan berbagai jenis data (angka, teks, dll.).  
- Bisa diubah nilainya selama program berjalan.  
- Penamaan variabel harus jelas dan mengikuti aturan Python.  

🔹 **Contoh sederhana variabel:**
```python
nama = "Andi"
umur = 25
tinggi = 170.5
is_student = True

print(nama)
print(umur)
print(tinggi)
print(is_student)
```
📌 **Hasil Output:**  
```
Andi  
25  
170.5  
True  
```

---

### **2. Aturan Penamaan Variabel di Python**  
✅ Harus dimulai dengan huruf atau underscore (`_`)  
✅ Tidak boleh menggunakan spasi (gunakan `_` jika perlu)  
✅ Tidak boleh diawali dengan angka  
✅ Harus bersifat deskriptif  

🔹 **Contoh yang benar:**
```python
nama_lengkap = "Budi Santoso"  # Menggunakan underscore
usia = 30
_jumlah_barang = 10  # Boleh menggunakan underscore di awal
```
🔹 **Contoh yang salah (akan error):**
```python
2angka = 50      # ❌ Tidak boleh diawali angka
nama lengkap = "Budi"  # ❌ Tidak boleh pakai spasi
if = "kondisi"   # ❌ Tidak boleh pakai kata kunci Python
```

---

### **3. Tipe Data di Python**  
Python memiliki beberapa tipe data utama:  

| Tipe Data  | Contoh | Keterangan |
|------------|--------|------------|
| **Integer (`int`)** | `10`, `-5`, `1000` | Bilangan bulat |
| **Float (`float`)** | `3.14`, `-0.99`, `100.5` | Bilangan desimal |
| **String (`str`)** | `"Hello"`, `'Python'` | Teks atau karakter |
| **Boolean (`bool`)** | `True`, `False` | Nilai logika |
| **List (`list`)** | `[1, 2, 3]`, `["a", "b", "c"]` | Kumpulan data dalam satu variabel |
| **Tuple (`tuple`)** | `(1, 2, 3)`, `("a", "b", "c")` | Mirip `list`, tapi tidak bisa diubah |
| **Dictionary (`dict`)** | `{"nama": "Ali", "umur": 25}` | Data berpasangan (key-value) |

🔹 **Contoh penggunaan tipe data:**
```python
# Integer
usia = 25

# Float
berat_badan = 60.5

# String
nama = "Dina"

# Boolean
is_menikah = False

# List
hobi = ["membaca", "berenang", "coding"]

# Tuple
koordinat = (10.5, 20.3)

# Dictionary
mahasiswa = {
    "nama": "Dina",
    "umur": 22,
    "jurusan": "Informatika"
}

print(usia, type(usia))
print(berat_badan, type(berat_badan))
print(nama, type(nama))
print(is_menikah, type(is_menikah))
print(hobi, type(hobi))
print(koordinat, type(koordinat))
print(mahasiswa, type(mahasiswa))
```
📌 **Output & tipe data yang dihasilkan:**  
```
25 <class 'int'>  
60.5 <class 'float'>  
Dina <class 'str'>  
False <class 'bool'>  
['membaca', 'berenang', 'coding'] <class 'list'>  
(10.5, 20.3) <class 'tuple'>  
{'nama': 'Dina', 'umur': 22, 'jurusan': 'Informatika'} <class 'dict'>  
```

---

### **4. Konversi Tipe Data**  
Kadang kita perlu mengubah tipe data satu ke yang lain.  

🔹 **Contoh konversi tipe data:**
```python
angka_str = "100"  # String
angka_int = int(angka_str)  # Ubah ke integer

angka_float = float(angka_int)  # Ubah ke float

bool_ke_str = str(True)  # Ubah boolean ke string

print(angka_int, type(angka_int))
print(angka_float, type(angka_float))
print(bool_ke_str, type(bool_ke_str))
```
📌 **Output:**  
```
100 <class 'int'>  
100.0 <class 'float'>  
True <class 'str'>  
```
📌 **Catatan:**  
- `int()` mengubah ke integer.  
- `float()` mengubah ke float.  
- `str()` mengubah ke string.  
- `bool()` mengubah ke boolean (`0 → False`, selain itu `True`).  

---

## **📝 Latihan**  
1️⃣ Buat variabel dengan tipe data `int`, `float`, `str`, dan `bool`, lalu cetak dengan `type()`.  
2️⃣ Minta input nama dan usia dari user, lalu cetak dengan format:  
   _"Halo, [Nama]! Tahun depan usiamu [Usia+1] tahun."_  
3️⃣ Buat program yang mengonversi input angka (string) ke `int` dan melakukan perhitungan.  

🔹 **Contoh Kode untuk latihan 2:**
```python
nama = input("Masukkan nama: ")
usia = int(input("Masukkan usia: "))

print(f"Halo, {nama}! Tahun depan usiamu {usia + 1} tahun.")
```

---
