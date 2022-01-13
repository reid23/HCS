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


def simGame():
    innings=0
    summaries = []
    scores = []
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
    playByPlay = ''
    summary = ''
    singleWSSum=''
    wsScore = [0, 0]
    astros.reset()
    braves.reset()
    for i in range(7):
        summaries, scores = simGame()
        playByPlay += f'========== Game {i+1} ==========\n'
        for summ, score in zip(summaries, scores): #for each inning's data:
            playByPlay += summ + '\n'
            playByPlay += f'Score: Astros: {score[0]}, Braves: {score[1]}\n'
        if scores[-1][0]>scores[-1][1]:
            wsScore[0]+=1
        if scores[-1][0]<scores[-1][1]:
            wsScore[1]+=1
        
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
    

# print()
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