class student:
    '''
    class developved by karthik for demo
    '''
    def __init__(self):
        self.name='karthik'
        self.rollno=101
        self.marks=75
    def talk(self):
        print('Hello I am',self.name)
        print('My rollno is', self.rollno)
        print('My mark is',self.marks)
s=student()
s.talk()
