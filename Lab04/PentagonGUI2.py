#%%
from graphics import *
import numpy as np

#%%
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

xs=np.array([i.getX() for i in points])
ys=np.array([i.getY() for i in points])

#*shoelace formula
#from wikipedia
# https://en.wikipedia.org/wiki/Shoelace_formula#Examples
# pentagon example

firstHalf=np.sum(np.roll(ys, -1)*xs)
secondHalf=np.sum(np.roll(xs, -1)*ys)

area=0.5*(abs(firstHalf-secondHalf))

areaText=Text(Point(300,50), f"Area: {area}")
areaText.draw(win)

quitButton=Rectangle(Point(250, 100), Point(350, 150))
quitButton.setFill('red')
quitText=Text(Point(300, 125), 'Quit')
quitButton.draw(win)
quitText.draw(win)

while True:
    p=win.getMouse()
    if p.getX()<350 and p.getX()>250 and p.getY()<150 and p.getY()>100:
        break
win.close()


