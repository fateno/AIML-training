print ("Tuple exercise")
'''subjects=('python', 'java', 'dotnet', 'sql','power bi')
print('All subjects are: \n')

for sub in subjects:
    print(sub, end="\t")

subjects=('python', 'java', 'dotnet', 'sql','power bi')
print('All subjects are: \n')

for sub in subjects:
    print(sub, end="\t")



numbers=(1,2,3,4,10,2,3,2,3,5,50,1)
print('Total numbers in tuple: ',len(numbers))
print (numbers)
for num in numbers:
    print(num,end="\n")

print ("Finding number")
search_num=int(input('\n Enter number to find out which index:\t'))
if search_num in numbers: 
    print(f'Index of {search_num} is: \t',numbers.index(search_num))
else: 
    print(f'No such number {search_num} in our tuple')

search_num=int(input('\nEnter number to find the frequency:\t'))
if search_num in numbers: 
    print(f'Frequency of {search_num} is:{numbers.count(search_num)} times')
else: 
    print(f'No such number {search_num} in our tuple')

    '''

numbers=(10,20,30,40)
total=sum(numbers)
print("Sum of numbers from tuple: ",total)