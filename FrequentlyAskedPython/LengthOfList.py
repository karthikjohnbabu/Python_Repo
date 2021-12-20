#Approach 1
# we need to read each and every item or value from the list
# then we have to count that value.

mylist= [1,4,6,7,8]
print(mylist)

count=0
for i in mylist:
    count = count+1
print("Length of List is:",count)

#Approach len()
#len is a built function in python
mylist= [1,4,6,7,8]
print(mylist)
print("Length of list using len() method is :",len(mylist))