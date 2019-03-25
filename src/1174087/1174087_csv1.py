# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:08:29 2019

@author: PandA23
"""

import csv

with open('1174087_write.csv', mode='w') as biodata_file:
    biodata_writer = csv.writer(biodata_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    biodata_writer.writerow(['Ilham Muhammad Ariq', 'Programmer', ])
    biodata_writer.writerow(['Reza', 'Accountinng'])