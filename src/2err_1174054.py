# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:15:33 2019

@author: Aegis
"""

#Keterampilan Penanganan Error

a = 1
b = "2"

try:
    c = a + b
    print(c)
except TypeError :
    print("Tipe datanya beda, anda harus mengubah tipe data sehingga bisa dijumlahkan!")