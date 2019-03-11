# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:43:02 2019

@author: Chandra Kirana Poetra
"""
#Pemahaman Teori
#soal no 1

def masukannamafungsidisini(inputannyadisini):
    return inputannyadisini

outputnya = masukannamafungsidisini("Kembalian Fungsi")
print(outputnya)

#soal no 2
import math
print("Nilai I adalah : ", math.pi)

#soal no 3
class Mahasiswa:
    jumlahMahasiswa = 0
    
    def __init__(self, npm,nama):
        self.npm = npm
        self.nama = nama
    Mahasiswa.jumlahMahasiswa +=1
    
    def tampilprofile(self):
        print("npm : ", self.npm)
        print("NIK : ", self.nama)
        print()

mahasiswa1 = Mahasiswa("1174079","Chandra Kirana Poetra")
mahasiswa2 = Mahasiswa("1174069","Bakti qilan")

mahasiswa1.tampilprofile()
mahasiswa2.tampilprofile()

print("total mahasiswa adalah", Mahasiswa.jumlahMahasiswa)

#soal no 4

from file.Mahasiswa import Mahasiswa

mahasiswa1 = Mahasiswa("1174079","Chandra Kirana Poetra")
mahasiswa2 = Mahasiswa("1174069","Bakti qilan")
mahasiswa1.tampilprofile()
mahasiswa2.tampilprofile()
print("total mahasiswa adalah", Mahasiswa.jumlahMahasiswa)

#soal no 5
from file import Kalkulator

hasil = Kalkulator.penambahan(7,6)
print(hasil)

#soal no 6
from file import Kalkulator

a = 120
b = 60

hasil1 = Kalkulator.penambahan(a,b)
hasil2 = Kalkulator.pengurangan(a,b)
hasil3 = Kalkulator.perkalian(a,b)
hasil4 = Kalkulator.pembagian(a,b)

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)

#soal no 7

from file.Mahasiswa import Mahasiswa

mahasiswa1 = Mahasiswa("1174079","Chandra Kirana Poetra")
mahasiswa2 = Mahasiswa("1174069","Bakti qilan")
mahasiswa1.tampilprofile()
mahasiswa2.tampilprofile()
print("total mahasiswa adalah", Mahasiswa.jumlahMahasiswa)

print(117407%9)
#keterampilan Pemrograman/praktek
#soal No.1
def AnswerNo1():
    
    npm = input("Masukan NPM Anda:")
    npm = list(str(npm))

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

AnswerNo1()

#Soal no.2
def perulangan(npm):
    hitung = 0
    while(hitung <79):
        print("Halo, " + str(npm) + " Apa Kabar?")
        hitung = hitung +1
perulangan(int(input("Masukkan NPM: ")))

#Soal no.3
def perulangan3digitakhir(npm):
    hitung = 0
    npm = str(npm)
    x = npm[4:7]
    while(hitung < 16):
        print("Halo, " + x + " Apa Kabar?")
        hitung = hitung +1
perulangan3digitakhir(int(input("Masukkan NPM: ")))

#Soal no.4
def digit3daribelakang(npm):
    npm = str(npm)
    x = npm[-3]
    print("Halo, " + x + " Apa Kabar?")
digit3daribelakang(int(input("Masukkan NPM: ")))

#Soal no5
def npmkebawah(npm):
    for i in npm:
        print (i)
    
npmkebawah(input("Masukkan NPM: "))

#Soal no.6
def penjumlahannpm(npm):
    jumlahkan = 0
    for i in npm:
        jumlahkan += int(i)
    print ("Hasil Penjumlahan NPM adalah : " +str(jumlahkan))
penjumlahannpm(input("Masukkan NPM: "))

#Soal No.7
def perkaliannpm(npm):
    kalikan = 0
    for i in npm:
        kalikan *= int(i)
    print ("Hasil Perkalian NPM adalah : " +str(kalikan))
perkaliannpm(input("Masukkan NPM: "))

#Soal No.8
def printdigitgenap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end ="")
printdigitgenap(input("Masukkan NPM Anda bray: "))

#Soal No.9
def printdigitganjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 !=0):
            print(n, end ="")
printdigitganjil(input("Masukkan NPM Anda bray: "))

#Soal No.10
def printdigitprima(npm):
    npm = list(map(int, npm))
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
printdigitprima(input("Masukkan NPM: "))

#Soal No.11


def cobainaye(masukinnama):
    try:
        print("UY " + str(masukinnama))
    except:
        print("ada yang salah bray")
cobainaye(input("Nama Mu nak"))