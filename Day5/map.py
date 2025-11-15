numbers = [10,25,30,40,2,1]
double_num = list(map(lambda x:2*x, numbers))
print ('Original list')
for num in numbers: 
    print(num, end=" ")

print ('\nDouble list')
for num in double_num: 
    print (num, end=" ")

print ("\n\nFilter example\n")
numbers = [10,25,30,40,2,1]
print ('Original list')
for num in numbers: 
    print(num, end=" ")

double_num = list(filter(lambda x:x%2==0, numbers))
print ('\nEven numbers from list')
for num in double_num: 
    print (num, end=" ")