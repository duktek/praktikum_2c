# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:46:10 2019

@author: Chandra Kirana Poetra
"""

#Soal no 1 Tipe data


#contoh integer
a = 1
b = 1.1
z = 2+1j

print(type(a))
print(type(b))
print(type(z))

# contoh string

a = "Chandra Kirana Poetra"
print(a[1]) 
#print ini digunakan untuk mencetak huruf yang dipilih indexnya

a = "Chandra Kirana Poetra"
print(a[2:5]) 
#print ini digunakan untuk mencetak huruf yang dipilih indexnya dengan mengisi
#nilai index tempat kita memilih index untuk memulai mengambil, dan juga nilai index
#akhirnya

a = "Chandra Kirana Poetra"
print(len(a)) 
#print ini digunakan untuk menjumlahkan length yang artinya panjang dari string a

a = "Chandra Kirana Poetra"
print(a.lower()) 
#print ini digunakan untuk mencetak huruf yang kecil semua

a = "Chandra Kirana Poetra"
print(a.upper()) 
#print ini digunakan untuk mencetak huruf yang besar semua

#boolean

a = 10
b = 8
if (a>b):
    print("Variabel A lebih besar dibandingkan dengan Variable B")
elif(a<b): 
    print("Variabel A lebih kecil dibandingkan dengan Variable B")
else:
    print("Variabel A Nilainya sama dengan Variable B")

#soal no 2
namalengkap = input("Masukan Nama lengkap kamu : ")
print("Halo "  + str(namalengkap))


#soal no 3

a = 1
b = 2
print(a+b)# ini merupakan contoh penjumlahan
print(a-b)# ini merupakan contoh pengurangan
print(a*b)# ini merupakan contoh perkalian
print(a/b)# ini merupakan contoh pembagian
print(a%b)# ini merupakan contoh modulus

#soal no 4
#While looping

a = 1
while a < 10:
    print(a)
    a +=1
    
# for looping
benda = ["Piring","Sendok","Garpu"]
for x in benda:
    print(x)

#soal no 5
#contoh if statement
    
a = 5
b = 10
if b > a:
    print("b ternyata lebih besar dari a")

#contoh elif statement
a = 5
b = 10
if a > b:
    print("a ternyata lebih besar dari b")
elif a < b:
    print("a ternyata lebih kecil dari b")
    
    
#contoh else statement
a = 5
b = 5
if a > b:
    print("a ternyata lebih besar dari b")
elif a < b:
    print("a ternyata lebih kecil dari b")
else:
    print("a dan b sama")
    
#soal no 7
try:
    print(g)
except:
    print("Ada error")