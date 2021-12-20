#constructor with variable number of arguments
class Test:
    def __init__(self,*args):
        print("Constructor with 0|1|2|3 number of arguments")
t=Test()
t=Test(10)
t=Test(10,20)
t=Test(10,20,30)
t=Test(10,20,30,40,50,60)

