#%%
from graphics import *
from reidList import reidList as r
# %%
class button():
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
        self.center=center #center is a point object
        self.boundary=Rectangle(Point(center.getX()-(size.get(0)/2), center.getY()-(ySize/2)), Point(center.getX()+(size.get(0)/2), center.getY()+(ySize/2)))
        self.boundary.setColor(color)
        self.boundary.setOutline(lineColor)
        self.text=Text(center, text)
        self.win=win
        if draw:
            self.draw(win)
    
    def draw(self, win=None):
        if not GraphWin:
            win=self.win
        self.boundary.draw(win)
        self.text.draw(win)
    def undraw(self):
        #don't need to worry about it already being drawn because
        #GraphicsObject.undraw() already handles this
        self.boundary.undraw()
        self.text.undraw()
    def move(self, dx, dy):
        self.boundary.move(dx,dy)
        self.text.move(dx,dy)
    def moveAbs(self, x, y):
        curPos=r(self.center.getX(), self.center.getY())
        endPos=r(x,y)
        movement=endPos-curPos
        self.move(movement(0), movement(1))
    def waitClick(self):
        pass
    def getClickState(self):
        pass



#%%
class Dye():
    def __init__(self, center, size=50, sides=6):
        """constructor for the dye class

        Args:
            center (Point object): the center point of the die
            size (int, optional): the side length of the square around the dye. Defaults to 50.
            sides (int, optional): The number of faces on the die. Defaults to 6.
        """
        self.center=center
        self.size=50
        self.sides=6
        self.border=Rectangle(Point(center.getX()-(size/2), center.getY()-(size/2)), Point(center.getX()+(size/2), center.getY()+(size/2)))
    def roll(self):
        pass
    def reid(self):
        pass