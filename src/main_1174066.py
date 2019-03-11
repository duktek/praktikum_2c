# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:28:38 2019

@author: D. Irga B. Naufal Fakhri
"""

#Pemanggilan library 3lib
from lib_1174066 import *

npm(1174066)
loop(input("Masukan NPM : "))
looptambah(input("Input: "))
hallo(input("Input: "))
array(input("NPM: "))
jumlah(input("NPM: "))
kali(input("NPM: "))
printgenap(input("NPM: "))
printganjil(input("NPM: "))
printprima(input("NPM: "))


#Pemanggilan kelas 3lib
from kelas3lib_1174066 import kelas3lib
npm = "1174066"
kelas = kelas3lib(npm)

kelas.npmprint()
kelas.loop()
kelas.looptambah()
kelas.hallo()
kelas.array()
kelas.jumlah()
kelas.kali()
kelas.printgenap()
kelas.printganjil()
kelas.printprima()