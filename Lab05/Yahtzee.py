'''
Author: Reid Dye

This is just main.py, but without the functions: maximum expansion!  Probably more wordy than necesary.
'''


#* Import block
from ReidList import ReidList as r
from ScoreCell import ScoreCell
from Die import Dye
from Button import Button
from MsgBox import MsgBox
from graphics import *
from time import sleep
from os import system



#* Window setup for start dialogue
#set up window
w, h = 300, 300
win=GraphWin('Yahtzee', w, h)


#* First Screen: 
#set up everything
t=Text(Point(w/2, (h/2)-40), "What's your name?")
e=Entry(Point(w/2, h/2), 10)
startButton=Button(Point(w/2, (h/2)+40), "Start")
t.draw(win)
e.draw(win)
err=Text(Point(w/2, h/2+80), "Please enter a name.")
startButton.draw(win)
err.setTextColor('red')
errFlag=False
#wait for start button to be clicked, and for name to be inputted
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
win.close() #end first screen

#fun fun fun
class InigoMontoyaError(Exception):
    def __init__(self, message="You are dead. Cause of death: Inigo Montoya.\nAlso, quit it with your book.  Nobody's going to buy it."):
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return self.message

if name=='Count Rugen':
    system("osascript -e 'Set Volume 5'")
    win=GraphWin('Easter Egg', 300, 300)
    t=Text(Point(150, 150), 'Hello.')
    t.draw(win)
    system('say Hello.')
    sleep(3)
    t.setText('My name is Inugo Montoya.')
    system('say "My name is inugo montoya."')
    sleep(2)
    t.setText('prepare.')
    system('say prepare')
    sleep(0.7)
    t.setText('to.')
    system("osascript -e 'Set Volume 6'")
    sleep(0.7)
    t.setTextColor('red')
    t.setText('DIE!')
    system("osascript -e 'Set Volume 10'")
    system('say DIE!')
    sleep(4)
    raise InigoMontoyaError

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
yülDye=Dye(Point((5*w)/6, 150)) #aaaay let's go full unicode support for python

#so we can loop through the dice
dice=r(willDye, mayDye, tyDye, riderDye, yülDye)

dyeMat.draw(win)

for d in dice:
    d.draw(win)

#width of each cell: 40
#width of all cells: 520
#half of all cell width: 260

#a list of all the types of cells
types=r('1s', '2s', '3s', '4s', '5s', '6s', 'three\nof a\nkind', 'four\nof a\nkind', 'full\nhouse', 'small\nstra-\night', 'large\nstra-\night', 'chance', 'yaht-\nzee', 'total')
cells=r()

#make all the cells
for t in types:
    cells.append(ScoreCell(Point(((w/2)+((len(cells)-6.5)*40)), h-150), t))

#draw all the scoreCells
for c in cells:
    c.draw(win)

#create a bunch of trackers and game elements
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
while True: #this loop is the multi-game loop: the program loops this once per game.
    while True: #this is the once-per-round loop: the program loops this once per scoreCell scored.
        #this section checks whether to break out of this loop (ending the current game)
        toBreak=True
        for c in cells:
            if c.getVal()=='-':
                toBreak=False
        if toBreak:
            break
        
        #reset this flag
        skipEndScoringFlag=False


        #the first step is to wait for the roll button to be clicked.
        #rollButton.waitClick()
        while True: #substitute for button.waitClick() so that it works with the quit button
            p=win.getMouse()
            if quitButton.clicked(p):
                exit()
            if rollButton.clicked(p):
                break
        #then display the directions
        msgbox.setText('Click the dice you would like to keep.\nClick roll to roll again.\nOr click a cell to score your roll now.')
        firstRoll=True
        for i in range(3): #for three rolls
            #roll dice and get values
            rolls=r()
            for d in dice:
                if d.getPos()(1)>200 or firstRoll==True:
                    if firstRoll: #because on first roll dice need to be tossed out
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
            cells(-1).setValue('?') #set total cell's value

            #on last iter, don't let the user change the dice anymore
            if i==2:
                continue

            #wait for user to choose dice and click roll
            breakFlag=False
            while True:
                p=win.getMouse()
                if quitButton.clicked(p):
                    exit()
                flag=False #now that we've gotten a click, score it!  if it's not in a valid scoreCell, then check if it's clicking on any of the dice.  
                for c in cells:
                    if c.inBounds(p) and c.getName()!='total' and c.getLocked()==False:
                        c.lockScore()
                        flag=True
                if flag:
                    for c in cells:
                        if not c.getLocked():
                            c.notLock()
                if flag:
                    breakFlag=True
                    break #this means that the user has scored their roll before using up their 3 rolls
                
                #dice re-arranging
                for d in dice:
                    if d.clicked(p):
                        if d.getPos()(1)>200:
                            d.setAttr(positionRel=r(0,-200))
                        else:
                            d.setAttr(positionRel=r(0, 200))
                        continue
                if rollButton.clicked(p):
                    break #go back to top of for loop when user is ready
            if breakFlag:
                skipEndScoringFlag=True #need multiple flags and breaks because you cant just break 3;
                #this case represents if the user scores early.  Then we don't have to score it when we break out of this for loop.
                break
            
        if not skipEndScoringFlag:
            #get the user's chosen scoreCell and score their roll
            msgbox.setText('Click the cell where you\nwould like to place this score.')
            flag=False #reset this
            while True:
                p=win.getMouse() #get mouse click
                if quitButton.clicked(p):
                    exit()
                for c in cells: #check if the click is in a valid cell, and if so, score and lock that cell
                    if c.inBounds(p) and c.getName()!='total' and c.getLocked()==False:
                        c.lockScore()
                        flag=True
                if flag: #check if the prev. loop found anything.  If so, unscoreify all the other cells
                    for c in cells:
                        if not c.getLocked():
                            c.notLock()
                    break
        curScores=0
        for c in cells.getRange(0, 13): #in all cells except total, add the score the the cum. sum
            if c.getVal()=='-' or c.getVal()=='None':
                pass
            else:
                curScores+=int(c.getVal())
        cells(-1).setValue(str(curScores)) #set the total cell's value


        for d in dice:
            d.setAttr(positionAbs=r(d.getPos()(0),150)) #reset the dice for the next round

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
        curScores+=35 #actually add the bonus points
    cells(-1).setValue(str(curScores))
    
    #increment the game counter and best score thing
    games += 1
    gamesTextVar='Games Played: ' + str(games)
    if curScores>best:
        best=curScores
    scoreTextVar='Best Score: ' + str(best)
    gamesText.setText(gamesTextVar)
    scoreText.setText(scoreTextVar)
    msgbox.setText('Game over!  Final scores are shown.')
    playAgainButton.draw(win)

    #play button logic
    while True:
        p=win.getMouse()
        if quitButton.clicked(p):
            exit()
        if playAgainButton.clicked(p):
            break

    #reset everything so it's like the beginning
    for c in cells:
        c.reset()
    for d in dice:
        d.reset()
    playAgainButton.undraw()
    bonusMessage.undraw()

    #instructions
    msgbox.setText('Click Roll! to begin!')