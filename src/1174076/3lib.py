# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 00:17:56 2019

@author: Difaal21
"""

# Nomor 1 Praktek
print("Nomor 1 Praktek")

def NPM(npm):
    npm = list(str(npm))
    
    angka1 = {"0":" ###### ", "1":"  ##", "2":" ####### ", "3":" ####### ", "4":"     ###", "5":"########", "6":" ####### ", "7":"#########", "8":" ####### ", "9":" #######"}
    angka2 = {"0":"###  ###", "1":"####", "2":"##    ###", "3":"##    ###", "4":"   #####", "5":"##      ", "6":"###      ", "7":"     ### ", "8":"###   ###", "9":"##    ###"}
    angka3 = {"0":"###  ###", "1":" ###", "2":"     ### ", "3":"    #### ", "4":" ###  ##", "5":"####### ", "6":"######## ", "7":"    ###  ", "8":" ### ### ", "9":"##    ###"}
    angka4 = {"0":"###  ###", "1":" ###", "2":"    ###  ", "3":"    #### ", "4":"########", "5":"     ###", "6":"###   ###", "7":"   ###   ", "8":" ### ### ", "9":" ########"}
    angka5 = {"0":"###  ###", "1":" ###", "2":"  ####   ", "3":"##    ###", "4":"     ###", "5":"##   ###", "6":"###   ###", "7":"  ###    ", "8":"###   ###", "9":"      ###"}
    angka6 = {"0":" ###### ", "1":" ###", "2":"#########", "3":" ####### ", "4":"     ###", "5":" ###### ", "6":" ####### ", "7":" ###     ", "8":" ####### ", "9":" ####### "}

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

# Nomor 2 Praktek
print("Nomor 2 Praktek")

def NPM(npm):
    i = 1
    x = int(npm[5:7])
    while(i <= x):
        print("Halo, "+str(npm)+" apa kabar?")
        i += 1

NPM(input("Masukan NPM anda: "))

# Nomor 3 Praktek
print("Nomor 3 Praktek")

def NPM(npm):
    i = 1
    x = list(map(int, npm[4:7]))
    x = sum(x)    
    while(i <= x):
        print("Halo, "+str(npm[-3:])+" apa kabar?")
        i += 1

NPM(input("Masukan NPM anda: "))

# Nomor 4 Praktek
print("Nomor 4 Praktek")

def NPM(npm):
    print("Halo, "+str(npm[-3])+" apa kabar?")

NPM(input("Input: "))

# Nomor 5 Praktek
print("Nomor 5 Praktek")

def NPM(npm):
    npm = list(map(int, npm))  
    for n in npm:
        print(n)

NPM(input("Masukan NPM anda: "))

# Nomor 6 Praktek
print("Nomor 6 Praktek")

def NPM(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil += x

    print(hasil)

NPM(input("Masukan NPM anda: "))

# Nomor 7 Praktek
print("Nomor 7 Praktek")

def NPM(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil *= x

    print(hasil)

NPM(input("Masukan NPM anda: "))

# Nomor 8 Praktek
print("Nomor 8 Praktek")

def NPM(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end = "")

NPM(input("Masukan NPM anda: "))
print ("")

#Nomor 9 Praktek
print("Nomor 9 Praktek")

def NPM(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 != 0):
            print(n, end = "")

NPM(input("Masukan NPM anda : "))
print ("")

# Nomor 10 Praktek
print("Nomor 10 Praktek")

def NPM(npm):
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

NPM(input("Masukan NPM anda: "))