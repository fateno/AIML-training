#lambda - one liner function 

def add(a,b):
    total= a+b
    return total

result = add(12,15)
print (result)

print ("Lambda example: \n")
add = lambda a,b:a+b 
multi = lambda a,b:a*b
div=lambda a,b:a/b
sayHi=lambda user: print("User: %s" %user)

print (f"Try lambda add for 10 and 5: {add(10,5)}")
print (f"Try lambda multi for 10 and 5: {multi(10,5)}")
print (f"Try lambda div for 10 and 5: {div(10,5)}")

#user = (input("What's your name?"))
#sayHi(user)
#print (f"Oops, I forgot to say hi  {sayHi(user)}")

check_odd = lambda n:"Odd Number" if n%2==1 else 'Even Number'
num1=int(input('Enter number to check odd or even:\t'))
print (check_odd(num1))