# N = 11
# arr[] = {1,1,2,2,3,3,4,4,4,4,5}
# x = 4, y = 5
# Output: 4
# Explanation:
# frequency of 4 is 4.
# # frequency of 5 is 1.
# Given an array arr[] of size N and two elements x and y, use counter variables to find which element appears most in the array, x or y.
# If both elements have the same frequency, then return the smaller element.
# Note:  We need to return the element, not its count.
arr=[1,1,2,2,3,3,4,4,4,4,5]
x=4
y=5
n=11
def majorityWins(arr, n, x, y):
    counterX = 0
    counterY = 0
    for i in range(n):
        if x==arr[i]:
            counterX+=1
        if y==arr[i]:
            counterY+=1
    if counterX>counterY:
        return x
    elif counterX<counterY:
        return y
    else:
        return min(x,y)

print(majorityWins(arr,n,x,y))

