import karthik
print(dir(karthik))
#['__builtins__', '__cached__',
# '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__',
# 'add', 'product', 'x']

#Extra members added by python intrepreter (PVM) for every module.

#Note: FOr every module at the time of execution python intrepretor will add
#some special properties/ members automatically for internal use.

#__doc__ this is the member added by python virtual machine to hold doc string
#__file__ this is the member added by python virtual machine to hold the file name
#__name__This we will discuss in the later part.
#__loader__ This is the member to know which module is it related to.

#Based on our requriment we can access these properties also in our program.
print(__name__)#main

#The Special variable __name__:
#For every python program a special variable __name__ will be added internally by pvm.
# This variable stores information regarding whether the program is executed as as individual program or
# as a module.
#If the program is executed as an individual program then the value of the variable __name__=__main__
#If the program is executed as a module from some other program then the value of this vraibel is the name
#of the module where it is defined.

#Hence by using this __name_ variable we can identify whether the program executed directly or as a module.






