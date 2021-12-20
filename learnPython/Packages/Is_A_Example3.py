#example for using super keyword
class Person:
    def __init__(self,name,age):##Karthik John Babu
        self.name= name
        self.age=age
    def eatndrink(self):
        print('Eat Briyani and drink coke')
class Employee(Person):
    def __init__(self,name,age,eno,esal):##Karthik Babu
        #self.name=name
        #self.age=age
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def work(self):
        print('Coding Python program')
    def empInfo(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.esal)
e=Employee('Karthik john Babu ','31','1234',10000)
e.eatndrink()
e.work()
e.empInfo()

#from the child class constructor I can call the parent class constrcutor by passing name and age as argument.
#From the child class constructor If i want to access the parent class members then we need to use super method or super function.