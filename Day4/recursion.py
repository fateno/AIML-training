#factorial example 
'''
def factorial(num): 
    if ((num==0)or(num==1)):
        return 1
    else: 
        #num=num-1
        print ("num is",num)
        return num*factorial(num-1)
    
    
num=int(input('Enter a number to find out factorial: '))
print(f'Factorial of {num} is {factorial(num)}')
'''
def convert(inch): 
    return (inch*2.5)

inch = float(input('Enter number in inches: \t'))
print (f"{inch}inches is {convert(inch)} cm")