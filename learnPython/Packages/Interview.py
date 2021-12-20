class Test:
    def __init__(self):
        print('constructor')
    def __del__(self):
        print("Destructor")
t=Test()
#del t # del t means refference variable deleted and correspoding object also deleted.
t=None# Here we are not deleting reference variable, but assigning the reference variavle to object none. So that we can reuse the reference variable
print("end of application")
print(t)#None