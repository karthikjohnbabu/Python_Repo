#self variable.
#self is a reference variable which is always pointing to current object.
#self reference variable we can use within the calss to refere current reference object.
#self reference variable is similar to this keyword in java.
#By using self we can access instance variable and instance method of objects.

class Test:
    def __init__(self):
        print('Address of object pointed by self:',id(self))
        pass
t=Test()
print('Address of object pointed by t:',id(t))

#I created an object
#Here the t is reference variable where i can use it only outside of the class.
#within the class to access the current object we need some reference variable that reference variable is nothing but self.



