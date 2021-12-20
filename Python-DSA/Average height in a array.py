def averageHeight(n,a):
    sum=0
    for x in a:
        sum=sum+x
    result=sum/n
    return result


n=6
a=[10,2,3,4,5,6,7,8,9]
print(averageHeight(n,a))