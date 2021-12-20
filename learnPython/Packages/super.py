class p:
    def m1(self):
        print('Parent method')
class c(p):
    def m2(self):
        super().m1()
        print('child method')
c=c()
c.m1()
