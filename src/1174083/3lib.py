# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:58:20 2019

@author: Bakti Qilan
"""
#No. 1
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
    
#No. 2
def NPMperulangan(npm):
    i = 1
    digit = int(npm[5:7])
    while(i <= digit):
        print("Halo, "+str(npm)+" apa kabar?")
        i += 1
   
#No. 3
def SumNPM_3digit(npm):
    ulang = 1
    sampai = list(map(int, npm[4:7]))
    sampai = sum(sampai)    
    while(ulang <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?")
        ulang += 1    
    
#No. 4
def NPMdigit3ter(npm):
    print("Output:")
    print("Halo, "+str(npm[-3])+" apa kabar?")       

#No. 5
def noNPMbarisSatu(npm):
    npm = list(map(int, npm))  
    for x in npm:
        print(x)

#No. 6
def PenjumlahanNPM(npm):
    npm = list(map(int, npm))
    semua = 0
    for a in npm:
        semua += a
    
    print(semua)        
    
#No. 7
def PerkalianNPM(npm):
    npm = list(map(int, npm))
    semua = 0
    for a in npm:
        semua *= a
    
    print(semua)        
    
#No. 8
def NPMgenapOnly(npm):
    npm = list(map(int, npm))
    for x in npm:
        if(x % 2 == 0):
            if(x != 0):
                print(x, end = "")    
    
#No. 9
def NPMganjilOnly(npm):
    npm = list(map(int, npm))
    for x in npm:
        if(x % 2 != 0):
            print(x, end = "")        
    
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
