#operasi aritmatika
a = 100
b = 10

penjumlahan = a + b
pengurangan = a - b
perkalian = a * b
pembagian = a / b
pembagian_bulat = a // b
sisa_bagi = a % b
pangkat = a ** b

print("ini adalah hasil penjumlahan =" ,penjumlahan)
print("ini adalah hasil pengurangan = " ,pengurangan)
print("ini adalah hasil perkalian = ",perkalian)
print("ini adalah hasil pembagian = ",pembagian)
print("ini adalah hasil pembagian bulat = ",pembagian_bulat)
print("ini adalah hasil sisa bagi = ",sisa_bagi)
print("ini adalah hasil pangkat dari a dan b = " ,pangkat)

# Python tidak mengizinkan konkatenasi (penggabungan) string dengan tipe data selain string. :
#contoh
#print("ini adalah hasil penjumlahan =" +penjumlahan) # ini akan muncul eror 
#  File "C:\Docker\Belajar Python\Fase 1 Dasar-Dasar Python 2 bulan\Week 1\variable dan type data\latihan2.py", line 23, in <module>
#    print("ini adalah hasil penjumlahan =" +penjumlahan)
#          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
#TypeError: can only concatenate str (not "int") to str


#Solusinya, ubah penjumlahan menjadi string menggunakan str(), seperti ini
print("ini adalah hasil penjumlahan =" + str(penjumlahan))

#Atau gunakan f-string untuk format yang lebih rapi:
print(f"Ini adalah hasil penjumlahan = {penjumlahan}")

#Atau gunakan , dalam print(), yang otomatis menangani tipe data berbeda:
print("Ini adalah hasil penjumlahan =", penjumlahan)
