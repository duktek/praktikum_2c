# Advent
class learn:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def penambahan(self):
        r = self.a + self.b
        return r
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

#No 2
def looping(npm):
    hitung = 0
    while(hitung < 78):
        print("Haiiiii, "+str(npm)+" apa kabar?")
        hitung = hitung +1

#No 3
def looping_3_digit(npm):
    hitung = 0
    npm = str(npm)
    bil = npm[4:7]
    
    while(hitung < 15):
        print("Halo, "+bil+" apa kabar?")
        hitung = hitung +1

#No 4
def looping_3_digit_terakhir(npm):
    npm = str(npm)
    bil = npm[-3]  
    print("Haiii, "+bil+" apa kabar?")

#No 5
def turun(npm):
    for i in npm:
        print (i)

#No 6
def addition(npm):
    jumlah = 0
    for i in npm:
        jumlah += int(i)
    print(str(jumlah)+" Adalah hasil penjumlahan")

#No 7
def multiplication(npm):
    jumlah = 0
    for i in npm:
        jumlah *= int(i)
    print(str(jumlah)+" Adalah hasil perkalian")

#No 8
def even():
    npm = [1,1,7,4,0,7,8]
    for i in npm:
        if (i % 2) == 0:
            print("Bilangan Genapnya : "+str(i))

#No 9 
def odd():
    npm = [1,1,7,4,0,7,8]
    for i in npm:
        if (i%2)==1:
            print("Bilangan Ganjilnya : "+str(i))

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