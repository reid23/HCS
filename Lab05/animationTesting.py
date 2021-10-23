from reidList import reidList as r
from reidList import reidList
from graphics import *
from math import *
from random import randrange

class Cube():
    def __init__(self):
        self.corners=r(
            r(1,1,1),
            r(-1,1,1),
            r(-1,-1,1),
            r(1,-1,1),
            r(1,1,-1),
            r(-1,1,-1),
            r(-1,-1,-1),
            r(1,-1,-1),
        )

    def _sort(self, arr, element):
        output=eval(repr(arr))
        for i in range(len(output)-1):
            for j in range(len(output)-i-1):
                # use < here instead of > to sort from greatest to smallest
                if output(j)(element) < output(j+1)(element) :
                    outputJ=output(j) #because we can't do multiple assignment with reidList elements
                    output.set(j, output(j+1))
                    output.set(j+1, outputJ)
        return output

    def _getDistance(self, p1, p2):
        return sqrt((p1(0)-p2(0))**2 + (p1(1)-p2(1))**2 + (p1(2)-p2(2))**2)


    def draw(self, dAng, win):
        self._lines(dAng)
        for l in self.lines:
            l.draw(win)
    def undraw(self):
        for l in self.lines:
            l.undraw()
    def _lines(self, dAng):
        #sort corners by z pos
        '''
        The legit way, that also works with dice with more than 6 sides:
        1. find the area of the polygon formed by all of the already-iterated-through
            points
        2. find the area of the polygon formed by all of the already-iterated-through
            points and the current point
        3. If the area is bigger with the new point, it should be displayed.  
            Otherwise, it should be discarded.
        But yahtzee uses only d6's, so here's the bodge way: remove the last point
        (the one lowest in z).  This is because there is always only one point that is
        under the "shadow" of the cube.  Actually, this is not true if the die is sitting
        flat on its face, but in that case the extra points will be underneath the
        existing points and it won't be visible to the veiwer.
        '''
        self._rotateQ(r(1,1,1), dAng)
        corners=self._sort(self.corners, 2)
        # print('length of corners[]:', len(self.corners))
        # print('corners:', corners)
        corners=corners.getRange(0, 7)
        lines=r()
        corners2=eval(repr(corners))
        for i in corners:
            for j in corners2:
                if abs(2-self._getDistance(i, j))>0.1:
                    pass
                else:
                    lines.append(Line(Point(i(0), i(1)), Point(j(0), j(1))))

        self.lines=lines
    
    #dot and cross products (for 3d vectors)
    def _dot(self, a, b):
        return a(0)*b(0) + a(1)*b(1) + a(2)*b(2)

    def _cross(self, a, b):
        return r(a(1)*b(2) - a(2)*b(1), a(2)*b(0) - a(0)*b(2), a(0)*b(1) - a(1)*b(0))

    #quaternion multiplication
    def _qMul(self, a, b):
        real=a(0)*b(0) - self._dot(a.getRange(1,4), b.getRange(1,4))
        c=b.getRange(1,4)*a(0) + a.getRange(1,4)*b(0) + self._cross(a.getRange(1,4), b.getRange(1,4))
        return r(
            real,
            c(0),
            c(1),
            c(2)
        )

    #rotate vectors using quaterions
    def _rotateQ(self, axis, degrees):
        """rotate a set of points by an angle around an arbitrary axis
        Args:
            axis (reidList): a 3d vector representing the axis around which to rotate the points
            degrees (float, int): the degrees around the axis to rotate the points
            points (reidList): The points, in form [[x0,y0,z0], [x1,y1,z1], ..., [xn, yn, zn]], to rotate
        Returns:
            reidList: a list of points, in the same format as the input points, that have been rotated.
        """
        #init output array
        output=r(length=len(self.corners))
        #convert axis to a unit vector
        ax=axis/sqrt((axis(0)**2 + axis(1)**2 + axis(2)**2))

        #create rotation quaternion
        ang=radians(degrees)
        rQ=r(cos(ang/2), ax(0)*sin(ang/2), ax(1)*sin(ang/2), ax(2)*sin(ang/2))
        CrQ=rQ*(-1)
        CrQ.set(0, CrQ(0)*(-1))
        counter=0
        for p in self.corners:
            #create input quaternion (just add zero as the real part, have x, y, z as i, j, k coefs)
            curPt=r(0, p(0), p(1), p(2))

            #multiply to rotate
            result=self._qMul(self._qMul(rQ, curPt), CrQ)
            
            output.set(counter, result)
            counter += 1
        
        counter=0
        for i in output:
            output.set(counter, i.getRange(1,4))
            counter += 1
        self.corners=output

    def _rotateRodrigues(self, axis, degrees):
        #the *slooooooooowest* algorithm in aaaaAAAAAALLLLllll of mexico
        #actually pretty efficient though
        output=r()
        ax=axis/sqrt((axis(0)**2 + axis(1)**2 + axis(2)**2))
        for p in self.corners:
            output.append(p*cos(radians(degrees)) + self._cross(ax, p) + ax*self._dot(ax, p)*(1-cos(radians(degrees))))

        self.corners=output



# one=r(0, 0, randrange(0, 360))
# two=r(0, 90, randrange(0, 360))
# three=r(-90, 0, randrange(0, 360))
# four=r(90, 0, randrange(0, 360))
# five=r(0, -90, randrange(0, 360))
# six=r(0, 180, randrange(0, 360))

win=GraphWin('animation testing', 1500, 1500, autoflush=False)
win.setCoords(-3,-3,3,3)


cube=Cube()

from time import sleep

for _ in range(10000):
    cube.draw(10, win)
    win.flush()
    cube.undraw()









'''
show(corners, win)

win.getMouse()
# win.close()
# win=GraphWin('animation testing', 1000, 1000)
# win.setCoords(-3,-3,3,3)


# print('rR:', rotateRodrigues(r(1,1,1), 60, corners))
# print('Q:', rotateQ(r(1,1,1), 60, corners))
show(rotateQ(r(1,1,1), 60, corners), win)

win.getMouse()
'''