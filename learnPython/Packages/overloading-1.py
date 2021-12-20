class Book:
    def __init__(self,pages):
        self.pages=pages

b1=Book(100)
b2=Book(200)
print(b1+b2)#TypeError: unsupported operand type(s) for +: 'Book' and 'Book'

#We can overload + operator to work with books objects also. ie python supports operator overloading.

#For every operator Magic method are availabe. To overload any operator we have to override that magic method in our class.

#Internally + operator is implemented by using __add__() method. This method is called magic method for + operator.
# we have to override this method in our class.

