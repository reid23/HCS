from reidList import reidList as r
from reidList import reidList
from graphics import *
from math import *
from random import randrange

corners=r(
    r(1,1,1),
    r(-1,1,1),
    r(-1,-1,1),
    r(1,-1,1),
    r(1,1,-1),
    r(-1,1,-1),
    r(-1,-1,-1),
    r(1,-1,-1),
)

# one=r(0, 0, randrange(0, 360))
# two=r(0, 90, randrange(0, 360))
# three=r(-90, 0, randrange(0, 360))
# four=r(90, 0, randrange(0, 360))
# five=r(0, -90, randrange(0, 360))
# six=r(0, 180, randrange(0, 360))

win=GraphWin('animation testing', 1000, 1000)
win.setCoords(-3,-3,3,3)

def sort(arr, element):
    output=eval(repr(arr))
    for i in range(len(output)-1):
        for j in range(len(output)-i-1):
            # use < here instead of > to sort from greatest to smallest
            if output(j)(element) < output(j+1)(element) :
                outputJ=output(j) #because we can't do multiple assignment with reidList elements
                output.set(j, output(j+1))
                output.set(j+1, outputJ)
    return output

def getDistance(p1, p2):
    return sqrt((p1(0)-p2(0))**2 + (p1(1)-p2(1))**2 + (p1(2)-p2(2))**2)

def show(corners, win):
    #sort corners by z pos
    pts=r()
    corners=sort(corners, 2)
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
    print('length of corners[]:', len(corners))
    corners=corners.getRange(0, 7)
    for c in corners:
        pts.append(Point(c(0), c(1)))
    for p in pts:
        p.draw(win)
    lines=r()
    corners2=eval(repr(corners))
    for i in corners:
        for j in corners2:
            print('i:', i)
            print('j:', j)
            print(abs(2-getDistance(i, j)))
            if abs(2-getDistance(i, j))>0.2:
                pass
            else:
                lines.append(Line(Point(i(0), i(1)), Point(j(0), j(1))))
    
    # lines=r(
    #     Line(pts(0), pts(1)),
    #     Line(pts(0), pts(2)),
    #     Line(pts(0), pts(3)),
    #     Line(pts(0), pts(4)),
    #     Line(pts(0), pts(5)),
    #     Line(pts(0), pts(6)),
    #     Line(pts(1), pts(2)),
    #     Line(pts(1), pts(3)),
    #     Line(pts(1), pts(4)),
    #     Line(pts(1), pts(5)),
    #     Line(pts(1), pts(6)),
    #     Line(pts(2), pts(3)),
    #     Line(pts(2), pts(4)),
    #     Line(pts(2), pts(5)),
    #     Line(pts(2), pts(6)),
    #     Line(pts(3), pts(4)),
    #     Line(pts(3), pts(5)),
    #     Line(pts(3), pts(6)),
    #     Line(pts(4), pts(5)),
    #     Line(pts(4), pts(6)),
    #     Line(pts(5), pts(6))
    # )
    for l in lines:
        l.draw(win)

dot=lambda a, b: a(0)*b(0) + a(1)*b(1) + a(2)*b(2)
cross=lambda a, b: r(a(1)*b(2) - a(2)*b(1), a(2)*b(0) - a(0)*b(2), a(0)*b(1) - a(1)*b(0))
def qMul(a, b):
    real=a(0)*b(0) - dot(a.getRange(1,4), b.getRange(1,4))
    c=b.getRange(1,4)*a(0) + a.getRange(1,4)*b(0) + cross(a.getRange(1,4), b.getRange(1,4))
    return r(
        real,
        c(0),
        c(1),
        c(2)
    )

def rotateQ(axis, degrees, points):
    """rotate a set of points by an angle around an arbitrary axis
    Args:
        axis (reidList): a 3d vector representing the axis around which to rotate the points
        degrees (float, int): the degrees around the axis to rotate the points
        points (reidList): The points, in form [[x0,y0,z0], [x1,y1,z1], ..., [xn, yn, zn]], to rotate
    Returns:
        reidList: a list of points, in the same format as the input points, that have been rotated.
    """
    #init output array
    output=r(length=len(points))
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

def rotateRodrigues(axis, degrees, points):
    #the *slooooooooowest* algorithm in aaaaAAAAAALLLLllll of mexico
    #actually pretty efficient though
    output=r()
    ax=axis/sqrt((axis(0)**2 + axis(1)**2 + axis(2)**2))
    for p in points:
        output.append(p*cos(radians(degrees)) + cross(ax, p) + ax*dot(ax, p)*(1-cos(radians(degrees))))

    return output
show(corners, win)

win.getMouse()
win.close()
win=GraphWin('animation testing', 1000, 1000)
win.setCoords(-3,-3,3,3)


print('rR:', rotateRodrigues(r(1,1,1), 60, corners))
print('Q:', rotateQ(r(1,1,1), 60, corners))
show(rotateRodrigues(r(1,1,1), 60, corners), win)

win.getMouse()