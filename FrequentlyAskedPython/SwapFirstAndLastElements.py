#Approach 2

mylist= [12,35,9,56,24]
first=mylist.pop(0) # 12
last= mylist.pop(-1) #24
mylist.insert(0,last)
mylist.append(first)

print("List after swapping :",mylist)


