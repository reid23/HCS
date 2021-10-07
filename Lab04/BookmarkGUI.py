'''
Author: Reid Dye

This file contains code to display a bookmark.
'''

from graphics import *

def main():
    win=GraphWin("Bookmark", 250, 600)
    win.setCoords(0,0,250,600)

    #using point
    point=Point(100,300)
    
    #using line
    line=Line(Point(80,500), Point(200,100))
    
    #using rectangle
    #this is the frame of the painting
    rect=Rectangle(Point(10,70), Point(240,590))
    innerRect=Rectangle(Point(150,150), Point(200,400))

    #using oval
    oval=Oval(Point(15,400), Point(50,300))

    #using circle
    circle=Circle(Point(200,200), 30)

    #using polygon
    poly1=Polygon(Point(20,100), Point(23,130), Point(50,150), Point(55, 110), Point(25, 90))
    
    #using clone
    poly2=poly1.clone()

    #using text
    #caption with title and info
    txt=Text(Point(125,50), '"Modern Art"')
    secondtxt=Text(Point(125,30), 'Graphics.py on Computer')
    thirdtxt=Text(Point(125,10), 'Reid Dye, 2021')

    #adding color
    circle.setFill('green')
    innerRect.setFill('blue')
    oval.setFill('red')
    poly1.setOutline('purple')
    poly1.setFill('black')
    poly2.move(150,400)
    poly2.setFill('cyan')

    #drawing all of the stuff
    poly2.draw(win)
    poly1.draw(win)
    txt.draw(win)
    secondtxt.draw(win)
    thirdtxt.draw(win)
    rect.draw(win)
    innerRect.draw(win)
    oval.draw(win)
    line.draw(win)
    point.draw(win)
    circle.draw(win)

    #making it close on click
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()