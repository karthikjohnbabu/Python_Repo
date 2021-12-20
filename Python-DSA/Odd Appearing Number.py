def findodd(l):
    res=None
    for x in l:
        count=l.count(x)
        if count%2!=0:
            res=x
            break
    return res
l=[10,20,20,30,10]
print(findodd(l))



