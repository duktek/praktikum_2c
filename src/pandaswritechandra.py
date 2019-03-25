# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 01:38:40 2019

@author: ACER
"""
import pandas
df = pandas.read_csv('contohchandrapandas.csv', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('hrdata_modified.csv')