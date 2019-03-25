# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:15:42 2019

@author: acer
"""

# import csv

# with open('employee_birthday.txt', mode='r') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
#    line_count = 0
#    for row in csv_reader:
#        if line_count == 0:
#            print(f'Column names are {", ".join(row)}')
#            line_count += 1
#        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
#        line_count += 1
#    print(f'Processed {line_count} lines.')


#	csv.reader :
#   Fungsi reader atau pembaca dirancang untuk mengambil setiap baris file dan membuat daftar semua kolom.
    
#   Contoh 
# import CSV
# Dengan terbuka ( 'some.csv', ' rb ') sebagai f:
# reader = csv.reader (f)
# f atau baris di pembaca:
# print baris 

#	csv.writer  :
#   Fungsi writer () akan membuat objek yang cocok untuk menulis. Untuk mengulang data di atas baris, Anda harus menggunakan fungsi writerow ( ) .
#   contoh 
# impor csv
# ifile = terbuka ('test.csv', " rb ")
# reader = csv.reader ( ifile )
# ofile = open ('ttest.csv', " wb ")
# penulis = csv.writer ( ofile , delimiter = ' ', quotechar = '"', mengutip = csv.QUOTE_ALL )

# untuk baris di pembaca:
#     writer.writerow (baris)

# ifile.close ()
# ofile.close () 
#	csv.register_dialect
#	csv.unregister_dialect
#	csv.get_dialect
#	csv.list_dialects
#	csv.field_size_limit




#Membuka dan menulis file CSV
  #Membaca file CSV 
#  pd.read_csv ('file_name.csv') 
  #Membaca file CSV yang disandikan dalam ISO-8859-1 
#  pd.read_csv ('file_name.csv', enkode = 'ISO-8859-1') 
  # Menulis file CSV 
#  pd.to_csv (name_of_the_file_to_save.csv ') 

#Membuka File Excel
#  xlsx = pd.ExcelFile ('your_excel_file.xlsx') 
#  df = pd.read_excel (xlsx, 'Sheet 1') 

#Menghapus baris dan kolom
  #Menghapus baris demi indeks 
#  s.drop ([0, 1]) 
  #Hapus kolom menggunakan argumen 'axis = 1' 
#  df.drop ('Negara', sumbu = 1) 

#Mengumpulkan informasi dasar tentang DataFrame
  # Jumlah Baris dan Kolom 
#  df.bentuk 
#  Deskripsi #Index 
#  df.index 
  # Kolom dalam DataFrame 
#  df.columns 
  # Jumlah data bukan nol 
#  df.count () 

#Membuat kolom baru di DataFrame
  # Ini akan membuat kolom bernama 'Kolom Baru' dengan 0 sebagai nilainya 
#  df ['Kolom Baru'] = 0 

#Mengganti nama kolom dari DataFrame
  #Jika DataFrame Anda memiliki 3 kolom, berikan 3 nilai baru dalam daftar 
#  df.columns = ['Kolom 1', 'Kolom 2', 'Kolom 3'] 

#Ringkasan data
  #Jumlah nilai dalam DataFrame 
#  df.sum () 
  # Nilai terendah dari DataFrame 
#  df.min () 
#  Nilai tertinggi 
#  df.max () 
  #Index dari nilai terendah 
#  df.idxmin () 
  #Index dengan nilai tertinggi 
#  df.idxmax () 
  #Statistik statistik dari DataFrame, dengan kuartil, median, dll. 
#  df.describe () 
#  Nilai rata-rata 
#  df.mean () 
#  Nilai-nilai #Median 
#  df.median () 

#Menerapkan fungsi
  #Menerapkan fungsi yang menggantikan 'a' dengan 'b' 
#  df.apply (lambda x: x.replace ('a', 'b')) 

#Nilai pemesanan
  # Memesan dalam urutan menaik 
#  df.sort_values () 
  # Memesan dalam urutan menurun 
#  df.sort_values (menanjak = Salah) 

#Operasi aritmatika dalam Seri
  #Contoh 
#  s = pd.Series ([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e']) 
  #Mengumpulkan semua nilai dalam Seri dengan 2 
#  s.add (2) 
  #Kurangi 2 dari semua nilai 
#  s (2) 
#  Nilai #Multiplying oleh 2 
#  s.mul (2) 
#  Nilai #Dividing oleh 2 
#  s.div (2) 

#Pengindeksan Boolean
  #Filtering DataFrame untuk hanya menampilkan nilai genap 
#  df [df ['Populasi']% 2 == 0] 
