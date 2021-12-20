class Test:
    def m1(self):
        def cal(a,b):
            print('The sum is:', a+b)
            print('The product is:', a*b)
            print('The difference is:', a-b)
            print('The average is:', (a+b)/2)
        cal(10,20)
        cal(100,200)
        cal(1000,2000)
t=Test()
t.m1()
