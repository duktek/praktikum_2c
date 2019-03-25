# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:53:03 2019

@author: ASUS X441U
"""

import csv

siswa = [
    ('Aulya', 'A', 90),
    ('Ardha', 'B', 85),
    ('Dita', 'A', 80),
    ('Anin', 'B', 90),
    ('Dilan', 'C', 70)
]

# tentukan lokasi file, nama file, dan inisialisasi csv
f = open('siswa.csv', 'w')
w = csv.writer(f)
w.writerow(('Nama','Kelas','Nilai'))

# menulis file csv
for s in siswa:
    w.writerow(s)

# menutup file csv
f.close()