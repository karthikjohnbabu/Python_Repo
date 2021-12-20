#Note: From overriding method of child class, we can call parent class method also by using super() method.

class parent:
    def property(self):
        print('Land+Gold+Cash+Power')
    def marry(self):
        print('Sarojamma') #this method is called as overriden method
class child(parent):
    def marry(self):
        super().marry()
        print('Katrina kaif')#This method is called as overriding method
c=child()
c.property()
c.marry()

