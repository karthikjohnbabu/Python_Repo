#write a generator function  to generate values for countdown with provided max value?
def countdonw_generator(num):
    while num >=1:
        yield num
        num= num-1
g=countdonw_generator(10)
import time
for x in g:
    print(x)
    time.sleep(1)