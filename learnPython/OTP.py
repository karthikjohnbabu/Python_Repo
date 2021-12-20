#Write a program to generate 6 digit random number which can be used as OTP.
#Here random digits (randint) always going to generate 0 to 9.

#1st approach
from random import*
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')#414414

#2nd Approach
from random import*
otp=''
for i in range(6):
    otp=otp+str(randint(0,9))
print(otp)#604019

