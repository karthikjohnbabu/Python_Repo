class SportsNews:
    def sportsInfo(self):
        print('Sports information-1')
        print('Sports information-2')
        print('Sports information-3')
        print('Sports information-4')
class MovieNews:
    def moviesInfo(self):
        print('Movie information-1')
        print('Movie information-2')
        print('Movie information-3')
        print('Movie information-4')
class PolicticsNews:
    def policticsInfo(self):
        print('Polictis information-1')
        print('Polictis  information-2')
        print('Polictis  information-3')
        print('Polictis  information-4')

class KarthikNewsChannel:
    def __init__(self,sports,movies,politics):
        self.sports=sports
        self.movies=movies
        self.politics=politics
    def getTotalNews(self):
        print("Welcome to karthk's new channel")
        self.sports.sportsInfo()
        self.movies.moviesInfo()
        self.politics.policticsInfo()
sports=SportsNews()
movies=MovieNews()
politics=PolicticsNews()
knc=KarthikNewsChannel(sports,movies,politics)
knc.getTotalNews()




