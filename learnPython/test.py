# You are writing an application that uses the sqrt function.
#The program must refer the function using the name sq.
# which of the following import statment is required to use?

#Member aliasing concept.

from math import sqrt as sq
print(sq(4))#2.0

#consider the code below. What will be the ouput?
import math
l=[str(round(math.pi))for i in range(1,6)]
print(l)

#for i in range(1,6)--> Means 1 to 5 that is 5 times
#pi= 3.145 after round it is 3  and later convert it to str. '3'
#'3'*5= '3','3','3','3','3'
#['3','3','3','3','3']