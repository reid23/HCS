#%%
from random import uniform as r
# from numba import int32, float32, typeof, njit
# from numba.experimental import jitclass
# #%%
# spec=[
#     ('lastName', typeof('test')),
#     ('firstName', typeof('test')),
#     ('battingAverage', float32),
#     ('hits', int32),
#     ('doubles', int32),
#     ('triples', int32),
#     ('homeRuns', int32),
#     ('singles', int32),
#     ('fails', float32),
#     ('homers', int32),

# ]
# #%%
# @jitclass(spec)


class Player:
    def __init__(self, lastName, firstName, battingAverage, hits, doubles, triples, homeRuns):
        self.lastName=lastName
        self.firstName=firstName
        self.formattedName=f'{self.firstName[:1]}. {self.lastName}'
        self.battingAverage=battingAverage
        self.hits=hits
        self.doubles=doubles
        self.triples=triples
        self.homeRuns=homeRuns
        self.singles=hits-(doubles+triples+homeRuns)
        self.fails=(hits/battingAverage)-hits #total number of misses
        self.homers = 0


        self.upperBound = self.fails+self.singles+self.doubles+self.triples+self.homeRuns
        self.out=self.fails
        self.single=self.fails+self.singles
        self.double=self.single+self.doubles
        self.triple=self.double+self.triples

        self.randNums=[r(0, self.upperBound) for _ in range(100000)]
        for counter, i in enumerate(self.randNums):
            if i<self.out:
                self.randNums[counter] = 0
            elif self.out<=i<self.single:
                self.randNums[counter] = 1
            elif self.single<=i<self.double:
                self.randNums[counter] = 2
            elif self.double<=i<self.triple:
                self.randNums[counter] = 3
            else:
                self.homers+=1
                self.randNums[counter] = 4
        self.n=0

    def __repr__(self):
        return f"Player('{self.lastName}', '{self.firstName}', {self.battingAverage}, {self.hits}, {self.doubles}, {self.triples}, {self.homeRuns})"


    def simHit(self):
        val=self.randNums[self.n]
        self.n+=1
        if self.n==100000: self.n=0
        if val==4: self.homers+=1
        return val
    
    def getHomers(self):
        return self.homers
    def resetHomers(self):
        self.homers=0
    
    def getName(self):
        return self.formattedName

# %%