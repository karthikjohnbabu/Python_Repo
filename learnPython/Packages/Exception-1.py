#where is else block used in real time
f=None
try:
  f=open('abc.txt','r')
except:
    print('Some problem while locating or opening file')
else:
    print('File opened successfully')
    print('The content of the file')
    print('#'*30)
    print(f.read())
finally:
    if f is not None:
        f.close();