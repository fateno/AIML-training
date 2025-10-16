def findMax(num1, num2, num3): 
    max_num=max(num1, num2, num3)
    print (f"The largest number is: {max_num}")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the first number: "))
num3 = float(input("Enter the first number: "))

while True: 
    try:
        if num1 and num2 and num3: 
            print ("Finding largest number: ")
            findMax(num1,num2,num3)
        else: 
            print ("Please input three numbers.")
            choice= input(print("Do you want to continue? (y/n)"))
            if (choice != 'y'):
                print ("Bye")
                break
    except Exception as e: 
        print ("Error: ", e)
    
