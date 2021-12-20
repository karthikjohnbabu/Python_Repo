#Mini Bank Application.
class Customer:
    '''This class was developved by karthik and describes Bank operations'''
    bankname='SBI-BANK'#Static variable
    def __init__(self,name,balance=0.0):#instance method
        self.name=name #instance variable
        self.balance=balance #instance variable
    def deposit(self,amount):#instance method
        self.balance=self.balance+amount
        print('After deposit, balance:',self.balance)
    def withdraw(self,amount):#instance method
        if amount >self.balance:
            print('Insufficient funds, cannot perform this operation')
        else:
            self.balance=self.balance-amount
            print('After withdraw ,balance is:',self.balance)
print('Welcome to ',Customer.bankname)
name=input('Enter your name:')
c=Customer(name)
while True:
    print('D-Deposit\n W-withdraw\n E-exit')
    option=input('Choose your option:')
    if option.lower()=='d':
        amount=float(input('Enter amount to deposit:'))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input('Enter amount to withdraw:'))
        c.withdraw(amount)
    elif option.lower()=='e':
        print('Thanks for banking with us, have a good day')
        break
    else:
        print('Your option is invalid, please choose a valid option')









