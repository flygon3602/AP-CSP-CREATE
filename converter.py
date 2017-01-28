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
J1=question('The fastest train in the world is in Japan', 'b', ['a)True', 'b)False'] )
J2=question('There are four different writing systems in Japan: Romaji, Katakana, Hiragana, and Kanji.', 'a', ['a)True','b)False'] )
J3=question('The World’s largest fish market is held in Japan?', 'a', ['a)True', 'b)False'])
J4=question('Coffee is very popular in Japan?', 'a', ['a)True', 'b)False'])
J5=question('Japan has the oldest continuing monarchy?', 'b', ['a)True', 'b)False'])
J6=question('The majority of smartphone users in the world are from Japan?', 'b', ['a)True', 'b)False'])
J7=question('Japan honors ancestors and the dead by letting lighted lanterns into the sky?', 'a', ['a)True', 'b)False'])
J8=question('Slurping noodles is considered a very rude gesture in Japan?', 'b', ['a)True', 'b)False'])
J9=question('Japan sells square watermelons commercially?', 'a', ['a)True', 'b)False'])
J10=question("In Japan, sleeping on the job is considered a sign of one's willingness to be fired?", 'b', ['a)True', 'b)False'])
J11=question('Japan has a highway passing through a major commercial building?', 'a', ['a)True', 'b)False'])
J12=question("Godzilla is a Japanese citizen.", 'a', ['a)True', 'b)False'])
J13=question('Tipping servers is rude in Japan?', 'a', ['a)True', 'b)False'])
J13=question('The 100th pokemon to appear in the Japanese pokedex is PIKACHU!', 'b', ['a)True', 'b)False'])
while score<point_choice:
    if question
