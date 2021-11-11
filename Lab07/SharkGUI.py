from graphics import *
import numpy as np
win=GraphWin('Shark Game', 800, 900)

#set the coordinates so it makes sense with the grid
win.setCoords(-0.5, -1.5, 9.5, 9.5)

#make the grid
for i in np.linspace(0, 9, 10):
    for j in np.linspace(0, 9, 10):
        Rectangle(Point(i-0.5, j-0.5), Point(i+0.5, j+0.5)).draw(win)


# pointLabel=Text(Point(5, -1), 'no point clicked yet')
# while True:
#     p=win.getMouse()
#     pointLabel.undraw()
#     p=np.array([p.getX(), p.getY()])
#     p=np.around(p)
#     pointLabel.setText(str(p))
#     pointLabel.draw(win)

class gui:
    def __init__(self, animalList, buttonDict, winTitle='SharkGUI', winSize=[800, 900]):
        self.animals={
            's': animalList[0],
            'a': animalList[1],
            'b': animalList[2],
            'c': animalList[3]
        }
        self.buttons=buttonDict
        self.win=GraphWin(winTitle, winSize[0], winSize[1])
    
    def changeButton(self, buttonName, operation, *args, **kwargs):
        exec(f"self.buttons[{buttonName}].{operation}(*{args}, **{kwargs})")
    
    def moveAnimal(self, shark=None, fishA=None, fishB=None, fishC=None):
        if not not shark:
            self.animals['s'].move(shark)
        if not not fishA:
            self.animals['a'].move(fishA)
        if not not fishB:
            self.animals['b'].move(fishB)
        if not not fishC:
            self.animals['c'].move(fishC)
    
    def getLocations(self):
        return {

        }


    def getAnimal(self, key:str):
        return self.animals[key]
    def setAnimal(self, key:str, animal):
        self.animals[key]=animal
    animal=property(getAnimal, setAnimal)

    def getButton(self, key:str):
        return self.buttons[key]
    def setButton(self, key:str, button):
        self.buttons[key]=button
    button=property(getButton, setButton)



class gui:
    def __init__(self, animalDict, buttonDict, winTitle='SharkGUI', winSize=[800, 900]):
        self.animals=animalDict
        self.buttons=buttonDict
        self.win=GraphWin(winTitle, winSize[0], winSize[1])
        self.grid=[Rectangle(Point(i-0.5, j-0.5), Point(i+0.5, j+0.5)) for i in range(10) for j in range(10)]
    
    def drawGrid(self):
        for r in self.grid: r.draw(self.win)
    def undrawGrid(self):
        for r in self.grid: r.undraw()

    
    def changeButton(self, operation=None, buttonName=None, *args, **kwargs):
        if not not buttonName:
            exec(f'self.buttons[{buttonName}].{operation}(*{args}, **{kwargs})')
        else:
            for name, button in self.buttons: exec(f'{button}.{operation}(*{args}, **{kwargs}')
    def evalButton(self, buttonName, operation, *args, **kwargs):
        # return eval(f"self.buttons[{buttonName}].{operation}(*{args}, **{kwargs})")
        if not not buttonName:
            return eval(f'self.buttons[{buttonName}].{operation}(*{args}, **{kwargs})')
        else:
            return [eval(f'{button}.{operation}(*{args}, **{kwargs}') for name, button in self.buttons]
    
    def moveAnimalDict(self, movements):
        for animal, dpos in movements:
            self.animals[animal].move(dpos)
    def moveAnimalArgs(self, **movements):
        for animal, dpos in movements:
            self.animals[animal].move(dpos)
    
    def getPos(self, *animals):
        return {animal:self.animals[animal].getPos() for animal in animals}
    def getRot(self, *animals):
        return {animal:self.animals[animal].getRot() for animal in animals}
    def getAttr(self, animals:list, attrs:list):
        return {animal:self.animals[animal].getAttr(attrs) for animal in animals}
        

    def getAnimal(self, key:str):
        return self.animals[key]
    def setAnimal(self, key:str, animal):
        self.animals[key]=animal
    animal=property(getAnimal, setAnimal)

    def getButton(self, key:str):
        return self.buttons[key]
    def setButton(self, key:str, button):
        self.buttons[key]=button
    button=property(getButton, setButton)

    def getMouse(self):
        p=self.win.getMouse()
        output={}
        for name, button in self.buttons:
            if button.clicked(p):
                output[name]=p.clone()
        return output