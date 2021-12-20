class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def __str__(self):
        return 'Name:{},rollno:{},marks:{}'.format(self.name,self.rollno,self.marks)
s1=Student('Karthik',101,60)
print(s1)#<__main__.Student object at 0x00000247EDE59460>
#when ever we are trying to print any object reference,
#Internally __Str method will be called. It is going to provide default string type.

#Importance of __Str__() method.
# #when ever we are trying to print any object reference, Internally __Str__() method will be called.
#The default implementation of this method returns the string in the following format #<__main__.Student object at 0x00000247EDE59460>
#To provide meaningful string representation of our object, we have to override __Str__()m method in our class.