Siap! Mari kita breakdown setiap **syntax** dalam kode yang kita buat dan buat **glosari** untuk pemahaman lebih dalam.  

---

## **📝 Glosari Syntax Python (Classes & Objects)**  

### **1️⃣ Definisi Kelas (`class`)**  
```python
class Anggota:
```
🔹 `class` digunakan untuk mendefinisikan **kelas (class)** dalam Python.  
🔹 `Anggota` adalah nama kelas yang kita buat.  

---

### **2️⃣ Constructor (`__init__`)**  
```python
def __init__(self, nama, id_anggota, tanggal_bergabung, status="Aktif"):
```
🔹 `__init__` adalah **constructor** yang akan otomatis dipanggil saat objek dibuat.  
🔹 `self` adalah referensi ke **instance (objek) yang sedang dibuat**.  
🔹 `nama`, `id_anggota`, `tanggal_bergabung`, dan `status` adalah **atribut (properties)** dari objek.  
🔹 `status="Aktif"` → nilai default **"Aktif"** jika tidak diberikan nilai saat objek dibuat.  

---

### **3️⃣ Atribut (`self.nama`, `self.id_anggota`, dst.)**  
```python
self.nama = nama
self.id_anggota = id_anggota
self.tanggal_bergabung = tanggal_bergabung
self.status = status
```
🔹 `self.nama` → **Atribut objek** yang menyimpan nama anggota.  
🔹 `self.id_anggota` → Menyimpan ID anggota.  
🔹 `self.tanggal_bergabung` → Menyimpan tanggal bergabung.  
🔹 `self.status` → Menyimpan status anggota.  

📌 **"self." digunakan untuk membuat atribut yang bisa diakses di seluruh class.**  

---

### **4️⃣ Method (`info()`)**  
```python
def info(self):
    return f"Nama: {self.nama} | ID: {self.id_anggota} | Bergabung: {self.tanggal_bergabung} | Status: {self.status}"
```
🔹 `def info(self):` → **Method (fungsi dalam class)** untuk menampilkan informasi anggota.  
🔹 `return f"...{self.nama}..."` → **Mengembalikan string format** yang berisi informasi anggota.  

---

### **5️⃣ Membuat Objek (Instansiasi Class)**  
```python
anggota1 = Anggota("Epul", "A91", "10 Maret 2025")
anggota2 = Anggota("Wahyudi", "A92", "12 Maret 2025")
```
🔹 `anggota1 = Anggota(...)` → Membuat objek baru dari class `Anggota`.  
🔹 `"Epul"` → Nama anggota pertama.  
🔹 `"A91"` → ID anggota pertama.  
🔹 `"10 Maret 2025"` → Tanggal bergabung anggota pertama.  

---

### **6️⃣ Memanggil Method (`info()`)**
```python
print(anggota1.info())
print(anggota2.info())
```
🔹 `anggota1.info()` → Memanggil method `info()` dari objek `anggota1`.  
🔹 `print(...)` → Menampilkan hasil method `info()`.  

📌 **Outputnya:**
```
Nama: Epul | ID: A91 | Bergabung: 10 Maret 2025 | Status: Aktif
Nama: Wahyudi | ID: A92 | Bergabung: 12 Maret 2025 | Status: Aktif
```

---

### **7️⃣ Method untuk Mengubah Atribut (`perbarui_status()`)**
```python
def perbarui_status(self, status_baru):
    self.status = status_baru
    print(f"Status {self.nama} diperbarui menjadi {self.status}")
```
🔹 `def perbarui_status(self, status_baru):` → **Method untuk memperbarui status anggota**.  
🔹 `self.status = status_baru` → Mengubah nilai atribut `status`.  
🔹 `print(f"...")` → Menampilkan konfirmasi perubahan.  

📌 **Contoh Pemanggilan:**  
```python
anggota1.perbarui_status("Non-Aktif")
```
💡 **Output:**  
```
Status Epul diperbarui menjadi Non-Aktif
```

---

### **8️⃣ List untuk Menyimpan Banyak Objek**
```python
daftar_anggota = [
    Anggota("Epul", "A91", "10 Maret 2025"),
    Anggota("Wahyudi", "A92", "12 Maret 2025"),
    Anggota("Siti", "A93", "15 Maret 2025")
]
```
🔹 `daftar_anggota = [...]` → **List untuk menyimpan banyak objek anggota**.  
🔹 `Anggota(...)` → Setiap elemen dalam list adalah objek dari class `Anggota`.  

---

### **9️⃣ Looping untuk Menampilkan Semua Anggota**
```python
for anggota in daftar_anggota:
    print(anggota.info())
```
🔹 `for anggota in daftar_anggota:` → **Looping melalui setiap objek dalam list**.  
🔹 `anggota.info()` → Memanggil method `info()` untuk setiap anggota dalam list.  

---

### **🔟 Program Utama dengan Input dari Pengguna**
```python
while True:
    print("\n=== Sistem Manajemen Anggota ===")
    print("1. Tampilkan daftar anggota")
    print("2. Tambah anggota")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        for anggota in daftar_anggota:
            print(anggota.info())
    elif pilihan == "2":
        nama = input("Masukkan nama: ")
        id_anggota = input("Masukkan ID anggota: ")
        tanggal = input("Masukkan tanggal bergabung: ")
        daftar_anggota.append(Anggota(nama, id_anggota, tanggal))
        print("Anggota berhasil ditambahkan!")
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
```
🔹 `while True:` → Loop **infinite** untuk menjalankan program terus menerus.  
🔹 `input("Pilih menu (1-3): ")` → Menerima input dari pengguna.  
🔹 `if pilihan == "1":` → Jika user memilih 1, tampilkan daftar anggota.  
🔹 `elif pilihan == "2":` → Jika user memilih 2, tambahkan anggota baru dengan input.  
🔹 `elif pilihan == "3": break` → Jika user memilih 3, keluar dari loop dan program berhenti.  


### **📌 11. `append()` → Menambahkan Objek ke List**  
```python
daftar_anggota = []

# Menambahkan anggota baru ke dalam list
anggota_baru = Anggota("Doni", "A94", "20 Maret 2025")
daftar_anggota.append(anggota_baru)

# Menampilkan semua anggota setelah penambahan
for anggota in daftar_anggota:
    print(anggota.info())
```
🔹 `daftar_anggota.append(anggota_baru)` → Menambahkan **objek baru** ke dalam list `daftar_anggota`.  
🔹 **`append()` selalu menambahkan di akhir list.**  

📌 **Contoh Output:**
```
Nama: Doni | ID: A94 | Bergabung: 20 Maret 2025 | Status: Aktif
```

---

### **📌 12. `remove()` → Menghapus Objek dari List**  
```python
id_hapus = "A94"  # ID anggota yang ingin dihapus

for anggota in daftar_anggota:
    if anggota.id_anggota == id_hapus:
        daftar_anggota.remove(anggota)
        print(f"Anggota dengan ID {id_hapus} berhasil dihapus.")
        break
```
🔹 `daftar_anggota.remove(anggota)` → **Menghapus objek dari list** berdasarkan ID yang cocok.  
🔹 `break` digunakan agar **loop berhenti** setelah menemukan anggota yang ingin dihapus.  

📌 **Contoh Output jika ID "A94" dihapus:**
```
Anggota dengan ID A94 berhasil dihapus.
```

---

### **📝 Perbaikan Menu Interaktif dengan `append()` & `remove()`**
Sekarang, kita modifikasi **menu interaktif** agar bisa menambah dan menghapus anggota.  

```python
daftar_anggota = [
    Anggota("Epul", "A91", "10 Maret 2025"),
    Anggota("Wahyudi", "A92", "12 Maret 2025"),
    Anggota("Siti", "A93", "15 Maret 2025")
]

while True:
    print("\n=== Sistem Manajemen Anggota ===")
    print("1. Tampilkan daftar anggota")
    print("2. Tambah anggota")
    print("3. Hapus anggota")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        for anggota in daftar_anggota:
            print(anggota.info())

    elif pilihan == "2":
        nama = input("Masukkan nama: ")
        id_anggota = input("Masukkan ID anggota: ")
        tanggal = input("Masukkan tanggal bergabung: ")
        daftar_anggota.append(Anggota(nama, id_anggota, tanggal))
        print("✅ Anggota berhasil ditambahkan!")

    elif pilihan == "3":
        id_hapus = input("Masukkan ID anggota yang ingin dihapus: ")
        for anggota in daftar_anggota:
            if anggota.id_anggota == id_hapus:
                daftar_anggota.remove(anggota)
                print(f"✅ Anggota dengan ID {id_hapus} berhasil dihapus.")
                break
        else:
            print("⚠️ ID tidak ditemukan!")

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("⚠️ Pilihan tidak valid!")
```

---

## **🚀 Kesimpulan**  
🔹 `append()` → Menambahkan anggota baru ke dalam list.  
🔹 `remove()` → Menghapus anggota dari list berdasarkan ID.  
🔹 Sekarang sistem bisa **menampilkan, menambah, dan menghapus anggota**!  
