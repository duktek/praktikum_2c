# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:25:12 2019

@author: PandA23
"""

#Keterampilan Penanganan Error
a = 1
b = "2"

try:
    c = a + b
    print(c)
except TypeError:
    print("Tipe data nya berbeda")