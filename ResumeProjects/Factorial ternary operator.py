def factorial(num):
    return 1 if (num==0 or num ==1)else num*factorial(num-1)

num=int(input("Enter the number"))
print("Factorial of", num, "is",factorial(num))
