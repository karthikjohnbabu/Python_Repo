class Test:
    def __init__(self):
        print('Address of object pointed by self:',id(self))#
        pass
t=Test()
print('Address of object by t:',id(t))

# Address of object pointed by self: 140690781710224
# Address of object by t: 140690781710224

# I created an object
# Here the t is reference variable where programmer can use it only outside of the class
# within the class to access the current object we need some reference variable. That reference variable is nothing but self.
