#list kumpulan item yang dapat dirubah
buah = ["apel", "jeruk", "mangga", "pisang"]
buah[0] = "anggur"  # mengubah elemen pertama
buah[1] = "Leci"
buah.append ("manggis") # menambah 1 elemen
buah.extend(["semangka", "melon"]) # menambah lebih dari 1 elemen
print(buah) #
print(f"{buah}")

#tuple kumpulan item yang tidak dapat dirubah
koordinat = (3, 5)
#koordinat[0] = 10  # ini akan error!

#dictionary kumpulan pasangan key-value
siswa = {
    "nama":"epul",
    "umur":28,
    "jurusan":"teknik informatika",
    "GPA":4.95
}
print(siswa["nama"])  #epul
siswa["alamat"] = "Jakarta"  # menambah pasangan key-value baru
keys = ["nama", "umur", "jurusan", "GPA", "alamat"] #comprehension untuk mencetak dictionery
print({key: siswa[key] for key in keys}) # loop data ini akan menampilkan data kesamping

keys = ["nama", "umur", "jurusan", "GPA", "alamat"]
for key in keys:
    print(f"{key}: {siswa[key]}") # ini menampilkan data berurut kebawah

