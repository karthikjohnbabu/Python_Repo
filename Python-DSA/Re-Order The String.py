# Python3 Program to implement
# the above approach
# Function to convert the strings
# to proper
def Convertstrings(s, index,n):
	res=list(s)
	str1=""
	for i in range(len(s)):
		res[index[i]-1]=s[i]
	for ele in res:
		str1 += ele
	return str1

# Driver Code
s = "abcd"
index = [2,4,3,1]
n=4
#dacb
print(Convertstrings(s, index,n))
