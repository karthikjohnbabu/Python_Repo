class Test:
    def __init__(self):
        self.a=10 #instance variable
        self.b=20 #instance variable
    def m1(self): #for instance method the first argument is self.
        self.c=30 #instance variable
t=Test()# Here a,b will be added to object t
t.m1()# c will be added to object
t.d=40# a new instance variable d will be added to object

# here a, b will be added to object t2
print(t.__dict__)
print(t2.__dict__)
# How to know the no of instance variable present in the object.
#__dict__ is a dictionary which holds the name of the instance variable and it respective value
#Here the dictionary holds the key value pairs, where key is the instance variable and value is the value of the variable.
#In other languages like Java we should declare the instance variable inside the class.
#outside of the class adding new instance variable is present only in python.
#in java the number of instance variable never varies from object to object.
#But in python the number of instance variable varies from object to object.
