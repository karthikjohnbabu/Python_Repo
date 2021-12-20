class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno= rollno
        self.marks=marks
    def talk(self):
        print('Hello I am', self.name )
        print('My rollno is ', self.rollno)
        print('My Marks are:', self.marks)
s=student('karthik',101,75)
s.talk()
t=student('john',102,60)
t.talk()
u=student('babu',103,50)
u.talk()
