#Jawaban No. 1
def variableNPM(npm):
    npm = list(str(npm))
    
    row1 = {"0":" ###### ", "1":"  ##", "2":" ####### ", "3":" ####### ", "4":"     ###", "5":"########", "6":" ####### ", "7":"#########", "8":" ####### ", "9":" #######"}
    row2 = {"0":"###  ###", "1":"####", "2":"##    ###", "3":"##    ###", "4":"   #####", "5":"##      ", "6":"###      ", "7":"     ### ", "8":"###   ###", "9":"##    ###"}
    row3 = {"0":"###  ###", "1":" ###", "2":"     ### ", "3":"    #### ", "4":" ###  ##", "5":"####### ", "6":"######## ", "7":"    ###  ", "8":" ### ### ", "9":"##    ###"}
    row4 = {"0":"###  ###", "1":" ###", "2":"    ###  ", "3":"    #### ", "4":"########", "5":"     ###", "6":"###   ###", "7":"   ###   ", "8":" ### ### ", "9":" ########"}
    row5 = {"0":"###  ###", "1":" ###", "2":"  ####   ", "3":"##    ###", "4":"     ###", "5":"##   ###", "6":"###   ###", "7":"  ###    ", "8":"###   ###", "9":"      ###"}
    row6 = {"0":" ###### ", "1":" ###", "2":"#########", "3":" ####### ", "4":"     ###", "5":" ###### ", "6":" ####### ", "7":" ###     ", "8":" ####### ", "9":" ####### "}
              
    scan1 = []
    scan2 = []
    scan3 = []
    scan4 = []
    scan5 = []
    scan6 = []
              
    for x in npm:
        scan1.append(row1[x])
        scan2.append(row2[x])
        scan3.append(row3[x])
        scan4.append(row4[x])
        scan5.append(row5[x])
        scan6.append(row6[x])
    
    print(*scan1, sep='    ')
    print(*scan2, sep='    ')
    print(*scan3, sep='    ')
    print(*scan4, sep='    ')
    print(*scan5, sep='    ')
    print(*scan6, sep='    ')
    
variableNPM(input("NPM : "))

#Jawaban No. 2
def variableNPM(npm):
    i = 1
    dua = int(npm[5:7])
    while(i <= dua):
        print("Halo, "+str(npm)+" apa kabar?")
        i += 1

variableNPM(input("NPM : "))        

#Jawaban No. 3
def variableNPM(npm):
    i = 1
    tiga = list(map(int, npm[4:7]))
    sampai = sum(tiga)    
    while(i <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?")
        i += 1
    
variableNPM(input("NPM : "))

#Jawaban No. 4
def variableNPM(npm):
    print("Halo, "+str(npm[-3])+" apa kabar?")
    
variableNPM(input("NPM : "))

#Jawaban No. 5
def variableNPM(npm):
    npm = list(map(int, npm))  
    for x in npm:
        print(x)
        
variableNPM(input("NPM : "))

#Jawaban No. 6
def variableNPM(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil += x
    
    print(hasil)
    
variableNPM(input("NPM : "))
    
#Jawaban No. 7
def variableNPM(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil *= x
    
    print(hasil)
    
variableNPM(input("NPM : "))

#Jawaban No. 8
def variableNPM(npm):
    npm = list(map(int, npm))
    for x in npm:
        if(x % 2 == 0):
            if(x != 0):
                print(x, end = "")
    
variableNPM(input("NPM : "))

#Jawaban No. 9
def variableNPM(npm):
    npm = list(map(int, npm))
    for x in npm:
        if(x % 2 != 0):
            print(x, end = "")
    
variableNPM(input("NPM : "))

#Jawaban No. 10
def variableNPM(npm):
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
    
variableNPM(input("NPM : "))
