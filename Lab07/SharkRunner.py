'''
Author: Derik Liu

The SharkRunner main function incorporates all other classes to create the game.
It primarily executes turn logic and calls the necessary methods from the other classes
in the right order.
'''



from Fish import *
from SharkGUI import *
from Button import *
from Shark import *

tracker=StalemateTracker()

def main():
    #initialize all the objects demanded by sharkGUI, then initializes and draws sharkGUI
    fisha = Fish(1, 1, 'a')
    fishb = Fish(1,1, 'b')
    fishc = Fish(1,1, 'c')
    fishList = [fisha,fishb,fishc]
    shark = Shark()
    startButton = Button(Point(1.5, 0), 0.75, 0.25, "Start")
    quitButton = Button(Point(3,0), 0.75, 0.25, "Quit")
    moveButton = Button(Point(4.5, 0), 0.75, 0.25, "Move")
    gui = Gui(shark, fisha, fishb, fishc, startButton,quitButton, moveButton, None, None, None, None)
    startButton.activate()
    quitButton.activate()
    moveButton.activate()
    #loop that allows user to continue playing multiple rounds, never breaks unless quit button is clicked
    programLoop = True
    while programLoop:
        for i in range(1,4):
            gui.undraw(i)
        gui.resetEntries()
        while True:
            gui.waitButtonClick(Gui.START)
            entryList = gui.getEntry()
            if not not entryList: break
            else: gui.thingMethod(Gui.MSGBOX, 'setText', True, False,
                                  'Invalid input. Enter three unique fish coordinates in the form x,y in the entry boxes, \nwhere x and y are integers in [1,10], then click Start.')
        #resets shark position. redundant on first round, adds visual clarity on subsequent rounds
        shark.reset()
        gui.moveAnimal(gui.SHARK, shark.getPos(), shark.getDirection(), shark.getFleeMode())
        gui.thingMethod(Gui.MSGBOX, 'setText', True, False, 'Click Move to move the animals.')
        for index, fish in enumerate(fishList):
            fish.setPos(entryList[index])
            gui.moveAnimal(index+1, entryList[index], fish.getDirection(), False)
        #the bulk of the turn logic starts here       
        continueGame = True
        stalemate = 0
        #continueGame loop runs the turn sequencing for each "round" of the game
        tracker.addState([fish.getPos() for fish in fishList], [fish.getDirection() for fish in fishList], shark.getPos())
        while continueGame == True: 
            tracker.addState([fish.getPos() for fish in fishList], [fish.getDirection() for fish in fishList], shark.getPos())
            gui.waitButtonClick(Gui.MOVE)
        #on each move turn, generates a ghost fish object to simulate the possible position of each fish if any positions overlap, the fish with the lower priority
        #has its turn skipped, fish a has highest priority and fish c lowest
            skip, ghostFishPosList = [], []
            for index, fish in enumerate(fishList):
                ghostFish = Fish(fish.getPos()[0], fish.getPos()[1], 'a')
                ghostFish.setDirection(fish.getDirection())
                ghostFish.turn(shark.getPos())
                ghostFishPosList.append(ghostFish.getPos())
                del ghostFish
            if ghostFishPosList[1] == ghostFishPosList[0]: skip.append(1)
            if ghostFishPosList[2] in ghostFishPosList[0:2]: skip.append(2)
            #passes a fish turn and moves the fish to new position. skips movement if collision detected
            for index, fish in enumerate(fishList):
               if index in skip: pass
               else:
                    fish.turn(shark.getPos())
                    gui.moveAnimal(index+1, fish.getPos(), fish.getDirection(), fish.getFleeMode())
            shark.setPos(shark.turn([fisha.getPos(), fishb.getPos(), fishc.getPos()]))
            gui.moveAnimal(gui.SHARK, shark.getPos(), shark.getDirection(), shark.getFleeMode())
            #moves the chasing box
            gui.undraw(gui.CHASINGBOX)
            gui.moveChasingBox(gui.getThing(shark.getChasing()).getPos())
            gui.draw(gui.CHASINGBOX)
            #fish eating logic: at the end of all object movements, a fish is "eaten" if a fish and shark share the same location
            for index, fish in enumerate(fishList):
                if fish.getPos() == shark.getPos():
                    stalemate = 0
                    fish.eaten()
                    gui.moveAnimal(index+1, fish.getPos(), fish.getDirection(), fish.getFleeMode())
                    if index == 0: fishName = 'Fish A'
                    if index == 1: fishName = 'Fish B'
                    if index == 2: fishName = 'Fish C'
                    gui.thingMethod(Gui.MSGBOX, 'setText', True, False, 'You caught ' + fishName + '!')
                    #undraws the chasing box for visual clarity
                    gui.undraw(gui.CHASINGBOX)
            if stalemate == 1: gui.thingMethod(Gui.MSGBOX, 'setText', True, False, 'Click Move to move the animals.')
            #stalemate counter increments with each move turn and resets when a fish is eaten
            tracker.addState([fish.getPos() for fish in fishList], [fish.getDirection() for fish in fishList], shark.getPos()) #records current positions
            stalemate += 1
            if stalemate >= 75: #game ends at 75 moves without eating a fish
                gui.thingMethod(Gui.MSGBOX, 'setText', True, False, 'The shark starved. Enter new fish coordinates and click Start to try again.')
                continueGame = False
            if tracker.checkStalemate(): #checks if the current gamestate has been repeated 3 times already
                gui.thingMethod(Gui.MSGBOX, 'setText', True, False, 'The shark starved. Enter new fish coordinates and click Start to try again.')
                continueGame = False
            if not (fishList[0].alive() or fishList[1].alive() or fishList[2].alive()):
                gui.thingMethod(Gui.MSGBOX, 'setText', True, False, 'All the fish have been eaten. Enter new fish coordinates and click Start to try again.')
                continueGame = False
        tracker.reset()
        gui.undraw(gui.CHASINGBOX)
        #when the continueGame loop is broken, the fish positions and values are reset
        for index, fish in enumerate(fishList):
            fish.reset()

if __name__=='__main__': 
    main()