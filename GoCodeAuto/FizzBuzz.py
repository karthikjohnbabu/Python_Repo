def fizzBuzz(n):
    for i in range(1,n+1):
        if i%3 and i%5!=0:
            print(i)
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print('Buzz')


if __name__ == '__main__':
    fizzBuzz(30)
    print()