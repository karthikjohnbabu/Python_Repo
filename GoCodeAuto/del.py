l=[1,2,2,3,4,'@']
a=l.pop(-1)
for i in range(len(l) -1, -1, -1):
        print(l[i], end="")
print(a)
