class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('Name:',self.name)
        print("Age :",self.age)

class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super().display()
        print('Roll no:',self.rollno)
        print('marks:',self.marks)
s1=Student('Karthik',30,101,60)
s1.display()

