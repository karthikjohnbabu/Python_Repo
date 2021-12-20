#working with math module.

#For microsoft python examination this topis is very important.
#Python provided inbuilt math module.
#This module defines several functions which can be used for mathematical operations
#The Main important functions are.
#sqrt(x)
#ceil(x)
#floor(x)
#log(x)
#sin(x)
#tan(x)

# Python certification question from math module.
#1. you are creating a function that manipulates a number. The function has the following requirements.
#2. A float value is passed to the function.
#3. The function must take absolute value of the float( ignore the sign)
#4. Any deciman after the integer must be removed.
#5. which two function should be used ?

#options:
#1.Math frexp()
#2.Math floor()
#3.Math fabs()
#4.Math Fmod()
#5.Math Ceil()

# First we need to choose fabs(x)
# Second we need to choose floor(x)

from math import*
print(floor(fabs(-12.893)))#12