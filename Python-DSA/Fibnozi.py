n_terms = int(input("How many terms the user wants to print? "))
x = 0
y = 1
count = 0
if n_terms <= 0:
    print("Please enter a positive integer, the given number is not valid")
elif n_terms == 1:
    print("The Fibonacci sequence of the numbers up to", n_terms, ": ")
    print(x)
else:
    print("The fibonacci sequence of the numbers is:")
    while count < n_terms:
        print(x)
        nth = x + y
        x = y
        y = nth
        count += 1