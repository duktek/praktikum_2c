# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:52:44 2019

@author: User
"""

a = 1
b = 1,1
x = 2+1j

print(type(a))
print(type(b))
print(type(x))

q = "Arrizal Furqona Gifary"
print(q[1])

q = "Arrizal Furqona Gifary"
print(q[2:5])

q = "Arrizal Furqona Gifary"
print(len(a))

q = "Arrizal Furqona Gifary"
print(q.lower())

q = "Arrizal Furqona Gifary"
print(q.upper())


a = 10
b = 8
if (a>b):
    print("Variable A lebih besar dibandingkan dengan Variable B)
elif(a<b):
    print("Variable A lebih kecil dibandingkan dengan Variable B)
else:
    print("Variable A nilainya sama dengan Variable B)
    
    

namalengkap = input("Maukan Nama Lengkap Kamu : ")
print("Hallo," + str(namalengkap))


a = 1
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)


a = 1
while a < 10:
    print(a)
    a +=1
    

benda = ("piring","sendok","garpu")
for x in benda:
    print(x)
    
a = 5
b = 10
if a > b:
    print("b ternyata lebih besar dari a")
    

a = 5
b = 10
if a > b:
    print("a ternyata lebih besar dari b")
elif a < b:
    print("a ternyata lebih kecil dari b")
    
a = 5
b = 5
if a > b:
    print("a ternyata lebih besar dari b")
elif a < b:
    print("a ternyata lebih kecil dari b")
else:
    print("a dan b sama")
    
try:
    print(g)
except:
    print("ada eror")
    