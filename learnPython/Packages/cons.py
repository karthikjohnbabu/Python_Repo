class student:
    '''Class developved by karthik for demo'''
    #the functions which are defined inside class are called methods

    def __init__(self,name,rollno, marks):#special method
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def talk(self):
        print('Hello I am :',self.name)
        print('My rollno is :',self.rollno)
        print('My Marks are:',self.marks)
s=student('karthik',101,60)# Reference variable = Classname()

#In python we have 3 types of variables.
#1. Instance variable / Object level variables
#2. Static variable
#3. Local variable



