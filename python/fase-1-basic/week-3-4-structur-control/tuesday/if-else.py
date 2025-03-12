#struktur dasar

umur = 17

if umur >= 18:
    print("anda sudah dewasa")
else:
    print("anda masih dibawah umur")


#if-elif-else untuk multiple conditions
nilai = 100

if nilai >= 90:
    grad = "A"
elif nilai >= 80:
    grad = "B"
elif nilai >= 70:
    grad = "C"
elif nilai <= 60:
    grad = "D"
else:
    grad = "E"

print(f"Nilai {nilai} mendapat grade {grad}")

#if bersarang
is_member = True
total_belanja = 200000

if is_member:
    print("Selamat datang, Member!")
    if total_belanja > 100000:
        diskon = 15
    else:
        diskon = 10
else:
    if total_belanja > 100000:
        diskon = 5
    else:
        diskon = 0

print(f"Anda mendapatkan diskon {diskon}%")