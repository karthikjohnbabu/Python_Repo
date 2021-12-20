class Bird:
    wings=2
    @classmethod
    def fly(cls,name):
        print('{} flying with {} wings'.format(name,cls.wings))
b=Bird()
b.fly
Bird.fly('Parrot')
Bird.fly('Eagle')