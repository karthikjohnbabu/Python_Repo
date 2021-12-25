from collections import namedtuple
#Declaring namedtuple()
Student=namedtuple('Student',['name','age','DOB'])
#Adding Values
S=Student('Karthik','30','22111988')
#Access using index
print('The Student age using index is:',end="")
print(S[1])
# Access using name
print('The Student name using keyname is:', end="")
print(S.name)

from collections import namedtuple
Student=namedtuple('Student',['name','age','Dob'])
#Adding values
S=Student('Karthik','33','22111988')
#Initializing iterable
li=['John','30','20122021']
#Intializing dict
di={'name':"nikhil",'age':19,'DOB':'1391997'}
#using _make() to return namedtuple()
print('The namedtuple instance using iterable is:')
print(Student._make(li))
#using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is:")
print(S._asdict())