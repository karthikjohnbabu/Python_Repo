from collections import ChainMap
d1={'a':1,'b':2}
d2={'c':3,'d':4}
d3={'e':5,'f':6}
#defining the chain map
c=ChainMap(d1,d2,d3)
#Accessing values using values() method.
print(c.values())
#Accessing keys using keys() method
print(c.keys)
# A new dictionary can be added by using the new_child() method.
#The newly added dictionary is added at the begining of the chainmap.
import collections
dic1={'a':1,'b':2}
dic2={'b':3,'c':4}
dic3={'f':5}

#intializing chaimap
chain=collections.ChainMap(dic1,dic2)

#printing chainMap
print("All the chainMap contents are:")
print(chain)

#using new_child() to add new dictionary
chain1=chain.new_child(dic3)

#printing chainMap
print("Displaying new Chainmap:")
print(chain1)