#finding min element
arr = [1,2,3,4,5]
min= arr[0]
n=len(arr)
for i in range(1, n):
    if arr[i]<min:
        min= arr[i]
print("Minimum element is", min)
