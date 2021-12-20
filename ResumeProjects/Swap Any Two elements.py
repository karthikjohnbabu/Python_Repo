#Approach 1 using simple swap

mylist= [23,65,19,90] #index or position starts from 0
print(mylist)
pos1, pos2 = 1,3 #65 90 here based on the positions we have swapped the values.
mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
print(mylist)

#Approach 2 using the pop function
mylist= [23,65,19,90]
pos1, pos2 = 1,3
first_element= mylist.pop(pos1) # 65
second_element= mylist.pop(pos2-1)# after 65 poping out we have only 23,19,90 Now there is no value there in position 3.

mylist.insert(pos1,second_element)
mylist.insert(pos2,first_element)

print(mylist)

#Approach 3 using tuple variable.

mylist= [23,65,19,90]
pos1, pos2 =1,3
get=(mylist[pos1],mylist[pos2])
mylist[pos2],mylist[pos1]=get
print(mylist)

