
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
    of the bases like a shift register which latches after every clock pulse.

    The play by play summary is stored in log, and can be accessed with its getter.
    """
    def __init__(self, number:int, team:str):
        """constructor for Inning class

        Args:
            number (int): the inning number this object represents
            team (str): the name of the team playing
        """
        self.runs = 0
        self.log = f'\nInning {number} - {team}'
        self.outs = 0
        self.bases = [0,0,0]
    def _shiftBit(self, bit, register:list): #modifies the list in place, returns the serial output
        s_o = register[-1] #s_o is serial out
        register[:] = [bit]+register #have to do [:] to re assign elements instead of re assigning "register" pointer
        register[:] = register[:-1]
        return s_o
    def addPlay(self, play, player):
        self.log+=f"\n{player} {['struck out', 'singled', 'doubled', 'tripled', 'homered'][play]}"
        if play==0:
            self.outs+=1
            return False if self.outs>=3 else True

        for i in range(play):
            a=self._shiftBit(player if i==0 else 0, self.bases)
            if a!=0: self.log += f' ({a} scored)'
            self.runs+=1 if not not a else 0
        return True

    def getSummary(self):
        return self.log
    def getRuns(self):
        return self.runs


with (open('_astros.data', 'r') as astros,
      open('_braves.data', 'r') as braves):
      astros = Team([Player(*i) for i in eval(astros.read())])
      braves = Team([Player(*i) for i in eval(braves.read())])

def printGraph(p:list):
    """prints an ascii graph of the probabilities p

    Args:
        p (list): list of length 8 
    """
    assert len(p) == 8, f'input list length is incompatable, expected len(p)==8 but received {len(p)}'
    p=p[0:4]+p[8:3:-1]

    #create graph basics
    graph = [
           f'{round(max(p))}%|'.rjust(5),
            '    |',
            '    |', 
            '    |', 
           f'{round(max(p)/2)}%|'.rjust(5), 
            '    |',
            '    |', 
            '    |', 
            '  0%|', 
            '    |---------------------------------------', 
            '      a4   a5   a6   a7   b7   b6   b5   b4']
    
    #for each win scenario,
    #   iterate through each row in the graph
    #       if the row represents the right probability, put the datapoint.  
    #       else put the equivalent number of spaces.
    for i in p:
        index = len(graph)-(round(8*(i/max(p)))+2)
        for j in range(len(graph)):
            if j==index: 
                graph[j] += ' **  '
            elif j<9:
                graph[j] += '     '
    for i in graph:
        print(i)

def simGame():
    innings=0
    summaries = []
    scores = []
    astros.resetScore()
    braves.resetScore()
    while innings<9 or astros.getScore()==braves.getScore():
        inning = Inning(innings+1, "Astros")
        for player in astros:
            if not inning.addPlay(player.simHit(), player.getName()):
                break
        summaries.append(inning.getSummary())
        astros.addScore(inning.getRuns())


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
    playByPlay, summary, singleWSSum = '', '', ''
    wsScore = [0, 0]
    astros.reset()
    braves.reset()
    for i in range(100): #just use big number
        summaries, scores = simGame()
        playByPlay += f'========== Game {i+1} ==========\n'
        for summ, score in zip(summaries, scores): #for each inning's data:
            playByPlay += f'{summ}\nScore: Astros: {score[0]}, Braves: {score[1]}\n' #add summary and scores to playByPlay
        if scores[-1][0]>scores[-1][1]:
            wsScore[0]+=1 #increment astros score
        if scores[-1][0]<scores[-1][1]:
            wsScore[1]+=1 #increment braves score
        
        summary += f"Game {i+1}: {f'Braves: {scores[-1][1]}, Astros: {scores[-1][0]}' if scores[-1][0]<scores[-1][1] else f'Astros: {scores[-1][0]}, Braves: {scores[-1][1]}'}\n"
        if 4 in wsScore:
            singleWSSum = 'Results of World Series simulation:\n\n'
            singleWSSum += summary+'\n'
            singleWSSum += f"\n{'Braves' if wsScore[1]>wsScore[0] else 'Astros'} win the series {max(wsScore)}-{min(wsScore)}\n\n"
            singleWSSum += '\nHome runs:\n'

            astrosHomers = ''
            for i in astros.getHomers():
                astrosHomers+=f" {i[0]} {i[1]},"
            singleWSSum += f'Astros:{astrosHomers[:-1]}\n'

            bravesHomers = ''
            for i in braves.getHomers():
                bravesHomers+=f" {i[0]} {i[1]},"
            singleWSSum += f'Braves:{bravesHomers[:-1]}\n'

            multiSeriesStr = f'{"Braves" if wsScore[1]>wsScore[0] else "Astros"} win in {sum(wsScore)}'

            break
    return singleWSSum, playByPlay, multiSeriesStr
    

def main():
    number = input('''Welcome to the World Series Simulator!

This program will simulate a World Series matchup between the
Houston Astros and the Atlanta Braves.

Enter the number of World Series you'd like to simulate: ''')
    while True:
        try:
            number=int(number)
            break
        except ValueError:
            number = input(f'{number} is an invalid input. Try again: ')

    if number==1:
        results = simOneWS()
        print(results[0])
        with open('WSPlayByPlay.log', 'w') as f:
            print(results[1], file=f)
    else:
        results = {
            'A4':0,
            'A5':0,
            'A6':0,
            'A7':0,
            'B4':0,
            'B5':0,
            'B6':0,
            'B7':0,
        }
        with open('WSmultiseries.log', 'w') as f:
            print('Astros-Braves World Series Simulation\n', file=f)
            for i in range(number):
                WSData = simOneWS()[2]
                results[f'{WSData[0]}{WSData[-1]}']+=1
                print(f'{i+1}: {WSData}', file=f)
        print(f'Results of {number} World Series Simulations\n')
        wins = tuple(results.values())
        sumWins = sum(wins)
        p = [round(i/sum(results.values())*100, 1) for i in results.values()]

        for i in range(4): print(f'Astros win in {i+4}: {p[i]}%')
        for i in range(4): print(f'Braves win in {i+4}: {p[i+4]}%')


        print('     '+'percentage of games in each scenario:'.center(40))
        print()
        printGraph(p)

        #print graph


    
if __name__=='__main__': main()

#%%
# a='''
#  24%|
#     |
#     |
#     |
#  12%|
#     |
#     |
#     |
#   0%|
#     |---------------------------------------
#       b4   b5   b6   b7   a7   a6   a5   a4
# '''
# b=a.split('\n')[1:-1]
# print(repr(b))
# %%
