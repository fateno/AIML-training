import math
import random


#num=int(input('Enter number to find our square root'))
#print(round(math.sqrt(num),2))
#round is to round off to 2 decimal places

#print ("Random number from 1 to 1000")
#print (random.randint(1,1000))

def findwinner():
    name=input("Enter your name: ")
    luckyNumber = random.randint(1,10)
    print (f'Welcome Mr.\\Ms {name} Coupon number: {luckyNumber}')
    if (luckyNumber==1):
        print ("You have won a car")
    elif (luckyNumber==3):
        print ("You have won an iPad")
    elif (luckyNumber == 9):
        print ("You have won an iPhone")
    else: 
        print("Better luck next time")

# import datetime 


# print('\n---Calling---\n')
# print(datetime.date.today())

# cttime=datetime.datetime.now().time()
# formatedtime=datetime.datetime.now().strftime('%I %M %S %p')

# print('Current time', cttime)
# print('Formated time', formatedtime)