# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:04:39 2019

@author: FannyCantik
"""
class latihan:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def penambahan(self):
        r = self.a + self.b
        return r


#NO1
def penulisan(npm):
    npm = list(str(npm))
    
    angka1 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ####","4":" ###   ### ","5":" ###### ","6":" ########## ","7":" ########### ","8":" ###### ","9":" ######### "}
    angka2 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ####","4":" ###   ### ","5":" ###### ","6":" ########## ","7":" ########### ","8":" ###### ","9":" ######### "}
    angka3 = {"0":" ##     ## ","1":" ### ","2":"    ### ","3":" ####","4":" ###   ### ","5":" ###### ","6":" ##         ","7":"        ###  ","8":" ###### ","9":" ##     ## "}
    angka4 = {"0":" ##     ## ","1":" ### ","2":"    ### ","3":" ####","4":" ###   ### ","5":" ###### ","6":" ##         ","7":"       ###   ","8":" ###### ","9":" ##     ## "}
    angka5 = {"0":" ##     ## ","1":" ### ","2":" ###### ","3":" ####","4":" ######### ","5":" ###### ","6":" ##         ","7":"      ###    ","8":" ###### ","9":" ##     ## "}
    angka6 = {"0":" ##     ## ","1":" ### ","2":" ###### ","3":" ####","4":"       ### ","5":" ###### ","6":" #########  ","7":"     ###     ","8":" ###### ","9":" ######### "}
    angka7 = {"0":" ##     ## ","1":" ### ","2":" ###    ","3":" ####","4":"       ### ","5":" ###### ","6":" ##     ##  ","7":"    ###      ","8":" ###### ","9":"       ### "}
    angka8 = {"0":" ##     ## ","1":" ### ","2":" ###    ","3":" ####","4":"       ### ","5":" ###### ","6":" ##     ##  ","7":"   ###       ","8":" ###### ","9":"       ### "}
    angka9 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ####","4":"       ### ","5":" ###### ","6":" ##     ##  ","7":"  ###        ","8":" ###### ","9":"       ### "}
    angka10 = {"0":"######### ","1":" ### ","2":" ###### ","3":" ####","4":"       ### ","5":" ###### ","6":" #########  ","7":" ###         ","8":" ###### ","9":" ######### "}
              
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
    
penulisan(int(input("Masukan NPM nyaa :")))

#NO2
def perulangan(npm):
    hitung = 0
    while(hitung < 69):
        print("Halo, "+str(npm)+" anyeong?")
        hitung = hitung +1

perulangan(int(input("Masukan NPM nyaa : ")))

#N03
def perulangan(npm):
    hitung = 0
    npm = str(npm)
    bil = npm[4:7]
    
    while(hitung < 9):
        print("Halo, "+bil+" wattsup?")
        hitung = hitung +1

perulangan(int(input("Masukan NPM nyaa : ")))

#NO4
def perulangan2(npm):
    npm = str(npm)
    bil = npm[-3]  
    print("Halo, "+bil+" wattsup?")

perulangan2(int(input("Masukan NPM nyaa : ")))

#NO5
def down(npm):
    for i in npm:
        print (i)

down(input("Masukan NPM nyaa : "))

#NO6
def penjumlahan(npm):
    jumlah = 0
    for i in npm:
        jumlah += int(i)
    print(str(jumlah)+" hasil penjumlahannya adalah ")

penjumlahan(input("Masukan NPM nyaa : "))

#NO7
def perkalian(npm):
    jumlah = 0
    for i in npm:
        jumlah *= int(i)
    print(str(jumlah)+" hasil perkaliannya adalah ")

perkalian(input("Masukan NPM nyaa : "))

#NO8
def genap():
    npm = [1,1,7,4,0,6,9]
    for i in npm:
        if (i % 2) == 0:
            print("Bilangan Genapnya : "+str(i))
genap()

#NO9
def ganjil():
    npm = [1,1,7,4,0,6,9]
    for i in npm:
        if (i%2)==1:
            print("Bilangan Ganjilnya : "+str(i))
ganjil()

#NO10
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
                print("Bilangan Primanya :"+str(num))
    else:
        print("Tidak Ada Bilangan Prima")
prima(int(input("Masukan NPM nyaa : ")))