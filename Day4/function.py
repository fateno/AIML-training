'''
def welcome(user):
    print("Welcome to function, %s" %user)
    print("This is our first function")

user= input("What's your name? ")
welcome(user)
'''

def add(num1,num2):
    return num1+num2

fnum=int(4)
snum=int(5)
tryRerun=add(fnum,snum)
print (tryRerun)

tryRerun2=add(int(5),int(3))
print (tryRerun2)