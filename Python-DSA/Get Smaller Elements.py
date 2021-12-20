def smallerelements(l,x):
    output = []
    for i in l:
        if i < x:
            output.append(i)
    return output


l=[100,20,40,60,80,200]
x=60
result=smallerelements(l,x)
print(result)
