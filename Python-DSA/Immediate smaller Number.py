def immediateSmaller(arr,x):
    out = 0
    for i in arr:
        if i < x:
            if out == 0:
                out = i
            elif i > out:
                    out = i
    return out
arr = [4,67,13,12,14,16]
x=15
print(immediateSmaller(arr,x))
