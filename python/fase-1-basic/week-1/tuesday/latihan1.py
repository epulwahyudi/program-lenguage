#contoh variable dan type data

#1. String (str): Teks atau karakter
name = "Epul"
address = "Jakarta"
#2. Boolean (bool): Nilai kebenaran (True/False)
is_male = True
is_female = False
#3. Numeric (Angka)
    #1 Integer(int): Bilangan Bulat
age = 26
    #2 Float: Bilangan desimal 
tinggi = 168.5
berat = 60.8
    #3 Complex: Bilangan kompleks
bilangan_komplek = 3 + 4j
#4. Sequence (Urutan)
    #1 List: Kumpulan data yang bisa diubah
hobi = ["menulis", "membaca","coding"]
angka = [1, 2, 3, 4, 5]
campur = ["epul", 1, True, 168.5]
    #2 Tuple: Kumpulan data yang tidak bisa diubah
koordinat = (4, 5)
warna_rgb = (255, 128, 0)
#5. Mapping
#Dictionary (dict): Kumpulan pasangan key-value
biodata = {
    "nama": "epul",
    "umur": 26,
    "hobi": ["membaca", "coding"]
}
#6. Set: Kumpulan data unik tanpa urutan
warna = {"merah", "hijau", "biru"}
angka_unik = {1, 2, 3, 3, 4, 4, 5}  # akan menjadi {1, 2, 3, 4, 5}

#memeriksa type data
print(type(name))                   #<class 'str'>
print(type(address))                #<class 'str'>
print(type(age))                    #<class 'int'>
print(type(is_male))                #<class 'bool'>
print(type(is_female))              #<class 'bool'>
print(type(tinggi))                 #<class 'float'>
print(type(berat))                  #<class 'float'>
print(type(bilangan_komplek))       #<class 'complex'>
print(type(hobi))                   #<class 'list'>
print(type(angka))                  #<class 'list'>
print(type(campur))                 #<class 'list'>
print(type(koordinat))              #<class 'tuple'>
print(type(warna_rgb))              #<class 'tuple'>
print(type(biodata))                #<class 'dict'>
print(type(warna))                  #<class 'set'>
print(type(angka_unik))             #<class 'set'>


#menampilkan data
print("Nama Saya : " ,name)
print("Alamat Saya : " ,address)
print("Usia Saya : " ,age)
print("Saya Laki-Laki : ", is_male)

