'''
Author: Reid Dye

A game
'''

#* Import block
from reidList import reidList as r
from moreClasses import *
from graphics import *

#* Functions
#other way, cleaner, more encapsulated
#will use this
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
        d.setAttr(positionRel=r(0,-200))


#* Window setup
#set up window
w, h = 800, 800
win=GraphWin('Yahtzee', w, h)


#* First Screen: 
#       get player name
t=Text(Point(w/2, (h/2)-40), "What's your name?")
e=Entry(Point(w/2, h/2), 10)
startButton=Button(Point(w/2, (h/2)+40))
t.draw(win)
e.draw(win)
startButton.draw(win)
startButton.waitClick()
name=e.getText()
t.undraw()
e.undraw()
startButton.undraw()


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

win.getMouse()

rollDice(dice)
diceOut(dice)

win.getMouse()

diceIn(dice)






win.getMouse()