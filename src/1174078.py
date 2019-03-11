"""
Spyder Editor

This is a temporary script file.
"""

#No.1
print (1174078%3)
print("###  ###  ########### ###   ###  ######### ########### #########")
print("###  ###  ##########  ###   ###  ######### ##########  #########")
print("###  ###        ###   ###   ###  ###   ###        ###  ###   ###")
print("###  ###       ###    ###   ###  ###   ###       ###   ###   ###")
print("###  ###      ###     #########  ###   ###      ###    #########")
print("###  ###     ###            ###  ###   ###     ###     #########")
print("###  ###    ###             ###  ###   ###    ###      ###   ###")
print("###  ###   ###              ###  #########   ###       #########")
print("###  ###  ###               ###  #########  ###        #########")

#No.2
npm  = input("Masukan NPM :")
hitung = 0
while(hitung < 78):
    print("Halo, " + str(npm) + " Apa Kabar?")
    hitung = hitung +1

#No.3    
npm =  input("Masukan NPM :")
hitung = 0
while(hitung < 15):
    print("Halo, " + str(npm[4:7]) + " Apa Kabar?")
    hitung = hitung +1
    
#No.4
npm = input("Masukan NPM :")
print("Halo, " + str(npm[-3]) + " Apa Kabar?")

#No.5
a = 1
b = 1
c = 7
d = 4
e = 0
f = 2
g = 6
h = a+b+c+d+e+f+g
i = a*b*c*d*e*f*g

print(a,b,c,d,e,f,g)

#No.6
print(h)

#No.7
print(i)

#No.8
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#No.9
print(d,e,g)

#No.10
print(a,b,c)

#No.11
print(c,f)
#
#j = "hati"
#k = 1
#print("Tetap" +str(j),k)
#
#l = input("Masukan NPM :")
#print("NPM Kamu Adalah : "+l)
#
#m = 10
#n = 2
#o = j + k
#3p = j * k 
#q = j - k
#r = j / k
#s = "10"
#print(o,p,q,r)
#print(int(s))
#print(str(m))
#
#t = 12
#for u in range(t):
#    print("Ini Yang Ke : "+str(u))
#
#while(t <= 15):
#    print("Yap Ini Betul")
#    t = t + 1
#
#v = 12
#if(v==12):
#    print("Dua Belas")
#
#if(v==13):
#    print("Tiga Belas")
#else:
#    print("Dua Belas")
#    
#if(v==11):
#    print("Sebelas")
#elif(v==12):
#    print("Sebelas")
#else :
#    print("Tiga Belas")
#
#w = 10
#x = "10"
#try:
#    y = w+x
#    print(y)
#except TypeError:
#    print("We Are Different")
    
def uji():
    print("Tugas Web Service")

uji()

def uji_param(nama):
    print("Nama saya :"+str(nama))

uji_param(input("Masukan Nama Kamu : "))

def uji_return(a,b):
    r = a + b
    return r

a = 10
b = 50
c = uji_return(a,b)
print(c)

#from fungsi_felix import *
#print(penulisan(int(input("Masukan NPM kamu : "))))

#class Employee:
#   'Common base class for all employees'
#   empCount = 0

#   def __init__(self, name, salary):
#      self.name = name
#      self.salary = salary
#      Employee.empCount += 1
   
#   def displayCount(self):
#     print ("Total Employee %d" % Employee.empCount)

#   def displayEmployee(self):
#      print ("Name : ", self.name,  ", Salary: ", self.salary)


#This would create first object of Employee class"
#emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
#emp2 = Employee("Manni", 5000)
#emp1.displayEmployee()
#emp2.displayEmployee()
#print ("Total Employee %d" % Employee.empCount)

#import belajar
#a = 100
#b = 50

#c = belajar.penambahan(a,b)
#print(c)

#def penanganan_error(a,b):
#    try :
#        c = a+b
#        print(c)
#    except TypeError:
#        print("kita beda")


#No 1
def speakup(npm):
    npm = list(str(npm))
    
    angka1 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ###","4":" ###   ### ","5":" ###### ","6":" ######### ","7":" ###########*","8":" ##########","9":" ########## "}
    angka2 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ###","4":" ###   ### ","5":" ###### ","6":" ######### ","7":" ########### ","8":" ##########","9":" ########## "}
    angka3 = {"0":" ###   ### ","1":" ### ","2":"    ### ","3":" ###","4":" ###   ### ","5":" ###### ","6":" ###       ","7":"        ###  ","8":" ####   ***","9":" ####  #### "}
    angka4 = {"0":" ###   ### ","1":" ### ","2":"    ### ","3":" ###","4":" ###   ### ","5":" ###### ","6":" ###       ","7":"       ###   ","8":" ####   ***","9":" ####  #### "}
    angka5 = {"0":" ###   ### ","1":" ### ","2":" ###### ","3":" ###","4":" ######### ","5":" ###### ","6":" ######### ","7":"      ###    ","8":" ##########","9":" ########## "}
    angka6 = {"0":" ###   ### ","1":" ### ","2":" ###### ","3":" ###","4":"       ### ","5":" ###### ","6":" ######### ","7":"     ###     ","8":" ##########","9":" ########## "}
    angka7 = {"0":" ###   ### ","1":" ### ","2":" ###    ","3":" ###","4":"       ### ","5":" ###### ","6":" ###   ### ","7":"    ###      ","8":" ####   ###","9":"        ### "}
    angka8 = {"0":" ###   ### ","1":" ### ","2":" ###    ","3":" ###","4":"       ### ","5":" ###### ","6":" ###   ### ","7":"   ###       ","8":" ####   ###","9":"        ### "}
    angka9 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ###","4":"       ### ","5":" ###### ","6":" ######### ","7":"  ###        ","8":" ##########","9":" ########## "}
    angka10= {"0":" ######### ","1":" ### ","2":" ###### ","3":" ###","4":"       ### ","5":" ###### ","6":" ######### ","7":" ###         ","8":" ##########","9":" ########## "}
              
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []
    hasil7 = []
    hasil8 = []
    hasil9 = []
    hasil10 = []
    
    for x in npm:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])
        hasil7.append(angka7[x])
        hasil8.append(angka8[x])
        hasil9.append(angka9[x])
        hasil10.append(angka10[x])
    
    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')
    print(*hasil7, sep=' ')
    print(*hasil8, sep=' ')
    print(*hasil9, sep=' ')
    print(*hasil10, sep=' ')

speakup(int(input("Masukan NPM : 117")))

#No 2
def looping(npm):
    hitung = 0
    while(hitung < 78):
        print("Haiiiii, "+str(npm)+" apa kabar?")
        hitung = hitung +1
        
looping(int(input("Masukan NPM : ")))

#No 3
def looping_3_digit(npm):
    hitung = 0
    npm = str(npm)
    bil = npm[4:7]
    
    while(hitung < 15):
        print("Halo, "+bil+" apa kabar?")
        hitung = hitung +1
        
looping_3_digit(int(input("Masukan NPM : ")))

#No 4
def looping_3_digit_terakhir(npm):
    npm = str(npm)
    bil = npm[-3]  
    print("Haiii, "+bil+" apa kabar?")
    
looping_3_digit_terakhir(int(input("Masukan NPM : ")))

#No 5
def down(npm):
    for i in npm:
        print (i)
        
down(input("Masukan NPM : "))


#No 6
def addition(npm):
    jumlah = 0
    for i in npm:
        jumlah += int(i)
    print(str(jumlah)+" Adalah hasil penjumlahan")
    
addition(input("Masukan NPM : "))

#No 7
def multiplication(npm):
    jumlah = 0
    for i in npm:
        jumlah *= int(i)
    print(str(jumlah)+" Adalah hasil perkalian")
    
multiplication(input("Masukan NPM : "))

#No 8
def even():
    npm = [1,1,7,4,0,7,8]
    for i in npm:
        if (i % 2) == 0:
            print("Bilangan Genapnya : "+str(i))
            
even()

#No 9 
def odd():
    npm = [1,1,7,4,0,7,8]
    for i in npm:
        if (i%2)==1:
            print("Bilangan Ganjilnya : "+str(i))
            
odd()

#No 10
def prime(npm):
    npm = str(npm)
    bil = npm[2]
    num = int(bil)
    if num > 1:
        for i in range(2,num):
            if (num%i)==0:
                print("Bukan Bilangan Prima")
                break
            else:
                print("Bilangan Primanya :"+str(num))
    else:
        print("Tidak Ada Bilangan Prima")
prime(int(input("Masukan NPM : ")))