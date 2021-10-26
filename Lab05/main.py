'''
Author: Reid Dye

A game
'''

#* Import block
from reidList import reidList as r
from moreClasses import *
from graphics import *

#* Functions
def score(cells, win, p=None):
    #yahtzee logic:

    global quitButton #so I don't have to pass quitButton as an arg
    flag=False
    if not p:
        while True:
            p=win.getMouse()
            if quitButton.clicked(p):
                exit()
            for c in cells:
                if c.inBounds(p) and c.getName()!='total' and c.getLocked()==False:
                    c.lockScore()
                    flag=True
            if flag:
                for c in cells:
                    if not c.getLocked():
                        c.notLock()
                break
    else:
        if quitButton.clicked(p):
            exit()
        for c in cells:
            if c.inBounds(p) and c.getName()!='total' and c.getLocked()==False:
                c.lockScore()
                flag=True
        if flag:
            for c in cells:
                if not c.getLocked():
                    c.notLock()
        return flag

def rollDice(dyeList):
    output=r(length=len(dice))
    counter=0
    for d in dyeList:
        d.roll()
        output.set(counter, d.reid())
        counter+=1
    return output

def diceOut(dyeList):
    for d in dyeList:
        d.setAttr(positionRel=r(0,200))

def diceIn(dyeList):
    for d in dyeList:
        d.setAttr(positionAbs=r(d.getPos()(0),150))

def getDone(cells):
    for c in cells:
        if c.getVal()=='-':
            return False
    return True


#* Window setup for start dialogue
#set up window
w, h = 300, 300
win=GraphWin('Yahtzee', w, h)


#* First Screen: 
#       get player name
t=Text(Point(w/2, (h/2)-40), "What's your name?")
e=Entry(Point(w/2, h/2), 10)
startButton=Button(Point(w/2, (h/2)+40), "Start")
t.draw(win)
e.draw(win)
err=Text(Point(w/2, h/2+80), "Please enter a name.")
startButton.draw(win)
err.setTextColor('red')
errFlag=False
while True:
    startButton.waitClick()
    name=e.getText()
    if name=='': #because do: while doesn't exist
        if not errFlag:
            err.draw(win)
        errFlag=True
    else:
        break
if errFlag:
    err.undraw()
t.undraw()
e.undraw()
startButton.undraw()
win.close()

#* Window setup for main game
#set up window
w, h = 800, 800
win=GraphWin('Yahtzee', w, h)


#* Setup Game
#dye holder area
dyeMat=Rectangle(Point(50,50), Point(w-50, 250))
dyeMat.setFill('grey')
#player name label
player=Text(Point(w/2, 25), f'Player: {name}')
player.draw(win)
#create 5d6
#These are all names that would have been
#funny for me or my sister
willDye=Dye(Point(w/6, 150))
mayDye=Dye(Point(w/3, 150))
tyDye=Dye(Point(w/2, 150))
riderDye=Dye(Point((2*w)/3, 150))
yülDye=Dye(Point((5*w)/6, 150))

#so we can loop through the dice
dice=r(willDye, mayDye, tyDye, riderDye, yülDye)

dyeMat.draw(win)

for d in dice:
    d.draw(win)

#width of each cell: 40
#width of all cells: 520
#half of all cell width: 260
types=r('1s', '2s', '3s', '4s', '5s', '6s', 'three\nof a\nkind', 'four\nof a\nkind', 'full\nhouse', 'small\nstra-\night', 'large\nstra-\night', 'chance', 'yaht-\nzee', 'total')
cells=r()
print('type of reidList object:', type(cells))
for t in types:
    cells.append(ScoreCell(Point(((w/2)+((len(cells)-6.5)*40)), h-150), t))
for c in cells:
    c.draw(win)

rollButton=Button(Point(w/2, h/2 - 100), 'ROLL!', r(100, 30), draw=True, win=win)
msgbox=MsgBox(win, Point(w/2, h/2 + 150), r(200, 75), 'Click roll to begin.', draw=True)
playAgainButton=Button(Point(w/2, h/2), 'Play Again!', r(150, 100))
gameTracker=Rectangle(Point(150, h-20), Point(w-150, h-70))
gameTrackerLine=Line(Point(w, h-20), Point(w, h-70))
games=0
best=0
gamesText=Text(Point((w/2)-75, h-45), 'Games Played: 0')
scoreText=Text(Point((w/2)+75, h-45), 'Best Score: 0')
gameTracker.draw(win)
gameTrackerLine.draw(win)
gamesText.draw(win)
scoreText.draw(win)

bonusMessageDrawn=False
bonusMessage=Text(Point(w/2, h/2), 'Nice! 1s-6s sum to >=63 points.\n+35 bonus points.')

quitButton=Button(Point(35, 10), 'Quit', color='red', draw=True, win=win)



#*start game!
while True:
    while getDone(cells)==False:
        skipEndScoringFlag=False
        #rollButton.waitClick()
        while True: #substitute for button.waitClick() so that it works with the quit button
            p=win.getMouse()
            if quitButton.clicked(p):
                exit()
            if rollButton.clicked(p):
                break
        msgbox.setText('Click the dice you would like to keep.\nClick roll to roll again.\nOr click a cell to score your roll now.')
        firstRoll=True
        for i in range(3):
            #roll dice and get values
            rolls=r()
            for d in dice:
                if d.getPos()(1)>200 or firstRoll==True:
                    if firstRoll:
                        d.setAttr(positionRel=r(0, 200))
                    d.roll()
                    rolls.append(d.reid())
                else:
                    rolls.append(d.reid())
            firstRoll=False

            #calculate score, at this point in time
            for c in cells:
                c.prelimCalc(rolls)
            #calculate and set total cell's value
            #not in prelimCalc because it requires external data other than dice
            curScores=r()
            for c in cells.getRange(0, 13):
                if c.getVal()=='-' or c.getVal()=='None':
                    pass
                else:
                    curScores.append(int(c.getVal()))
            cells(-1).setValue('?')

            #on last iter, don't let the user change the dice anymore
            if i==2:
                continue
            #wait for user to choose dice and click roll
            breakFlag=False
            while True:
                p=win.getMouse()
                if quitButton.clicked(p):
                    exit()
                if score(cells, win, p):
                    breakFlag=True
                    break
                for d in dice:
                    if d.clicked(p):
                        if d.getPos()(1)>200:
                            d.setAttr(positionRel=r(0,-200))
                        else:
                            d.setAttr(positionRel=r(0, 200))
                        continue
                if rollButton.clicked(p):
                    break
            if breakFlag:
                skipEndScoringFlag=True
                break
            
        if not skipEndScoringFlag:
            msgbox.setText('Click the cell where you\nwould like to place this score.')
            score(cells, win)
        curScores=0
        for c in cells.getRange(0, 13):
            if c.getVal()=='-' or c.getVal()=='None':
                pass
            else:
                curScores+=int(c.getVal())
        cells(-1).setValue(str(curScores))


        diceIn(dice)

        msgbox.setText('Next round!\nClick roll to begin.')

    #*end of game stuff
    
    #upper bonus:
    upperSum=0
    for c in cells.getRange(0, 6):
        upperSum+=int(c.getVal())
    if upperSum>=63:
        bonusMessage.draw(win)
        bonusMessageDrawn=True

    #calculate total score again
    curScores=0
    for c in cells.getRange(0, 13):
        if c.getVal()=='-' or c.getVal()=='None':
            pass
        else:
            curScores+=int(c.getVal())
    if bonusMessageDrawn:
        curScores+=35
    cells(-1).setValue(str(curScores))
    
    games += 1
    gamesTextVar='Games Played: ' + str(games)
    if curScores>best:
        best=curScores
    scoreTextVar='Best Score: ' + str(best)
    gamesText.setText(gamesTextVar)
    scoreText.setText(scoreTextVar)
    msgbox.setText('Game over!  Final scores are shown.')
    playAgainButton.draw(win)
    while True:
        p=win.getMouse()
        if quitButton.clicked(p):
            exit()
        if playAgainButton.clicked(p):
            break
    for c in cells:
        c.reset()
    for d in dice:
        d.reset()
    playAgainButton.undraw()
    bonusMessage.undraw()
    msgbox.setText('Click Roll! to begin!')