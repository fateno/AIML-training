#import math 
#import random

#print('Your lucky number from 1 to 100 is: ',random.randint(1,100))

#To check function inside module

import math 
import inspect 
functions = inspect.getmembers(math, inspect.isbuiltin)
print(functions)

#for n, func in functions: 
#    print(n)

print ('Sin 90 is ',math.sin(90))
print('Cos90 is: ',math.cos(90))
print ('Tan90 is ',math.tan(90))

deg=int(input('Degree to find out cos '))
print(f'Cos {deg} is: ',math.cos(deg))