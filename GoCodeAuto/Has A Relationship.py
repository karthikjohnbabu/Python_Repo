class Engine:
    def __init__(self):
        self.power='125KW'
    def useEngine(self):
        print('Engine Specific Functionality')
class car:
    def __init__(self):
        self.engine=Engine()
    def useCar(self):
        self.engine.useEngine()
        print(self.engine.power)
c=car()
c.useCar()

# By using name or by creating object we can access members of one class inside another class.
# And this is called as composition or Has A relationship




