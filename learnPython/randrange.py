#Randrange.
#Return a random number from range.
#Randrange([start], stop, [Step])
#Start argument is optional and default value is 0
# step argument is optional and default value is 1
# stop argument is mandatory.

#randrange(10)--> Generates a number from 0 to 9
#randrange(1,11)--> Generates a number from 1 to 10.
#randrange(1,11,2)--> Generates a number from 1,3,5,7,9,

from random import*
for i in range(10):
    print(randrange(5))