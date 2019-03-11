# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:22:44 2019

@author: User
"""
def loop(npm = "1174091"):
    for x in range(87):
       print("hallo " + npm + " apa kabar")
loop("1174091")
#yabg atas jawaban no 2
#bawah jawaban no 3
npm=1174091
def loop(npm):
    for x in range(15):
       print("hallo " + str(npm)[4:7] +" apa kabar")

loop(npm)

#bawah jawaban no 4
def helloword(npm):
    npm="1174091"
    print("halo " +str(npm)[4] + " apa kabar")    
helloword(npm)

#bawah jawaban 5
def test(npm):
    npm = ['1','1','7','4','0','9','1']
    for x in npm:
        print(x) 
test(npm)

#jawaban no 6
def jmlnpm(npm):
    npm = [1,1,7,4,0,9,1]
    hasil = 0
    for x in npm:
        hasil += x
    
    print(hasil)
jmlnpm(npm)

#jawaban no 7
def kalinpm(npm):
    npm = [1,1,7,4,0,9,1]
    hasil = 0
    for x in npm:
        hasil *= x
    
    print(hasil)
kalinpm(npm)

#jawaban no 8
def npmgenap(npm):
    npm = [1,1,7,4,0,9,1]
    for num in npm :
        if (num % 2 == 0):
            print (num, end ="")
npmgenap(npm)

#jawaban no 9
def npmprima(npm):
    npm = list(map(int, npm))
    for num in npm :
        if (num % 2 != 0):
            print (num, end ="")
npmprima(input("Masukan NPM anda: "))