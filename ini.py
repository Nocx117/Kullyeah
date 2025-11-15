print("="*35)
print("Program Menghitung Luas Bangun Datar")
print("="*35)

while True:
    print("""\nSilahkan pilih nomor berapa untuk menghitung bangun datar yang ada di bawah ini
    1) Lingkaran
    2) Persegi
    3) Persegi panjang
    4) Segitiga
    """)
    inputan = input("Nomor ke = ")
    if inputan == "1" or inputan.lower() in "lingkaran":
        jari_jari = int(input("Masukkan jari jari = "))
        if jari_jari % 7 == 0:
            luas = 22/7 * jari_jari*jari_jari
        else:
            luas = 3.14 * jari_jari*jari_jari
    elif inputan == "2" or inputan.lower() in "persegi":
        sisi = int(input("Masukkan sisi = "))
        luas = sisi * sisi
    elif inputan == "3" or inputan.lower() in "persegi panjang":
        p = int(input("Masukkan panjang = "))
        l = int(input("Masukkan lebar = "))
        luas = p * l
    elif inputan == "4" or inputan.lower() in "segitiga":
        a = int(input("Masukkan alas = "))
        t = int(input("Masukkan tinggi = "))
        luas = a * t / 2
    else:
        print("Masukkan angka yang bener dong!")
        continue
    print("="*35)
    ulang = input("Program Selesai ingin mengulang? (y/n)= ")
    if ulang.lower() == "n":
        print("Terimakasih")
        print("="*35)
        break
    else:
        print("="*35)
        continue
