class Calculator:
    num = 100 # class Variables
    #variables defined inside construtor are called instance variables

    #default Constructor
    def __init__(self,a,b):
        self.firstNumber=a
        self.secondNumber=b
        print('I am called automatically when object is created')

    def getData(self):
        print("I am now Executing as method is class")

    def Summation(self):
        return self.firstNumber+self.secondNumber+Calculator.num

obj=Calculator(2,3)
print(obj.Summation())