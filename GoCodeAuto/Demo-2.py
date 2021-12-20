class parent:
    def m1(self):
        print('Parent Method')
class child(parent):
    def m2(self):
        print('Child method')
c=child()
c.m1()
c.m2()