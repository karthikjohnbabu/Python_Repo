from abc import abstractmethod, ABC
class vechile(ABC):
    @abstractmethod
    def getNoofWheels(self):
        pass
class bus(vechile):
    def getNoofWheels(self):
        return 6
class auto(vechile):
    def getNoofWheels(self):
        return 3
b=bus()
print(b.getNoofWheels())
a=auto()
print(a.getNoofWheels())

#The most important conclusion is:
#1 If a class contains at least one abstract method and if we are extending ABC class then intstantiation is not possible
# (Object creation is not possible)
# For abstract class with abstract methods  instantion(Object creation) is not possible.
from abc import*
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass
t= Test()

