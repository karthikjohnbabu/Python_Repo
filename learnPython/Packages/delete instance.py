class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def m1(self):
        del self.c
t1=Test()# a,b,c,d will be added to the t1 object
t1.m1()# c instane variable will be deleted from t1 object
t2=Test()#a,b,c,d will be added to the t2 object
del t2.b, t2.d
print(t1.__dict__)#{'a': 10, 'b': 20, 'd': 40}
print(t2.__dict__)# a and c will be present.

