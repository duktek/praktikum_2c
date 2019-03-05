# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:27:25 2019

@author: Reza
"""

a = 1
b = "2"

try:
    c = a + b
    print(c)
except TypeError :
    print("Tipe Data Berbeda!")