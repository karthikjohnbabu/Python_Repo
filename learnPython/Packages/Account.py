class Account:
    def __init__(self,intial_balance):
        self.__balance=intial_balance
    def getbalance(self):
        #validating or authentication
        return self.__balance
    def deposit(self,amount):
        #validations and authentication
        self.__balance= self.__balance+amount
    def withdraw(self,amount):
        #validations and authentications
        self.__balance=self.__balance-amount