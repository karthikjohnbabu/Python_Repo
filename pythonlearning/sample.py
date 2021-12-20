a=[10,20,30,50,256]
print(type(a))
b=bytearray(a)
print(type(b))
b[3]=40
for i in b:
    print(i)#ValueError: byte must be in range(0, 256)


