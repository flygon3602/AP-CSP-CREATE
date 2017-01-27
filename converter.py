point_choice='100, 200, or, 300 point game (enter 100, 200, or 300)'
class player:
    def __init__(self, name, weighting, score):
        self.name=name
        self.weighting=weighting
        self.score=score

class category:
    def __init__(self, name, question):
        self.name=name
        self.question=question

class question:
    def __init__(self,description,answer,option):
        self.description=description
        self.answer=answer
        self.option=option
player1 = player(str(input('name: ')), )
while score<point_choice:
    if question
