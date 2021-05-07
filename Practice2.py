class team_haedal:

    def __init__(self,team_name,number,lang):
        self.team_name = team_name
        self.number = number
        self.lang = lang

    def info(self):
        print(f'팀이름 : {self.team_name}')
        print(f'인원 수 : {self.number}')
        print(f'사용 언어 : {self.lang}')
        print()

    def lang(self, lang_num):
        print(self.lang[lang_num])

team1 = team_haedal('1팀', 30, ['c','c#','python'])
team2 = team_haedal('2팀', 35, ['css','jvs','html'])
team3 = team_haedal('3팀', 25, ['java','c++','Go'])

team1.info()
team2.info()
team3.info()

