# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:42:48 2019

@author: PandA23
"""

import pandas
tambah_data = {'Nama': ['Ilham Muhammad Ariq'], 
               'Kelas': ['D4TI2C']}
df = pandas.DataFrame(tambah_data, columns = ['Nama', 'Kelas'])
df.to_csv('1174087_write1.csv')
print(df)