def getMax(l):
    for i in l:
        for j in l:
            if j>i:
                break
        else:
                return i
    return None

l=[10,5,20,8]
print(getMax(l))
