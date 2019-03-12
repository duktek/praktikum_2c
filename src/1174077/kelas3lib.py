# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:29:01 2019

@author: ASUS
"""

class kelas3lib:
    def __init__(self, npm):
        self.npm = npm
        
    #Ketrampilan Pemrograman
    #Jawaban No. 1
    def printNPM(self):
        
        npm = list(str(self.npm))
        
        angka1 = {"0":" ****** ", "1":"  **", "2":" ******* ", "3":" ******* ", "4":"     ***", "5":"********", "6":" ******* ", "7":"*********", "8":" ******* ", "9":" *******"}
        angka2 = {"0":"***  ***", "1":"****", "2":"**    ***", "3":"**    ***", "4":"   *****", "5":"**      ", "6":"***      ", "7":"     *** ", "8":"***   ***", "9":"**    ***"}
        angka3 = {"0":"***  ***", "1":" ***", "2":"     *** ", "3":"    *** ",  "4":" ***  **", "5":"******* ", "6":"******** ", "7":"    ***  ", "8":" *** *** ", "9":"**    ***"}
        angka4 = {"0":"***  ***", "1":" ***", "2":"    ***  ", "3":"    *** ",  "4":"********", "5":"     ***", "6":"***   ***", "7":"   ***   ", "8":" *** *** ", "9":" ********"}
        angka5 = {"0":"***  ***", "1":" ***", "2":"  ***   ",  "3":"**    ***", "4":"     ***", "5":"**   ***", "6":"***   ***", "7":"  ***    ", "8":"***   ***", "9":"      ***"}
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
    
    #Jawaban No. 2
    def printNPMDuaDijit(self):
        ulang = 1
        sampai = int(self.npm[5:7])
        while(ulang <= sampai):
            print("Halo, "+str(self.npm)+" apa kabar?")
            ulang += 1       
    
    #Jawaban No. 3
    def printNPMTigaDijit(self):
        ulang = 1
        sampai = list(map(int, self.npm[4:7]))
        sampai = sum(sampai)    
        while(ulang <= sampai):
            print("Halo, "+str(self.npm[-3:])+" apa kabar?")
            ulang += 1
    
    #Jawaban No. 4
    def printNPMDigitKetiga(self):
        print("Output:")
        print("Halo, "+str(self.npm[-3])+" apa kabar?")
    
    #Jawaban No. 5
    def printNPMSatuPersatu(self):
        npm = list(map(int, self.npm))  
        for n in npm:
            print(n)
    
    #Jawaban No. 6
    def printNPMPenjumlahan(self):
        npm = list(map(int, self.npm))
        hasil = 0
        for x in npm:
            hasil += x
        
        print(hasil)
        
    #Jawaban No. 7
    def printNPMPerkalian(self):
        npm = list(map(int, self.npm))
        hasil = 0
        for x in npm:
            hasil *= x
        
        print(hasil)
    
    #Jawaban No. 8
    def printNPMDijitGenap(self):
        npm = list(map(int, self.npm))
        for n in npm:
            if(n % 2 == 0):
                if(n != 0):
                    print(n, end = "")
        print()
    #Jawaban No. 9
    def printNPMDijitGanjil(self):
        npm = list(map(int, self.npm))
        for n in npm:
            if(n % 2 != 0):
                print(n, end = "")
        print()
    #Jawaban No. 10
    def printNPMDijitPrima(self):
        npm = list(map(int, self.npm))
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
            print()