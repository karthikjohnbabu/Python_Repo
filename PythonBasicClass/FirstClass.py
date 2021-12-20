values=[1,2,"Karthik",4,5]
#list is a data type that allows multiple values and can be different data types.
print(values[0]) #1
print(values[3]) #4
print(values[4]) #5
print(values[-1])#5
print(values[1:3])#[2,'karthik']
values.insert(3,"Babu") #inserting a new value at a specified index
print(values)
values.append("End") #append method always appends data to the last index of the list.
print(values)
values[2]="KARTHIK" #updating
print(values)
del values[0]
print(values)
