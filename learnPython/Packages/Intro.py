#write a program to create a student class and create an object to it.
#call the method talk() to display student details .

class student:
    '''Class developved by karthik for demo'''
    #the functions which are defined inside class are called methods

    def __init__(self):#special method
        self.name='karthik'
        self.rollno='1234'
        self.marks='70'
    def talk(self):
        print('Hello I am :',self.name)
        print('My rollno is :',self.rollno)
        print('My Marks are:',self.marks)
s=student()# Reference variable = Classname()
print(s.marks)
print(s.name)
print(s.rollno)
s.talk()

