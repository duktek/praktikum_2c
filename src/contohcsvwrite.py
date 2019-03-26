# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 01:38:14 2019

@author: ACER
"""
import csv
with open('contohchandra.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['aaaaaaaa', 'Accounting', 'November'])
    employee_writer.writerow(['bbbbb Meyers', 'IT', 'March'])