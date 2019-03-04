# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#teori
#No 1
#Boolean
boolean1 = True
print(boolean1)

#String
str1 = "Ariq"
print(str1)

#Integer
int1 = 1174087
print(int1)

#Float
float1 = 5.5
print(float1)

#Hexadecimal
hexadecimal1 = 0x5
print(hexadecimal1)

#Complex
complex1 = 5j
print(complex1)

#List
list1 = [1,2,3]
print(list1)
print(list1[0])

#Tuple
tuple1 = (1,2,3)
print(tuple1)
print(tuple1[0])

#Set
set1 = {1,2,3}
print(set1)


#Dictionary
dictionary1 = {1:'satu', 2:'dua', 'tiga':3}
print(dictionary1)
print(dictionary1[1])

#No 2
#Input dan Output
npm = input('Masukan Npm anda : ')
print(npm, "adalah Npm kamu")

#No 3
a = 2 #int
b = 3 #int
c = "1" #str

print(a+b) #tambah
print(a-b) #kurang
print(a*b) #kali
print(a/b) #bagi
print(int(c)) # string ke integer
print(str(a)) # int ke string

#No 4
#While Loop
hitung = 1
while (hitung < 5):
    print (hitung)
    hitung += 1
    
#For Loop
angka = [1,2,3]
for x in angka:
    print(x)
    
#No 5
#If
nilai = 70
if nilai > 70:
    print("Grade A")

#If Else
nilai = 50
if angka > 70:
    print("Grade A")
else:
    print("Grade B")

#Elif
urutan = input("Masukan Urutan:")
jenis = input("Masukan Jenis:")
if urutan == 1:
    print("Kamu anak pertama")
elif jenis == "perempuan":
    print("Benar")
else:
    print("Salah")
    
#No 7
try:
  print(ter)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#praktek
#No 1
print(1174087%3)

print(" ##  ## ######   ###  ####  ###### ######")
print("### ###    ##  ## ## ##  ## ##  ##    ##")
print(" ##  ##   ##  ###### ##  ## ######   ##")
print(" ##  ##  ##       ## ##  ## ##  ##  ##")
print(" ##  ## ##        ##  ####  ###### ##")
      
#No 2      
i = 1 
npm = input("Masukan Npm:")
while i <87:
    print("Hallo,",npm, "apa kabar?" )
    i += 1

#No 3
i = 1 
npm = input("Masukan Npm:")    
while i < 15:
    print("Hallo,",npm[4:8],"apa kabar?")
    i+= 1
    
#No 4
npm = input("Masukan Npm:") 
print("Hallo,",npm[4],"apa kabar?")

#No 5
a = 1
b = 1
c = 7
d = 4
e = 0
f = 8
g = 7
print(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g))

#No 6
print(a+b+c+d+e+f+g)

#No 7
print(a*b*c*d*e*f*g)

#No 8
npm = [a,b,c,d,e,f,g]
for x in npm:
   print(x)

#No 9
for n in npm:
    if(n % 2 == 0):
        if(n != 0):
            print(n, end ="")
            
#No 10      
for n in npm:
    if(n % 2 != 0):
        print(n, end ="")

#No 11
print(str(c)+str(g))



    
    


