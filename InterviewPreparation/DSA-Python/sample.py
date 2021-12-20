class Customer:
    ''' This class is developed by karthik and describes Banking application '''
    bankname= 'SBI-BANK' #Static Variable.
    def __init__(self,name,balance=0.0): # instance method
        self.name= name #instance variable
        self.balance= balance #instance variable
    def deposit(self,amount):#instance method
        self.balance=self.balance+amount
        print('After deposit balance is:',self.balance)
    def withdrawl(self,amount): #instance method
        if amount>self.balance:
            print('Insufficient funds, cannot perform this operation')
        else:
            self.balance=self.balance-amount
            print('After withdrawl balance is:',self.balance)
print('Welcome to', Customer.bankname)
name=input('Enter your name:')
c=Customer(name)
while True:
    print('D-Deposit\nW-Withdrawl\nE-Exit')
    option=input('Choose your option:')
    if option.lower()=='d':
        amount=float(input('Enter amount to deposit:'))
        c.deposit(amount)
    elif option.lower()=='w':
        amount = float(input('Enter amount to withdraw:'))
        c.withdrawl(amount)
    elif option.lower()=='e':
        print('Thanks for Banking with us, have a good Day')
        break
    else:
        print('Your option is invalid, Please choose valid option')











