class student:
    def __init__(self,name, rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks = marks
    def __str__(self):
        return self.name
s1=student('Durga',101,95)
s2=student('Ravi',102,98)
print(s1)
print(s2)



