# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:16:22 2019

@author: fernandols
"""

from fungsi_fernando import penulisan
from 3lib import penulisan

print(penulisan(int(input("Masukan NPM :"))))

import kalkulator

a=100
b=50

hasil1=kalkulator.Penambahan(a,b)
hasil2=kalkulator.Pengurangan(a,b)
hasil3=kalkulator.Perkalian(a,b)
hasil4=kalkulator.Pembagian(a,b)

from Ngitung import Ngitung

a=200
b=25

hitung = Ngitung(a, b)

hasil1 = hitung.Penambahan()
hasil2 = hitung.Pengurangan()
hasil3 = hitung.Perkalian()
hasil4 = hitung.Pembagian()

lib = __import__('3lib')

npm = "1174072"

lib.printNPM(npm)
lib.printNPMDuaDijit(npm)
lib.printNPMTigaNomor(npm)
lib.printNPMAngkaUrutTiga(npm)
lib.printNPMBerbaris(npm)
lib.printPenjumlahanNPM(npm)
lib.printPerkalianNPM(npm)
lib.printAngkaGenapNPM(npm)
lib.printAngkaGenjilNPM(npm)
lib.printAngkaPrimaNPM(npm)
print()
from kelas3lib import kelas3lib

npm = "1174072"

k3lib = kelas3lib(npm)

k3lib.printNPM()
k3lib.printNPMDuaDijit()
k3lib.printNPMTigaNomor()
k3lib.printNPMAngkaUrutTiga()
k3lib.printNPMSatuPersatu()
k3lib.printPenjumlahanNPM()
k3lib.printPerkalianNPM()
k3lib.printAngkaGenapNPM()
k3lib.printAngkaGanjilNPM()
k3lib.printAngkaPrimaNPM() 