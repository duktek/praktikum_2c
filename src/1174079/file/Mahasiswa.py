# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:58:05 2019

@author: ACER
"""

class Mahasiswa:
    jumlahMahasiswa  = 0
    
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        Mahasiswa.jumlahMahasiswa +=1
        
    def tampilprofile(self):
        print("NPM ", self.npm)
        print("Nama ", self.nama)
        print()