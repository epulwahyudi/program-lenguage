# For loop - untuk iterasi yang sudah diketahui jumlahnya
print("For loop dengan list")
for buah in ["apel","jeruk","manggis"]:
    print(f"Saya suka {buah}")

# Foor loop dengan range
print("\nFor loop dengan range:")
for i in range(1,6):  # 1 sampai 5
    print(f"iterasi ke-{i}")

# For loop dengan dictionary
print("\nFor loop dengan dictionary")
siswa = {"nama": "Andi", "umur": 16, "kelas": "12A"}
for key in siswa:
    print(f"{key}:{siswa[key]}")

# For loop dengan item() untuk dictionary
print("\nFor loop dengan items():") 
for key, value in siswa.items():
    print(f"{key}: {value}")


# while loop - untuk iterasi yang belum diketahui jumlahnya
print("\nWhile loop")
count = 1
while count <=10:
    print(f"Count: {count}")
    count += 1   #incrment count


#While loop degan break
print("\nWhile loop dengan break:")
i = 1
while True:
    print(f"Iterasi {i}")
    if i >=3:
        print("Break!")
        break
    i += 1


# For loop dengan continue
print("\nFor loop dengan continue:")
for i in range(1, 6):
    if i == 3:
        print("Skip 3!")
        continue  # skip iterasi ini
    print(f"Nilai: {i}")