#There are 5 important functions under random module.
#1. Random()
#2. Uniform()
#3. Randint()
#4. Randrange()
#5. choice()

#Random() Function.
#This functions always generate some float value between 0 and 1.
# 0<x<1(Greater than 0 and lesseer than 1.
# But it will not generate 0 and 1 at any point of time
# Random function will not take any input or argument.

from random import*
print(random())#0.4348144392984421

#if i want to print such random niumber for 10 times
from random import*
for i in range(10):
    print(random())