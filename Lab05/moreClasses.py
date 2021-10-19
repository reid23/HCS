#%%
from graphics import *
from reidList import reidList as r
from random import randrange as rand

# %%
class ScoreCell():
    def __init__(self):
        pass

#%%
class Button():
    """A button class for the graphics library
        This is just a container for a box and some text that can be clicked.
        So it's not a graphicsObject, even though some methods may be similar.
        It's just a collection of graphicsObjects
    """
    def __init__(self, center, text: str = "Button", size=r(70,20), color='white', lineColor='black', draw=False, win=None):
        """constructor for a button

        Args:
            center (Point object): the center point of the button
            text (str, optional): the label on the button. Defaults to "Button"
            size (reidList, optional): the (x,y) dimensions of the button, in px. Defaults to r(70,20).
            color (str, optional): the background color of the button. Defaults to 'white'.
            lineColor (str, optional): the color of the border of the button. Defaults to 'black'.
            draw (bool, optional): Whether to draw the button upon initialization. Defaults to False.
            win ([type], optional): the GraphWin to use when drawing, if not passed in draw(), or when drawn upon intialization. Defaults to None.
        """
        self.center=center.clone() #center is a point object
        self.boundary=Rectangle(Point(center.getX()-(size(0)/2), center.getY()-(size(1)/2)), Point(center.getX()+(size(0)/2), center.getY()+(size(1)/2)))
        self.boundary.setFill(color)
        self.boundary.setOutline(lineColor)
        self.text=Text(center, text)
        self.win=win
        self.size=size
        self.drawn=False
        if draw:
            self.draw(win)
            self.drawn=True
    
    def draw(self, win=None):
        if not win:
            win=self.win
        if self.drawn:
            self.undraw()
        self.boundary.draw(win)
        self.text.draw(win)
        self.drawn=True
        self.win=win
    def undraw(self):
        #don't need to worry about it already being drawn because
        #GraphicsObject.undraw() already handles this
        self.boundary.undraw()
        self.text.undraw()
        self.drawn=False
    def move(self, dx, dy):
        self.boundary.move(dx,dy)
        self.text.move(dx,dy)
    def moveAbs(self, x, y):
        curPos=r(self.center.getX(), self.center.getY())
        endPos=r(x,y)
        movement=endPos-curPos
        self.move(movement(0), movement(1))
    def setSize(self, x, y):
        self.size=r(x,y)
        self.boundary=Rectangle(Point(self.center.getX()-(self.size(0)/2), self.center.getY()-(self.size(1)/2)), Point(self.center.getX()+(self.size(0)/2), self.center.getY()+(self.size(1)/2)))
        if self.drawn:
            self.draw()
    def waitClick(self, win=None, outputAsList=True):
        """wait for a click and return the clicked point

        Args:
            win (GraphWin object, optional): the graphwin to wait for a click in. defaults to none, will use self.win.
            outputAsList (bool, optional): whether to output as reidList or as Point object. Defaults to True (reidList).

        Returns:
            point: Point object or reidList describing the clicked point
        """
        if not win:
            win=self.win
        
        while(True):
            p=win.getMouse()
            l=r(p.getX(), p.getY())
            if self.boundary.getP1().getX()<l(0)<self.boundary.getP2().getX() and self.boundary.getP1().getY()<l(1)<self.boundary.getP2().getY():
                break
        if outputAsList:
            return l
        else:
            return p



#%%
class Dye():
    def __init__(self, center, size=50, sides=6):
        """constructor for the dye class

        Args:
            center (Point object): the center point of the die
            size (int, optional): the side length of the square around the dye. Defaults to 50.
            sides (int, optional): The number of faces on the die. Defaults to 6.
        """
        self.center=center.clone()
        self.size=size
        self.sides=sides
        self.curVal=1
        self.border=Rectangle(Point(center.getX()-(size/2), center.getY()-(size/2)), Point(center.getX()+(size/2), center.getY()+(size/2)))
        self.number=Text(self.center, str(self.curVal))
        self.drawn=False
    def draw(self, win):
        if self.drawn:
            self.undraw()
        self.border.draw(win)
        self.number.draw(win)
        self.drawn=True
        self.win=win
    def roll(self):
        self.curVal=rand(1,self.sides+1, 1)
        self.number.setText(str(self.curVal))
        if self.drawn:
            self.draw(self.win)
    def reid(self):
        return self.curVal
    def undraw(self):
        self.border.undraw()
        self.number.undraw()
        self.drawn=False
    def setAttr(self, color=None, outline=None, size=None, positionAbs=None, positionRel=None):
        assert not (positionRel and positionAbs), "you may only set positionRel or positionAbs, not both."
        if color:
            self.border.setFill(color)
        if outline:
            self.border.setOutline(outline)
        if size:
            self.size=size
            self.border.undraw()
            del self.border
            self.border=Rectangle(Point(self.center.getX()-(size/2), self.center.getY()-(size/2)), Point(self.center.getX()+(size/2), self.center.getY()+(size/2)))
        if positionRel:
            self.border.move(positionRel(0), positionRel(1))
            self.center.move(positionRel(0), positionRel(1))
            self.number.move(positionRel(0), positionRel(1))
        elif positionAbs:
            curPos=r(self.center.getX(), self.center.getY())
            endPos=r(positionAbs(0), positionAbs(1))
            movement=endPos-curPos
            self.border.move(movement(0), movement(1))
            self.center.move(movement(0), movement(1))
            self.number.move(positionAbs(0), positionAbs(1))
        if self.drawn:
            self.draw(self.win)
    def getPos(self):
        return r(self.center.getX(), self.center.getY())
# %%
if __name__ == '__main__':
    win=GraphWin()
    b=Button(Point(100, 100), win=win)
    b.draw(win)
    while True:
        print(b.waitClick())