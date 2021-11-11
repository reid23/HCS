from graphics import *
class gui:
    def __init__(self, animalNames, animalObjects, buttonNames, buttonObjects, winTitle='SharkGUI', winSize=[800, 900]):
        self.animals=dict(zip(animalNames, animalObjects))
        self.buttons=dict(zip(buttonNames, buttonObjects))
        self.win=GraphWin(winTitle, winSize[0], winSize[1])
        self.win.setCoords(-0.5, -1.5, 9.5, 9.5)
        self.grid=[Rectangle(Point(i-0.5, j-0.5), Point(i+0.5, j+0.5)) for i in range(10) for j in range(10)]
        for name, button in self.buttons:
            for obj in button.getGraphicsObjects():
                obj.draw(self.win)
        for name, animal in self.animals:
            for obj in animal.getGraphicsObjects():
                obj.draw(self.win)
    
    def drawGrid(self):
        for i in self.grid: i.draw(self.win)
    def undrawGrid(self):
        for i in self.grid: i.undraw(self.win)
    
    def getWin(self): return self.win
    
    def setWin(self, win):
        self.win.close()
        del(self.win)
        self.win=win
    
    def getButton(self, name): return self.buttons[name]
    def setButton(self, name, button):
        self.buttons[name].undraw()
        self.buttons[name]=button
    

    def drawButton(self, name):
        for obj in self.buttons[name].getGraphicsObjects(): obj.draw(self.win)
    def undrawButton(self, name): self.buttons[name].undraw()
    
    def getAnimal(self, name): return self.animals[name]
    
    def drawAnimal(self, name): 
        for obj in self.animals[name].getGraphicsObjects(): obj.draw(self.win)
    def undrawAnimal(self, name): self.animals[name].undraw()

    def getMouse(self): return self.win.getMouse()

    def waitButtonClick(self, buttonName=None):
        while True:
            p=self.win.getMouse()
            if buttonName:
                if self.buttons[buttonName].clicked(p):
                    return True
                continue
            for name, button in self.buttons: 
                if button.clicked(p): return name