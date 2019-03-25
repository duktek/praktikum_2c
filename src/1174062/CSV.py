# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:12:56 2019

@author: USER
"""

#Contoh No 1

import csv

Mahasiswa = [
    ('Izzah', 'C','TI', 2017),
    ('Fanny', 'C','TI', 2017),
    ('Dita', 'C','TI', 2017),
    ('Nadia', 'A','MB', 2017),
    ('Sri', 'B','LB', 2017)
]

# tentukan lokasi file, nama file, dan inisialisasi csv
f = open('Mahasiswa.csv', 'w')
w = csv.writer(f)
w.writerow(('Nama','Kelas','Jurusan','Angkatan'))

# menulis file csv
for s in Mahasiswa:
    w.writerow(s)

# menutup file csv
f.close()