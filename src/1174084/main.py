# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:04:32 2019

@author: Reza
"""

import kalkulator

a=100
b=50

hasil1=kalkulator.Penambahan(a,b)
hasil2=kalkulator.Pengurangan(a,b)
hasil3=kalkulator.Perkalian(a,b)
hasil4=kalkulator.Pembagian(a,b)

from ngitung import Ngitung

a=100
b=50

hitung = Ngitung(a, b)

hasil1 = hitung.Penambahan()
hasil2 = hitung.Pengurangan()
hasil3 = hitung.Perkalian()
hasil4 = hitung.Pembagian()

lib = __import__('3lib')

npm = "1174084"

lib.NPM(npm)
lib.NPMDuaDijit(npm)
lib.NPMTigaDijit(npm)
lib.NPMDigitKetiga(npm)
lib.NPMSatuPersatu(npm)
lib.penjumlahanNPM(npm)
lib.perkalianNPM(npm)
lib.genap(npm)
lib.ganjil(npm)
lib.prima(npm)
print()
from kelas3lib import kelas3lib

npm = "1174084"

k3lib = kelas3lib(npm)

k3lib.NPM()
k3lib.NPMDuaDijit()
k3lib.NPMTigaDijit()
k3lib.NPMDigitKetiga()
k3lib.NPMSatuPersatu()
k3lib.penjumlahanNPM()
k3lib.perkalianNPM()
k3lib.genap()
k3lib.ganjil()
k3lib.prima()