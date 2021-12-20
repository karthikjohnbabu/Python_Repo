n=5
arr=[1,3,4,2,1]
x=1

def findElement(n,arr,x):
    for i in range(n):
        if arr[i]==x:
            return i
    return -1

res=findElement(n,arr,x)
print(res)