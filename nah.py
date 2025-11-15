print("="*35)
print("Program Menghitung Luas Bangun Datar")
print("="*35,"\n")

def cek_inputan():
     global cek
     cek = list(inputan.lower())
     if 's' in cek and 'i' in cek:
        return persegi()
     if 'p' in cek or 'panjang' in cek:
          return persegi_panjang()
     if 'j' in cek or 'jari' in cek:
          return lingkaran()

def persegi():
     if cek.count("s") == 2 or cek.count("i") == 2:
          anu = len(cek)
     if cek.index('s') != 0:
          kan = cek.index('s')
          del cek[0:kan]
     if anu >= 3:
          sisi = cek[4:anu]
     if "=" in sisi:
          sisi.remove("=")
     sisi = [str(digit) for digit in sisi]
     sisi = "".join(sisi)
     sisi = int(sisi)
     print("luas perseginya", sisi * sisi)
     return sisi * sisi

def lingkaran():
     if cek.count("j") >= 1 or cek.count("jari") >= 1:
          anu = len(cek)
     if cek.index('j') != 0:
          kan = cek.index('j')
          del cek[0:kan]
     if cek.count("j") > 1:
          jari_jari = cek[9:anu]
     if cek.count('j') == 1:
          jari_jari = cek[5:anu]
     if "=" in jari_jari:
          jari_jari.remove("=")
     jari_jari = [str(digit) for digit in jari_jari]
     jari_jari = "".join(jari_jari)
     jari_jari = int(jari_jari)
     if jari_jari % 7 == 0:
          luas = 22/7 * jari_jari * jari_jari
          print("luas lingkarannya",luas)
     else:
          luas = 3.14 * jari_jari * jari_jari
          print("luas lingkarannya", luas)
     return luas

def persegi_panjang():
     if 'p' in cek and 'l' in cek:
          if cek.count("p") == 1 and cek.count("l") == 1:
               anu = len(cek)
               if cek.index('p') != 0:
                    kan = cek.index('p')
                    del cek[0:kan]
               p = cek[6:anu]
               if "=" in p:
                    p.remove("=")
               p = [str(digit) for digit in p]
               p = "".join(p)
               p = int(p)
               if cek.index('l') != 0:
                    kan = cek.index('l')
                    del cek[0:kan]
               l = cek[5:anu]
               if "=" in l:
                    l.remove("=")
               l = [str(digit) for digit in l]
               l = "".join(l)
               l = int(l)
               print("luas persegi panjangnya", p * l)
               return p * l
while True:
    print("Silahkan menginputkan manual sisi/panjang/lebar/tinggi/jari jari/alas bangun datar yang ingin dihitung luasnya cth: sisi=5 atau jari jari = 7\nEnnter untuk keluar")
    inputan = input("")
    if inputan == "":
         break
    cek_inputan()
    ulang = input("Apakah ingin menghitung lagi? (y/n): ")
    if ulang.lower() == "n":
         print("Terimakasih")
         print("="*35)
         break
    else:
     continue
    
