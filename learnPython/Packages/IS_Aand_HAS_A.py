class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getInfo(self):
        print("\t CarName:{}\n\t Model:{}\n\t color:{}".format(self.name,self.model,self.color))
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print('Eat Briyani and Drink COke')
class Employeee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car=car
    def work(self):
        print(' Coding python is as easy')
    def empinfo(self):
        print('Employee Name:',self.name)
        print('Employee Age:',self.age)
        print('Employee Number:',self.eno)
        print("Employee Salary:",self.esal)
        print('Emplpyee Car Info:')
        self.car.getInfo()
c=Car('Seltos','High ENd','Black')
e=Employeee('Karthik',31,1234,10000,c)
e.eatndrink()
e.work()
e.empinfo()
#
