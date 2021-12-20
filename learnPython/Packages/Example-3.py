#How to track number of objects created for a class?
class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def getNoofobjects(cls):
        print('The no of objects created:',cls.count)#Here this is called as a class method
        #because in this method we are no where using instance variable rather only static variable/class level variable
t1=Test()
t2=Test()
t3=Test()
Test.getNoofobjects()