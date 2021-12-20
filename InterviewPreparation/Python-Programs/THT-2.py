F1= [['u1','u2'],['u3','u4'],['u1','u5'],['u2','u1'],['u3','u4']]
F2=[]
res = list(set(tuple(sorted(x)) for x in F1))
F2=res
print(F2)