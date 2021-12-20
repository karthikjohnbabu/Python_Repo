#Demo program to overload + operator for our Book class objects.
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        total_pages =self.pages+other.pages
        return total_pages
b1=Book(100)
b2=Book(200)
b3=Book(300)
print(b1+b2)#300 Here b1 will become self at add method and b2 will become other at add method
print(b1+b3)#400 Here b1 will become self at add method and b3 will become other ad add method
print(b2+b3)#500

#Python supports operator overloading by using magic method (__add__)



