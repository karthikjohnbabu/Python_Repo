from abc import*
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass
class SubTest(Test):
    pass
s=SubTest()
# TypeError: Can't instantiate abstract class SubTest with abstract methods m1

#If we are creating child class for abstract clas, then for every abstract method of parent class compulsory we should provide implementation
#in the child class, other wise child class is also abstract and we cannot create object for child class.





