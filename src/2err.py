# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:17:38 2019

@author: Difaal21
"""

a = 100
b = "50"

try:
    c = a + b
    print("Hasil :", c)
except TypeError :
    print("Tipe data tidak sama") 
    
#Solusi
    
a = 100
b = "50"

try:
    c = a + int(b)
    print("Hasil :", c)
except TypeError :
    print("Tipe data tidak sama") 
    
for x in range(1, 100):
for y in range(2, x):
if x%y == 0 :break
else:
    print (x, sep='', end='')
