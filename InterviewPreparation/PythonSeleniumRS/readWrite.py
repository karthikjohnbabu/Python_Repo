file= open('test.txt')
#read all the contents of the file
#read n number of characters by passing parameter
#print(file.read(5))
#read one single line at a time readline()
#print(file.readline())
#print(file.readline())

line=file.readline()
while line!="":
    print(line)
    line =file.readline()


for line in file.readlines():
    print(line)
file.close()