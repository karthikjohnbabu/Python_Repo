def leftRotate(l,d):
    for i in range(0,d):
        l.append(l.pop(0))

l=[10,20,30,40,50]
d=3
leftRotate(l,d)
print(l)
