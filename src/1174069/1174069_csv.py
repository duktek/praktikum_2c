# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:48:59 2019

@author: FannyCantik
"""

import csv

siswa = [
    ('fanny', 'A', 90),
    ('shafira', 'B', 85),
    ('dama', 'A', 80),
    ('yanti', 'B', 90),

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