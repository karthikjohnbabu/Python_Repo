def squareit(n):
    return n*n
result=squareit(2)
print(result)


s=lambda n:n*n
print(s(5))


s=lambda n:n*n
for i in range(1,11):
    print('The square of {} is {}'.format(i,s(i)))