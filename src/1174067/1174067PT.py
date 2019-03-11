###1###
#fungsi
def fungsi():
    print("string")
fungsi() #memanggil pungsi

#inputan fungsi
def luasSegitiga(alas, tinggi):
    luas = (alas * tinggi)/2
    print ("Luas segitiga : %f" % luas) # %f float 
luasSegitiga(8, 12) #memanggil fungsi luasSegitiga

#kembalian fungsi
def luasSegitiga(alas, tinggi):
    luas = (alas * tinggi)/2
    return luas
print ("Luas segitiga : %f" % luasSegitiga(8, 12))


###2###
import tes.moduleKaka
print(tes.moduleKaka.fullName())

##3##
#file identitas.py
class Identitas:
  def __init__(self, saya):
    self.saya = saya
  def nama(self):
    r = self.saya
    return r

#file nain.py
from identitas import Identitas
saya = "Kaka"
siapa = Identitas(saya)
hasil1=siapa.nama()

##4##
