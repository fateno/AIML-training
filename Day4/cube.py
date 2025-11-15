'''
print("Write a function to find out the cube of given number")

def cube(num):
    return (num*num*num)

num = int(input("Please input number for cube operation:\t "))
result = cube(num)
print (f"Result for cube of {num} is {result}")

print ("Shorter version")
print(f'Result of cube of {num} is', cube(num))
'''
print ("Independent exercise: Write a function to find out bonus of a given salary")

def calcBonus(salary):
    return 0.1*salary

salary = float(input("Please key in your salary: \t"))
print (f"Your bonus for salary of {salary} is", calcBonus(salary))
print ('Your take home salary (includes bonus) is', calcBonus(salary)+salary)