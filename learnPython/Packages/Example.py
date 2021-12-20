class Test:
    def m1(x):
        print('Some method')
t=Test()
t.m1()
t.m1(10)#This method will be treated as invalid
#TypeError: m1() takes 1 positional argument but 2 were given
#Where PVM Is already providing one value (Self) and method call is providing value(10)
#But the method is able to accept only one value .Hence the error.



