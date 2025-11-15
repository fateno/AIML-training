class Account:
    def __init__(self,ac_holder,balance):
        self.ac_holder=ac_holder
        self.balance=balance
    
    def deposit(self, amount):
        self.balance+=amount
        print("Balance after deposit: ",self.balance)

    def withdraw(self,amount):
        if (self.balance>=amount):
            self.balance-=amount
            print("Balance after withdrawal: ",self.balance)
        else: 
            print("Balance is not sufficient")
            print("Transaction failed.")

    def display(self):
        print(f'Owner:{self.ac_holder}, Balance:{self.balance}')

'''
ac1=Account('sameer',50000)
ac2=Account('Chang',14000)
ac1.display()
ac2.display()
wamount=float(input('Enter amount to withdraw: '))
ac1.withdraw(wamount)
ac1.display()
'''
ac=Account('Sam',15000)
ac.display()
print('Please choose \n 1. Deposit 2. Withdraw 3. Balance Info')
op=int(input())

if (op==1):
    damount=float(input('Enter amount to deposit: '))
    ac.deposit(damount)
elif (op==2):
    damount=float(input('Enter amount to withdraw: '))
    ac.withdraw(damount)
elif (op==3):
    ac.display()
else: 
    print ("Wrong choice.")