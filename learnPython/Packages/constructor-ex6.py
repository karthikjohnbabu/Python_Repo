class Test:
    def __init__(self):
        print('No arg constructor')

    def __init__(self,x):
        print('One arg constructor')
#t=Test()
t=Test(10)
#This is perfectly invalid
#m1(x):
#m1(x,y)
#Methods with same name and different arguments are called over loading.
#In python method over loading concepts are not there.
# Hence constructor over loading is also not supported.
#We can't take more than one constructor, if we are trying to take more than one constrcutor, then PVm will consider the most recent or last
#constructor.


