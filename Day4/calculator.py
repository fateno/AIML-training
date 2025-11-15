def add(num1,num2):
    return num1+num2

def multi(num1,num2):
    return num1*num2

def average(num1,num2):
    return (num1+num2)/2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2


print ("Welcome to our Calculator")
while True: 
    print ('Select operation:' \
    '1=add'
    '2=multiplication' \
    '3=average')
    op=int(input("Enter your operation choice(1-6):\t"))
    if (op==6):
        print("Goodbye")
        break
    fnum=float(input("Enter first number: \t"))
    snum=float(input("Enter second number: \t"))

    if (op==1):
        result=add(fnum,snum)
        print (result)
    elif (op==2):
        result=multi(fnum,snum)
        print (result)
    elif (op==3):
        result=average(fnum,snum)
        print (result)
    elif (op==4):
        result=sub(fnum,snum)
        print (result)
    elif (op==5):
        result=div(fnum,snum)
        print (result)
    else:
        print("Operation is not defined")
        break

