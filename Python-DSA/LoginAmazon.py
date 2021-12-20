string = 'Bangalore'
dictionary = {}
for char in string:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char]=1
print(dictionary)
