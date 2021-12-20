def sumofnatural(n):
    sum = 0
    for i in range(1,n+1):
         #print(i)
         sum=i+sum
    return sum

sum=sumofnatural(5)
print(sum)
