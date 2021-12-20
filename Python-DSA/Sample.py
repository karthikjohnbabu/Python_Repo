from math import *


# TODO: Implement this method
def numberOfDivisorsAndSum(n):
    sum=0
    i = 1
    while (i * i < n):
        if (n % i == 0):
            sum=sum+i
            # print(i, end=" ")

        i += 1

    for i in range(int(sqrt(n)), 0, -1):
        if (n % i == 0):
            sum=sum+n//i
            # print(n // i, end=" ")
    return sum


# NOTE: Please do not modify this function
def main():
    n = 4
    list = numberOfDivisorsAndSum(n)
    print(list)


if __name__ == "__main__":
    main()