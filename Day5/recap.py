def salBonus(salary):
    return salary*0.10

my_sal=float(input("Enter salary to find out bonus: \t"))
bonus=salBonus(my_sal)
print(f'Salary {my_sal} bonus: {bonus}')
print(f'Salary after bonus =\t',(my_sal+bonus))