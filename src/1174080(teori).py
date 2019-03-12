# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 23:03:52 2019

@author: handihermawan
"""

#Pemahaman Teori
#Jawaban No. 1
def namaFungsi(inputanFungsi):
    return inputanFungsi

output = namaFungsi("Kembalian Fungsi")
print(output)

#Jawaban No. 2
import math
print("Nilai pi adalah: ", math.pi)

#Jawaban No. 3
class Mahasiswa:
    jumlahMahasiswa = 0
    
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        Mahasiswa.jumlahMahasiswa +=1
            
    def tampilkanProfil(self):
        print("NPM :", self.npm)
        print("Nama :", self.nama)
        print()

mahasiswa1 = Mahasiswa("1174080", "Handi Hermawan")
mahasiswa2 = Mahasiswa("1174076", "Difa Al")

mahasiswa1.tampilkanProfil()
mahasiswa2.tampilkanProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)

#Jawaban No. 4
from Mahasiswa import Mahasiswa

mhs1 = Mahasiswa("1174080", "Handi Hermawan")
mhs2 = Mahasiswa("1174076", "Difa Al")

mhs1.tampilkanProfil()
mhs2.tampilkanProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)

#Jawaban No. 5
from kalkulator import Penambahan

hasil = Penambahan(10, 5)
print(hasil)

#Jawaban No. 6
from folder import kalkulator

a=100
b=50

hasil1=kalkulator.Penambahan(a,b)
hasil2=kalkulator.Pengurangan(a,b)
hasil3=kalkulator.Perkalian(a,b)
hasil4=kalkulator.Pembagian(a,b)

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)

#Jawaban No. 7
from folder.Mahasiswa import Mahasiswa

mhs1 = Mahasiswa("1174080", "Handi Hermawan")
mhs2 = Mahasiswa("1174076", "Difa Al")

mhs1.tampilkanProfil()
mhs2.tampilkanProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)

class Mahasiswa:
    jumlahMahasiswa = 0
    
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        Mahasiswa.jumlahMahasiswa +=1
            
    def tampilkanProfil(self):
        print("NPM :", self.npm)
        print("Nama :", self.nama)
        print()