# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:05:12 2019

@author: ACER
"""
class kelas3lib:
    def __init__(self, npm):
        self.npm = npm
#Soal No.1
    def AnswerNo1(self):
    
        npm = list(str(self.npm))
    
        number1 = {"0":" ++++++ ", "1":"  ++", "2":" +++++++  ", "3":"  +++++++  ", "4":"   +++++", "5":"+++++++", "6":" +++++++", "7":"++++++++", "8":" +++++ ", "9":" ++++++  "}
        number2 = {"0":"+++  +++", "1":"+++", "2":"++    +++ ", "3":"+++     +++", "4":"  ++  ++", "5":"++     ", "6":"+++     ", "7":"++++++++", "8":"++   ++", "9":"++    ++ "}
        number3 = {"0":"+++  +++", "1":" +++", "2":"     +++  ", "3":"      ++++ ", "4":" ++   ++", "5":"++     ", "6":"+++     ", "7":"   +++ ", "8":" +++++ ", "9":"++    ++ "}
        number4 = {"0":"+++  +++", "1":" +++", "2":"    +++   ", "3":"      ++++ ", "4":"++++++++", "5":"++++++ ", "6":"++++++++", "7":"  +++  ", "8":"+++++++", "9":"++++++++ "}
        number5 = {"0":"+++  +++", "1":" +++", "2":"  ++++    ", "3":"+++     +++", "4":"      ++", "5":"     ++", "6":"+++  +++", "7":" +++   ", "8":"++   ++", "9":"      ++ "}
        number6 = {"0":" ++++++ ", "1":" +++", "2":"+++++++++ ", "3":"  +++++++  ", "4":"      ++", "5":"++++++ ", "6":" ++++++ ", "7":"+++    ", "8":" +++++ ", "9":"+++++++  "}
              
        Result1 = []
        Result2 = []
        Result3 = []
        Result4 = []
        Result5 = []
        Result6 = []
    
        for x in npm:
            Result1.append(number1[x])
            Result2.append(number2[x])
            Result3.append(number3[x])
            Result4.append(number4[x])
            Result5.append(number5[x])
            Result6.append(number6[x])
        
        print(*Result1, sep=' ')
        print(*Result2, sep=' ')
        print(*Result3, sep=' ')
        print(*Result4, sep=' ')
        print(*Result5, sep=' ')
        print(*Result6, sep=' ')
    
    
    #Soal no.2
    def AnswerNo2(self):
        hitung = 0
        while(hitung <79):
            print("Halo, " + str(self.npm) + " Apa Kabar?")
            hitung = hitung +1
    
    
    #Soal no.3
    def AnswerNo3(self):
        hitung = 0
        npm = str(self.npm)
        x = npm[4:7]
        while(hitung < 16):
            print("Halo, " + x + " Apa Kabar?")
            hitung = hitung +1
    
    
    #Soal no.4
    def AnswerNo4(self):
        npm = str(self.npm)
        x = npm[-3]
        print("Halo, " + x + " Apa Kabar?")
    
    
    #Soal no5
    def AnswerNo5(self):
        for i in self.npm:
            print (i)
        
    
    #Soal no.6
    def AnswerNo6(self):
        jumlahkan = 0
        for i in self.npm:
            jumlahkan += int(i)
        print ("Hasil Penjumlahan NPM adalah : " +str(jumlahkan))
    
    
    #Soal No.7
    def AnswerNo7(self):
        kalikan = 0
        for i in self.npm:
            kalikan *= int(i)
        print ("Hasil Perkalian NPM adalah : " +str(kalikan))
    
    
    #Soal No.8
    def AnswerNo8(self):
        npm = list(map(int, self.npm))
        for n in npm:
            if(n % 2 == 0):
                if(n != 0):
                    print(n, end ="")
    
    
    #Soal No.9
    def AnswerNo9(self):
        npm = list(map(int, self.npm))
        for n in npm:
            if(n % 2 !=0):
                print(n, end ="")
    
    
    #Soal No.10
    def AnswerNo10(self):
        npm = list(map(int, self.npm))
        prima = []
        for n in npm:
            bilPrima = True
            if n == 0 or n ==1:
                bilPrima = False
            for x in range(2, n):
                if n % x == 0:
                    bilPrima = False
            if bilPrima:
                prima.append(n)
                    
            for p in prima:
                print(p, end = "")
    
