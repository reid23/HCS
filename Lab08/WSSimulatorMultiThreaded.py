#%%
# Author: Reid Dye

# This file contains the code to run world series simulations, except using multiple threads (4) to speed up computation.
# because throwing more computing power at your slow python algorithms is always the right answer

# At lower numbers of simulations, it's much slower than the standard single threaded simulator, but it's much faster
# when doing many simulations.

# currently, 1,000,000 simulations takes 186.84535884857178s (3:06.84, or 1.86845x10^(-4) sec/sim), using 4 cores on my macbook pro 2019.
# (all apps closed except vscode, prusaslicer, terminal, chrome (2 tabs), spotify, messages, which are all (except chrome) pretty lightweight)

# it's all very hacky, so definately not the best way to implement it, but it works.  As with the single-threaded optimized version,
# the comments are mostly out of date.

# as they say, "this software is provided as-is, without any warranty".  Run at your own risk.

import time
from WSPlayer import Player
from multiprocessing import Process, Pipe
import numpy as np

#%%
class Team:
    """this class represents a team.  It holds players and does 
    all processing related to home runs.  It also allows iteration 
    functionality similar to itertools.cycle.
    """
    def __init__(self, players:list):
        """constructor for team class

        Args:
            players (list): an iterable containing all of the player objects.
        """
        self.players = players
        self.numPlayers=len(players)
        self.n = 0
        self.score = 0
    def __next__(self):
        """implementation of iteration for Team class

        Returns:
            Player: the next player up to bat
        """
        self.n+=1 #n is the counter, it increments every time
        if self.n>=self.numPlayers: #this just puts the counter back to zero when it gets too big
            self.n = 0
        return self.players[self.n]
    def __iter__(self):
        """__iter__ implementation for Team class

        Returns:
            Team: self. Nothing happens here because no counters need to be reset every time you create a for loop; you want it to start from where it left off.
        """
        return self
    def __repr__(self):
        """__repr__ implementation for Team class.

        Returns:
            str: the string representation of self
        """
        output = 'Team('
        for i in self.players: output+= "\n\t" + repr(i)
        output += ")"
        return output
    def reset(self):
        """resets the home run counter for all players
        """
        for i in self.players:
            i.resetHomers()
        
    def getHomers(self):
        """returns all of the home runs, sorted correctly

        Returns:
            tuple: the sorted home runs, in the form ((playerName:str, homeRuns:int), ...)
        """
        output=[]
        for i in self.players:
            homers=i.getHomers()
            if not not homers:
                output.append((i.getName(), homers))

        #my lazy sorting, because i forget how gt, lt, ge, le, etc. are implemented for strings
        #sort several times from lowest to highest priority, so that ties are determined by the next highest priority untied thing
        output.sort(key=lambda a:a[0][3:]) #sort by last name
        output.sort(key=lambda a:-a[1])   #sort by home runs

        return output
        
    def addScore(self, points):
        """simple method to add $points to this team

        Args:
            points (int): the number of points to add
        """
        self.score+=points
    def getScore(self):
        """gets the current score

        Returns:
            int: the current score of this team
        """
        return self.score
    def resetScore(self):
        """resets the score.
        """
        self.score=0

#%%
#@jitclass
class Inning:
    """Inning contains all data and functions needed for one inning.  It keeps track
    of the bases with a virtual 3-bit SIPO shift register.

    The play by play summary is stored in log, and can be accessed with its getter.
    """
    words=['struck out', 'singled', 'doubled', 'tripled', 'homered']
    def __init__(self, number:int, team:str, single:bool):
        """constructor for Inning class

        Args:
            number (int): the inning number this object represents
            team (str): the name of the team playing
        """
        self.runs = 0
        self.single=single
        if single: self.log = '\nInning {num} - {tm}'.format(num=number, tm=team) #log the start
        self.outs = 0
        self.bases = [0,0,0] #our shift register is 3 bits long, for 3 bases (serial out represents home base)

    def _shiftBit(self, bit):
        """shift $bit into $register.  Modifies $register in place and returns the serial out bit. 
        Calling this function is analagous to setting SD_i, sending one clock pulse, then latching.

        Args:
            bit (any): object to shift into the register
            register (list): the shift register to be modified.

        Returns:
            int: the serial out bit. type depends on what was shifted in.
        """

        self.bases.insert(0, bit) #put new bit at beginning

        return self.bases.pop() #remove last element and return it (this is s_o)
    
    #@profile
    def addPlay(self, play, player): #1000x = 5.2261e-3 sec
        """adds a play to the inning, and deals with whatever that causes for the bases and scoring.  
        Returns False if the inning should end (too many outs), otherwise True.

        Args:
            play (int): the number of bases hit.  Must be 0, 1, 2, 3, or 4.
            player (str): the name of the player who is hitting, formatted correctly (use player.getName)

        Returns:
            bool: whether the inning should/can continue (ie false if this play was the third out of the inning)
        """
        if self.single: self.log+="\n{person} {result}".format(person=player, result=self.words[play]) #add to playByPlay
        
        # increment self.outs if the batter struck out, and return the appropriate 
        # value (to not continue the function, because we shouldn't shift anything
        # if the player struck out)
        if not play:
            self.outs+=1
            return self.outs<3

        # actually shift the bit
        # shifts 1 for the first base, then shifts enough zeroes to move 
        # everyone the appropriate amount.  For example, for a triple, 
        # this shifts in [1, 0, 0], so that there's now a player on third,
        # and everyone else has been pushed three bases.

        # if the serial out bit is non-zero for any given shift, the score 
        # (self.runs) is incremented, because a 1 in serial out 
        # represents a player reaching home base (leaving the register).
        # This information is then written to self.log.  

        for i in range(play):
            a=self._shiftBit(player if not i else 0)
            
            if not not a: #not not is fast bool()
                self.runs+=1
                if self.single:
                    self.log += ' ({person} scored)'.format(person=a)

        # then also return true because we know there wasn't a new out
        return True

    def getSummary(self):
        """get the string containing the formatted summary of this inning, so far.

        Returns:
            str: the summary.
        """
        return self.log #we do all the formatting when we write to self.log, so no work is needed here.  Just a getter method
    def getRuns(self):
        """get the current number of runs.  

        Returns:
            int: the current number of runs in this inning
        """
        return self.runs

#%%

###! END OF CLASSES

#load data
with (open('_astros.data', 'r') as astros,
      open('_braves.data', 'r') as braves):
      astros = Team([Player(*i) for i in eval(astros.read())])
      braves = Team([Player(*i) for i in eval(braves.read())])


def printGraph(p:list):
    """returns an ascii graph of the probabilities p

    Args:
        p (list): list of length 8, with all of the probabilities
    """
    #make sure its the right length
    #assert len(p) == 8, f'input list length is incompatable, expected len(p)==8 but received {len(p)}'

    #reorder the second half so it looks like a bell curve in the graph
    #because the odds should go a6, a7, b7, b6, etc to make sense
    p=p[0:4]+p[8:3:-1]

    #create graph basics
    maximum=max(p)
    graph = [
           '{maxVal}%|'.format(maxVal=round(maximum)).rjust(5), #max probability
            '    |',
            '    |', 
            '    |', 
           '{midVal}%|'.format(midVal=round(maximum/2)).rjust(5), #middle probability
            '    |',
            '    |', 
            '    |', 
            '  0%|', 
            '    |---------------------------------------', 
            '      a4   a5   a6   a7   b7   b6   b5   b4']
    
    # for each win scenario,
    #    iterate through each row in the graph
    #       if the row represents the right probability, put the datapoint.  
    #       else put the equivalent number of spaces.
    for i in p:
        index = 11-(round(8*(i/maximum))+2) #11 is len(graph)
        for j in range(9): #9 because there's 8 rows in the graph
            graph[j]+=' **  ' if j==index else '     '
            #the line above does the following faster:
            # if j==index: 
            #     graph[j] += ' **  '
            # elif j<9:
            #     graph[j] += '     '

    #then return a printable version
    return '\n'.join(graph)

#%%
#@jit(forceobj=True, nogil=True)
def simGame(single):
    """simulates one game.

    Returns:
        tuple: the results, in the form (summaries, scores) where summaries is a list of
        the summaries for each inning and scores is a list of the score after each inning, in
        the form [[astros_0, braves_0], [astros_1, braves_1], ... , [astros_n, braves_n]]
    """
    #init vars
    innings=0
    summaries = []
    scores = []
    #reset team scores from any previous games
    astros.resetScore()
    braves.resetScore()
    # loop while they're tied or haven't finished 9 innings:
    #    create inning object
    #    run astros inning
    #    add inning summary to summaries
    #    add inning runs to astros score

    #    creae inning object
    #    run braves inning
    #    add inning summary to summaries
    #    add inning runs to braves score

    #    add [astros_n, braves_n] to scores list

    #    increment innings counter
    while innings<9 or astros.getScore()==braves.getScore():
        inning = Inning(innings+1, "Astros", single)
        for player in astros:
            # inning.addPlay takes the number of bases ran, which we get using player.simHit, 
            # and the player's name, which we get pre-formatted with player.getName.

            # it returns a boolean value based on the number of outs, so we just check
            # that with an if and break out of the infinite for loop if inning.addPlay 
            # says the inning should be over.

            # the for loop is infinite because of how __next__ is implemented: it always 
            # just returns the next player up to bat.  It never runs out of players because 
            # it just cycles back to the start. Additionally, __iter__ doesn't reset the
            # counters, so we don't need to store the last player that hit in order to start
            # with them the next time; __next__ just picks up where it left off. This is why
            # we can just loop until the inning is over then forget about it.
            if not inning.addPlay(player.simHit(), player.getName()):
                break
        
        if single: #removing this append saves ~0.2s per 10000 ws sims
            summaries.append(inning.getSummary())
        astros.addScore(inning.getRuns())

        #this is the same as the astros inning
        inning = Inning(innings+1, "Braves", single)
        for player in braves:
            if not inning.addPlay(player.simHit(), player.getName()): 
                break

        if single: #same time savings
            summaries.append(inning.getSummary())
        braves.addScore(inning.getRuns())


        if single: scores.append([astros.getScore(), braves.getScore()])

        innings+=1
    if not single: scores=[[astros.getScore(), braves.getScore()]] #extra axis for compatability, this if also saves about the same amount of time
    return summaries, scores

#%%
#@jit(forceobj=True, nogil=True)
def simOneWS(single=False):
    """simulate one world series.

    Returns:
        tuple: the results of the world series, in the form (summaryForSingleWSShellOutputPreFormatted:str, playByPlayLogPreFormatted:str, multiSeriesRecapLineFormattedForFileOutput:str)
    """
    playByPlay, summary, singleWSSum = '', '', ''
    wsScore = [0, 0]
    astros.reset()
    braves.reset()
    for i in range(10): #just use big number
        summaries, scores = simGame(single) #actually simulate the game
        
        if scores[-1][0]>scores[-1][1]:
            wsScore[0]+=1
        else:
            wsScore[1]+=1

        if single: #save time if these logs are not needed
            # header for playbyplay log
            # this is the only reason i'm using a for loop instead of a while
            playByPlay += f'========== Game {i+1} ==========\n'
            
            for summ, score in zip(summaries, scores): #for each inning's data:
                playByPlay += f'{summ}\nScore: Astros: {score[0]}, Braves: {score[1]}\n' #add ths game's summary and scores to playByPlay
            
            #add the summary of this game, with the ordering right based on who's winning
            summary += f"Game {i+1}: {f'Braves: {scores[-1][1]}, Astros: {scores[-1][0]}' if scores[-1][0]<scores[-1][1] else f'Astros: {scores[-1][0]}, Braves: {scores[-1][1]}'}\n"
        

        if 4 in wsScore: #check if anyone's won the WS
            ### all the stuff for singleWSSum:
            astrosHomers, bravesHomers = '', '' #init vars

            for i in astros.getHomers(): astrosHomers+=" {name} {homes},".format(name=i[0], homes=i[1]) #format the sorted list into a presentable string
            for i in braves.getHomers(): bravesHomers+=" {name} {homes},".format(name=i[0], homes=i[1]) # ^
            
            #\n's expanded for readability, at the expense of the aesthetics
            #seriously this looks super weird with the string not indented
            if single: 
                singleWSSum=(
"""Results of World Series simulation:

{summ}

{team} win the series {score1}-{score2}


Home runs:
Astros:{aHomers}
Braves:{bHomers}
""".format(summ=summary, team='Braves' if wsScore[1]>wsScore[0] else 'Astros', score1=max(wsScore), score2=min(wsScore), aHomers=astrosHomers[:-1], bHomers=[bravesHomers[:-1]])) #as long as we don't put a comma it doesn't register as a tuple, and parens let the first line not be weirdly indented here


            ### all the stuff for multiSeriesStr (the thing to output to the file)
            else:
                multiSeriesStr = '{first} win in {num}'.format(first="Braves" if wsScore[1]>wsScore[0] else "Astros", num=sum(wsScore))
            # then break out of the 10x for loop because the ws is over and we shouldn't sim more games
            break

    #return stuff!
    if single:
        return singleWSSum, playByPlay
    else:
        return multiSeriesStr
    

#%%


def main():
    'main function!'

    parent0, child0 = Pipe()
    parent1, child1 = Pipe()
    parent2, child2 = Pipe()
    parent3, child3 = Pipe()

    number = input('''Welcome to the World Series Simulator!

This program will simulate a World Series matchup between the
Houston Astros and the Atlanta Braves.

Enter the number of World Series you'd like to simulate: ''')
    #wait for valid input
    while True:
        try:
            number=int(number)
            assert number>0
            break
        except ValueError:
            number = input(f'{number} is an invalid input. Try again: ')
    startTime=time.time()
    #if we only need to do one ws, do this.  Just does one and prints the stuff and writes to the file.
    if number==1:
        results = simOneWS(True) #simulate
        print(results[0])    #print preformatted shell output
        with open('WSPlayByPlay.log', 'w') as f:
            f.write(results[1]) #log preformatted play by play
            #by writing all the stuff at the end, we save a lot of computation time.  
            #writing to files is much slower that saving to a string in ram
    else:
        #you've probably only got four cores
        d=divmod(number, 4)
        perProcess=[d[0], d[0], d[0], d[0]+d[1]]

        a=Process(target=simMultiple, args=(perProcess[0], child0))
        b=Process(target=simMultiple, args=(perProcess[1], child1))
        c=Process(target=simMultiple, args=(perProcess[2], child2))
        d=Process(target=simMultiple, args=(perProcess[3], child3))

        a.start()
        b.start()
        c.start()
        d.start()

        
        aResults, aLog = parent0.recv()
        bResults, bLog = parent1.recv()
        cResults, cLog = parent2.recv()
        dResults, dLog = parent3.recv()

        results=aResults+bResults+cResults+dResults #adds elementwise because they're numpy arrays
        multiLog=aLog+bLog+cLog+dLog #concatenates because they're python lists

        a.join() #wait for each to finish
        b.join()
        c.join()
        d.join()



        
        #output stuff to file
        with open('WSmultiseries.log', 'w') as f:
            #header
            f.write('Astros-Braves World Series Simulation\n\n{mL}'.format(mL='\n'.join(['{k}: {v}'.format(k=counter+1, v=i) for counter, i in enumerate(multiLog)])))

        
        ### shell output
        #header
        shellOutput='\nResults of {num} World Series Simulations\n'.format(num=number)
        
        #get the probabilities by dividing each outcome's frequency by the total number of outcomes
        sumWins = sum(results)
        p = [round(i/sumWins*100, 1) for i in results] #create list of probabilities of each case happening

        #print the probabilities
        for i in range(8): shellOutput+='\nAstros win in {num}: {prob}%'.format(num=i+4 if i<4 else i, prob=p[i])

        ### print an ascii graph
        #title
        shellOutput+='\n     '+'percentage of games in each scenario:'.center(40)+'\n\n'

        #graph and all other shell output
        print(shellOutput+printGraph(p))


    endTime=time.time()

    print(f'\nTime taken for {number} simulations: {endTime-startTime}s')

#@jit(forceobj=True, nogil=True)
def simMultiple(num, conn):
    multiLog=[]
    # results = {
    #     'A4':0,
    #     'A5':0,
    #     'A6':0,
    #     'A7':0,
    #     'B4':0,
    #     'B5':0,
    #     'B6':0,
    #     'B7':0,
    # }
    results = {
        'Astros win in 4': 0,
        'Astros win in 5': 0,
        'Astros win in 6': 0,
        'Astros win in 7': 0,
        'Braves win in 4': 0,
        'Braves win in 5': 0,
        'Braves win in 6': 0,
        'Braves win in 7': 0,
    }
    for _ in range(num):
        WSData = simOneWS(False)
        results[WSData]+=1
    multiSeriesString=np.concatenate([[i[0]]*i[1] for i in results.items()]).ravel()
    np.random.shuffle(multiSeriesString) #to get realistic looking order, because threading messes up true order anyway
    conn.send((np.array(list(results.values())), multiSeriesString.tolist()))

    conn.close()
    
if __name__=='__main__': 
    # import cProfile
    # import pstats

    # with cProfile.Profile() as pr:
    #     main()

    # stats = pstats.Stats(pr)
    # stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    # stats.dump_stats(filename='needs_profiling.prof')
    main()