# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Nomor 1 TEORI
x = 21
y = "Difa Al Fansha"
print("Nama Kamu ",x)
print("Umur Kamu", y)


#Nomor 2 TEORI
# Mengambil input
nama = input("Siapa nama kamu : ")
umur = input("Berapa umur kamu : ")

# Menampilkan output
print ("Hello",nama,"umur kamu adalah",umur,"tahun")

# Nomor 3 TEORI
a = 21
b = 7
c = "Difa Al Fansha"
d = "17"
# Tambah
print (a + b)
# Kurang
print (a - b)
# Kali
print (a * b)
# Bagi
print (a / b)
# String ke int
print ("Nama :",c, "Dan", "Umur :", int(d))
# Int ke String
print (str(a) + str(b))

# Nomor 4 TEORI
# For Loops
Nama = ["Difa Al Fansha"]
for x in Nama :
    print (x)
    
# While Loops
e = 1
while e < 6 :
    print (e)
    e += 1
    
# Nomor 5 TEORI
f = 50
g = 200
if g > f :
    print ("G Lebih besar dari F")
    if g == 200:
        print ("Nilai G adalah 200")
else :
    print ("F Lebih besar dari G")

# Nomor 6 TEORI
        
# Nomor 7 TEORI
try :
    print (Hello)
except :
    print ("Ada yang salah")
    
    
# Nomor 1 PRAKTEK
print (1174076%3)
# mod 3 = 1

print("  ##   ## #########    ###  ######   #########  #########")
print("#### #### ########   ##### ###  ###  #########  ###      ")
print(" ###  ###     ###  ### ### ###  ###      ###    ###      ")
print(" ###  ###    ###  ######## ###  ###     ###     #########")
print(" ###  ###   ###        ### ###  ###    ###      ###   ###")
print(" ###  ###  ###         ###  ######    ###       #########") 

# Nomor 2 PRAKTEK
Npm = input("Input : ")
sebanyak = 1
while(sebanyak <= 76):
    print("Halo, "+str(Npm)+" apa kabar?")
    sebanyak += 1
    
# Nomor 3 PRAKTEK
Npm = input("Input NPM : ")
sebanyak = 1
while(sebanyak <= 13):
    print("Halo, "+str(Npm[4:7])+" Apa kabar?")
    sebanyak += 1
    
# Nomor 4 PRAKTEK
Npm = input("Input Npm : ")
print("Halo, "+str(Npm[-3])+" Apa kabar?")

# Nomor 5 PRAKTEK  
h = 1
i = 1
j = 7
k = 4
l = 0
m = 7
n = 6

Npm = [h,i,j,k,l,m,n]

for y in Npm:
    print(y, end ="")
print("")

# Nomor 6 PRAKTEK 
print(h+i+j+k+l+m+n)
 
# Nomor 7 PRAKTEK
print(h*i*j*k*l*m*n)

# Nomor 8 PRAKTEK
for z in Npm:
    print(z)
    
# Nomor 9 PRAKTEK
for n in Npm:
    if(n % 2 == 0):
        if(n != 0):
            print(n, end ="")
print()

# Nomor 10 PRAKTEK
for n in Npm:
    if(n % 2 != 0):
        print(n, end ="")
print()

# Nomor 11 PRAKTEK
for n in Npm:
    if(n % 2 == 0):
        if(n != 0):
            print(n, end ="")
print()