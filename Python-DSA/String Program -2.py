#write a program to access each character in string in forward and Backward direction using while loop
s='Learning python is easy'
n=len(s)
i=0
print('Forward Direction')
while i<n:
    print(s[i],end='')
    i=i+1
print('Backward Direction')
i=-1
while i>=-n:
    print(s[i],end='')
    i=i-1

