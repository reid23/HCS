#%%
from graphics import *
from reidList import reidList as r
from math import *
#%%


#%%
def rotMat(yaw, pitch, roll):
    a=radians(yaw)
    b=radians(pitch)
    c=radians(roll)
    mat=r(
        r(cos(a)*cos(b), sin(a)*cos(b), -sin(b)), 
        r((cos(a)*sin(b)*sin(c))-(sin(a)*cos(c)), (sin(a)*sin(b)*sin(c))+(cos(a)*cos(c)), cos(b)*sin(c)),
        r((cos(a)*sin(b)*cos(c))+(sin(a)*sin(c)), (sin(a)*sin(b)*cos(c))-(cos(a)*sin(c)), cos(b)*cos(c))
    )
    return mat

dot=lambda a, b: a(0)*b(0) + a(1)*b(1) + a(2)*b(2)
cross=lambda a, b: r(a(1)*b(2) - a(2)*b(1), a(2)*b(0) - a(0)*b(2), a(0)*b(1) - a(1)*b(0))
def qMul(a, b):
    real=a(0)*b(0) - dot(a.getRange(1,4), b.getRange(1,4))
    c=a(0)*b + b(0)*a + cross(a.getRange(1,4), b.getRange(1,4))
    return r(
        real,
        c(0),
        c(1),
        c(2)
    )

def rotate(axis, degrees, points):
    """rotate a set of points by an angle around an arbitrary axis
    Args:
        axis (reidList): a 3d vector representing the axis around which to rotate the points
        degrees (float, int): the degrees around the axis to rotate the points
        points (reidList): The points, in form [[x0,y0,z0], [x1,y1,z1], ..., [xn, yn, zn]], to rotate
    Returns:
        reidList: a list of points, in the same format as the input points, that have been rotated.
    """
    #init output array
    output=r(len(points))
    #convert axis to a unit vector
    ax=axis/sqrt((axis(0)**2 + axis(1)**2 + axis(2)**2))

    #create rotation quaternion
    ang=radians(degrees)
    rQ=r(cos(ang/2), ax(0)*sin(ang/2), ax(1)*sin(ang/2), ax(2)*sin(ang/2))
    CrQ=rQ*(-1)
    CrQ.set(0, CrQ(0)*(-1))
    counter=0
    for p in points:
        #create input quaternion (just add zero as the real part, have x, y, z as i, j, k coefs)
        curPt=r(0, p(0), p(1), p(2))

        #multiply to rotate
        result=qMul(qMul(rQ, curPt), CrQ)
        
        output.set(counter, result)
        counter += 1
    
    counter=0
    for i in output:
        output.set(counter, i.getRange(1,4))
        counter += 1
    return output


#%%
class Dye():
    def __init__(self, center, size=50, sides=6):
        """constructor for the dye class

        Args:
            center (Point object): the center point of the die
            size (int, optional): the side length of the square around the dye. Defaults to 50.
            sides (int, optional): The number of faces on the die. Defaults to 6.
        """

        #TODO: implement different numbers of sides
        self.vecs=r(
            r(1,1,1),
            r(-1,1,1),
            r(-1,-1,1),
            r(1,-1,1),
            r(1,1,-1),
            r(-1,1,-1),
            r(-1,-1,-1),
            r(1,-1,-1),
        )
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