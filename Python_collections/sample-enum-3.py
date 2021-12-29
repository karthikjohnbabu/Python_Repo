#python code to demonstrate enumerations
#Access and comparison
# importing enum for enumerations
import enum
#creating enumerations using class
class Animal(enum.Enum):
    dog=1
    cat=2
    lion=3
#Accessing enum member using value
print("The enum member associated with value 2 is : ",end="")
print(Animal(2))
#Accessing enum member using name
print('The enum member associated with name lion is:',end="")
print(Animal['lion'])