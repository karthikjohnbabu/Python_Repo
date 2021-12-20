class Outer:
    def __init__(self):
        print('Outer object creation')
    class Inner:
        def __init__(self):
            print('Inner class object creation')
        def m1(self):
            print('Inner class method')
Outer().Inner().m1()

