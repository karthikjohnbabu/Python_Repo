class employee:
    def __init__(self,name,salaryPerDay):
        self.name=name
        self.salaryPerDay=salaryPerDay
    def __mul__(self, other):
        return(self.salaryPerDay*other.WorkingDays)
class TimeSheet:
    def __init__(self,name,WorkingDays):
        self.name=name
        self.WorkingDays= WorkingDays
e=employee('Karthik',1000)
t=TimeSheet('Karthik',25)
print('This month salary:',e*t)

