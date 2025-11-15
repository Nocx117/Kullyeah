print("="*35)
print("Program Menghitung Luas Bangun Datar")
print("="*35,"\n")

def cek_inputan():
     global cek
     cek = list(inputan.lower())
     if 's' in cek and 'i' in cek or 'sisi' in cek:
          olah_angka()
          global sisi
          sisi = int(inputan)
     if 'p' in cek or 'panjang' in cek:
          olah_angka()
          global panjang
          panjang = int(inputan)
     if 'l' in cek or 'lebar' in cek:
          olah_angka()
          global lebar
          lebar = int(inputan)
     if 'j' in cek or 'jari' in cek or 'jari jari' in cek:
          olah_angka()
          global jari_jari
          jari_jari = int(inputan)

def logic():
     try:
          persegi()
     except:
          pass
     try:
          lingkaran()
     except:
          pass
     try:
          persegi_panjang()
     except:
          pass

def clear_cache():
     global sisi, panjang, lebar, jari_jari
     sisi = None
     panjang = None
     lebar = None
     jari_jari = None

def olah_angka():
     for i in list(cek):
          try:
               int(i)
          except:
               cek.remove(i)
     global inputan
     inputan = "".join(cek)

def persegi():
     print("luas perseginya", sisi * sisi)
     return sisi * sisi

def lingkaran():
     if jari_jari % 7 == 0:
          luas = 22/7 * jari_jari * jari_jari
     else:
          luas = 3.14 * jari_jari * jari_jari
     print("luas lingkarannya",luas)
     return luas

def persegi_panjang():
     try:
          print("luas persegi panjangnya", panjang * lebar)
          return panjang * lebar
     except NameError:
          if panjang != None:
               print("Kami tidak bisa menghitung luas persegi panjang karena lebar belum diinputkan")
          try:
               if lebar != None:
                    print("Kami tidak bisa menghitung luas persegi panjang karena panjang belum diinputkan")
          except NameError:
               pass
     
def inputannya():
     global inputan
     print("Silahkan menginputkan manual sisi/panjang/lebar/tinggi/jari jari/alas bangun datar yang ingin dihitung luasnya\ncth: sisi=5 atau jari jari = 7\nEnter untuk keluar\n")
     while True:
          inputan = input("")
          cek_inputan()
          if inputan == "":
               break

if __name__== "__main__":
     while True:
          inputannya()
          logic()
          clear_cache()
          ulang = input("Apakah ingin menghitung lagi? (y/n): ")
          if ulang.lower() == "n" or ulang == "":
               print("Terimakasih")
               print("="*35)
               break
          else:
               continue
          
