#Demo program to call parent class constructor by using super()

class person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('Height',self.height)
        print('weight',self.weight)
class employee(person):
    def __init__(self,name,age,height,weight,eno,esal):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.eno=eno
        self.esal=esal
    def display(self):
        super().display()
        print('Name:', self.name)
        print('Age:', self.age)
        print('Height', self.height)
        print('weight', self.weight)
        print('Employee Number:',self.eno)
        print("Employee Salary:",self.esal)
e=employee('Modi','60','5.10','65','ind01','1000')
e.display()

