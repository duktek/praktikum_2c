# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print (1174083%3)

#No.1
print("  **   ** ********    *****  ******   ******  ********")
print("**** **** ********   ****** ***  *** ******** ********")
print(" ***  ***      ***  **   ** ***  *** ***  ***      ***")
print(" ***  ***     ***  ***   ** ***  *** ******** ********")
print(" ***  ***    ***   ******** ***  *** ******** ********")
print(" ***  ***   ***    ******** ***  *** ***  ***      ***")
print(" ***  ***  ***          *** ***  *** ******** ********")
print(" ***  *** ***           ***  ******   ******  ********")

#No. 2
npm = input("Masukkan NPM : ")
ulang = 1
while(ulang <= 83):
    print("Halo, "+str(npm)+" apa kabar?")
    ulang += 1

#No. 3
npm = input("Masukkan NPM : ")
ulang = 1
while(ulang <= 83):
    print("Halo, "+str(npm[4:7])+" apa kabar?")
    ulang += 1
    
#No. 4
npm = input("Masukkan NPM : ")
print("Halo, "+str(npm[-3])+" apa kabar?")

#No. 5
a = 1
b = 1
c = 7
d = 4
e = 0
f = 8
g = 3

npm = [a,b,c,d,e,f,g]

for n in npm:
    print(n, end ="")

print()

#No. 6
print(a+b+c+d+e+f+g)

#No. 7
print(a*b*c*d*e*f*g)

#No. 8
for n in npm:
    print(n)
         
#No. 9    
for n in npm:
    if(n % 2 == 0):
        if(n != 0):
           print(n, end ="")

print()        

#No. 10        
for n in npm:
    if(n % 2 != 0):
        print(n, end ="")

print()


#No. 11

for n in npm:
    if(n % 2 != 0):
        print(n, end ="")

print()

"""
Tugas Chapter 3 Teori

"""

def HasilBagi(a,b):
    h = a / b
    return h

a = 50
b = 2
c = int(HasilBagi(a,b))
#menggunakan int() karena jika tidak, maka hasilnya akan menjadi format float.

def penambahan(c,d):
    r = c + d
    return r
def pengurangan(c,d):
    r = c - d
    return r
def perkalian(c,d):
    r = c * d
    return r
def pembagian(c,d):
    r = c / d
    return r

#

class berhitung:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def Penambahan(self):
        z = self.x + self.y 
        return z
    def Pengurangan(self):
        z = self.x - self.y 
        return z
    def Perkalian(self):
        z = self.x + self.y 
        return z
    def Pembagian(self):
        z = self.x + self.y 
        return z
#
        
import test_1174083 as test

m = 10
n = 5

coba = test.test_1174083(m,n)

hasil_1 = coba.Penambahan()
hasil_2 = coba.Pengurangan()
hasil_3 = coba.Perkalian()
hasil_4 = coba.Pembagian()
    
#

"""
from contoh_fungsi import
print(int(input("input NPM : ")))
"""    

import coba

p = 20
q = 10

hasilnya = coba.penambahan(p,q)
print(hasilnya)

############################################################################
"""
Chapter 3 Praktek
"""

#No. 1
print(1174083%3)
# hasil mod3 = 0
def printNPM(npm):
    
    npm = list(str(npm))
    
    angka1 = {"0":" ****** ", "1":"  **", "2":" *******  ", "3":"  *******  ", "4":"   *****", "5":"*******", "6":" *******", "7":"*******", "8":" ***** ", "9":" ******  "}
    angka2 = {"0":"***  ***", "1":"****", "2":"**    *** ", "3":"***     ***", "4":"  **  **", "5":"**     ", "6":"***     ", "7":"*******", "8":"**   **", "9":"**    ** "}
    angka3 = {"0":"***  ***", "1":" ***", "2":"     ***  ", "3":"      **** ", "4":" **   **", "5":"**     ", "6":"***     ", "7":"   *** ", "8":" ***** ", "9":"**    ** "}
    angka4 = {"0":"***  ***", "1":" ***", "2":"    ***   ", "3":"      **** ", "4":"********", "5":"****** ", "6":"********", "7":"  ***  ", "8":"*******", "9":"******** "}
    angka5 = {"0":"***  ***", "1":" ***", "2":"  ****    ", "3":"***     ***", "4":"      **", "5":"     **", "6":"***  ***", "7":" ***   ", "8":"**   **", "9":"      ** "}
    angka6 = {"0":" ****** ", "1":" ***", "2":"******** ", "3":"  ********  ", "4":"      **", "5":"****** ", "6":" ****** ", "7":"***    ", "8":" ***** ", "9":"*******  "}
              
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []
              
    for x in npm:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])
    
    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')
    
printNPM(input("Masukan NPM anda: "))

#No. 2
def NPMperulangan(npm):
    i = 1
    digit = int(npm[5:7])
    while(i <= digit):
        print("Halo, "+str(npm)+" apa kabar?")
        i += 1
    
NPMperulangan (input("Masukan NPM : "))

#No. 3
def SumNPM_3digit(npm):
    ulang = 1
    sampai = list(map(int, npm[4:7]))
    sampai = sum(sampai)    
    while(ulang <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?")
        ulang += 1
    
SumNPM_3digit(input("Masukan NPM: "))

#No. 4
def NPMdigitter3(npm):
    print("Output: Halo, "+str(npm[-3])+" apa kabar?")
    
NPMdigitter3(input("Masukan NPM: "))

#No. 5
def noNPMbarisSatu(npm):
    npm = list(map(int, npm))  
    for x in npm:
        print(x)
        
noNPMbarisSatu(input("Masukan NPM : "))

#No. 6
def PenjumlahanNPM(npm):
    npm = list(map(int, npm))
    semua = 0
    for a in npm:
        semua += a
    
    print(semua)
    
PenjumlahanNPM(input("Masukan NPM : "))

#No. 7
def PerkalianNPM(npm):
    npm = list(map(int, npm))
    semua = 0
    for a in npm:
        semua *= a
    
    print(semua)
    
PerkalianNPM(input("Masukan NPM : "))

#No. 8
def NPMgenapOnly(npm):
    npm = list(map(int, npm))
    for x in npm:
        if(x % 2 == 0):
            if(x != 0):
                print(x, end = "")
    
NPMgenapOnly(input("Masukan NPM : "))

#No. 9 
def NPMganjilOnly(npm):
    npm = list(map(int, npm))
    for x in npm:
        if(x % 2 != 0):
            print(x, end = "")
    
NPMganjilOnly(input("Masukan NPM : "))

#No. 10
def NPMprimaOnly(npm):
    npm = list(map(int, npm))
    prima = []
    for a in npm:
        bilPrima = True
        if a == 0 or a == 1:
            bilPrima = False
        for b in range(2, a):
            if a % b == 0:
                bilPrima = False
        if bilPrima:
            prima.append(a)

    for c in prima:
        print(c, end = "")
    
NPMprimaOnly(input("Masukan NPM : "))

#No. 11

#No. 12


#Ketrampilan Penanganan Error
#No. 1
def coba(inputan):
    try:
        print("Hallo, "+str(inputan))
    except:
        print("Terjadi error") 

coba(input("Inputan : "))