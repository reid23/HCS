from random import uniform as r
class Player:
    def __init__(self, lastName, firstName, battingAverage, hits, doubles, triples, homeRuns):
        self.lastName=lastName
        self.firstName=firstName
        self.battingAverage=battingAverage
        self.hits=hits
        self.doubles=doubles
        self.triples=triples
        self.homeRuns=homeRuns
        self.singles=hits-(doubles+triples+homeRuns)
        self.fails = hits/battingAverage #total number of misses
        self.homers = 0

    def __repr__(self):
        return f"Player('{self.lastName}', '{self.firstName}', {self.battingAverage}, {self.hits}, {self.doubles}, {self.triples}, {self.homeRuns})"

    def simHit(self):
        val=r(0, self.fails+self.singles+self.doubles+self.triples+self.homeRuns)
        if val<=self.fails:
            return 0
        elif self.fails<val<=self.fails+self.singles:
            return 1
        elif self.fails+self.singles<val<=self.fails+self.singles+self.doubles:
            return 2
        elif self.fails+self.singles+self.doubles<val<=self.fails+self.singles+self.doubles+self.triples:
            return 3
        else:
            self.homers+=1
            return 4
    
    def getHomers(self):
        return self.homers
    def resetHomers(self):
        self.homers=0
    
    def getName(self):
        return f'{self.firstName[:1]}. {self.lastName}'
