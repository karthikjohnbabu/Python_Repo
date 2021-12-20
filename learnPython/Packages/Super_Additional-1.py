class P:
    def __init__(self):
        print('Parent constructor')
    def m1(self):
        print('Parent class instance method')
    @classmethod
    def m2(cls):
        print('Parent Class method')
    @staticmethod
    def m3():
        print('Parent static method')
class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
c=C()
c.m1()

#From child class constructor  and instance method we can access parent class constructor, instance method, static method and class method
#by using super()

