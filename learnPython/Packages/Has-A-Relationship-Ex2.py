class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getInfo(self):
        print('Car Name: {},Model:{},color:{}'.format(self.name,self.model,self.color))
class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    def empInfo(self):
        print('Employee Name:',self.ename)
        print('Employee Number:',self.eno)
        print('Employee Car info:'),self.car.getInfo()
car=Car('Innova','2.5v','Black')
e=Employee('Karthik','1234',car)
e.empInfo()

#Note: In the above program employee Class HAS-A car reference and hence employee class can access all members of car class





