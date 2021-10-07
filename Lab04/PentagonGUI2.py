'''
Author: Reid Dye

This file contains code to let the user draw a pentagon.  It then
calculates and displays this information.
'''

from graphics import *
import numpy as np

def main():
    #make window
    win=GraphWin('Pentagon',600,800)

    #display instructions
    instructions=Text(Point(300,400), 'Click your first point to start.')
    instructions.draw(win)

    points=[0,0,0,0,0] #avoid list.append()

    #wait for the points
    #could have used a loop, but whatever
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

    #unpack list for Polygon()
    p0,p1,p2,p3,p4=points

    #create polygon and make it look good
    pentagon=Polygon(p0,p1,p2,p3,p4)
    pentagon.draw(win)
    pentagon.setFill(color_rgb(150, 150, 150))

    #get coords from Point objects
    xs=np.array([i.getX() for i in points])
    ys=np.array([i.getY() for i in points])

    #*shoelace formula
    #from wikipedia
    # https://en.wikipedia.org/wiki/Shoelace_formula#Examples
    # pentagon example

    #please excuse my use of np
    #I didn't want to write out x1= blah, x2=blah, x3=blah, etc
    firstHalf=np.sum(np.roll(ys, -1)*xs)
    secondHalf=np.sum(np.roll(xs, -1)*ys)

    #calculate and display area
    area=0.5*(abs(firstHalf-secondHalf))
    areaText=Text(Point(300,50), f"Area: {area} px^2")
    areaText.draw(win)

    #make and show quit button
    quitButton=Rectangle(Point(250, 100), Point(350, 150))
    quitButton.setFill('red')
    quitText=Text(Point(300, 125), 'Quit')
    quitButton.draw(win)
    quitText.draw(win)

    #wait until quit button is clicked, then close window
    while True:
        p=win.getMouse()
        if p.getX()<350 and p.getX()>250 and p.getY()<150 and p.getY()>100:
            break
    win.close()


if __name__ == '__main__':
    main()