class Test:
    def __init__(self):
        self.__x=10 #private variable
    def __m1(self):#private method
        print('Private method')
    def m2(self):
        print(self.__x)
        self.__m1()
t=Test()
t.m2()
t._Test__m1()# Name mangling.
print(t._Test__x)#10

#Name Mangling and accessing private members from outside of the class
# we cannot access private members directly from outside of the class, But we can access indirectly as follows

#name mangling will be happened for the private variable. Hence every private variable name will be changed to new name.

#_variableName--> _ClassName_VariableName

#Hence we can access private from outside of the class as follows.

#print(objectreference._Classname__variablename)