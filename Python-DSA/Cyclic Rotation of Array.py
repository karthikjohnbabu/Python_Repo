n=5
arr=[1,2,3,4,5]
k=2

def rotate(arr, n):
    x = arr[n - 1]
    for i in range(n - 1, 0, -1):
        print(i)
        arr[i] = arr[i - 1]
    arr[0] = x
    return arr
print(rotate(arr,n))
