class Test:
    a=10
    def __init__(self):
        self.b=20
t1=Test()
t2=Test()
print('t1:',t1.a,t1.b)#: 10 20
print('t2:',t2.a,t2.b)#10 20
t1.a=888
t1.b=999
print('t1:',t1.a,t1.b)# 888 999
print('t2:',t2.a,t2.b)#10 20
