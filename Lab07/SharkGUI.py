'''
Author: Reid Dye

This file contains the Gui class, which handles
all graphical elements of the Shark lab.
'''

from graphics import *
class Gui:
    SHARK, FISHA, FISHB, FISHC, START, QUIT, MOVE, ENTRYA, ENTRYB, ENTRYC, MSGBOX, CHASINGBOX = list(range(0, 12)) #index constants
    NORTH, EAST, SOUTH, WEST = '000', '090', '180', '270'
    def __init__(self, shark, fisha, fishb, fishc, start, quit, move, entrya, entryb, entryc, msgbox, winTitle='SharkGUI', winSize=[770, 840], drawButtons=True, drawAnimals=True, drawEntries=True, drawMsgBox=True, drawGrid=True):
        """Constructor for Gui class

        Args:
            shark (shark object): the shark object
            fisha (fish object): the first fish object
            fishb (fish object): the second fish object
            fishc (fish object): the third fish object
            start (button object): the start button
            quit (button object): the quit button
            move (button object): the move button
            entrya (None): depricated, pass None.  Argument not removed for backwards compatability (aka laziness)
            entryb (None): depricated, pass None.  Argument not removed for backwards compatability (aka laziness)
            entryc (None): depricated, pass None.  Argument not removed for backwards compatability (aka laziness)
            msgbox (None): depricated, pass None.  Argument not removed for backwards compatability (aka laziness)
            winTitle (str, optional): the title of the game window. Defaults to 'SharkGUI'.
            winSize (list, optional): the dimensions (in px) of the game window. Defaults to [770, 840].
            drawButtons (bool, optional): whether or not to draw the buttons. Defaults to True.
            drawAnimals (bool, optional): whether or not to draw the animals. Defaults to True.
            drawEntries (bool, optional): whether or not to draw the entries. Defaults to True.
            drawMsgBox (bool, optional): whether or not to draw the message box. Defaults to True.
            drawGrid (bool, optional): whether or not to draw the grid. Defaults to True.
        """
        chasingBox=Rectangle(Point(0.5, 0.5), Point(1.5, 1.5))
        chasingBox.setWidth(5)
        chasingBox.setOutline('green')
        msgbox = Text(Point(5.5, -0.5), 'Welcome to the fish game! Please enter fish coordinates of the form x,y in the entry boxes, then click Start.')
        self.objects=[
                shark, 
                fisha, fishb, fishc, 
                start, quit, move, 
                Entry(Point(6.5, 0), 5), Entry(Point(8, 0), 5), Entry(Point(9.5, 0), 5),
                msgbox, chasingBox]
        self.win=GraphWin(winTitle, winSize[0], winSize[1]) #make window
        self.win.setCoords(0, -1, 11, 11) #fix it so that grid locations are integers
        #create grid
        #just loops through rows and colums, creating squares at every location.
        self.grid=[Rectangle(Point(i-0.5, j-0.5), Point(i+0.5, j+0.5)) for i in range(1,11) for j in range(1,11)]

        #drawing all the stuff, if needed
        for animal in self.objects[0:4]: 
            animal.setImage(Image(Point(animal.getPos()[0], animal.getPos()[1]), animal.getImgPath().replace('___', (animal.getDirection()[0:2] + ('X' if animal.getFleeMode() else '0')))))
        if drawButtons:
            for button in self.objects[4:7]:
                for obj in button.getGraphicsObjects():
                    obj.draw(self.win) #draw all the buttons
        if drawAnimals:
            for animal in self.objects[0:4]:
                for obj in animal.getGraphicsObjects(): 
                    obj.draw(self.win) #draws all the animal objects
        if drawEntries:
            for entry in self.objects[7:10]: 
                entry.draw(self.win)
        if drawMsgBox: 
            self.objects[10].draw(self.win)
        if drawGrid:
            for rect in self.grid: rect.draw(self.win)
    def moveAnimal(self, animal, pos, rot, flee, absolutePos=False):
        """move an animal in the gui.add()

        Args:
            animal (int): The animal to move.  Pass a Gui class constant, like Gui.FISHC
            pos (list): the movement, in the form [x, y].  Relative or absolute, depending on absolutePos.add()
            rot (str): the animal's new angle.  pass a gui class constant, like Gui.NORTH
            flee (bool): what to show the animal's flee mode as
            absolutePos (bool, optional): whether pos should be interpreted as absolute or relative. Defaults to False (relative).
        """
        self.undraw(animal)
        if flee: rot=rot[0:2] + 'X'
        self.objects[animal].setImage(Image(Point(*self.objects[animal].getPos()), self.objects[animal].getImgPath().replace('___', rot)))
        self.draw(animal)
        if absolutePos:
            pos[0] += self.objects[animal].getPos()[0]
            pos[1] += self.objects[animal].getPos()[1]
    def resetEntries(self):
        for i in range(3):
            self.objects[i+Gui.ENTRYA].setText('fish '+['A', 'B', 'C'][i])
    def drawGrid(self):
        'draws the grid'
        for i in self.grid: 
            i.draw(self.win)
    def undrawGrid(self):
        'undraws the grid'
        for i in self.grid: 
            i.undraw()
    def getChasingBoxPos(self): 
        'gets the position of the chasing box'
        return self.objects[11].getCenter().getX(), self.objects[11].getCenter().getY()
    def moveChasingBox(self, pos, absolutePos=True):
        """moves the chasing box

        Args:
            pos (list): the new position of the chasing box, in the form [x, y].
            absolutePos (bool, optional): whether pos should be interpreted as absolute or relative. Defaults to True (absolute).
        """
        if absolutePos: 
            pos=[pos[0]-self.getChasingBoxPos()[0], pos[1]-self.getChasingBoxPos()[1]]
        self.objects[11].move(pos[0], pos[1])
    def getThing(self, thing):
        """returns any of the graphics objects, given one of the gui class constants"""
        return self.objects[thing]
    def setThing(self, thing, newObject):
        """sets the [thing] to [newObject], given [thing] as gui class constant"""
        self.objects[thing]=newObject
    def thingMethod(self, thing, func, eva=True, exe=True, *args, **kwargs): #so we don't have to import graphics anywhere else
        """runs one of the objects methods.  Exists because I origionally thought we couldn't use the graphics library anywhere other than SharkGUI.

        Args:
            thing (int): the thing whose method is to be run.  Pass a Gui class constant, like Gui.FISHC
            func (str): the method's name
            eva (bool, optional): whether to evaluate the method and return the output. Defaults to True.
            exe (bool, optional): whether to simply execute the function then return. Defaults to True.

        Returns:
            any: the output of the function, or a string representing any errors that occurred.
        """
        try:
            if exe:
                exec(f'self.objects[{thing}].{func}(*{args}, **{kwargs})')
            if eva:
                return eval(f'self.objects[{thing}].{func}(*{args}, **{kwargs})')
        except Exception as e:
            print('Error occurred!', e)
            return e
    def draw(self, thing): 
        """draws any of the graphics objects, given [thing] as a gui class constant"""
        if thing==11: self.objects[thing].draw(self.win)
        elif thing==10: self.objects[thing].draw(self.win)
        else:
            for obj in self.objects[thing].getGraphicsObjects(): 
                obj.draw(self.win)
    def undraw(self, thing): 
        """undraws any of the graphics objects, given [thing] as a gui class constant"""
        if thing==11: self.objects[thing].undraw()
        elif thing==10: self.objects[thing].undraw()
        else:
            for obj in self.objects[thing].getGraphicsObjects():
                obj.undraw()
    def getMouse(self): 
        """just win.getMouse without having to use win"""
        return self.win.getMouse()
    def waitButtonClick(self, buttonName=None, quitIfQuit=True):
        """waits for a button click
        Args:
            buttonName (str, optional): the name of the button to monitor. if not given, the first button to be clicked is returned. Defaults to None.
        Returns:
            str: the name of the button that was clicked
        """
        while True: #main loop
            p=self.win.getMouse() #get mouse pos
            if self.objects[Gui.QUIT].clicked(p) and quitIfQuit: self.quitProgram()
            if buttonName: #if buttoName was passed
                if self.objects[buttonName].clicked(p): #check if it was clicked correctly 
                    return Gui.START if buttonName==4 else (Gui.QUIT if buttonName==5 else Gui.MOVE)  #for compatibility
                continue #don't do the other for loop
            for button in self.objects[4:7]: #loop through all the buttons
                if button.clicked(p): #check if this button was clicked
                    return Gui.START if button==self.objects[4] else (Gui.QUIT if button==self.objects[5] else Gui.MOVE) #return the appropriate button
    def _valid(self, input: str):
        """input validation function

        Args:
            input (str): the given input, from one entry

        Returns:
            tuple or bool: the coordinates that were entered, or False if the input is invalid.
        """
        coords=input.split(',')
        if len(coords)!=2: return False
        try: coords=[int(coords[0]), int(coords[1])]
        except: return False
        if not 0<coords[0]<11: return False
        if not 0<coords[1]<11: return False
        return tuple(coords)
    def getEntry(self):
        """gets the points from the three entries

        Returns:
            list: the three points, in the form [[x,y] [x,y] [x,y]]
        """
        entryList=[]
        for entry in self.objects[7:10]:
            entryList.append(self._valid(entry.getText()))
        entryList=tuple(entryList)
        if False in entryList: return False
        if len(set(entryList))<len(entryList): return False #check if there are multiple of the same point
        return entryList

    def quitProgram(self):
        """quit the program.
        """
        self.win.close()
        exit()
            
        
#ok
#I don't know where to put this
#I can't put it in sharkRunner, but it doesn't really fit here
#whatever it works here
class StalemateTracker:
    def __init__(self):
        #states are stored as {[state]:[number of times it's been reached]}
        self.states={}
    def addState(self, fishPoses, fishRots, sharkPos):
        state=[*fishPoses, *fishRots, sharkPos] #flatten the list, for simplicity
        state=tuple([tuple(i) for i in state])  #convert to tuple, because lists are mutable

        #this try/except increments the counter for each state.  if a state is new, there's a keyError, so it assigns instead of incrementing (sets to 1)
        try:
            self.states[state]+=1
        except KeyError:
            self.states[state]=1

    def checkStalemate(self, repetitions=3):
        if max(self.states.values())>=repetitions: #check if anything has been repeated more than repititions times
            return True
        return False
    def reset(self):
        self.states={} #resets the log of states