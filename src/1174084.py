# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:45:34 2019

@author: Reza
"""

a ='1174084' #variabel/angka yang akan di konversi.
integer = int(a) #konversi string ke integer

a = 1174084 #variabel/angka yang akan di konversi.
string = str(a) #konversi integer ke string

#while loop
i = 1
while i < 6:
  print(i)
  i += 1
#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
#if 
a = 33
b = 200
if b > a:
  print("b lebih besar dari a")
#elif
a = 33
b = 33
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a dan b sama")

#if bersarang
gaji = 10000000
berkeluarga = True

if gaji > 3000000:
    print("Gaji sudah diatas UMR")
    if berkeluarga:
        print("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print("Tidak perlu ikutan asuransi")
else:
    print("Gaji belum UMR")
    
#try except
try:
  print(x)
except:
  print("An exception occurred")
  
  
#no. 1
print (1174084%3)

print("***  ***  *********** ***   ***  *********  *********  ***   ***")
print("***  ***  **********  ***   ***  *********  *********  ***   ***")
print("***  ***        ***   ***   ***  ***   ***  ***   ***  ***   ***")
print("***  ***       ***    ***   ***  ***   ***  ***   ***  ***   ***")
print("***  ***      ***     *********  ***   ***  *********  *********")
print("***  ***     ***            ***  ***   ***  ***   ***        ***")
print("***  ***    ***             ***  ***   ***  ***   ***        ***")
print("***  ***   ***              ***  *********  *********        ***")
print("***  ***  ***               ***  *********  *********        ***")

#no. 2
npm  = input("Masukan NPM :")
nilai = int(npm[5:7])
hitung = 0
while(hitung < nilai):
    print("Halo, " + str(npm) + " Apa Kabar?")
    hitung = hitung +1

#no. 3 
npm = input("Masukan NPM :")
nilai = int(npm[4:5]) + int(npm[5:6]) + int(npm[6:7])
hitung = 0
while(hitung < nilai):
    print("Halo, " + str(npm[4:7]) + " Apa Kabar?")
    hitung = hitung +1

#no. 4
npm = input("Masukan NPM :")
print("Halo, " + str(npm[-3]) + " Apa Kabar?")

#no. 5
a = 1
b = 1
c = 7
d = 4
e = 0
f = 8
g = 4
npm = [a,b,c,d,e,f,g]

for a in npm:
    print(a, end ="")

#no. 6
print(a+b+c+d+e+f+g)

#no. 7
print(a*b*c*d*e*f*g)

#no. 8
for a in npm:
    print(a)

#no. 9
for n in npm:
    if(n % 2 == 0):
        if(n != 0):
            print(n, end ="")

#no. 10
for n in npm:
    if(n % 2 != 0):
        print(n, end ="")

#no. 11
print(c)

#no. 11
print (7)