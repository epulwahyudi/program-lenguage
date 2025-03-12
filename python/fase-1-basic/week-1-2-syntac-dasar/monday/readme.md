Saya akan menjelaskan tentang variabel dan tipe data dalam Python secara detail.

### Variabel
Variabel adalah tempat untuk menyimpan data dalam program. Bayangkan variabel seperti sebuah kotak yang diberi nama, dimana Anda bisa menyimpan nilai di dalamnya. 

Aturan penamaan variabel di Python:
1. Harus dimulai dengan huruf atau underscore (_)
2. Hanya boleh mengandung huruf, angka, dan underscore
3. Case sensitive (nama_saya berbeda dengan Nama_Saya)
4. Tidak boleh menggunakan kata kunci Python (seperti if, for, while, dll)

Contoh:
```python
nama = "epul"          # valid
_umur = 25             # valid
nama1 = "Andi"         # valid
1nama = "Citra"        # tidak valid (dimulai dengan angka)
nama saya = "Dedi"     # tidak valid (mengandung spasi)
```

### Tipe Data di Python
1. **Numeric (Angka)**
   - **Integer (int)**: Bilangan bulat
     ```python
     umur = 25
     jumlah_siswa = -10
     ```
   - **Float**: Bilangan desimal
     ```python
     tinggi = 175.5
     berat = 65.8
     ```
   - **Complex**: Bilangan kompleks
     ```python
     bilangan_kompleks = 3 + 4j
     ```

2. **String (str)**: Teks atau karakter
   ```python
   nama = "Budi"
   alamat = 'Jalan Merdeka'
   paragraf = """Ini adalah
   paragraf panjang"""
   ```

3. **Boolean (bool)**: Nilai kebenaran (True/False)
   ```python
   is_married = False
   is_working = True
   ```

4. **Sequence (Urutan)**
   - **List**: Kumpulan data yang bisa diubah
     ```python
     hobi = ["membaca", "menulis", "coding"]
     angka = [1, 2, 3, 4, 5]
     campuran = ["Budi", 25, True, 175.5]
     ```
   - **Tuple**: Kumpulan data yang tidak bisa diubah
     ```python
     koordinat = (4, 5)
     warna_rgb = (255, 128, 0)
     ```

5. **Mapping**
   - **Dictionary (dict)**: Kumpulan pasangan key-value
     ```python
     biodata = {
         "nama": "Budi",
         "umur": 25,
         "hobi": ["membaca", "coding"]
     }
     ```

6. **Set**: Kumpulan data unik tanpa urutan
   ```python
   warna = {"merah", "hijau", "biru"}
   angka_unik = {1, 2, 3, 3, 4, 4, 5}  # akan menjadi {1, 2, 3, 4, 5}
   ```

### Memeriksa Tipe Data
Anda bisa menggunakan fungsi `type()` untuk memeriksa tipe data:
```python
nama = "Budi"
umur = 25
tinggi = 175.5

print(type(nama))    # <class 'str'>
print(type(umur))    # <class 'int'>
print(type(tinggi))  # <class 'float'>
```

### Konversi Tipe Data
Python memungkinkan konversi antar tipe data:
```python
# String ke Integer
angka_str = "123"
angka_int = int(angka_str)    # 123

# Integer ke String
umur = 25
umur_str = str(umur)          # "25"

# String ke Float
tinggi_str = "175.5"
tinggi_float = float(tinggi_str)  # 175.5
```
