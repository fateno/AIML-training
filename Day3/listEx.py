emps=['Smiski', 'Sonny', 'Crybaby', 'Dimoo', 'Labubu']
print("Number of Employees: ", len(emps))
for emp in emps: 
    print(emp,end=" ")

'''
emps.sort() #ascending order
print("List after sorting")
for e in emps:
    print(e, end=" ")

#reverse example
#listName.reverse()
emps.reverse()
print('\n Employees in Descending Order')
for e in emps: 
    print(e, end=" ")

newEmp=input("\n Enter employee name to add to the list:\t")
#insert(index,item): This will add item at given index
pos=int(input("enter position where you want to insert inside list:\t"))
emps.insert(pos,newEmp)
#emps.append(newEmp)
print("\n Updated number of employees: ",len(emps))
for emp in emps: 
    print(emp, end="\n")

#remove
delEmp=input("\n Enter employee name to remove from the list:\t")
#insert(index,item): This will add item at given index
#pos=int(input("enter position where you want to insert inside list:\t"))
#emps.insert(pos,newEmp)
#emps.append(newEmp)
if delEmp in emps: 
    emps.remove(delEmp)
    print(f"Number of employees after deleting {delEmp} in list are: ",len(emps))
    for emp in emps: 
        print(emp,end=" ")
    print("\n Updated number of employees: ",len(emps))

else: 
    print(f'No such item {delEmp} in employee list')
'''

print ("\n Pop example")

del_index=int(input("Enter index number to pop item:\t"))
print('Pop result: ',emps.pop(del_index))

print("Number of employees after pop() are: ",len(emps))
for emp in emps: 
    print (emp, end="\n") 
count=len(emps)
print('\n First element: ',emps[0])
print('\n Second last element: ',emps[-2])
print('\n Last element: ',emps[count-1])

