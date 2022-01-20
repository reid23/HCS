class Team:
    def __init__(self, players):
        self.players = players
        self.numPlayers=len(players)
        self.n = 0
        self.score = 0
    def __next__(self):
        self.n+=1
        if self.n>=self.numPlayers:
            self.n = 0 #wrap around the list
        return self.players[self.n]
    def __iter__(self):
        return self
    def __repr__(self):
        output = 'Team('
        for i in self.players: output+= "\n\t" + repr(i)
        output += ")"
        return output
    def reset(self):
        for i in self.players:
            i.resetHomers()
        
    def getHomers(self):
        output={}
        for i in self.players:
            if not i.getHomers()==0:
                output[i.getName()]=i.getHomers()
        output=list(output.items())

        #my lazy sorting, because i forget how gt, lt, ge, le, etc. are implemented for strings
        output.sort(key=lambda a:a[0][3]) #sort by last name first char
        output.sort(key=lambda a:a[0][4]) #sort by last name second char
        output.sort(key=lambda a:a[0][5]) #sort by last name third char
        output.sort(key=lambda a:-a[1])    #sort by home runs

        return tuple(output)
        
    def addScore(self, points):
        self.score+=points
    def getScore(self):
        return self.score
    def resetScore(self):
        self.score=0
