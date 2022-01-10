class Team:
    def __init__(self, players):
        self.players = players
        self.n = 0
        self.score = 0
    def __next__(self):
        self.n+=1
        if self.n>=len(self.players):
            self.n-=len(self.players)
        return self.players[self.n]
    def __iter__(self):
        return self
    def __repr__(self):
        output = 'Team('
        for i in self.players: output+= "\n\t" + repr(i)
        output += ")"
        return output
    def addScore(self, points):
        self.score+=points
    def getScore(self):
        return self.score
