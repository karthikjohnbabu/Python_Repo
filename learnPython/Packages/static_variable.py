#6.6.outside of class by using class name.
class Test:
    a=10#static variable
    def __init__(self):
        Test.b=20#static variable
    def m1(self):
        Test.c=30#static variable
    @classmethod
    def m2(cls):
        cls.d=40
        Test.e=50
    @staticmethod
    def m3():
        Test.f=60
t=Test()
t.m1()
Test.g=70
print(Test.__dict__)




