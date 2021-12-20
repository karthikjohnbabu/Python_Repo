d={100:'Karthik',101:'John',102:'Babu',103:'Evan',104:'John'}
print(type(d))#<class 'dict'>
print(d)#{100: 'Karthik', 101: 'John', 102: 'Babu', 103: 'Evan', 104: 'John'}
# Duplicate values are allowed inside dictionary.


e={100:'Karthik',101:'John',100:'Babu'}
print(type(e))#<class 'dict'>
print(e)#{100: 'Babu', 101: 'John'}
# Duplicate keys are not allowed inside dictionary


f={'a':10,'b':10.5, 'c':True, 'd':10+20j, 's':'Karthik'}
print(type(f))#<class 'dict'>
print(f) #{'a': 10, 'b': 10.5, 'c': True, 'd': (10+20j), 's': 'Karthik'}
#Hetrogenous objects are allowed.

g={10:'int value','karthik':20}
print(type(g))
print(g)

