#write a program to find the number of occurences of each character present in the given string?
#input: ABCSHASJHJH
#Output: A-2,b=1,c=3

s='abbacba'
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
print(l)
for ch in l:
    print('{} occurs {} times'.format(ch,s.count(ch)))
