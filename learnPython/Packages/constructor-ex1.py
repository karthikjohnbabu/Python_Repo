#program to demonstrate constructor will execute only once per object.

class Test:
    def __init__(self):
        print('Constructor Execution')

    def m1(self):
        print('Method Execution')
t1=Test()
t2=Test()
t3=Test()
t3.m1()

