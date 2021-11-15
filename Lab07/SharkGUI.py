from graphics import *
class Things:
    #these are all index constants
    SHARK = 0
    FISHA = 1
    FISHB = 2
    FISHC = 3

    START = 4
    QUIT  = 5
    MOVE  = 6

    ENTRYA = 7
    ENTRYB = 8
    ENTRYC = 9

    MSGBOX = 10
class gui:
    def __init__(self, shark, fisha, fishb, fishc, start, quit, move, entrya, entryb, entryc, msgbox, winTitle='SharkGUI', winSize=[800, 900], drawButtons=True, drawAnimals=True):
        """constructor for gui

        Args:
            animalNames (list): a list of the names of the animals
            animalObjects (list): the actual animal objects, in the same order as the name list
            buttonNames (list): a list of the names of the buttons
            buttonObjects (list): the actual button objects, in the same order as the name list
            winTitle (str, optional): the title of the graphics window. Defaults to 'SharkGUI'.
            winSize (list, optional): the size of the graphics window. Defaults to [800, 900].
        """
        self.animals=dict(zip(animalNames, animalObjects)) #store animals
        self.buttons=dict(zip(buttonNames, buttonObjects)) #store buttons
        self.win=GraphWin(winTitle, winSize[0], winSize[1]) #make window
        self.win.setCoords(-0.5, -1.5, 9.5, 9.5) #fix it so that grid locations are integers
        self.grid=[Rectangle(Point(i-0.5, j-0.5), Point(i+0.5, j+0.5)) for i in range(10) for j in range(10)] #create grid
        if drawButtons:
            for _, button in self.buttons:
                for obj in button.getGraphicsObjects(): obj.draw(self.win) #draw all the buttons
        if drawAnimals:
            for _, animal in self.animals:
                for obj in animal.getGraphicsObjects(): obj.draw(self.win) #draw all the animals
    def drawGrid(self):
        'draws the grid'
        for i in self.grid: i.draw(self.win)
    def undrawGrid(self):
        'undraws the grid'
        for i in self.grid: i.undraw(self.win)
    
    @property
    def win(self): return self.win

    @win.setter
    def setWin(self, win):
        self.win.close()
        del(self.win)
        self.win=win
    
    def getButton(self, name): 
        'returns the button object with the name [name].'
        return self.buttons[name]
    def setButton(self, name, button):
        'adds a button'
        self.buttons[name].undraw()
        self.buttons[name]=button
    def drawButton(self, name):
        'draws a specific button'
        for obj in self.buttons[name].getGraphicsObjects(): obj.draw(self.win)
    def undrawButton(self, name): 
        'undraws a specific button'
        self.buttons[name].undraw()
    def getAnimal(self, name): 
        'returns the animal object with the name [name]'
        return self.animals[name]
    def drawAnimal(self, name): 
        'draws a specific animal'
        for obj in self.animals[name].getGraphicsObjects(): obj.draw(self.win)
    def undrawAnimal(self, name): 
        'undraws a specific animal'
        self.animals[name].undraw()
    def getMouse(self): 
        'just win.getMouse without having to use win'
        return self.win.getMouse()
    def waitButtonClick(self, buttonName=None):
        """waits for a button click

        Args:
            buttonName (str, optional): the name of the button to monitor. if not given, the first button to be clicked is returned. Defaults to None.

        Returns:
            str: the name of the button that was clicked
        """
        while True: #main loop
            p=self.win.getMouse() #get mouse pos
            if buttonName: #if buttoName was passed
                if self.buttons[buttonName].clicked(p): #check if it was clicked correctly 
                    return buttonName #for compatibility
                continue #don't do the other for loop
            for name, button in self.buttons: 
                if button.clicked(p): return name #check clicked state


def foo(arg1, arg2, *args, **kwargs):
    print(args)