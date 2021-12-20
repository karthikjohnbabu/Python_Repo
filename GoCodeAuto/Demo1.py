class Account:
    def __init__(self,intial_balance):
        self.__balance=intial_balance
    def getbalance(self):
        #validation or Authentications
        return self.__balance
    def deposit(self,amount):
        #Validations/Authentications
        self.__balance=self.__balance+amount
    def withdraw(self,amount):
        #validation and Authentications
        self.__balance=self.__balance-amount

