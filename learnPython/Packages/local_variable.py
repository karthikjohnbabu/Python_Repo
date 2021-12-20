class Test:
    @staticmethod
    def average(list):
        result=sum(list)/len(list)#result is a local variable
        print('The Avreage of the list elements:',result)
list=[10,20,30,40,50]
Test.average(list)



