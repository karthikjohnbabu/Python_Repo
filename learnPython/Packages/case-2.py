import time
class Test:
    def __init__(self):
        print('object initialization activities')
    def __del__(self):
        print('Fullfilling last wish and performing cleanup activities')
t1=Test()
t2=Test()
t1=None
t2=None
print('ENd of application')

#object initialization activities
#object initialization activities
#Fullfilling last wish and performing cleanup activities
#Fullfilling last wish and performing cleanup activities
#ENd of application