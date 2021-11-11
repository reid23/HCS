from graphics import *
import numpy as np
win=GraphWin('Shark Game', 800, 900)

#set the coordinates so it makes sense with the grid
win.setCoords(-0.5, -1.5, 9.5, 9.5)

#make the grid
for i in np.linspace(0, 9, 10):
    for j in np.linspace(0, 9, 10):
        Rectangle(Point(i-0.5, j-0.5), Point(i+0.5, j+0.5)).draw(win)

win.getMouse()

pointLabel=Text(Point(5, -1), 'no point clicked yet')
while True:
    p=win.getMouse()
    pointLabel.undraw()
    p=np.array([p.getX(), p.getY()])
    p=np.around(p)
    pointLabel.setText(str(p))
    pointLabel.draw(win)
    