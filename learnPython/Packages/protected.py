class Test:
    def __init__(self):
        self._x=10 #protected
    def m1(self):
        print(self._x)
class subTest(Test):
    def m2(self):
        print(self._x)
t=subTest()
t.m1()
t.m2()
#protected members we can access within the class from anywhere but from outside of the class we can access only in child class
#we can declare members as protected explicitly by prefixing with one underscore symbol.
# Its just a naming convention.
