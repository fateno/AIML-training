import calc
import ex3_module_recap

first_num=float(input('Enter first number: '))
second_num=float(input('Enter second number: '))

print (f"Addition for {first_num},{second_num} = \t", calc.add(first_num,second_num))
print (f"Average for {first_num},{second_num} = \t", calc.avg(first_num,second_num))

ex3_module_recap.findwinner()