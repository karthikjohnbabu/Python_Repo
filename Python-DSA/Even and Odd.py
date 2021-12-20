l=[10,41,30,15,80]
even=[]
odd=[]

def evenandodd(l):
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print('Even list is:',even)
    print('Odd list is:',odd)

evenandodd(l)