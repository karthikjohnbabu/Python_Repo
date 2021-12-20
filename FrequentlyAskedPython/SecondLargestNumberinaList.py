#method 2
mylist = [10,20,4,45,99]
new_list= set (mylist)
new_list.remove(max(new_list))
print(new_list)# {4,10,45,20}
print(max(new_list))
