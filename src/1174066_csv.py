# -*- coding: utf-8 -*-
"""
Chapter 4

author: D. Irga B. Naufal Fakhri.
"""
import csv
import pandas

def read():
    with open('1174066.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\tNomor NPM: {row[0]} Nama: {row[1]} Kelas: {row[2]}.')
                line_count += 1
                print(f'Processed {line_count} lines.')
read()

def readdict():
    with open('1174066.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\tNomor NPM: {row["npm"]} Nama: {row["nama"]} Kelas: {row["kelas"]} ')
            line_count += 1
        print(f'Processed {line_count} lines.')   
readdict()

def write():
    with open('1174066_write.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['npm', 'nama', 'kelas'])
        employee_writer.writerow(['1174066', 'D. Irga 3', 'D4 Teknik Informatika 2C'])        
write()

def readpanda():
    df = pandas.read_csv('1174066.csv')
    print(df)
readpanda()

def writepanda():
    df = pandas.read_csv('1174066.csv', 
            index_col='npm', 
            parse_dates=['namalengkap'],
            header=0, 
            names=['npm', 'namalengkap', 'kelas'])
    df.to_csv('1174066_diedit.csv')
writepanda()