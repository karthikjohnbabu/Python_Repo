class Student:
    school_name ='karthik-School' # static variable.
    def __init__(self,name, rollno): #methods with self keyword is called instance method
        self.name=name # instance Variable
        self.rollno= rollno #instance Variable

    def getStudentInfo(self) :
        print('Student Name:',self.name)
        print('Student Rollno:',self.rollno)

    @classmethod
    def getSchoolName(cls): # methods with cls variable is called class method
        print('School Name:',cls.school_name)

    @staticmethod
    def getSum(a,b): # methods with labels @staticmethod and arguments are without self are called static method
        sum=a+b # local variable
        return sum
#
# s1=Student('Rahul',101)
# s1.getStudentInfo()
# s1.getSchoolName()
#
# s2=Student('Dravid',102)
# s2.getSchoolName()
# s2.getStudentInfo()

s3=Student('Vijay',201)
result=s3.getSum(10,2)
#print(s3.getSum(10,2))
print(result)