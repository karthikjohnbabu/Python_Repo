def immediateGreater(arr,x):
    out = 0
    for i in arr:
        if i > x:
            if out == 0:
                out = i
            elif i < out:
                    out = i
    return out
arr = [4,67,13,12,15]
x=16
print(immediateGreater(arr,x))