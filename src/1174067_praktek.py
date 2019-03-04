#1
print(1174067%3)
#mod3 = 1

print("  ++    ++  +++++++++     +++   ++++++    +++++++  +++++++++")
print("++++  ++++  ++++++++    +++++  +++  +++  +++       ++++++++ ")
print(" +++   +++      +++   +++ +++  +++  +++  +++           +++  ")
print(" +++   +++     +++   ++++++++  +++  +++  ++++++++     +++   ")
print(" +++   +++    +++         +++  +++  +++  +++   +++   +++    ")
print(" +++   +++   +++          +++   ++++++    +++++++   +++     ")

#2
NPM = input("NPM : ")
jumlah = 0
while(jumlah <= 67):
    print("Hallo, " + str(NPM) + " Apa kabar?")
    jumlah = jumlah +1
        
#3    
NPM = input("NPM : ")
jumlah = 0
while(jumlah <= 6):
    print("Halo, " + str(NPM[4:7]) + " Apa kabar?")
    jumlah = jumlah +1 

#4
NPM = input("NPM : ")
print("Hello, " + str(NPM[-3]) + " Apa kabar?")

#5
a = int(NPM[0])
b = int(NPM[1])
c = int(NPM[2])
d = int(NPM[3])
e = int(NPM[4])
f = int(NPM[5])
g = int(NPM[6])
NPM = [a,b,c,d,e,f,g]

for x in NPM:
    print(x, end="")
print()

#6
print(a + b + c + d + e + f + g)

#7
print(a * b * c * d * e * f * g)

#8
for x in NPM:
    print(x)
    
#9
for x in NPM:
    if(x % 2 == 0):
        if(x != 0):
            print(x, end ="")
print()  
#10
for x in NPM:
    if(x % 2 != 0):
        print(x, end ="")

print()

#11
print(a,b,c,g)
