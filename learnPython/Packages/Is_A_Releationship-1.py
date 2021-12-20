class p:
    def m1(self):
        print("Parent method")#Parent has only one method.
class c(p):
    def m2(self):
        print('Child method')#Child class has 2 methods.
c=c()
c.m1()
c.m2()

#What ever variables, methods and constructors available in the parent class by default availbe to the child classes and we are not
#required to rewrite.
#Hence the main advantage of inheritance is code reusability and we can extent existing functionlaity with some additional features to child class

#syntax : Class childclassname(Parentclass)

