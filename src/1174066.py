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
    

"""
Chapter 3

author: D. Irga B. Naufal Fakhri.
"""
#Contoh fungsi inputan
def printteks( str ):
   print (str)
   return

printteks("Ini adalah Contoh fungsi")

#Contoh fungsi outputan
def output( str ):
   full = "Ini adalah contoh dari " + str
   return full

print(output("fungsi outputan"))


#Contoh import library atau package
import fungsi_1174066

input(fungsi_1174066.hello("Dirga"))

#Contoh Class
class Mahasiswa:
    def __init__(self,nama,npm,kelas):
        self.nama = nama
        self.npm = npm
        self.kelas = kelas
        
    def datadiri(self):
        print ("Nama: ", self.nama,  ", NPM: ", self.npm, ", Kelas: ", self.kelas)

#Pembuatan Object
mhs1 = Mahasiswa("D. Irga",11174066,"D4TI2C")
mhs1.datadiri();


#Contoh cara memanggil library atau package
import fungsi_1174066

x = 3
y = 7
print(fungsi_1174066.Tambah(x,y))


#Contoh cara memanggil library atau package dari from import
from fungsi_1174066 import Tambah

x = 3
y = 7
print(Tambah(x,y))

#Contoh cara memanggil library atau package dari folder
from 1174066.fungsi_1174066 import Tambah

x = 3
y = 7
print(Tambah(x,y))


#Bagian Keterampilan Pemograman Chapter 3
#Jawaban nomor 1
def npm(npm):
    text = str(npm)
    from PIL import Image, ImageDraw, ImageFont
    import numpy as np
    myfont = ImageFont.truetype("verdanab.ttf", 12)
    size = myfont.getsize(text)
    img = Image.new("1",size,"black")
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, "white", font=myfont)
    pixels = np.array(img, dtype=np.uint8)
    if int(text) % 3 == 0:    
        chars = np.array([' ','*'], dtype="U1")[pixels]
    elif int(text) % 3 == 1:
        chars = np.array([' ','#'], dtype="U1")[pixels]
    elif int(text) % 3 == 2:
        chars = np.array([' ','+'], dtype="U1")[pixels]        
    strings = chars.view('U' + str(chars.shape[1])).flatten()
    print( "\n".join(strings))

npm(1174066)

#Jawaban nomor 2
def loop(npm):
    i = 1
    while(i <= int(npm[5:])):
        print("Hallo, "+str(npm)+" apa kabar?")
        i += 1

loop(input("Masukan NPM : "))

#Jawaban nomor 3
def looptambah(npm):
    i = 1
    akhir = int(npm[4:5]) + int(npm[5:6]) + int(npm[6:7])
    while(i <= akhir):
        print("Hallo, "+str(npm[4:7])+" apa kabar?")
        i += 1
        
looptambah(input("Input: "))

#Jawaban nomor 4
def hallo(npm):
    print("Halo, "+str(npm[-3])+" apa kabar?")
    
hallo(input("Input: "))

#Jawaban nomor 5
def array(npm):
    for x in npm:
        print (x)
        
array(input("NPM: "))        


#Jawaban nomor 6
def jumlah(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil += x
    print("Hasil perjumlahan dari npm anda adalah: " + str(hasil))

jumlah(input("NPM: "))

#Jawaban nomor 7
def kali(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil *= x
    print("Hasil perkalian dari npm anda adalah: " + str(hasil))

kali(input("NPM: "))


#Jawaban nomor 8
def printgenap(npm):
    npm = list(map(int, npm))
    for x in npm:
        if(x % 2 == 0):
            if(x != 0):
                print(x, end = "")

printgenap(input("NPM: "))

#Jawaban nomor 9
def printganjil(npm):
    npm = list(map(int, npm))
    for x in npm:
        if(x % 2 != 0):
            print(x, end = "")

printganjil(input("NPM: "))


#Jawaban nomor 10
def printprima(npm):
    npm = list(map(int, npm))
    prima = []
    for n in npm:
        bilPrima = True
        if n == 0 or n == 1:
            bilPrima = False
        for x in range(2, n):
            if n % x == 0:
                bilPrima = False
        if bilPrima:
            prima.append(n)

    for p in prima:
        print(p, end = "")

printprima(input("NPM: "))



#Ketrampilan Penanganan Error
#Jawaban No. 1
def hallo(nama):
    try:
        print("Hallo, "+str(nama))
    except:
        print("Terjadi error") 

hallo(input("Masukan nama anda: ")) 