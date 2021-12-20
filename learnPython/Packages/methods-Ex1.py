class Student:
    school_name='modisoft tech school'# static variable
    def __init__(self,name,rollno):
        self.name= name #instance variable
        self.rollno= rollno #instance variable
    def getStudentInfo(self):# for instance method there is no need to use decorator.
        print('Student Name:',self.name)
        print('Student rollno:',self.rollno)
    @classmethod
    def getSchoolName(cls):
        print('school Name:',cls.school_name)

    @staticmethod
    def getSum(a,b):
        sum =a+b
        return sum
