employee={"id":1,
          "name":"Sam",
          "salary":5500.00
          }


print("employee details as follows: ")
for key,value in employee.items():
        print(key,"->",value)

#adding key
employee["city"]="Muscat"
print('\n Dictionary after adding City\n')

print("employee details as follows: ")
for key,value in employee.items():
        print(key,"->",value)

del employee["salary"]
print("employee details as follows: ")
for key,value in employee.items():
        print(key,"->",value)

print("All keys from employee")
for k in employee.keys():
        print (k,end="\t")

print("\n All values from employee \n")
for v in employee.values():
        print(v,end="\t")

print("\nKey:Value\n")
for k,v in employee.items():
        print (k,":",v)


    