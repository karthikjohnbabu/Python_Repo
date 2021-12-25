from collections import UserList
#Creating a List where
# Deletion is not allowed
class MyList(UserList):
    #Function to stop deletion
    # from list
    def remove(self, s=None):
        raise RuntimeError("Deletion not allowed")
    #Function to stop pop from List
    def pop(self,s=None):
        raise RuntimeError('Deletion not allowed')

#Driver's Code
L=MyList([1,2,3,4])
print("original List")
#inserting to list
L.append(5)
print('After Insertion')
print(L)

#Deleting from List
L.remove()


