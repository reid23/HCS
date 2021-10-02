from graphics import *
import numpy as np

win=GraphWin('Pentagon',600,800)

instructions=Text(Point(300,400), 'Click your first point to start.')
instructions.draw(win)

points=[0,0,0,0,0] #avoid list.append()


p=win.getMouse()
points[0]=p

instructions.undraw()

p=win.getMouse()
points[1]=p

p=win.getMouse()
points[2]=p

p=win.getMouse()
points[3]=p

p=win.getMouse()
points[4]=p

p0,p1,p2,p3,p4=points
pentagon=Polygon(p0,p1,p2,p3,p4)
pentagon.draw(win)

win.getMouse()
win.close()


