from graphics import *
class Gui:
    SHARK, FISHA, FISHB, FISHC, START, QUIT, MOVE, ENTRYA, ENTRYB, ENTRYC, MSGBOX, CHASINGBOX = list(range(0, 12)) #index constants
    NORTH, EAST, SOUTH, WEST = '000', '090', '180', '270'
    def __init__(self, shark, fisha, fishb, fishc, start, quit, move, entrya, entryb, entryc, msgbox, winTitle='SharkGUI', winSize=[800, 900], drawButtons=True, drawAnimals=True, drawEntries=True, drawMsgBox=True):
        chasingBox=Rectangle(Point(0.5, 0.5), Point(1.5, 1.5))
        chasingBox.setWidth(5)
        chasingBox.setOutline('green')
        self.objects=[shark, fisha, fishb, fishc, start, quit, move, Entry(Point(3, -0.2), 5), Entry(Point(5, -0.2), 5), Entry(Point(7, -0.2), 5), msgbox, chasingBox]
        self.win=GraphWin(winTitle, winSize[0], winSize[1]) #make window
        self.win.setCoords(-0.5, -1.5, 9.5, 9.5) #fix it so that grid locations are integers
        self.grid=[Rectangle(Point(i-0.5, j-0.5), Point(i+0.5, j+0.5)) for i in range(10) for j in range(10)] #create grid
        for animal in self.objects[0:4]: animal.setImage(Image(Point(*animal.getPos()), animal.getImgPath().replace('___', (animal.getDirection()[0:2] + ('X' if animal.getFleeMode() else '0')))))
        if drawButtons:
            for button in self.objects[4:7]:
                for obj in button.getGraphicsObjects(): obj.draw(self.win) #draw all the buttons
        if drawAnimals:
            for animal in self.objects[0:4]:
                for obj in animal.getGraphicsObjects(): obj.draw(self.win) #draw all the animals
        if drawEntries:
            for entry in self.objects[7:]: entry.draw(self.win)
        if drawMsgBox:
            for obj in self.objects[10].getGraphicsObjects(): obj.draw(self.win)
    def _getImgNumber(self, animal):
        return animal.getDirection()[0:2] + ('X' if animal.getFleeMode() else '0')
    def moveAnimal(self, animal, pos, rot, flee=False, absolutePos=False):
        self.undraw(animal)
        if flee: rot=rot[:2].append('X')
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
        for i in self.grid: i.undraw()
    def getChasingBoxPos(self): return self.objects[11].getCenter().getX(), self.objects[11].getCenter().getY()
    def moveChasingBox(self, pos, absolutePos=True):
        if absolutePos: pos=[pos[0]-self.getChasingBoxPos()[0], pos[1]-self.getChasingBoxPos()[1]]
        self.objects[11].move(pos[0], pos[1])
    def getThing(self, thing):
        """returns any of the graphics objects, given one of the gui class constants"""
        return self.objects[thing]
    def setThing(self, thing, newObject):
        """sets the [thing] to [newObject], given [thing] as gui class constant"""
        self.objects[thing]=newObject
    def thingMethod(self, thing, func, eva=True, exe=True, *args, **kwargs): #so we don't have to import graphics anywhere else
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
            for obj in self.objects[thing].getGraphicsObjects(): obj.draw(self.win)
    def undraw(self, thing): 
        """undraws any of the graphics objects, given [thing] as a gui class constant"""
        if thing==11: self.objects[thing].undraw()
        elif thing==10: self.objects[thing].undraw()
        else:
            for obj in self.objects[thing].getGraphicsObjects(): obj.undraw()
    def getMouse(self): 
        """just win.getMouse without having to use win"""
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