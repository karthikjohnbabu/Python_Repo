ItemsInCart=0

if ItemsInCart != 2:
    #raise Exception('Products cart not matching')
    pass

assert(ItemsInCart==0)

try:
    with open('test1.txt', 'r') as reader:
         reader.read()

except Exception as e:
    print(e)

finally:
    print("Cleaning up resources")
