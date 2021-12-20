file= open('test.txt')
#print(file.read()) #it will read the entire file content
#print(file.read(7)) #it will read each character in the line including the charater(enter) for next line
print(file.readline()) #first line is read
print(file.readline())# second line is read
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

