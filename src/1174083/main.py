# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:37:17 2019

@author: Bakti Qilan
"""

lib = __import__('3lib')

npm = str(input("Masukan NPM: "))

hasil1 = lib.printNPM(npm)
hasil2 = lib.NPMperulangan(npm)
hasil3 = lib.SumNPM_3digit(npm)
hasil4 = lib.NPMdigit3ter(npm)
hasil5 = lib.noNPMbarisSatu(npm)
hasil6 = lib.PenjumlahanNPM(npm)
hasil7 = lib.PerkalianNPM(npm)
hasil8 = lib.NPMgenapOnly(npm)
print()
hasil9 = lib.NPMganjilOnly(npm)
print()
hasil10 = lib.NPMprimaOnly(npm)
print()

from kelas3lib import kelas3lib

npm = str(input("Masukan NPM: "))

kel3lib = kelas3lib(npm)

kel3lib.printNPM()
kel3lib.NPMperulangan()
kel3lib.SumNPM_3digit()
kel3lib.NPMdigit3ter()
kel3lib.noNPMbarisSatu()
kel3lib.PenjumlahanNPM()
kel3lib.PerkalianNPM()
kel3lib.NPMgenapOnly()
print()
kel3lib.NPMganjilOnly()
print()
kel3lib.NPMprimaOnly()