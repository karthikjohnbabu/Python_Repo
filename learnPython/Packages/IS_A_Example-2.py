class p:
    a=10 #static variable
    def __init__(self):
        print('Parent constructor')
        self.b=20
    def m1(self):
        print('Parent Instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent class static method')
class c(p):
    pass
c=c()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()
