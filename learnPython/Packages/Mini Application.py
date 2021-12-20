#Example
class movie:
    '''This class was developved by karthik for demo'''
    def __init__(self,title,hero,heroine):#There are argument variable
        self.title= title
        self.hero = hero
        self.heroine = heroine
    def info(self):
        print('Movie Name',self.title)
        print("Hero Name:",self.hero)
        print('Heroine Name:',self.heroine)
list_of_movie=[]
while True:
    title= input('Enter movie name:')
    hero= input('Enter Hero name:')
    heroine= input('Enter Heroine name:')
    m=movie(title,hero,heroine)
    list_of_movie.append(m)
    print('Movie Added successfully')
    option= input('Do you want to add one more movie:[yes/no]:')
    if option.lower()=='no':
        break
print('All movies information')
for movie in list_of_movie:
    movie.info()
    print()
