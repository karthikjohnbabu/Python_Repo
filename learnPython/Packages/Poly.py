class Duck:
    def talk(self):
        print('Quack,Quack')
class Dog:
    def talk(self):
        print('Bow ..Bow')
class Cat:
    def talk(self):
        print('Meow Meow')
class Goat:
    def talk(self):
        print('Myaah Myahh')
def f1(obj):
    obj.talk()
l=[Duck(),Cat(),Dog(),Goat()]
for obj in l:
    f1(obj)

