#classes are user defined or  a blue print or a prototype to perform a specific task.
#class will have methods, class variables, instance vraibles, constructor objects.

class Student:
    num= 40


    def getData(self):
        print("I am now executing as method in class")

exam= Student() #syntax to create objects in python
exam.getData()
print(exam.num)
