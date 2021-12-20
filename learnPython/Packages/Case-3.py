import time
class Test:
    def __init__(self):
        print('object initialization activities')
    def __del__(self):
        print('Fullfilling last wish and performing cleanup activities')
t1=Test()
t2=t1
t3=t1
del t1
time.sleep(10)
print('Object not destroyed after deleting t1')
del t2
time.sleep(10)
print('Object not destroyed after deleting even t2')
print('Removing last reference')
del t3
print('ENd of application')