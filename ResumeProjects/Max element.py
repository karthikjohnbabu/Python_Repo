arr = [1,2,3,4,5]

#finding max element
max= arr[0]
n=len(arr)
for i in range(1, n):
    if arr[i]>max:
        max= arr[i]
print("maximum elemenet is",max)
