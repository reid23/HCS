from graphics import *
class Gui:
    SHARK, FISHA, FISHB, FISHC, START, QUIT, MOVE, ENTRYA, ENTRYB, ENTRYC, MSGBOX = list(range(0, 11)) #index constants
    NORTH, EAST, SOUTH, WEST = '000', '090', '180', '270'
    def __init__(self, shark, fisha, fishb, fishc, start, quit, move, entrya, entryb, entryc, msgbox, winTitle='SharkGUI', winSize=[800, 900], drawButtons=True, drawAnimals=True, drawEntries=True, drawMsgBox=True):
        self.objects=[shark, fisha, fishb, fishc, start, quit, move, entrya, entryb, entryc, msgbox]
        self.win=GraphWin(winTitle, winSize[0], winSize[1]) #make window
        self.win.setCoords(-0.5, -1.5, 9.5, 9.5) #fix it so that grid locations are integers
        self.grid=[Rectangle(Point(i-0.5, j-0.5), Point(i+0.5, j+0.5)) for i in range(10) for j in range(10)] #create grid
        for animal in self.objects[0:5]: animal.setImage(Image(Point(*animal.getPos()), animal.getImgPath().replace('___', '000')))
        if drawButtons:
            for button in self.objects[4:7]:
                for obj in button.getGraphicsObjects(): obj.draw(self.win) #draw all the buttons
        if drawAnimals:
            for animal in self.objects[0:5]:
                for obj in animal.getGraphicsObjects(): obj.draw(self.win) #draw all the animals
        if drawEntries:
            for entry in self.objects[7:]:
                for obj in entry.getGraphicsObjects(): obj.draw(self.win)
        if drawMsgBox:
            for obj in self.objects[10].getGraphicsObjects(): obj.draw(self.win)
    def moveAnimal(self, animal, pos, rot, absolutePos=False):
        self.undraw(animal)
        self.objects[animal].setImage(Image(Point(*animal.getPos()), animal.getImgPath().replace('___', rot)))
        self.draw(animal)
        if absolutePos:
            pos[0] += self.objects[animal].getPos()[0]
            pos[1] += self.objects[animal].getPos()[1]
        for obj in self.objects[animal].getGraphicsObjects(): obj.move(*pos)
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
        """sets win to a window
        Args:
            win (GraphWin): the new window
        """
        self.win.close()
        del(self.win)
        self.win=win
    def getThing(self, thing):
        """returns any of the graphics objects
        Args:
            thing (gui constant): the thing to get, in the form Gui.FISHC
        Returns:
            animal, button, etc: the object
        """
        return self.objects[thing]
    def setThing(self, thing, newObject):
        """sets the [thing] to [newObject]
        Args:
            thing (Gui constant): the thing to set. In the form Gui.FISHC
            newObject (button, animal, etc. object): the thing to set Gui.[whatever] to.
        """
        self.objects[thing]=newObject
    def thingMethod(self, thing, func, eva=True, exe=True, *args, **kwargs):
        try:
            if exe:
                exec(f'self.objects[{thing}].{func}(*{args}, **{kwargs})')
            if eva:
                return eval(f'self.objects[{thing}].{func}(*{args}, **{kwargs})')
        except Exception as e:
            print('Error occurred!', e)
            return e
    def draw(self, thing): 
        """draws any of the graphics objects
        Args:
            thing (Gui constant): the thing to draw. In the form Gui.FISHC
        """
        for obj in self.objects[thing].getGraphicsObjects(): obj.draw(self.win)
    def undraw(self, thing): 
        """undraws any of the graphics objects
        Args:
            thing (Gui constant): the thing to undraw. In the form Gui.FISHC
        """
        self.objects[thing].undraw()
    def getMouse(self): 
        'just win.getMouse without having to use win'
        return self.win.getMouse()
    def waitButtonClick(self, button=None):
        """waits for a button click
        Args:
            buttonName (str, optional): the name of the button to monitor. if not given, the first button to be clicked is returned. Defaults to None.
        Returns:
            str: the name of the button that was clicked
        """
        while True: #main loop
            p=self.win.getMouse() #get mouse pos
            if button: #if buttoName was passed
                if self.buttons[button].clicked(p): #check if it was clicked correctly 
                    return 'START' if button==4 else ('QUIT' if button==5 else 'MOVE')  #for compatibility
                continue #don't do the other for loop
            for button in self.objects[4:7]: 
                if button.clicked(p): 
                    return 'START' if button==4 else ('QUIT' if button==5 else 'MOVE')
                    