#Constructor Concept.
#constructor is a special method in python.
#In python the name of the constructor should be always __init__(self)
#In Java the name of the constructor is same as the name of the class.
#class Test
#{
    #Test()
        #{

        #}
#}
#Constructor will be executed automatically at the time of object creation.
#We are not required to call the constructor method explicitly.
#Per object constructor will be executed only once.
class Test:
    def __init__(self):
        print('constructor')
t1=Test()
t2=Test()
t3=Test()
#Here constructor will be executed 3 times based on the no of objects created. Also constructor willbe executed per object only once.
#The main purpose of constructor is to declare and initialize instance variable
#Constructor can take atleast one argument atleast one (self)
#Constructor is optional and if we are not providing any constructor then python will provide default constructor.