'''
phyMarks=int(input("Enter marks obtained in Physics"))
chemMarks=int(input("Enter marks obtained in Chemistry"))
mathsMarks=int(input("Enter marks obtained in Maths"))

if (mathsMarks>=55) and (phyMarks>=55) and (chemMarks>=60):
    print ("You are eligible to sit for pre exam")
else: 
    print ("Try again, son")


idProof = input ("Enter id proof you have \t")
if (idProof == "passport") or (idProof == "IC") or (idProof == "driving license"): 
    print (f"Valid Id {idProof} we accept here")
    print ("valid ID %s we accept welcome friend" %idProof)
else: 
    print ("Sorry mate, %s is not valid here" %idProof)

    '''

mathMarks = int(input("Enter marks obtained in Maths: \t"))
gapYear = int(input("Enter year gap if any otherwise 0: \t"))
if (mathMarks>=55) and (gapYear!=0): 
    print ("Not eligible for exam?")
else: 
    print ("Eligible yay")