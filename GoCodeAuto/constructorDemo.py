class Test:
    def __init__(self):
        print('constructor')
    def m1(self,x):
        print('x value is :',x)
t=Test() # when ever we are creating the object automatically the special method will be called. This special method is called as constructor in python
t.m1(10)

