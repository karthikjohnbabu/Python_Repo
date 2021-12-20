#Choice Function
#To Generate a random object from list, tuple, string etc.
# It wont return random number
# From the list of object I want to generate a random object.

IPL_Teams_2021= ['RCB','CSK','SRH','RR','DD','MI','KP','KNR']
from random import*
print(choice(IPL_Teams_2021))

#Here there is a loop hole.  THis choice function will work only for idexable sequence.
#This choice function will work for list, tuple and not for set.
#Because in set there is no indexing concept applicable becausre there is no order concept in set.

from random import*
IPL_Teams_2021= {'RCB','CSK','SRH','RR','DD','MI','KP','KNR'}
#print(choice(IPL_Teams_2021))#TypeError: 'set' object is not subscriptable

from random import choice
alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(choice(alphabets))#C

from random import choice
alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(5):
    print(choice(alphabets))#C