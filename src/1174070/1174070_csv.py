# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:00:04 2019

@author: User
"""
import pandas
import csv

def bacacsv():
    with open('1174070.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t NPM : {row[0]} Nama : {row[1]} Kelas : {row[2]}.')
                line_count += 1
                print(f'Processed {line_count} lines.')

def bacadictionary():
    with open('1174070.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t NPM : {row["name"]} Nama : {row["department"]} Kelas :  {row["birthday month"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')

def nulis():
    with open('test-tulis.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['Ucok', 'Tukang', 'November'])
        employee_writer.writerow(['Udin', 'Mandor', 'April'])

def bacapandas():
    df = pandas.read_csv('1174070.csv')
    print(df)