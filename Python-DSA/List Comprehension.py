even=[x for x in range(11) if x%2==0]
print("Even numbers are:",even)

odd=[x for x in range(11) if x%2!=0]
print("Odd numbers are:", odd)

def getSmaller(l,x):
    return [i for i in l if i<x]
l=[9,15,12,3,7,11]
x=10
print(getSmaller(l,x))

def getEvenOdd(l):
    even=[x for i in l if i%2==0]
    odd=[x for i in l if i%2!=0]
    return even,odd

l=[10,41,30,15,80]
getEvenOdd(l)
print(even)
print(odd)

s='geeksforgeeks'
l1=[i for i in s if i in "aeiou"]
print(l1)

l2=['geeks','ide','courses','gfg']
l3=[x for x in l2 if x.startswith("g")]
print(l3)

l1=['geeks','for','geeks','gfg','ide']
l2=[x.upper() for x in l1 if x.startswith("g")]
print(l2)