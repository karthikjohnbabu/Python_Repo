class student:
    def __init__(delf,name,rollno,marks):
        delf.name=name
        delf.rollno=rollno
        delf.marks=marks
    def talk(delf):
        print('Hello I am : ',delf.name)
        print('My roll no is :',delf.rollno)
        print('My marks are:',delf.marks)

s=student('Karthik',101,75)
s.talk()
# here we are using self multiple times.
# is self keyword in python?
# self is not a keyword in python.  Instead of self I can use any word in python.
# self is recomended to used universally
# self keyword should be used only within the class. It cannot be used outside of the class.


#In python class we have 3 types of variables.
# 1. Instance variables or object level varibales
# 2. Static Variable
# 3. Local variable
