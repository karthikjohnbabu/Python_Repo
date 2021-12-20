# Write a program to read Employee Data from the Keyboard and print the data.

eno=int(input('Enter Employee Number:'))
ename=input('Enter Employee Name:')
esal=float(input('Enter salary details:'))
eaddr=input('Enter Employee Address:')
emarr=eval(input('Employee Married ?[True|False]:'))
print(type(emarr))
print(emarr)

# If the employee Married? [True|False] String
#If the statement or string is empty then only it returns false or else it will return true only.
#Example bool(str) --> returns false only for empty string.

# Reading boolean data from the keyboard needs special care, for that we use eval function.





