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
from threading import Thread
class randBuffer:
    def __init__(self):
        self.num=[]
        self.t=Thread(target=self.genNums)
    def pop(self):
        return self.num.pop()

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

    def __repr__(self):
        return f"Player('{self.lastName}', '{self.firstName}', {self.battingAverage}, {self.hits}, {self.doubles}, {self.triples}, {self.homeRuns})"


    def simHit(self):
        val=r(0, self.upperBound)
        if val<self.out:
            return 0
        elif self.out<=val<self.single:
            return 1
        elif self.single<=val<self.double:
            return 2
        elif self.double<=val<self.triple:
            return 3
        else:
            self.homers+=1
            return 4
    
    def getHomers(self):
        return self.homers
    def resetHomers(self):
        self.homers=0
    
    def getName(self):
        return self.formattedName

# %%