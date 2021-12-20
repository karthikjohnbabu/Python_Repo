def listaverage(list):
    length=len(list)
    sum=0
    for i in list:
        sum=sum+i
    print('The Average of the list is:',sum//length)

list=[10,20,30,40]
listaverage(list)