class multiplier:
    def __init__(self,a):
        self.a = a

    def multiply(self, b=1):
        print(b*(self.a))

x=multiplier("Hello")
x.multiply(2)
