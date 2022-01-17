
# Author: Reid Dye

# This file contains the code to run world series simulations, as per the Lab08 specs.

#* I used top-down design for planning, then prototyping to implement that.  I planned out that
#* I would need the main function to handle input, output, and calling simulations multiple times.
#* Then I would need a function to simulate one world series, which would in turn need a function
#* to simulate one game.  That's how I came up with the structure for this file.add()

#* For the other objects, I knew I would need a player, and I also added a team class and an 
#* inning class.  The team class takes care of tracking and reporting home runs, and allows me to
#* iterate through all of the players in a team in a similar way to itertools.cycle.  I added
#* the inning class to keep track of things that happened at the inning level, namely logging the
#* score based on the player's runs.

#* I chose top-down design because I knew that I would need to keep track of all of these different
#* peices of data which all needed to be reset at different times.  Writing these directly into 
#* functions or as part of simGame/simOneWS would be hard to understand and debug.  Therefore, I
#* put everything into its own class. 

#* However, once I'd planned out everything, I implemented it all in a spiral development style.
#* I started with Player, importing the data, and simulating, then added Team, then Inning, then
#* simGame, then simWS, then main with all of the input, output, and logging.  It was all done 
#* based on the classes though, not just making all of the classes and working on all of them 
#* concurrently, which helped speed up the process a lot.


from WSPlayer import Player

#* Team and Inning classes below. Classes end on line 208. 
#C-u 176 C-n
#* Then there's functions.  Main() is on 
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
        self.n = 0
        self.score = 0
    def __next__(self):
        """implementation of iteration for Team class

        Returns:
            Player: the next player up to bat
        """
        self.n+=1 #n is the counter, it increments every time
        if self.n>=len(self.players): #this just puts the counter back to zero when it gets too big
            self.n-=len(self.players)
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
        output={}
        for i in self.players:
            if not i.getHomers()==0:
                output[i.getName()]=i.getHomers()
        output=list(output.items())

        #my lazy sorting, because i forget how gt, lt, ge, le, etc. are implemented for strings
        #sort several times from lowest to highest priority, so that ties are determined by the next highest priority untied thing
        output.sort(key=lambda a:a[0][3]) #sort by last name first char
        output.sort(key=lambda a:a[0][4]) #sort by last name second char
        output.sort(key=lambda a:a[0][5]) #sort by last name third char
        output.sort(key=lambda a:-a[1])    #sort by home runs
        #! CHECK ABOUT d'Arnold
        #? HOW TO SORT?'
        #? maybe make players sortable

        return tuple(output)
        
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
class Inning:
    """Inning contains all data and functions needed for one inning.  It keeps track
    of the bases with a virtual 3-bit SIPO shift register.

    The play by play summary is stored in log, and can be accessed with its getter.
    """
    def __init__(self, number:int, team:str):
        """constructor for Inning class

        Args:
            number (int): the inning number this object represents
            team (str): the name of the team playing
        """
        self.runs = 0
        self.log = f'\nInning {number} - {team}' #log the start
        self.outs = 0
        self.bases = [0,0,0] #our shift register is 3 bits long, for 3 bases (serial out represents home base)
    def _shiftBit(self, bit, register:list):
        """shift $bit into $register.  Modifies $register in place and returns the serial out bit. 
        Calling this function is analagous to setting SD_i, sending one clock pulse, then latching.

        Args:
            bit (any): object to shift into the register
            register (list): the shift register to be modified.

        Returns:
            int: the serial out bit. type depends on what was shifted in.
        """
        s_o = register[-1] #s_o is serial out
        register[:] = [bit]+register #have to do [:] to re assign elements instead of re assigning "register" pointer
        register[:] = register[:-1] #chop off last bit, to keep the register at length 3.  We've already saved this last bit in s_o.
        return s_o
    def addPlay(self, play, player):
        """adds a play to the inning, and deals with whatever that causes for the bases and scoring.  
        Returns False if the inning should end (too many outs), otherwise True.

        Args:
            play (int): the number of bases hit.  Must be 0, 1, 2, 3, or 4.
            player (str): the name of the player who is hitting, formatted correctly (use player.getName)

        Returns:
            bool: whether the inning should/can continue (ie false if this play was the third out of the inning)
        """
        self.log+=f"\n{player} {['struck out', 'singled', 'doubled', 'tripled', 'homered'][play]}" #add to playByPlay
        
        # increment self.outs if the batter struck out, and return the appropriate 
        # value (to not continue the function, because we shouldn't shift anything
        # if the player struck out)
        if play==0:
            self.outs+=1
            return False if self.outs>=3 else True

        # actually shift the bit
        # shifts 1 for the first base, then shifts enough zeroes to move 
        # everyone the appropriate amount.  For example, for a triple, 
        # this shifts in [1, 0, 0], so that there's now a player on third,
        # and everyone else has been pushed three bases.

        # if the serial out bit is 1 for any given shift, the score 
        # (self.runs) is incremented, because a 1 in serial out 
        # represents a player reaching home base (leaving the register).
        # This information is then written to self.log.  

        for i in range(play):
            a=self._shiftBit(player if i==0 else 0, self.bases)
            if a!=0: self.log += f' ({a} scored)'
            self.runs+=1 if bool(a) else 0 #TODO: ask is this okay "$player homered ($player scored) ($player1 scored)"

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
            [type]: [description]
        """
        return self.runs

###! END OF CLASSES

#load data
with (open('_astros.data', 'r') as astros,
      open('_braves.data', 'r') as braves):
      astros = Team([Player(*i) for i in eval(astros.read())])
      braves = Team([Player(*i) for i in eval(braves.read())])

def printGraph(p:list):
    """prints an ascii graph of the probabilities p

    Args:
        p (list): list of length 8, with all of the probabilities
    """
    #make sure its the right length
    assert len(p) == 8, f'input list length is incompatable, expected len(p)==8 but received {len(p)}'

    #reorder the second half so it looks like a bell curve in the graph
    #because the odds should go a6, a7, b7, b6, etc to make sense
    p=p[0:4]+p[8:3:-1]

    #create graph basics
    graph = [
           f'{round(max(p))}%|'.rjust(5), #max probability
            '    |',
            '    |', 
            '    |', 
           f'{round(max(p)/2)}%|'.rjust(5), #middle probability
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
        index = len(graph)-(round(8*(i/max(p)))+2)
        for j in range(len(graph)):
            if j==index: 
                graph[j] += ' **  '
            elif j<9:
                graph[j] += '     '

    #then print the actual thing (go through and print each element of the list)
    for i in graph: print(i)

def simGame():
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
        inning = Inning(innings+1, "Astros")
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
        
        summaries.append(inning.getSummary())
        astros.addScore(inning.getRuns())

        #this is the same as the astros inning
        inning = Inning(innings+1, "Braves")
        for player in braves:
            if not inning.addPlay(player.simHit(), player.getName()): 
                break
        summaries.append(inning.getSummary())
        braves.addScore(inning.getRuns())


        scores.append([astros.getScore(), braves.getScore()])

        innings+=1
    return summaries, scores

def simOneWS():
    """simulate one world series.

    Returns:
        tuple: the results of the world series, in the form (summaryForSingleWSShellOutputPreFormatted:str, playByPlayLogPreFormatted:str, multiSeriesRecapLineFormattedForFileOutput:str)
    """
    playByPlay, summary, singleWSSum = '', '', ''
    wsScore = [0, 0]
    astros.reset()
    braves.reset()
    for i in range(100): #just use big number
        summaries, scores = simGame() #actually simulate the game

        # header for playbyplay log
        # this is the only reason i'm using a for loop instead of a while
        playByPlay += f'========== Game {i+1} ==========\n'
        
        for summ, score in zip(summaries, scores): #for each inning's data:
            playByPlay += f'{summ}\nScore: Astros: {score[0]}, Braves: {score[1]}\n' #add ths game's summary and scores to playByPlay
        
        if scores[-1][0]>scores[-1][1]:
            wsScore[0]+=1 #increment astros WS score
        if scores[-1][0]<scores[-1][1]:
            wsScore[1]+=1 #increment braves WS score
        
        #add the summary of this game, with the ordering right based on who's winning
        summary += f"Game {i+1}: {f'Braves: {scores[-1][1]}, Astros: {scores[-1][0]}' if scores[-1][0]<scores[-1][1] else f'Astros: {scores[-1][0]}, Braves: {scores[-1][1]}'}\n"

        if 4 in wsScore: #check if anyone's won the WS
            ### all the stuff for singleWSSum:
            astrosHomers, bravesHomers = '', '' #init vars

            for i in astros.getHomers(): astrosHomers+=f" {i[0]} {i[1]}," #format the sorted list into a presentable string
            for i in braves.getHomers(): bravesHomers+=f" {i[0]} {i[1]}," #^
            
            #\n's expanded for readability, at the expense of the aesthetics
            #seriously this looks super weird with the string not indented
            singleWSSum=(
f"""Results of World Series simulation:

{summary}

{'Braves' if wsScore[1]>wsScore[0] else 'Astros'} win the series {max(wsScore)}-{min(wsScore)}


Home runs:
Astros:{astrosHomers[:-1]}
Braves:{bravesHomers[:-1]}
""") #as long as we don't put a comma it doesn't register as a tuple, and parens let the first line not be weirdly indented here


            ### all the stuff for multiSeriesStr (the thing to output to the file)
            multiSeriesStr = f'{"Braves" if wsScore[1]>wsScore[0] else "Astros"} win in {sum(wsScore)}'

            # then break out of the 100x for loop because the ws is over and we shouldn't sim more games
            break

    #return stuff!
    return singleWSSum, playByPlay, multiSeriesStr
    

def main():
    'main function!'
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
    #if we only need to do one ws, do this.  Just does one and prints the stuff and writes to the file.
    if number==1:
        results = simOneWS() #simulate
        print(results[0])    #print preformatted shell output
        with open('WSPlayByPlay.log', 'w') as f:
            f.write(results[1]) #log preformatted play by play
            #by writing all the stuff at the end, we save a lot of computation time.  
            #writing to files is much slower that saving to a string in ram
    else:
        results = { #init var
            'A4':0,
            'A5':0,
            'A6':0,
            'A7':0,
            'B4':0,
            'B5':0,
            'B6':0,
            'B7':0,
        }

        #output stuff to fiel
        with open('WSmultiseries.log', 'w') as f:
            #header
            f.write('Astros-Braves World Series Simulation\n')

            #simulate all the WS's
            for i in range(number):
                WSData = simOneWS()[2] #do the simulation
                results[f'{WSData[0]}{WSData[-1]}']+=1 #increment the correct area in the results dict corrosponding to the result of the simulation
                f.write(f'{i+1}: {WSData}') #write the line to the file, with the ws number and the outcome.
        
        ### shell output
        #header
        print(f'Results of {number} World Series Simulations\n')
        
        #get the probabilities by dividing each outcome's frequency by the total number of outcomes
        wins = tuple(results.values())
        sumWins = sum(wins)
        p = [round(i/sum(results.values())*100, 1) for i in results.values()] #create list of probabilities of each case happening

        #print the probabilities
        for i in range(4): print(f'Astros win in {i+4}: {p[i]}%')
        for i in range(4): print(f'Braves win in {i+4}: {p[i+4]}%')

        ### print an ascii graph
        #title
        print('     '+'percentage of games in each scenario:'.center(40)+'\n')
        #actual graph
        printGraph(p)


    
if __name__=='__main__': main()
