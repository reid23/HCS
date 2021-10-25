#%%
from graphics import *
from reidList import reidList as r
from random import randrange as rand

# %%
class ScoreCell():
    def __init__(self, center, label: str):
        self.types=r('1s', '2s', '3s', '4s', '5s', '6s', 'bonus', 'three\nof a\nkind', 'four\nof a\nkind', 'full\nhouse', 'small\nstra-\night', 'large\nstra-\night', 'chance', 'yaht-\nzee', 'total')
        assert self.types.exists(label), f'{label} is not a valid type of ScoreCell.\n Valid types are {self.types}'
        self.center=center
        self.boundary=Rectangle(Point(center.getX()-20, center.getY()-50), Point(center.getX()+20, center.getY()+50))
        self.line=Line(Point(center.getX()-20, center.getY()-20), Point(center.getX()+20, center.getY()-20))
        p=center.clone()
        p.move(0, 15)
        self.label=Text(p, label)
        self.locked=False
        self.yahtzeeUsed=False
        self.yahtzeeUsable=True
        
        p.move(0, -50)
        self.value=Text(p, '-')
        self.drawn=False
    def reset(self):
        self.locked=False
        self.yahtzeeUsed=False
        self.yahtzeeUsable=True
        self.value.setTextColor('black')

    def _calc(self, dice):
    #should have used a switch here...
    #switch statements have been added in python 3.10!
    #very exciting
        label=self.label.getText()
        if label=='1s':
            return dice.count(1)
        elif label=='2s':
            return dice.count(2)*2
        elif label=='3s':
            return dice.count(3)*3
        elif label=='4s':
            return dice.count(4)*4
        elif label=='5s':
            return dice.count(5)*5
        elif label=='6s':
            return dice.count(6)*6
        elif label=='three\nof a\nkind':
            c=dice.toCounter()
            for i in c:
                if i(1) >= 3:
                    return sum(dice)
            return 0
                
        elif label=='four\nof a\nkind':
            c=dice.toCounter()
            for i in c:
                if i(1) >= 4:
                    return sum(dice)
            return 0

        elif label=='full\nhouse':
            c=dice.toCounter()
            if not(len(c)==2 or len(c)==1):
                return 0
            if c(0)(1)==2 or c(0)(1)==3 or c(0)(1)==5:
                return 25
            return 0

        elif label=='small\nstra-\night':
            if dice.exists(r(1,2,3,4)) or dice.exists(r(2,3,4,5)) or dice.exists(r(3,4,5,6)):
                return 30
            return 0
                    
        elif label=='large\nstra-\night':
            if dice.exists(r(1,2,3,4,5) or r(2,3,4,5,6)):
                return 40
            return 0
        elif label=='chance':
            print(dice)
            return sum(dice)
        elif label=='yaht-\nzee':
            if len(dice.toCounter())==1 and self.value.getText()!='0':
                if self.yahtzeeUsed:
                    return int(self.value.getText())+100
                return 50
            return 0
        elif label=='total':
            pass
    def draw(self, win):
        if self.drawn==False:
            self.line.draw(win)
            self.boundary.draw(win)
            self.label.draw(win)
            self.value.draw(win)
        self.drawn=True
    def setValue(self, val):
        self.value.setText(str(val))
    def getVal(self):
        return self.value.getText()
    def getName(self):
        return self.label.getText()
    def undraw(self):
        if self.drawn:
            self.line.undraw()
            self.boundary.undraw()
            self.label.undraw()
            self.value.undraw()
        self.drawn=False
    def inBounds(self, p):
        if abs(p.getX()-self.center.getX()) <= 20 and abs(p.getY()-self.center.getY()) <= 50:
            return True
        return False
    def lockScore(self):
        if self.value.getText()=='0':
            self.yahtzeeUsable=False
        self.yahtzeeUsed=True
        self.locked=True
        self.value.setTextColor('black')
    def prelimCalc(self, dice):
        if not self.getLocked():
            self.value.setTextColor('red')
            self.value.setText(str(self._calc(dice)))
    def notLock(self):
        self.value.setTextColor('black')
        self.locked=False
        
        #TODO: sort out this --if-- garbage
        if self.label.getText()=='yaht-\nzee':
            if self.value.getText()=='0':
                if not self.yahtzeeUsable:
                    return
            elif self.value.getText()=='50':
                pass
        self.value.setText('-')
    def getLocked(self):
        if self.getName()=='yaht-\nzee':
            return not self.yahtzeeUsable
        return self.locked

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
    def clicked(self, point):
        l=r(point.getX(), point.getY())
        if self.boundary.getP1().getX()<l(0)<self.boundary.getP2().getX() and self.boundary.getP1().getY()<l(1)<self.boundary.getP2().getY():
            return True
        return False



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
        self.curVal='?'
        self.border=Rectangle(Point(center.getX()-(size/2), center.getY()-(size/2)), Point(center.getX()+(size/2), center.getY()+(size/2)))
        self.number=Text(self.center, str(self.curVal))
        self.drawn=False
    def reset(self):
        self.curVal='?'
        self.number=Text(self.center, self.curVal)
    def draw(self, win):
        if self.drawn:
            self.undraw()
        self.border.draw(win)
        self.number.draw(win)
        self.drawn=True
        self.win=win
    def roll(self):
        self.curVal=rand(1,self.sides+1, 1)
        self.curVal=6
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
            self.number.move(movement(0), movement(1))
        if self.drawn:
            self.draw(self.win)
    def getPos(self):
        return r(self.center.getX(), self.center.getY())
    def clicked(self, point):
        if abs(self.center.getX()-point.getX()) < self.size/2 and abs(self.center.getY()-point.getY()) < self.size/2:
            return True
        return False

#%%
class MsgBox(): #i've been spending too much time in ahk
    def __init__(self, win, center, size, text='message', color='white', draw=False):
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
        
    def draw(self, win=None):
        if self.drawn:
            return
        if win:
            self.win=win
        self.border.draw(self.win)
        self.text.draw(self.win)
        self.drawn=True
    def undraw(self):
        if not self.drawn:
            return
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
            self.drawn=False
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

# %%
if __name__ == '__main__':
    win=GraphWin()
    b=Button(Point(100, 100), win=win)
    b.draw(win)
    while True:
        print(b.waitClick())