class Test:
    def m1(self):
        print('no arg in this method')
    def m1(self,x):
        print('one arg in this method')
    def m1(self,x,y):
        print('Two arg in this method')
t=Test()
t.m1(10,20)