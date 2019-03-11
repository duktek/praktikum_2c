# -*- coding: utf-8 -*-
"""
Chapter 2

author: D. Irga B. Naufal Fakhri.
"""

#Boolean
varbool = True
print(varbool)

#String
varstr = "D. Irga B. Naufal Fakhri"
print(varstr)

#Integer
varint = 1174066
print(varint)

#Float
varflt = 1.1
print(varflt)

#Hexadecimal
varhex = 0x1
print(varhex)

#Complex
varcmp = 7j
print(varcmp)

#List
varli = [1,2,3]
print(varli)
print(varli[2])

#Tuple
vartu = (1,2,3)
print(vartu)
print(vartu[2])

#Set
varset = {1,2,3}
print(varset)

#Dictionary
vardic = {1:'satu', 2:'dua', 'tiga':3}
print(vardic)
print(vardic[1])

#Input dan Output
nama = input('Tolong masukan nama anda: ')
print('Hallo, '+nama)

#Operator Dasar Aritmatika
#Perjumlahan
var1 = 1
var2 = 2
hasil = var1 + var2
print(hasil)

#Pengurangan
var1 = 4
var2 = 3
hasil = var1 - var2
print(hasil)

#Perkalian
var1 = 5
var2 = 6
hasil = var1 * var2
print(hasil)

#Pembagian
var1 = 8
var2 = 2
hasil = var1 / var2
print(hasil)

#Modulus
var1 = 7
var2 = 3
hasil = var1 % var2
print(hasil)

#Perpangkatan
var1 = 10
var2 = 2
hasil = var1 ** var2
print(hasil)

#Pembulatan Kebawah Pada Hasil Pembagian
var1 = 11
var2 = 3
hasil = var1 // var2
print(hasil)

#Mengubah Tipe Data
#String menjadi Integer
varstr = '1'
varint = int(varstr)
print(varint)

#Interger menjadi String
varint = 2
varstr = str(varint)
print(varstr)


#Looping
#While Loop
hitung = 1
while (hitung < 6):
    print (hitung)
    hitung += 1

#For Loop
angka = [1,2,3,4,5]
for a in angka:
    print(a)

#Nested Loop
i = 1
while(i < 5):
    j = 1
    while(j <= 5):
        print('TEST')
        j += 1
    i += 1


#Kondisi
#If
var = 1
if var > 0:
    print(var, "adalah angka lebih dari 0")

#If Else
var = -1
if var > 0:
    print(var, "adalah angka kurang dari 0")
else:
    print(var, "adalah angka lebih dari 0")

#Elif
var = 0
if var > 0:
    print(var, "adalah angka lebih dari 0")
elif var < 0:
    print(var, "adalah angka kurang dari 0")
else:
    print(var, "adalah angka yang sama dengan 0")


#Kondisi di dalam kondisi
if var > 0:
    print(var, "adalah angka lebih dari 0")
    if var > 10:
        print(var, "adalah angka lebih dari 10.")
    else:
        print(var, "adalah angka lebih dari 10.")
elif var < 0:
    print(var, "adalah angka kurang dari 0")
else:
    print(var, "adalah angka yang sama dengan 0")


#Try Except
try:
    print(tidakada)
except:
    print("Terjadi kesalahan penulisan kode")
finally:
    print("Try except telah selesai") 


#Jawaban No. 1

print(1174066%3)
#mod3 = 1

print("  ##   ## #########    ###  ######  ########  ########")
print("#### #### ########   ##### ###  ### ###      ###")
print(" ###  ###     ###  ### ### ###  ### ###      ###")
print(" ###  ###    ###  ######## ###  ### ######## ########")
print(" ###  ###   ###        ### ###  ### ###  ### ###   ###")
print(" ###  ###  ###         ###  ######   ######   #######")
#Cara kedua Penulisan NPM tanda pagar menurut https://stackoverflow.com/questions/9632995/how-to-easily-print-ascii-art-text
text = "1174066"
from PIL import Image, ImageDraw, ImageFont
import numpy as np
myfont = ImageFont.truetype("verdanab.ttf", 12)
size = myfont.getsize(text)
img = Image.new("1",size,"black")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, "white", font=myfont)
pixels = np.array(img, dtype=np.uint8)
chars = np.array([' ','#'], dtype="U1")[pixels]
strings = chars.view('U' + str(chars.shape[1])).flatten()
print( "\n".join(strings))


#Jawaban No. 2

npm = input("Input : ")
i = 1
while(i <= int(npm[5:])):
    print("Halo, "+str(npm)+" apa kabar?")
    i += 1


#Jawaban No. 3

npm = input("Input : ")
i = 1
akhir = int(npm[4:5]) + int(npm[5:6]) + int(npm[6:7])
while(i <= akhir):
    print("Hallo, "+str(npm[4:7])+" apa kabar?")
    i += 1


#Jawaban No. 4

npm = input("Input : ")
print("Halo, "+str(npm[-3])+" apa kabar?")


#Jawaban No. 5

a = 1
b = 1
c = 7
d = 4
e = 0
f = 6
g = 6

npm = [a,b,c,d,e,f,g]

for n in npm:
    print(n, end ="")
print()


#Jawaban No. 6

print(a+b+c+d+e+f+g)


#Jawaban No. 7

print(a*b*c*d*e*f*g)


#Jawaban No. 8

for n in npm:
    print(n)


#Jawaban No. 9

for n in npm:
    if(n % 2 == 0):
        if(n != 0):
            print(n, end ="")

print()


#Jawaban No. 10

for n in npm:
    if(n % 2 != 0):
        print(n, end ="")

print()


#Jawaban No. 11

for n in npm:
    for x in range(2,n):
        if n%x != 0:
            
            break
        print(n, "Bilangan prima")
        break