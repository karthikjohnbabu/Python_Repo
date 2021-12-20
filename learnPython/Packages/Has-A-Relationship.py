class Engine:
    def __init__(self):
        self.power='125KW'
    def useEngine(self):
        print('Engine Specific Functionality ')
class Car:
    def __init__(self):
        self.engine=Engine()
    def useCar(self):
        print('Car required engine Functionality')
        self.engine.useEngine()
        print(self.engine.power)
c=Car()
c.useCar()






