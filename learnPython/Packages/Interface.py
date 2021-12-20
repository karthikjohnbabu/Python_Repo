from abc import*
class collegeAutomation(ABC):
    @abstractmethod
    def m1(self):pass
    @abstractmethod
    def m2(self):pass
    @abstractmethod
    def m3(self):pass
class AbsCls(collegeAutomation):
    def m1(self):
        print('m1 method implementation')
    def m2(self):
        print('m2 method implementation')
class concreateCls(AbsCls):
    def m3(self):
        print("m3 method Implemenation")
c=concreateCls()
c.m1()
c.m2()
c.m3()
