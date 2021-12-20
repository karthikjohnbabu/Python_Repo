from collections import OrderedDict
print('The is a Dict:')
d={}
d['a']=1
d['b']=2
d['c']=3
d['d']=4
for key, value in d.items():
    print(key, value)
print('This is an ordered Dict:')
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
for key, value in od.items():
    print(key,value)

#while deleting and re-inserting the same key wil push the key to the last
# to maintain the order of insertion of the key.

from collections import OrderedDict

od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4

print('Before Deleting')
for key, value in od.items():
    print(key, value)

#Deleting element
od.pop('a')

#Re-inserting the same
od['a']=1

print('After re-inserting')
for key, value in od.items():
    print(key, value)

