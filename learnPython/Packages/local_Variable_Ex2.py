class Test:
    def m1(self):
        a=10
        print(a)
    def m2(self):
        print(a)#NameError: name 'a' is not defined
t=Test()
t.m1()
t.m2()

#Local variables are local to that method. Within the method we can access, outside of the method we cannot access.
#Local variable will be created at the time of  method execution and destroyed once method execution completes.