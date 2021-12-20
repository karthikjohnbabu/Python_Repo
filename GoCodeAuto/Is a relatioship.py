class parent:
    def m1(self):
        print('This is parent method')
class child(parent):
    def m2(self):
        print('The is child method')
c=child()
c.m1()
c.m2()

# By Inheritance (IS a Relationship)
# Parent to child relationship
# Parent class members are by default availabe to the child class and hence child class can reuse parent class functionality
# CHild class can define new members also, hence child class can extend parent class functionality(Code Extendibility)


