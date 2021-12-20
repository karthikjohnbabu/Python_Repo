class Calculator:
    num = 100 #class variable
    4

    def __init__(self,a,b):
        self.firstnumber=a
        self.secondnumber=b
        print("Am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstnumber+self.secondnumber+Calculator.num

obj =Calculator(2,3)#syntax to create objects in python
obj.getData()
print(obj.Summation())

