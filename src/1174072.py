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





