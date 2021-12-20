#Accessing members of one class inside another class.
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print('Employee Number:',self.eno)
        print('Employee name:',self.ename)
        print('Employee salary:',self.esal)
class manager:
    def updateEmpSal(emp):
        emp.esal= emp.esal+500
        emp.display()
emp=Employee(101,'karthik',1000)
manager.updateEmpSal(emp)



