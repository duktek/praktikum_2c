# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:35:12 2019

@author: User
"""
def uji():
    print("Tugas Web Service")

uji()

def uji_param(nama):
    print("Nama saya :"+str(nama))

uji_param(input("Masukan Nama Kamu : "))

def uji_return(a,b):
    r = a + b
    return r

a = 12
b = 70
c = uji_return(a,b)
print(c)

#from fungsi_izal import *
#print(penulisan(int(input("Masukan NPM kamu : "))))

#class Employee:
#   'Common base class for all employees'
#   empCount = 0

#   def __init__(self, name, salary):
#      self.name = name
#      self.salary = salary
#      Employee.empCount += 1
   
#   def displayCount(self):
#     print ("Total Employee %d" % Employee.empCount)

#   def displayEmployee(self):
#      print ("Name : ", self.name,  ", Salary: ", self.salary)


#This would create first object of Employee class"
#emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
#emp2 = Employee("Manni", 5000)
#emp1.displayEmployee()
#emp2.displayEmployee()
#print ("Total Employee %d" % Employee.empCount)

#import belajar
#a = 100
#b = 50

#c = belajar.penambahan(a,b)
#print(c)

#Ketrampilan Pemrograman
#No.1
def jawabanNo1():
    
    npm = input("Masukan NPM :")
    npm = list(str(npm))

    angka1 = {"0":" ###### ", "1":"  ##", "2":" #######  ", "3":"  #######  ", "4":"   #####", "5":"#######", "6":" #######", "7":"#######", "8":" ##### ", "9":" ######  "}
    angka2 = {"0":"###  ###", "1":"####", "2":"##    ### ", "3":"###     ###", "4":"  ##  ##", "5":"##     ", "6":"###     ", "7":"#######", "8":"##   ##", "9":"##    ## "}
    angka3 = {"0":"###  ###", "1":" ###", "2":"     ###  ", "3":"      #### ", "4":" ##   ##", "5":"##     ", "6":"###     ", "7":"   ### ", "8":" ##### ", "9":"##    ## "}
    angka4 = {"0":"###  ###", "1":" ###", "2":"    ###   ", "3":"      #### ", "4":"########", "5":"###### ", "6":"########", "7":"  ###  ", "8":"#######", "9":"######## "}
    angka5 = {"0":"###  ###", "1":" ###", "2":"  ####    ", "3":"###     ###", "4":"      ##", "5":"     ##", "6":"###  ###", "7":" ###   ", "8":"##   ##", "9":"      ## "}
    angka6 = {"0":" ###### ", "1":" ###", "2":"######### ", "3":"  #######  ", "4":"      ##", "5":"###### ", "6":" ###### ", "7":"###    ", "8":" ##### ", "9":"#######  "}
          
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

jawabanNo1()

#no.2
def ulang(npm):
    hitung = 0
    while(hitung <70):
        print("Halo, " + str(npm) + " Apa Kabar?")
        hitung = hitung +1
ulang(int(input("Masukkan NPM: ")))

#no.3
def ulang3digitakhir(npm):
    hitung = 0
    npm = str(npm)
    x = npm[4:7]
    while(hitung < 7):
        print("Halo, " + x + " Apa Kabar?")
        hitung = hitung +1
ulang3digitakhir(int(input("Masukkan NPM: ")))

#no.4
def digit3daribelakang(npm):
    npm = str(npm)
    x = npm[-3]
    print("Halo, " + x + " Apa Kabar?")
digit3daribelakang(int(input("Masukkan NPM: ")))

#no5
def kebawah(npm):
    for i in npm:
        print (i)
    
kebawah(input("Masukkan NPM: "))

#no.6
def tambah(npm):
    jumlah = 0
    for i in npm:
        jumlah += int(i)
    print ("Hasil Penjumlahan NPM adalah : " +str(jumlah))
tambah(input("Masukkan NPM: "))

#No.7
def kali(npm):
    kalikan = 0
    for i in npm:
        kalikan *= int(i)
    print ("Hasil Perkalian NPM adalah : " +str(kalikan))
kali(input("Masukkan NPM: "))

#N0.8
def digitgenap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end ="")
digitgenap(input("Masukkan NPM: "))

#No.9
def digitganjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 !=0):
            print(n, end ="")
digitganjil(input("Masukkan NPM: "))

#No.10
def digitprima(npm):
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
digitprima(input("Masukkan NPM: "))

#def penanganan_error(a,b):
#    try :
#        c = a+b
#        print(c)
#    except TypeError:
#        print("We Are Different")