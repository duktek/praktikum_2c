# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x = 5
y = "John"
print(x)
print(y)

x1 = 4 
x1 = "Sally"
print(x1)
 
x2 = "awesome"
print("Python is " + x2)

x3 = "Python is "
y3 = "awesome"
z3 =  x3 + y3
print(z3)

x4 = 5
y4 = 10
print(x4 + y4)

x5 = 1    # int
y5 = 2.8  # float
z5 = 1j   # complex

print(type(x5))
print(type(y5))
print(type(z5))

xint = 1
yint = 35656222554887711
zint = -3255522

print(type(xint))
print(type(yint))
print(type(zint))

xflt = 1.10
yflt = 1.0
zflt = -35.59

print(type(xflt))
print(type(yflt))
print(type(zflt))

xcom = 3+5j
ycom = 5j
zcom = -5j

print(type(xcom))
print(type(ycom))
print(type(zcom))


x6 = int(1)   # x6 menjadi 1
y6 = int(2.8) # y6 menjadi 2 
z6 = int("3") # z6 menjadi 3

x7 = float(1)     # x7 menjadi 1.0
y7 = float(2.8)   # y7 menjadi 2.8
z7 = float("3")   # z7 menjadi 3.0
w7 = float("4.2") # w7 menjadi 4.2

x8 = str("s1") # x8 menjadi 's1'
y8 = str(2)    # y8 menjadi '2'
z8 = str(3.0)  # z8 menjadi '3.0'

a = "Hello, World!"
print(a[1])

b = "Hello, World!"
print(b[2:5])

a = " Hello, World! "
print(a.strip()) # menampilkan "Hello, World!"

a = "Hello, World!"
print(len(a))

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

print("Enter your name:")
x = input()
print("Hello, " + x)

x9 = 5
y9 = 3

print(x9 + y9)


x10 = 5
y10 = 3

print(x10 - y10)

x11 = 5
y11 = 3

print(x11 * y11)

x12 = 12
y12 = 3

print(x12 / y12)

x13  = 12
y13 = "3"

x14 = str(x13)

y14 = int(y13)

print(x14)
print(y14)

i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
try:
  print(x15)
except NameError:
  print("Variable x15 tidak sesuai")
except:
  print("Terjadi Error")
