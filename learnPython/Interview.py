#Write a program to generate a password of length 6.
#Where 1,3,5 characters are alphabets symbols
#2,4,6 characters are digits

#sample : Alphanumeric Password: a2c4e6

from random import*
alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
print(choice(alphabets),choice(digits),choice(alphabets),choice(digits),choice(alphabets),choice(digits),sep='')

from random import*
alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits="0123456789"
print(choice(alphabets+digits),choice(alphabets+digits),choice(alphabets+digits),choice(alphabets+digits),
      choice(alphabets+digits),choice(alphabets+digits),sep='')