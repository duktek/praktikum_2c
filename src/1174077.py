# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#variabel
x = "Python is "
y = "awesome"
z =  x + y
print(z)

#input
print('Enter your name:')
x = input()
print('Hello, ' + x)

#output
print("Hello World")

#tambah
x = 5
y = 3

print(x + y)

#kuarang
x = 5
y = 3

print(x - y)

#kali
x = 5
y = 3

print(x * y)

#bagi
x = 12
y = 3

print(x / y)

#string to integer
a ='1212' #variabel/angka yang akan di konversi.

integer = int(a) #konversi string ke integer

#integer to string
a=100 #variabel/angka yang akan di konversi.

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

#kondisi
a = 33
b = 200
if b > a:
  print("b is greater than a")

#kondisi dalam kondisi
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
#try except
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
#soal no 1
print (1174077%3)

print("***  ***  *********** ***   ***  *********  ***********  ***********")
print("***  ***  **********  ***   ***  *********  **********   **********")
print("***  ***        ***   ***   ***  ***   ***        ***          ***")
print("***  ***       ***    ***   ***  ***   ***       ***          ***")
print("***  ***      ***     *********  ***   ***      ***          ***")
print("***  ***     ***            ***  ***   ***     ***          ***")
print("***  ***    ***             ***  ***   ***    ***          ***")
print("***  ***   ***              ***  *********   ***          ***")
print("***  ***  ***               ***  *********  ***          ***")

#soal no 2
npm  = input("Masukan NPM :")
nilai = int(npm[5:7])
hitung = 0
while(hitung < nilai):
 print("Halo, " + str(npm) + " Apa Kabar?")
hitung = hitung +1
    
#soal no 3
npm = input("Masukan NPM :")
nilai = int(npm[4:5]) + int(npm[5:6]) + int(npm[6:7])
hitung = 0
while(hitung < nilai):
 print("Halo, " + str(npm[4:7]) + " Apa Kabar?")
hitung = hitung +1

#soal no 4
npm = input("Masukan NPM :")
print("Halo, " + str(npm[-3]) + " Apa Kabar?")

#soal no 5
a = 1
b = 1
c = 7
d = 4
e = 0
f = 7
g = 7
npm = [a,b,c,d,e,f,g]

for a in npm:
    print(a, end ="")
    
#soal no 6
a = 1
b = 1
c = 7
d = 4
e = 0
f = 7
g = 7
print(a+b+c+d+e+f+g)

#soal no 7
a = 1
b = 1
c = 7
d = 4
e = 0
f = 7
g = 7
print(a*b*c*d*e*f*g)

#soal no 8
a = 1
b = 1
c = 7
d = 4
e = 0
f = 7
g = 7
for a in npm:
    print(a)
    
#soal no 9
a = 1
b = 1
c = 7
d = 4
e = 0
f = 7
g = 7
for n in npm:
    if(n % 2 == 0):
      if(n != 0):
        print(n, end ="")
        
#soal no 10
a = 1
b = 1
c = 7
d = 4
e = 0
f = 7
g = 7
for n in npm:
    if(n % 2 != 0):
        print(n, end ="")
        
#soal no 11
a = 1
b = 1
c = 7
d = 4
e = 0
f = 7
g = 7
print(c)





