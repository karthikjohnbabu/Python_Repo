#[15,6,7,10,12,20,10,28,10]
#Approach 3 using counter method which is present inside the collection package.
from collections import Counter
mylist= [15,6,7,10,12,20,10,28,10]
x=10
dic = Counter(mylist) #{ 5:1, 6:1, 7:1, 10:3.....} counter returns the data in key value pairs.
print("{} has occured {} times".format(x,dic[x]))
