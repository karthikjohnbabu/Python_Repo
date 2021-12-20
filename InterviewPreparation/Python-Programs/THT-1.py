str1=(input('Enter the first string: ')).lower()
str2=input('Enter the second string: ').lower()
options= int(input('Please choose the options:[1/2] '))
#opt1 should contain all the characters which are present in str1 but NOT present in str2.
result=''
if options==1:
    for x in str1:
        if x not in str2:
            result=result+x
    print("Option 1 output is:",result)
#op2 should contain all the characters which are present in str2 but NOT present in str1.
if options==2:
    for x in str2:
        if x not in str1:
            result=result+x
    print("Option 2 output is:",result)

