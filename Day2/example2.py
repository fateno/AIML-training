'''
num=1
print('Printing numbers from 1 to 100')
while(num<=100):
    print(num,end = " ")
    num+=1



print ("Conditional while loop")
num=1
while(num<=100):
    print(num,end=" ")
    num+=1 
    #without break, this would be an infinite loop
'''
num=1
#print("Print numbers from 1 to 100 before we get the numbers divisible by 11")
while(num<=100):
    if(num%2==0):
        print ("Even number is ",num)
        num+=1
        continue
        #break
    print(num,end= "\t")
    num+=1
    #num+=1