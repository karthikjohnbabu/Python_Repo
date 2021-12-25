from collections import UserDict

#Creating a Dictionary Where
# Deletion is not allowed
class MyDict(UserDict):
    #Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")
    #Function to stop pop from
    #dictionary
    def pop(self, s=None):
        raise RuntimeError('Deletion not allowed')
    #Function to stop popitem
    # from dictionary
    def popitem(self,s=None):
        raise RuntimeError('Deletion not allowed')

#Driver's Code
d=MyDict({'a':1,'b':2,'c':3})
d.pop(1)

