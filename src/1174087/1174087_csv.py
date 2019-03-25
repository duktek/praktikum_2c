# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:26:52 2019

@author: PandA23
"""

import csv

with open('1174087_open.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Nama Kolom meliputi {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t Nama saya {row[0]} dan Pekerjaan {row[1]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')