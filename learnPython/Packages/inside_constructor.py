class Employee:
    def __init__(self):
        self.eno=100
        self.ename='Karthik'
        self.esal='1000'
e=Employee()
print(e.__dict__) #Once we create a object, automatically these instance variables will be added to the object.