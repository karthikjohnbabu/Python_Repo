#class A(A):
    #pass#NameError: name 'A' is not defined

class A(B):
    pass
class B(A):
    pass#NameError: name 'B' is not defined
