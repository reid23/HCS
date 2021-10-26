from ReidList import ReidList as r
from random import randrange as rand
from graphics import *

#! please excuse my creative liberties on the naming here
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
        self.curVal='?'
        self.border=Rectangle(Point(center.getX()-(size/2), center.getY()-(size/2)), Point(center.getX()+(size/2), center.getY()+(size/2)))
        self.number=Text(self.center, str(self.curVal))
        self.drawn=False

    #like scoreCell.reset(), does the same things
    def reset(self):
        self.curVal='?'
        self.number.setText(self.curVal)
    
    #draw and undraw, also just bundles again
    def draw(self, win):
        if self.drawn:
            self.undraw()
        self.border.draw(win)
        self.number.draw(win)
        self.drawn=True
        self.win=win
    def undraw(self):
        self.border.undraw()
        self.number.undraw()
        self.drawn=False

    def roll(self):
        """roll the dye!  doesn't return anything, but updates all internal stuff and graphics.
        """
        self.curVal=rand(1,self.sides+1, 1) #get random val
        self.number.setText(str(self.curVal)) #set the number on the die
        if self.drawn: #redraw the die if needed
            self.draw(self.win)
    def reid(self): #reid the dye, basically a getter method for self.curVal
        return self.curVal

    #I decided to combine all the setters because
    #who doesn't love extra complexity?
    def setAttr(self, color=None, outline=None, size=None, positionAbs=None, positionRel=None):
        """All the setters for the Dye class!

        Args:
            color (str, optional): The color to set the die to. Defaults to None.
            outline (str, optional): The color to set the borderto. Defaults to None.
            size (ReidList, optional): The new size of the dye. Defaults to None.
            positionAbs (ReidList, optional): The new absolute position. Defaults to None.
            positionRel (ReidList, optional): The amount to move the dye by. Defaults to None.
        """
        #input validation, because there's no way to say this in the definition of the method
        assert not (positionRel and positionAbs), "you may only set positionRel or positionAbs, not both."

        #set all the stuff, pretty simple, just a big switch statement
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
            #calculate the relative positioning
            curPos=r(self.center.getX(), self.center.getY())
            endPos=r(positionAbs(0), positionAbs(1))
            movement=endPos-curPos
            #actually move stuff
            self.border.move(movement(0), movement(1))
            self.center.move(movement(0), movement(1))
            self.number.move(movement(0), movement(1))
        
        #redraw stuff if needed
        if self.drawn:
            self.draw(self.win)
    
    #get the current position of the dye
    def getPos(self):
        return r(self.center.getX(), self.center.getY())

    #exactly the same as clicked() for a button.
    #asdjfksla;fjsdkafjsfinheritancejfasdklfjasdk;fjals;df7dshaf;klsdjkaf
    def clicked(self, point):
        if abs(self.center.getX()-point.getX()) < self.size/2 and abs(self.center.getY()-point.getY()) < self.size/2:
            return True
        return False