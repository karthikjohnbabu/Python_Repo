class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
n=int(input('Enter no of students:'))
students=[]
for i in range(n):
    s=Student()
    name=input('Enter student name:')
    marks=int(input('Enter marks:'))
    s.setName(name)
    s.setMarks(marks)
    students.append(s)
for s in students:
    print('Hello:',s.getName())
    print('your marks are:',s.getMarks())
    print()

#I can go for constructor only when I know the values at the begining.
#When we dont have enough data during the object creation we can choose setter and getter methods.






