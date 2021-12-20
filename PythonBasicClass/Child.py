from Calculator import Calculator
class child(Calculator):
    num2 = 200 # Class variable.

    def __init__(self):#child constructor
        Calculator.__init__(self,2,10) #parent constructor

    def getCompleteData(self):
        return self.num2+self.num+self.Summation()

obj=child()
print(obj.getCompleteData())