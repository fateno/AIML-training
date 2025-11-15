# try: 
#     fnum=float(input('Enter first number: '))
#     snum=float(input('Enter second number: '))
#     result = fnum/snum

#     print(f'Result:{round(result,4)} after dividing {fnum} by {snum}')

# except Exception as e: 
#     print ("Error", e)

# finally: 
#     print ("Goodbye")

from ourpack import calc
calc.test()
while True: 
    try: 
        fnum=float(input('Enter first number: '))
        snum=float(input('Enter second number: '))

        result=calc.div(fnum,snum)
        #result = add(fnum,snum)
        print (f"Result of div: {result}")

    except ZeroDivisionError as e: 
        print ("Error!", e)
    except Exception as e: 
        print ("Error!", e)

    choice=input('Do you want to continue. - y or n: ')
    if (choice!= 'y'):
        print ('Bye')
        break