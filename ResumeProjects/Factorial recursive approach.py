#5 * 4 * 3 * 2 * 1 = 120
def factorial(num):
    if (num==0 or num==1):
        return 1
    else:
        return num * factorial(num-1) #5 * 4 * 3 * 2 * 1

num=int(input("Enter the number"))
print("Factorial of", num, "is",factorial(num))

