print("set in Python")
set_one={'laptop', 'earphone','ipad'}
print('number of items in set_one are: ',len(set_one))
for item in set_one: 
    print(item, end=" ")

'''
set_one.clear()
print('After clear, number of items in set_one are: ',len(set_one))
for item in set_one: 
    print(item, end=" ")
'''
print ("\n\n removing earphone")
set_one.remove('earphone')
print('\n After removing one item from set: ',len(set_one))
for item in set_one: 
    print (item, end=" ")

print ("Set union example: ")
set_one={100,200,300,500,700,900,150}
set_two={100,400,700,1000,1300}
set_three={1,2,3}

print(f'set_one: {len(set_one)} numbers')
print (set_one)
print(f'set_two: {len(set_two)} numbers')
print (set_two)
print (f'set_three: {len(set_three)} numbers. {set_three}')

print ("Union of three sets")
unionset=set_one.union(set_two,set_three)
print(f'union set: {len(unionset)} numbers')
print (unionset)