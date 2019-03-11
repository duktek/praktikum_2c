# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 00:27:44 2019

@author: Difaal21
"""

import kalkulator

a=100
b=50

hasil1=kalkulator.Penambahan(a,b)
hasil2=kalkulator.Pengurangan(a,b)
hasil3=kalkulator.Perkalian(a,b)
hasil4=kalkulator.Pembagian(a,b)

from Ngitung import Ngitung

a=100
b=50

hitung = Ngitung(a, b)

hasil1 = hitung.Penambahan()
hasil2 = hitung.Pengurangan()
hasil3 = hitung.Perkalian()
hasil4 = hitung.Pembagian()

lib = __import__('3lib')

npm = "1174006"

lib.printNPM(npm)
lib.printNPMDuaDijit(npm)
lib.printNPMTigaDijit(npm)
lib.printNPMDigitKetiga(npm)
lib.printNPMSatuPersatu(npm)
lib.printNPMPenjumlahan(npm)
lib.printNPMPerkalian(npm)
lib.printNPMDijitGenap(npm)
lib.printNPMDijitGanjil(npm)
lib.printNPMDijitPrima(npm)
print()
from kelas3lib import kelas3lib

npm = "1174006"

k3lib = kelas3lib(npm)

k3lib.printNPM()
k3lib.printNPMDuaDijit()
k3lib.printNPMTigaDijit()
k3lib.printNPMDigitKetiga()
k3lib.printNPMSatuPersatu()
k3lib.printNPMPenjumlahan()
k3lib.printNPMPerkalian()
k3lib.printNPMDijitGenap()
k3lib.printNPMDijitGanjil()
k3lib.printNPMDijitPrima() 