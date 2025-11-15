'''
user=input("Who are you? \t")
age=int(input("how old are you? \t"))

if (user=="cat"):
    print ("hello cat")
    name=input("whats your name, cat?\t")
    if (age>=18):
        print ("Wow you can vote, %s. You go glen coco" %name)
    else: 
        print ("Wait first ah")
elif (age>=18):
    print ("can vote but you no cat")
elif (age<=18):
    print("not cat, not old enough, aiya")
else: 
    print ("where's cat? i want cat.")

print ("************")

marks = int(input("Enter marks percentage (without '%' sign)"))
if (marks<=30): 
    print("Failed in exam. try again")
else: 
    print("Good job, you passed")
'''

print ("***********")
accessCode=input("Enter access code \t")
if (accessCode!="smiski"):
    print ("Invalid code")
else: 
    print("good job")