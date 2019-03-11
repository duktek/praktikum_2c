# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:06:03 2019

@author: Reza
"""

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
    


#no. 2
def NPMDuaDijit(npm):
    ulang = 1
    sampai = int(npm[5:7])
    while(ulang <= sampai):
        print("Halo, "+str(npm)+" apa kabar?")
        ulang += 1 



#no. 3
def NPMTigaDijit(npm):
    ulang = 1
    sampai = list(map(int, npm[4:7]))
    sampai = sum(sampai)    
    while(ulang <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?")
        ulang += 1


        
#no. 4
def NPMDigitKetiga(npm):
    print("Output:")
    print("Halo, "+str(npm[-3])+" apa kabar?")



#no. 5
#Jawaban No. 5
def NPMSatuPersatu(npm):
    npm = list(map(int, npm))  
    for n in npm:
        print(n)


    
#Jawaban No. 6
def penjumlahanNPM(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil += x   
    print(hasil)
        
   
    
#Jawaban No. 7
def perkalianNPM(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil *= x
    print(hasil)
    

    
#Jawaban No. 8
def genap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end = "")

    
#Jawaban No. 9
def ganjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 != 0):
            print(n, end = "")

    
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
