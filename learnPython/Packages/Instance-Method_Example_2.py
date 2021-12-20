class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('Hi:',self.name)# Inside Method implementation I am using instance variable such type of methods by default
        print('your marks are:',self.marks)#called as instance method
    def grade(self):
        if self.marks>=60:
            print('You got first grade')
        elif self.marks>=50:
            print('you got second grade')
        elif self.marks>=35:
            print('You got third grade')
        else:
            print('You are not qualified, please retry')
n=int(input('Enter no of students:'))
for i in range(n):
    name=input('Enter student name:')
    marks=int(input("Enter student Marks:"))
    s=student(name,marks)
    s.display()
    s.grade()
    print()

