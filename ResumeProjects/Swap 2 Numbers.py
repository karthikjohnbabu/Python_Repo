#num1 = 10
#num2 = 20

num1 = input("Enter num1 value:")
num2 = input("Enter num1 value:")


# I need to swap these two numbers
print("value of num1 before swapping:",num1)
print("value of num2 before swapping:",num2)

#to swap two numbers i am using a temporary variable.

temp= num1 #10
num1= num2 #20
num2= temp #10

print("value of num1 after swapping:",num1)
print("value of num2 after swapping:",num2)


