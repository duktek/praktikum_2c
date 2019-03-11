# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:20:04 2019

@author: D. Irga B. Naufal Fakhri
"""
class kelas3lib:
    def __init__(self, npm):
        self.npm = npm
        
    #Jawaban nomor 1
    def npmprint(self):
        text = str(self.npm)
        from PIL import Image, ImageDraw, ImageFont
        import numpy as np
        myfont = ImageFont.truetype("verdanab.ttf", 12)
        size = myfont.getsize(text)
        img = Image.new("1",size,"black")
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), text, "white", font=myfont)
        pixels = np.array(img, dtype=np.uint8)
        if int(text) % 3 == 0:    
            chars = np.array([' ','*'], dtype="U1")[pixels]
        elif int(text) % 3 == 1:
            chars = np.array([' ','#'], dtype="U1")[pixels]
        elif int(text) % 3 == 2:
            chars = np.array([' ','+'], dtype="U1")[pixels]        
        strings = chars.view('U' + str(chars.shape[1])).flatten()
        print( "\n".join(strings))
    
    
    #Jawaban nomor 2
    def loop(self):
        i = 1
        while(i <= int(self.npm[5:])):
            print("Hallo, "+str(self.npm)+" apa kabar?")
            i += 1
    
    
    #Jawaban nomor 3
    def looptambah(self):
        i = 1
        akhir = int(self.npm[4:5]) + int(self.npm[5:6]) + int(self.npm[6:7])
        while(i <= akhir):
            print("Hallo, "+str(self.npm[4:7])+" apa kabar?")
            i += 1
    
    
    #Jawaban nomor 4
    def hallo(self):
        print("Halo, "+str(self.npm[-3])+" apa kabar?")
    
    
    #Jawaban nomor 5
    def array(self):
        for x in self.npm:
            print (x)
    
    
    #Jawaban nomor 6
    def jumlah(self):
        self.npm = list(map(int, self.npm))
        hasil = 0
        for x in self.npm:
            hasil += x
        print("Hasil perjumlahan dari npm anda adalah: " + str(hasil))
    
    
    #Jawaban nomor 7
    def kali(self):
        self.npm = list(map(int, self.npm))
        hasil = 0
        for x in self.npm:
            hasil *= x
        print("Hasil perkalian dari npm anda adalah: " + str(hasil))
    
    
    #Jawaban nomor 8
    def printgenap(self):
        self.npm = list(map(int, self.npm))
        for x in self.npm:
            if(x % 2 == 0):
                if(x != 0):
                    print(x, end = "")
    
    
    #Jawaban nomor 9
    def printganjil(self):
        self.npm = list(map(int, self.npm))
        for x in self.npm:
            if(x % 2 != 0):
                print(x, end = "")
    
    
    #Jawaban nomor 10
    def printprima(self):
        self.npm = list(map(int, self.npm))
        prima = []
        for n in self.npm:
            bilPrima = True
            if n == 0 or n == 1:
                bilPrima = False
            for x in range(2, n):
                if n % x == 0:
                    bilPrima = False
            if bilPrima:
                prima.append(n)
    
        for p in prima:
            print(p, end = "")
