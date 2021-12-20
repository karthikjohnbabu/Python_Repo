#input : arr[] = {10,20,4}
#max output : 20
#min Output : 4

#Approach 1 using logic
#Assume arr[0]to be the maximum
#compare 1 with 2, and if 1 is greater than 2. Let the number 1 be there in the same place. Likewise compare 1 with all the numbers.
arr = [1,2,3,4,5]

#finding max element
max= arr[0]
n=len(arr)
for i in range(1, n):
    if arr[i]>max:
        max= arr[i]
print("maximum elemenet is",max)

#finding min element
arr = [1,2,3,4,5]
min= arr[0]
n=len(arr)
for i in range(1, n):
    if arr[i]<min:
        min= arr[i]
print("Minimum element is", min)


