class student:
    def __init__(self,name,rollno,marks):
        print('Creating instance Variable and performing initialization.....')
        self.name=name #instance variable name is created
        self.rollno= rollno # instance variable rollno is created
        self.marks= marks # instance variavle marks can be created
s1=student('karthik',101,60)
print(s1.name,s1.rollno,s1.marks)
s2=student('john',102,65)
print(s2.name,s2.rollno,s2.marks)