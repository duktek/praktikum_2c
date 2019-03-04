#1
_variableName0 = "value"

#2
_variableName1 = input("Enter your name:")
print("Hello, " + _variableName1)

#3
#Addition :
x = 5
y = 3
print(x + y)

#Subtraction :
x = 5
y = 3
print(x - y)

#Multiplication :
x = 5
y = 3
print(x * y)

#Division :
x = 5
y = 3
print(x / y)

#Modulus :
x = 5
y = 3
print(x % y)

#Equal :
x = 5
y = 3
print(x == y)

##Non Equal :
x = 5
y = 3
print(x != y)

##Greater than :
x = 5
y = 3
print(x > y)

##Less than :
x = 5
y = 3
print(x < y)

## Greater than or equal to :
x = 5
y = 3
print(x >= y)

## Less than or equal to :
x = 5
y = 3
print(x <= y)


#4
##while :
i = 1
while i < 6:
    print(i)
    i += 1

##for :
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#5
##Contoh kondisi didalam kondisi :
gaji = 10000000
berkeluarga = True
punyaRumah = True

if gaji > 3000000:
    print ("Gaji sudah diatas UMR")
    if berkeluarga:
        print ("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print ("Tidak perlu ikutan asuransi")
    if punyaRumah:
        print ("wajib bayar pajak rumah")
    else:
        print ("tidak wajib bayar pajak rumah")
else:
    print ("Gaji belum UMR")

##Contoh kondisi :
umur = 20
if umur > 18:
    print ("Sudah beranjak dewasa")
else:
    print ("Masih dibawah umur")

#7
x = 0
try:
    x = 1 / 0
except Exception as e:
    print (e)

print(x + 1)

#maka akan muncuk :
#division by zero
#1

