class Test:
    def __init__(self):
        print("constructor Execution")
t=Test()
t.__init__()
t.__init__()
t.__init__()
t.__init__()
#Here we are calling constructor explicitly.
#Based on our requirement we can alll the constructor explicitly
#If we call the constructor explicitly, it will be executed as a normal method and a new object will not be created.
#But when ever we are creating a object, contructor will be executed.
