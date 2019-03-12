# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:47:37 2019

@author: PandA23
"""

#Chapter 3
#Teori
#No 1
def cek(a,b):
    c = a + b
    return c

a = 1
b = 2
hasil = cek(a,b)
print(hasil)

#Praktek
#No 1
def cetaknpm(npm):

    npm = list(str(npm))

    angka1 = {"0":" ###### ", "1":"  ##", "2":"########", "3":"########", "4":"     ###", "5":"########", "6":"#########", "7":"#########", "8":"#########", "9":"#########"}
    angka2 = {"0":"###  ###", "1":"####", "2":"     ###", "3":"     ###", "4":"   #####", "5":"##      ", "6":"###      ", "7":"     ### ", "8":"###   ###", "9":"##    ###"}
    angka3 = {"0":"###  ###", "1":" ###", "2":"     ###", "3":" #######", "4":" ###  ##", "5":"########", "6":"#########", "7":"    ###  ", "8":"#########", "9":"##    ###"}
    angka4 = {"0":"###  ###", "1":" ###", "2":"    ### ", "3":" #######", "4":"########", "5":"########", "6":"###   ###", "7":"   ###   ", "8":"#########", "9":"#########"}
    angka5 = {"0":"###  ###", "1":" ###", "2":"  ####  ", "3":"     ###", "4":"     ###", "5":"     ###", "6":"###   ###", "7":"  ###    ", "8":"###   ###", "9":"      ###"}
    angka6 = {"0":" ###### ", "1":" ###", "2":"########", "3":"########", "4":"     ###", "5":"########", "6":"#########", "7":" ###     ", "8":"#########", "9":"#########"}

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

cetaknpm(input("Masukan NPM anda: "))

#No 2
def cetaknpm2dijit(npm):
    i = 1
    while(i <= 87):
        print("Hallo, "+npm[4:8]+" apa kabar?")
        i += 1
print("Masukan Npm: ")
npm = input()
print(cetaknpm2dijit(npm))

#No 3
def cetaknpm2dijit(npm):
    i = 1
    sampai = list(map(int, npm[4:8]))
    sampai = sum(sampai)    
    while(i <= sampai):
        print("Halo, "+str(npm)+" apa kabar?")
        i += 1
print("Masukan Npm: ")
npm = input()
print(cetaknpm2dijit(npm))

#No 4
def cetaknpmdijitke3(npm):
    print("Halo, "+str(npm[-3])+" apa kabar?")
print("Masukan Npm: ")
npm = input()
print(cetaknpmdijitke3(npm))

#No 5
def cetaknpmsatupersatu(npm):
    npm = list(map(int, npm))  
    for n in npm:
        print(n)
print("Masukan Npm: ")
npm = input()
print(cetaknpmsatupersatu(npm))

#No 6
def cetakpenjumlahannpm(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil += x

    print(hasil)
print("Masukan Npm: ")
npm = input()
print(cetakpenjumlahannpm(npm)) 

#No 7
def cetakperkaliannpm(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil *= x

    print(hasil)
print("Masukan Npm: ")
npm = input()
print(cetakperkaliannpm(npm)) 

#No 8
def cetaknpmgenap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end = "")
print("Masukan Npm: ")
npm = input()
print(cetaknpmgenap(npm)) 

#No 9
def cetaknpmganjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 != 0):
            print(n, end = "")
print("Masukan Npm: ")
npm = input()
print(cetaknpmganjil(npm)) 

#No 10
def cetaknpmprima(npm):
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
print("Masukan Npm: ")
npm = input()
print(cetaknpmprima(npm))          

#KeterampilanPenangananError
def menyapa(nama):
    try:
        print("Hallo, "+str(nama))
    except:
        print("Terjadi error") 

menyapa(input("Masukan nama anda: "))      
                