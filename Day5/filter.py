our_list=[4,2,5,6,7,3,1,10]
#double_num = list(filter(lambda x:x%2==0, numbers))
findNumber=list(filter(lambda x:x<5, our_list))

print (f"Original list is : {our_list}")
print ("Numbers smaller than 5 are:")
for num in findNumber: 
    print (num, end=" ")

print ("Second example")
student_marks={'Smiski': 50, 
               'Sonny':40, 
               'Crybaby':35,
               'Faten':80, 
               'Sofea':90}
print (student_marks)
for v in student_marks.values(): 
    print (v, end="\n")
pass_students=dict(filter(lambda item:item[1]>=40,student_marks.items()))
print("Passed student")
print(pass_students)

sort_pass_students=sorted(pass_students.items(), key=lambda x:x[1])
print ('Passed Students list: ')
for k,v in pass_students.items():
    print(f'Name: {k} -> marks: {v}')

print ('Ascending order')
sort_pass_students=dict(sorted(pass_students.items(),key=lambda x:x[0]))
#x[1] - sort based on marks 
#x[0] - sort based on names
for k,v in sort_pass_students.items(): 
     print(f'Name: {k} -> marks: {v}')

print ('Descending order')
sort_pass_students=dict(sorted(pass_students.items(),key=lambda x:x[0], reverse=True))
#x[1] - sort based on marks 
#x[0] - sort based on names
for k,v in sort_pass_students.items(): 
     print(f'Name: {k} -> marks: {v}')