from collections import defaultdict
#defining the dict
d=defaultdict(int)

L=[1,2,3,4,2,4,1,2]

#iterate through the list
# for keeping the count

for i in L:
    d[i]+=1

print(d)

from collections import defaultdict

#defining a dict
d=defaultdict(list)

for i in range(5):
    d[i].append(i)
    
print("Dictionary with values as list:")
print(d)
