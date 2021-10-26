from graphics import *
from ReidList import ReidList as r

class MsgBox(): #i've been spending too much time in ahk
    def __init__(self, win, center, size, text='message', color='white', draw=False):
        """Constructor for MsgBox object

        Args:
            win (GraphWin): the graphWin to place the msgbox in
            center (Point object): The center point of the box
            size (ReidList): the size, in [x,y], of the box
            text (str, optional): the message in the box. Defaults to 'message'.
            color (str, optional): the color of the box. Defaults to 'white'.
            draw (bool, optional): Whether or not to draw the msgbox upon instantiation. Defaults to False.
        """
        self.win=win
        self.center=center
        self.size=size
        self.border=Rectangle(Point(center.getX()+size(0)/2, center.getY()+size(1)/2), Point(center.getX()-size(0)/2, center.getY()-size(1)/2))
        self.text=Text(center, text)
        self.border.setFill(color)
        if draw:
            self.border.draw(win)
            self.text.draw(win)
            self.drawn=True
        else:
            self.drawn=False
    
    #draw and undraw
    def draw(self, win=None):
        if self.drawn:
            return
        if win:
            self.win=win
        if self.drawn:
            self.undraw()
        self.border.draw(self.win)
        self.text.draw(self.win)
        self.drawn=True
    def undraw(self):
        self.border.undraw()
        self.text.undraw()
        self.drawn=False
    
    #getters and setters
    def setText(self, text):
        self.text.setText(text)
    def setColor(self, color):
        self.border.setFill(color)
    def setSize(self, size):
        self.size=size
        self.border=Rectangle(Point(self.center.getX()+size(0)/2, self.center.getY()+size(1)/2), Point(self.center.getX()-size(0)/2, self.center.getY()-size(1)/2))
        self.text=Text(self.center, self.text.getText())
        if self.drawn:
            self.draw()
    def moveRel(self, pos):
        self.border.move(pos(0), pos(1))
        self.text.move(pos(0), pos(1))
    def moveAbs(self, pos):
        self.center=Point(pos(0), pos(1))
        self.border=Rectangle(Point(self.center.getX()+self.size(0)/2, self.center.getY()+self.size(1)/2), Point(self.center.getX()-self.size(0)/2, self.center.getY()-self.size(1)/2))
        self.text=Text(self.center, self.text.getText())
        if self.drawn:
            self.drawn=False
            self.draw()