class Alphabet:
    def __init__(self,value):
        self.value=value
    #getting the values
    def getValue(self):
        print('Getting Value')
        return self._value
    #Setting the values
    def setValue(self,value):
        print('Setting value to '+ value)
        self._value= value
    #deleting the values
    def delValue(self):
        print('Deleting value')
        del self._value
    value=property(getValue,setValue,delValue,)

#passing the value
x=Alphabet("GeeksforGeeks")
print(x.value)
x.value="gfg"




