import time
class Test:
    def __init__(self):
        print('object initialization activities')
    def __del__(self):
        print('Fullfilling last wish and performing cleanup activities')
t1=Test()
t2=Test()
print('ENd of application')


