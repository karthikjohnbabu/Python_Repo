from abc import*
class Test(ABC):
    def m1(self):
        print('Non abstract method')
    @abstractmethod
    def m2(self):
        pass
class SubTest(Test):
    def m2(self):
        print('M2 method implementation')
s=SubTest()
s.m1()
s.m2()

