mylist= [12,35,9,56,24]
size= len(mylist)
temp = mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp
print("List after swapping :",mylist)


#Approach 2
mylist= [12,35,9,56,24]
mylist[0],mylist[-1]=mylist[-1],mylist[0]
print("List after swapping :",mylist)


#Approach 3 using a tuple variable.
mylist= [12,35,9,56,24]
get=(mylist[-1],mylist[0]) # packing 24 12
mylist[0],mylist[-1]=get #unpacking
print("List after swapping :",mylist)


#Approach 4 using the * operand
mylist= [12,35,9,56,24]
start,*middle, end =mylist
print(start)
print(middle)
print(end)
mylist=[end,*middle,start]
print("List after swapping :",mylist)

#Approach 5 using pop () built in function

mylist= [12,35,9,56,24]
first=mylist.pop(0) # 12
last= mylist.pop(-1) #24
mylist.insert(0,last)
mylist.append(first)
print("List after swapping :",mylist)

