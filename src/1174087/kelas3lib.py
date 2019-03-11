# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:39:15 2019

@author: PandA23
"""
#Teori
#No 3
class Mahasiswa:
    def __init__(self,nama):
        self.nama = nama
    def biodata(self):
        print("Nama saya", self.nama) 
        
NamaMhs = Mahasiswa("Ariq")
NamaMhs.biodata()