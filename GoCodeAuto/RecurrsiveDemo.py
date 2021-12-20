#Req is to find factorial of a number.

def factorial(n):
    if n==0:
        result=1
    else:
       result= n*factorial(n-1)
    return result
print('Factorial of 5 is:', factorial(997) )
