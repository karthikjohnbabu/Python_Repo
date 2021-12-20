#demo program with variable number of arguments.
class Test:
    def m1(self,*args):
        print('Variable length argument method')
t=Test()
t.m1()#no argument method
t.m1(10)
t.m1(10,20)
t.m1(10,20,30)
t.m1(10,20,30,40,50,60,"Karthik",10.5)