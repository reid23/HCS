from os import WSTOPSIG
from WSPlayer import Player
from WSGamestate import Inning
from WSTeam import Team

a = []
b = []

with open('_astros.data', 'r') as f:
    for i in eval(f.read()):
        a.append(Player(*i))
with open('_braves.data', 'r') as f:
    for i in eval(f.read()):
        b.append(Player(*i))

astros = Team(a)
braves = Team(b)

# print('astros:')
# print(repr(astros))

# print()

# print('braves:')
# print(repr(braves))

def simGame():
    innings=0
    summaries = []
    scores = []
    while innings<9 or astros.getScore()==braves.getScore():
        print(astros.getScore(), braves.getScore())
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
        scores.append([[astros.getScore()], [braves.getScore()]])

        innings+=1
    return summaries, scores

def printHomeRuns(sums):
    astros = 'Astros - '
    a = []
    braves = 'Braves - '
    b = []
    for i in sums:
        if 'homered' in i:


def simOneWS():
    playByPlay = ''
    summary = ''
    wsScore = [0, 0]
    for i in range(7):
        summaries, scores = simGame()
        playByPlay += f'========== Game {i+1} ==========\n'
        for summ, score in zip(summaries, scores): #for each inning's data:
            playByPlay += summ + '\n'
            playByPlay += f'Score: Astros: {score[0]}, Braves: {score[1]}\n'
        print(wsScore)
        if scores[-1][0]>scores[-1][1]:
            wsScore[0]+=1
        if scores[-1][0]<scores[-1][1]:
            wsScore[1]+=1
        summary += f"Game {i+1}: {f'Braves: {scores[-1][1]}, Astros: {scores[-1][0]}' if scores[-1][0]<scores[-1][1] else f'Astros: {scores[-1][0]}, Braves: {scores[-1][1]}'}\n"
        if 4 in wsScore:
            print('Results of World Series simulation:\n')
            print(summary)
            print(f"\n{'Braves' if wsScore[0]>wsScore[1] else 'Astros'} win the series {max(wsScore)}-{min(wsScore)}\n")
            print('\nHome runs: \n')
            printHomeRuns(summaries)

            break

    

    

def simMoreThanOneWS(times):
    pass
    

print()
number = input(
'''Welcome to the World Series Simulator!

This program will simulate a World Series matchup between the
Houston Astros and the Atlanta Braves.

Enter the number of World Series you'd like to simulate: '''
)
while True:
    try:
        number=int(number)
        break
    except ValueError:
        number = input(f'{number} is an invalid input. Try again: ')

print(*simGame())
input()
simOneWS()