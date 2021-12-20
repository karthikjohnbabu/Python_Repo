class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
t=Test()
t.m1()
print(t.__dict__)#If any instance variable is declared inside instance method,
# that instance variable will be added once we call that instance method.
