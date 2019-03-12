#No.1
print (1174072%3)
print("+++  +++  +++++++++++ +++   +++  +++++++++  +++++++++++  +++++++++")
print("+++  +++  ++++++++++  +++   +++  +++   +++  ++++++++++   +++++++++")
print("+++  +++        +++   +++   +++  +++   +++        +++          +++")
print("+++  +++       +++    +++   +++  +++   +++       +++           +++")
print("+++  +++      +++     +++++++++  +++   +++      +++      +++++++++")
print("+++  +++     +++            +++  +++   +++     +++       +++      ")
print("+++  +++    +++             +++  +++   +++    +++        +++      ")
print("+++  +++   +++              +++  +++++++++   +++         +++++++++")
print("+++  +++  +++               +++  +++++++++  +++          +++++++++")

#no.2
npm  = input("Masukan NPM :")
hitung = 0
while(hitung <=72):
    print("Halo, " + str(npm) + " Apa Kabar?")
    hitung += 1

#no.3
npm = input("masukan NPM : ")
ulang = 1
while(ulang <= 72):
    print("Halo, "+str(npm[4:7])+" apa kabar?")
    ulang += 1


#no.4
npm = input("Input : ")
print("Halo, "+str(npm[-3])+" apa kabar?")

#no.5
a = 1
b = 1
c = 7
d = 4
e = 0
f = 7
g = 2

npm = [a,b,c,d,e,f,g]

for n in npm:
    print(n, end ="")
    print()

#No.6

print(a+b+c+d+e+f+g)

#No.7

print(a*b*c*d*e*f*g)

#No.8

for n in npm:
    print(n)

#No.9

for n in npm:
    if(n % 2 == 0):
        if(n != 0):
            print(n, end ="")

print()        

#No.10

for n in npm:
    if(n % 2 != 0):
        print(n, end ="")

print()

#no.11
for n in npm:
    if(n % 1 != 0):
        print(n, end ="")

print()

#Pemahaman Teori
def Tugas():
    print("Kerjakan Tugas")

Tugas()


def Tugas(inputanTugas):
    return inputanTugas


output = Tugas("Kembali Nama Fungsi")
print(output)


#2
import math
print("Nilai: ", math.pi)

#3
class Jurusan:
    jumlahMahasiswa = 0

    def __init__(self, prodi, nama):
        self.prodi = prodi
        self.nama = nama
        Jurusan.jumlahMahasiswa +=1

    def tampilkanProfil(self):
        print("Prodi :", self.prodi)
        print("Nama :", self.nama)
        print()

mahasiswa1 = Jurusan("TI", "FernandoLS")
mahasiswa2 = Jurusan("TI", "bebas")

mahasiswa1.tampilkanProfil()
mahasiswa2.tampilkanProfil()

print("Jumlah Mahasiswa  ", Jurusan.jumlahMahasiswa)

#4
from Jurusan import Jurusan

mhs1 = Jurusan("TI", "Fernandols")
mhs2 = Jurusan("TI", "bebas")

mhs1.tampilkanProfil()
mhs2.tampilkanProfil()

print("Total mahasiswa ", Jurusan.jumlahMahasiswa)

#5
from kalkulator import Penambahan

hasil = Penambahan(20, 10)
print(hasil)


#6
from folder import kalkulator

a=120
b=60

hasil1=kalkulator.Penambahan(a,b)
hasil2=kalkulator.Pengurangan(a,b)
hasil3=kalkulator.Perkalian(a,b)
hasil4=kalkulator.Pembagian(a,b)

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)

#7
from folder.Jurusan import Jurusan

mhs1 = Jurusan("TI", "fernandols")
mhs2 = Jurusan("TI", "bebas")

mhs1.tampilkanProfil()
mhs2.tampilkanProfil()

print("Total mahasiswa  ", Jurusan.jumlahMahasiswa)

#Ketrampilan Pemrograman
#1
def printNPM(npm):

    npm = list(str(npm))

    angka1 = {"0":" ++++++ ", "1":"  ++", "2":" +++++++ ", "3":" +++++++ ", "4":"     +++", "5":"++++++++", "6":" +++++++ ", "7":"+++++++++", "8":" +++++++ ", "9":" +++++++ "}
    angka2 = {"0":"+++  +++", "1":"++++", "2":"++    +++", "3":"++    +++", "4":"   +++++", "5":"++      ", "6":"+++      ", "7":"     +++ ", "8":"+++   +++", "9":"++    +++"}
    angka3 = {"0":"+++  +++", "1":" +++", "2":"     +++ ", "3":"    ++++ ", "4":" +++  ++", "5":"+++++++ ", "6":"++++++++ ", "7":"    +++  ", "8":" +++ +++ ", "9":"++    +++"}
    angka4 = {"0":"+++  +++", "1":" +++", "2":"    +++  ", "3":"    +++  ", "4":"++++++++", "5":"     +++", "6":"+++   +++", "7":"   +++   ", "8":" +++ +++ ", "9":" ++++++++"}
    angka5 = {"0":"+++  +++", "1":" +++", "2":"  +++    ", "3":"++    +++", "4":"     +++", "5":"++   +++", "6":"+++   +++", "7":"  +++    ", "8":"+++   +++", "9":"      +++"}
    angka6 = {"0":" ++++++ ", "1":" +++", "2":"+++++++++", "3":" +++++++ ", "4":"     +++", "5":" ++++++ ", "6":" +++++++ ", "7":" +++     ", "8":" +++++++ ", "9":" +++++++ "}

    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []

    for x in npm:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])

    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')

printNPM(input("Masukan NPM anda: "))

#2
def printNPM(npm):
    ulang = 1
    sampai = int(npm[5:7])
    while(ulang <= sampai):
        print("Halo, "+str(npm)+" apa kabar?")
        ulang += 1

printNPM(input("Harap MAsukan NPM: "))        

#3
def printNPMTigaNomor(npm):
    ulang = 1
    sampai = list(map(int, npm[4:7]))
    sampai = sum(sampai)    
    while(ulang <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?")
        ulang += 1

printNPMTigaNomor(input("Masukan NPM anda: "))

#4
def printNPMAngkaUruttiga(npm):
    print("Output:")
    print("Halo, "+str(npm[-3])+" apa kabar?")

printNPMAngkaUruttiga(input("Input: "))

#5
def printNPMBerbaris(npm):
    npm = list(map(int, npm))  
    for n in npm:
        print(n)

printNPMBerbaris(input("Masukan NPM anda: "))

#6
def printPenjumlahanNPM(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil += x

    print(hasil)

printPenjumlahanNPM(input("Masukan NPM anda: "))

#7
def printPerkalianNPM(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil *= x

    print(hasil)

printPerkalianNPM(input("Masukan NPM anda: "))

#8
def printAngkaGenapNPM(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end = "")

printAngkaGenapNPM(input("Masukan NPM anda: "))

#9
def printAngkaGanjilNPM(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 != 0):
            print(n, end = "")

printAngkaGanjilNPM(input("Masukan NPM anda: "))

#10
def printAngkaPrimaNPM(npm):
    npm = list(map(int, npm))
    prima = []
    for n in npm:
        isPrime = True
        if n == 0 or n == 1:
            isPrime = False
        for x in range(2, n):
            if n % x == 0:
                isPrime = False
        if isPrime:
            prima.append(n)

    for p in prima:
        print(p, end = "")

printAngkaPrimaNPM(input("Masukan NPM anda: "))

#11

#12

#Ketrampilan Penanganan Error
#Jawaban No. 1
def panggil(nama):
    try:
        print("Hallo, "+str(nama))
    except:
        print("Terjadi kesalahan") 

panggil(input("Masukan nama anda: ")) 