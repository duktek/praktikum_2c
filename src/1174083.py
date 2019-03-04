# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print (1174083%3)

#No.1
print("  **   ** ********    *****  ******   ******  ********")
print("**** **** ********   ****** ***  *** ******** ********")
print(" ***  ***      ***  **   ** ***  *** ***  ***      ***")
print(" ***  ***     ***  ***   ** ***  *** ******** ********")
print(" ***  ***    ***   ******** ***  *** ******** ********")
print(" ***  ***   ***    ******** ***  *** ***  ***      ***")
print(" ***  ***  ***          *** ***  *** ******** ********")
print(" ***  *** ***           ***  ******   ******  ********")

#No. 2
npm = input("Masukkan NPM : ")
ulang = 1
while(ulang <= 83):
    print("Halo, "+str(npm)+" apa kabar?")
    ulang += 1

#No. 3
npm = input("Masukkan NPM : ")
ulang = 1
while(ulang <= 83):
    print("Halo, "+str(npm[4:7])+" apa kabar?")
    ulang += 1
    
#No. 4
npm = input("Masukkan NPM : ")
print("Halo, "+str(npm[-3])+" apa kabar?")

#No. 5
a = 1
b = 1
c = 7
d = 4
e = 0
f = 8
g = 3

npm = [a,b,c,d,e,f,g]

for n in npm:
    print(n, end ="")

print()

#No. 6
print(a+b+c+d+e+f+g)

#No. 7
print(a*b*c*d*e*f*g)

#No. 8
for n in npm:
    print(n)
         
#No. 9    
for n in npm:
    if(n % 2 == 0):
        if(n != 0):
           print(n, end ="")

print()        

#No. 10        
for n in npm:
    if(n % 2 != 0):
        print(n, end ="")

print()


#No. 11

for n in npm:
    if(n % 2 != 0):
        print(n, end ="")

print()


