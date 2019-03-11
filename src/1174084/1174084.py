# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:45:34 2019

@author: Reza
"""

a ='1174084' #variabel/angka yang akan di konversi.
integer = int(a) #konversi string ke integer

a = 1174084 #variabel/angka yang akan di konversi.
string = str(a) #konversi integer ke string

#while loop
i = 1
while i < 6:
  print(i)
  i += 1
#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
#if 
a = 33
b = 200
if b > a:
  print("b lebih besar dari a")
#elif
a = 33
b = 33
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a dan b sama")

#if bersarang
gaji = 10000000
berkeluarga = True

if gaji > 3000000:
    print("Gaji sudah diatas UMR")
    if berkeluarga:
        print("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print("Tidak perlu ikutan asuransi")
else:
    print("Gaji belum UMR")
    
#try except
try:
  print(x)
except:
  print("An exception occurred")
  
  
#no. 1
print (1174084%3)

print("***  ***  *********** ***   ***  *********  *********  ***   ***")
print("***  ***  **********  ***   ***  *********  *********  ***   ***")
print("***  ***        ***   ***   ***  ***   ***  ***   ***  ***   ***")
print("***  ***       ***    ***   ***  ***   ***  ***   ***  ***   ***")
print("***  ***      ***     *********  ***   ***  *********  *********")
print("***  ***     ***            ***  ***   ***  ***   ***        ***")
print("***  ***    ***             ***  ***   ***  ***   ***        ***")
print("***  ***   ***              ***  *********  *********        ***")
print("***  ***  ***               ***  *********  *********        ***")

#no. 2
npm  = input("Masukan NPM :")
nilai = int(npm[5:7])
hitung = 0
while(hitung < nilai):
    print("Halo, " + str(npm) + " Apa Kabar?")
    hitung = hitung +1

#no. 3 
npm = input("Masukan NPM :")
nilai = int(npm[4:5]) + int(npm[5:6]) + int(npm[6:7])
hitung = 0
while(hitung < nilai):
    print("Halo, " + str(npm[4:7]) + " Apa Kabar?")
    hitung = hitung +1

#no. 4
npm = input("Masukan NPM :")
print("Halo, " + str(npm[-3]) + " Apa Kabar?")

#no. 5
a = 1
b = 1
c = 7
d = 4
e = 0
f = 8
g = 4
npm = [a,b,c,d,e,f,g]

for a in npm:
    print(a, end ="")

#no. 6
print(a+b+c+d+e+f+g)

#no. 7
print(a*b*c*d*e*f*g)

#no. 8
for a in npm:
    print(a)

#no. 9
for n in npm:
    if(n % 2 == 0):
        if(n != 0):
            print(n, end ="")

#no. 10
for n in npm:
    if(n % 2 != 0):
        print(n, end ="")

#no. 11
print(c)

#chapter 3
#teori no.1

def hello():
    print ("Hello world")

hello()

#teori no.2
#luas.py
def persegi(p,l):
    luas = p * l #p = panjang, l = lebar
    return luas

def lingkaran(r): 
    luas = 3.14 * (r**2) #r = jari-jari
    return luas

def segitiga(a,t):
    luas = (a * t)/2 #a = alas, t = tinggi
    return luas

#kemampuan
#no. 1
def NPM(npm):
    npm = list(str(npm))
        
    angka1 = {"0":" ****** ", "1":"  **", "2":" ******* ", "3":" ******* ", "4":"     ***", "5":"********", "6":" ******* ", "7":"*********", "8":" ******* ", "9":" *******"}
    angka2 = {"0":"***  ***", "1":"****", "2":"**    ***", "3":"**    ***", "4":"   *****", "5":"**      ", "6":"***      ", "7":"     *** ", "8":"***   ***", "9":"**    ***"}
    angka3 = {"0":"***  ***", "1":" ***", "2":"     *** ", "3":"    **** ", "4":" ***  **", "5":"******* ", "6":"******** ", "7":"    ***  ", "8":" *** *** ", "9":"**    ***"}
    angka4 = {"0":"***  ***", "1":" ***", "2":"    ***  ", "3":"    **** ", "4":"********", "5":"     ***", "6":"***   ***", "7":"   ***   ", "8":" *** *** ", "9":" ********"}
    angka5 = {"0":"***  ***", "1":" ***", "2":"  ****   ", "3":"**    ***", "4":"     ***", "5":"**   ***", "6":"***   ***", "7":"  ***    ", "8":"***   ***", "9":"      ***"}
    angka6 = {"0":" ****** ", "1":" ***", "2":"*********", "3":" ******* ", "4":"     ***", "5":" ****** ", "6":" ******* ", "7":" ***     ", "8":" ******* ", "9":" ******* "}
                  
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
    
NPM(input("Masukan NPM anda: "))

#no. 2
def NPMDuaDijit(npm):
    ulang = 1
    sampai = int(npm[5:7])
    while(ulang <= sampai):
        print("Halo, "+str(npm)+" apa kabar?")
        ulang += 1 

NPMDuaDijit(input("Masukan NPM anda: "))

#no. 3
def NPMTigaDijit(npm):
    ulang = 1
    sampai = list(map(int, npm[4:7]))
    sampai = sum(sampai)    
    while(ulang <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?")
        ulang += 1

NPMTigaDijit(input("Masukan NPM anda: "))
        
#no. 4
def NPMDigitKetiga(npm):
    print("Output:")
    print("Halo, "+str(npm[-3])+" apa kabar?")

NPMDigitKetiga(input("Masukan NPM anda: "))

#no. 5
#Jawaban No. 5
def NPMSatuPersatu(npm):
    npm = list(map(int, npm))  
    for n in npm:
        print(n)

NPMSatuPersatu(input("Masukan NPM anda: "))
    
#Jawaban No. 6
def penjumlahanNPM(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil += x   
    print(hasil)
        
penjumlahanNPM(input("Masukan NPM anda: "))   
    
#Jawaban No. 7
def perkalianNPM(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil *= x
    print(hasil)
    
perkalianNPM(input("Masukan NPM anda: "))
    
#Jawaban No. 8
def genap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end = "")
genap(input("Masukan NPM anda: "))
    
#Jawaban No. 9
def ganjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 != 0):
            print(n, end = "")
ganjil(input("Masukan NPM anda :"))
    
#Jawaban No. 10
def prima(npm):
    npm = list(map(int, npm))
    prima = []
    for n in npm:
        isPrime = True
        if n == 0 or n == 1:
            isPrime = False
        for x in range(2, n):
            if n % x == 0:
                isPrime = False
        if isPrime:
            prima.append(n)
    
    for p in prima:
        print(p, end = "")
prima(input("Masukan NPM anda: "))

#Ketrampilan Penanganan Error
#Jawaban No. 1
def siapa(nama):
    try:
        print("Hallo, "+str(nama))
    except:
        print("Terjadi error") 

siapa(input("Masukan nama anda: "))