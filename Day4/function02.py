'''
def info(id,name,city="KL"):
    #default value for city is KL 
    print(f"Details as follows: \n ID: {id} Name:{name} City:{city}")

info(1,'Faten','Kuching')
info(2,'Sofea')

#Create a single method that can add 2,3,4 numbers and return correct total 

def add(n1=0,n2=0,n3=0,n4=0,n5=0):
    return n1+n2+n3+n4+n5 

print(f"result is ",add(30,40,50))

'''

def add(*args):
    return min(args)

print('min of 1,10,11,34 is: \t', add(1,10,11,34))

