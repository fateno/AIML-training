#write function to check if number is odd or even 

def even(input): 
    if (input % 2) == 0: 
        print (f"{input} is even number.")
    else: 
        print (f"{input} is odd number.")

num=int(input("Please input a number: "))
even(num)