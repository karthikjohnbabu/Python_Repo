import sys
class Test:
    pass
t1=Test()
t2=Test()
t3=t2
t4=t3
del t3,t4
print(Test.__dict__)
print(sys.getrefcount(t1))#5, #3