class student:
    school_name='karthiktech school'# static variable
    def __init__(self,name,rollno):
        self.name=name# instance Variable
        self.rollno= rollno # instance variable
    def info(self):
        x=10 # x is local variable
        for i in range(x):# is is local variable
            print(i)
s=student('karthik',101)
print(s.name)
print(s.rollno)
s.info()