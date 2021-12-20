class p:
    a=10
    def __init__(self):
        print('Parent constructor')
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')
class c(p):
    def __init__(self):
        print('child constructor')
    def method1(self):
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
        super().__init__()
c=c()
c.method1()

#super() is a built method which is useful to call the super class constructors, variables and methods from the child class.
#Note: If there is naming conflict use the keyword super.  no naming conflict use the word self only.
