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
    """Player class.
    """
    def __init__(self, lastName, firstName, battingAverage, hits, doubles, triples, homeRuns):
        """constructor for the Player class

        Args:
            lastName (str): the player's last name
            firstName (str): the player's first name
            battingAverage (float): the player's batting average
            hits (int): the number of hits in the ws
            doubles (int): the number of doubles in the ws
            triples (int): the number of triples in the ws
            homeRuns (int): the number of home runs in the ws
        """
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

        #calculate probabilities, and the buckets
        self.upperBound = self.fails+self.singles+self.doubles+self.triples+self.homeRuns
        self.out=self.fails
        self.single=self.fails+self.singles
        self.double=self.single+self.doubles
        self.triple=self.double+self.triples

        #create the probabilities
        self.randNums=[r(0, self.upperBound) for _ in range(100000)]

        #convert floats to ints 0-4 representing the hits
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
                self.randNums[counter] = 4

        # iterator var for the random numbers
        self.n=0

    def __repr__(self):
        """repr for Player class

        Returns:
            str: the repr string
        """
        return f"Player('{self.lastName}', '{self.firstName}', {self.battingAverage}, {self.hits}, {self.doubles}, {self.triples}, {self.homeRuns})"


    def simHit(self):
        """simulates one hit, and returns the number of bases run

        Returns:
            int: the number of bases the player ran.
        """
        val=self.randNums[self.n] #number of bases is just next in the list
        self.n+=1 #increment n for next time
        if self.n==100000: self.n=0 #reset n if its too big
        if val==4: self.homers+=1
        return val
    
    def getHomers(self):
        """get the number of homers this player has hit

        Returns:
            int: the number of homers
        """
        return self.homers
    def resetHomers(self):
        """resets the homer counter
        """
        self.homers=0
    
    def getName(self):
        """gets the formatted name

        Returns:
            str: this player's name, in the form '$FIRST_INITIAL. $LAST_NAME'
        """
        return self.formattedName

# %%