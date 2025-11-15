# import random

# print('Random Number from 1 to 1000')

# print(random.randint(1,10))

import random
def findwinner():
    name=input('Enter Your name: ')
    luckyNumber=random.randint(1,10)
    print(f'Welcome Mr.\\Ms { name} Cuppon Number: {luckyNumber}')
    if(luckyNumber==1):
        print('you have won Proton LX-65 Car')
    elif(luckyNumber==3):
        print('you have won a IPad')  
    elif(luckyNumber==9):   
      print('you have won a IPhone')  
    else:
        print('Better Luck Next Time') 
     
