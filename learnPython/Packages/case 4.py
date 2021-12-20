import time
class Test:
    def __init__(self):
        print('Construction execution')
    def __del__(self):
        print('Destruction execution')
l=[Test(),Test(),Test()]
print('Making list object eligible for GC')
del l
time.sleep(5)
print('end of application')

#Note: Once control reaches end of program. all objects which are created as the part of the program are by default eligible for GC.
#If the object does not contain reference variable. then it is eligible for GC. That means if the reference count is zero then
#only object is eligible for garbage collection.

