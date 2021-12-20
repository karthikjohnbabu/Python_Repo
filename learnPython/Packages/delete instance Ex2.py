class Test:
    def __init__(self):
        self.a=10
        self.b=20
t1=Test()
t1.a=888
t1.b=999
t2=Test()
print('t1:',t1.a,t1.b)#t1: 888,999
print('t2:',t2.a,t2.b)#t2:10,20

#Note: If we are changing the values of instance variable of one object. then those changes wont be reflected
# to othe objects.
# Because for every object a seperate copy of isntance variable will be available.