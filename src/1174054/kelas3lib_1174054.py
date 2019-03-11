# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:13:14 2019

@author: ASUS X441U
"""

class tugas:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def penambahan(self):
        r = self.a + self.b
        return r

#No 1
def penulisan(npm):
    npm = list(str(npm))
    
    angka1 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ####","4":" ###   ### ","5":" ###### ","6":" ###### ","7":" ########### ","8":" ###### ","9":" ###### "}
    angka2 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ####","4":" ###   ### ","5":" ###### ","6":" ###### ","7":" ########### ","8":" ###### ","9":" ###### "}
    angka3 = {"0":" ##     ## ","1":" ### ","2":"    ### ","3":" ####","4":" ###   ### ","5":" ###    ","6":" ###### ","7":"        ###  ","8":" ###### ","9":" ###### "}
    angka4 = {"0":" ##     ## ","1":" ### ","2":"    ### ","3":" ####","4":" ###   ### ","5":" ###    ","6":" ###### ","7":"       ###   ","8":" ###### ","9":" ###### "}
    angka5 = {"0":" ##     ## ","1":" ### ","2":" ###### ","3":" ####","4":" ######### ","5":" ###### ","6":" ###### ","7":"      ###    ","8":" ###### ","9":" ###### "}
    angka6 = {"0":" ##     ## ","1":" ### ","2":" ###### ","3":" ####","4":"       ### ","5":" ###### ","6":" ###### ","7":"     ###     ","8":" ###### ","9":" ###### "}
    angka7 = {"0":" ##     ## ","1":" ### ","2":" ###    ","3":" ####","4":"       ### ","5":"    ### ","6":" ###### ","7":"    ###      ","8":" ###### ","9":" ###### "}
    angka8 = {"0":" ##     ## ","1":" ### ","2":" ###    ","3":" ####","4":"       ### ","5":"    ### ","6":" ###### ","7":"   ###       ","8":" ###### ","9":" ###### "}
    angka9 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ####","4":"       ### ","5":" ###### ","6":" ###### ","7":"  ###        ","8":" ###### ","9":" ###### "}
    angka10 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ####","4":"       ### ","5":" ###### ","6":" ###### ","7":" ###         ","8":" ###### ","9":" ###### "}
              
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []
    hasil7 = []
    hasil8 = []
    hasil9 = []
    hasil10 = []
    
    for x in npm:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])
        hasil7.append(angka7[x])
        hasil8.append(angka8[x])
        hasil9.append(angka9[x])
        hasil10.append(angka10[x])
    
    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')
    print(*hasil7, sep=' ')
    print(*hasil8, sep=' ')
    print(*hasil9, sep=' ')
    print(*hasil10, sep=' ')
    
penulisan(int(input("Masukkan NPM Anda :")))

#No 2
def perulangan(npm):
    hitung = 0
    while(hitung < 54):
        print("Halo, "+str(npm)+" apa kabar?")
        hitung = hitung +1

perulangan(int(input("Masukan NPM Anda : ")))

#No 3
def perulangan_3_digit(npm):
    hitung = 0
    npm = str(npm)
    bil = npm[4:7]
    
    while(hitung < 9):
        print("Halo, "+bil+" apa kabar?")
        hitung = hitung +1

perulangan_3_digit(int(input("Masukan NPM Anda : ")))

#No 4
def perulangan_3_digit_terakhir(npm):
    npm = str(npm)
    bil = npm[-3]  
    print("Halo, "+bil+" apa kabar?")

perulangan_3_digit_terakhir(int(input("Masukan NPM Anda : ")))

#No 5
def down(npm):
    for i in npm:
        print (i)

down(input("Masukan NPM Anda : "))

#No 6
def penjumlahan(npm):
    jumlah = 0
    for i in npm:
        jumlah += int(i)
    print(str(jumlah)+" merupakan hasil dari penjumlahan")

penjumlahan(input("Masukkan NPM Anda : "))

#No 7
def perkalian(npm):
    jumlah = 0
    for i in npm:
        jumlah *= int(i)
    print(str(jumlah)+" merupakan hasil dari perkalian")

perkalian(input("Masukan NPM Anda : "))

#No 8
def genap():
    npm = [1,1,7,4,0,2,7]
    for i in npm:
        if (i % 2) == 0:
            print("Bilangan Genapnya adalah : "+str(i))
genap()

#No 9 
def ganjil():
    npm = [1,1,7,4,0,2,7]
    for i in npm:
        if (i%2)==1:
            print("Bilangan Ganjilnya adalah : "+str(i))
ganjil()

#No 10
def prima(npm):
    npm = str(npm)
    bil = npm[2]
    num = int(bil)
    if num > 1:
        for i in range(2,num):
            if (num%i)==0:
                print("Bukan Bilangan Prima")
                break
            else:
                print("Bilangan Prima :"+str(num))
    else:
        print("Tidak Ada Bilangan Prima")
prima(int(input("Masukan NPM Anda : ")))