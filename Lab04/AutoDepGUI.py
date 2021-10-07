'''
Author: Reid Dye

This file contains code to calculate depreciation over time at a 15% depreciation rate.
It then graphs this information.
'''


from graphics import *
from math import *
import numpy as np

def main():
    #make window
    win=GraphWin('AutoDep', 800, 600)

    #make textboxes and labels
    valueInput=Entry(Point(250, 70), 10)
    yearInput=Entry(Point(550, 70), 10)
    valueText=Text(Point(250, 50), 'Initial Value')
    yearText=Text(Point(550, 50), 'Time Since Purchase (Y)')

    #set default values
    valueInput.setText('10000')
    yearInput.setText('15')

    #draw all of the stuff
    valueInput.draw(win)
    yearInput.draw(win)
    valueText.draw(win)
    yearText.draw(win)

    #make calculate button and label
    calcButton=Rectangle(Point(350, 170), Point(450, 200))
    calcButton.setFill(color_rgb(100, 160, 255))
    calcText=Text(Point(400, 185), 'Calculate')
    calcButton.draw(win)
    calcText.draw(win)

    #wait until button is pressed
    while True:
        p=win.getMouse()
        if p.getX()>350 and p.getX()<450 and p.getY()<200 and p.getY()>170:
            break

    #get the user's input
    initialVal=float(valueInput.getText())
    years=int(yearInput.getText())+1

    #init the values[] array
    #a friend at robotics told me this:
    # > A brit making sure your
    # > class has a constructor:
    # > "__init__'s in it, innit?"
    values=np.zeros(years)
    values[0]=initialVal

    #hide all the stuff
    calcButton.undraw()
    calcText.undraw()
    yearInput.undraw()
    yearText.undraw()
    valueInput.undraw()
    valueText.undraw()


    #prevent my brain from breaking
    #make the window coords the same as the graph coords
    #or at least the same direction
    win.setCoords(0,0,800,600)

    #create array with all of the values for each year
    for i in range(years):
        if i==0:
            continue
        values[i]=values[i-1]*0.85
    
    #(0, 0) in the graph, for future use
    g0=np.array([50, 50])

    #create axes
    xAx=Line(Point(0, g0[1]), Point(800, g0[1]))
    yAx=Line(Point(g0[0], 0), Point(g0[0], 600))
    xAx.draw(win)
    yAx.draw(win)


    #make labels
    labels=np.empty(5, dtype='S7') #should be long enough
    for i in range(5):
        labels[i]=str(round((initialVal*(i/4))/1000, 1)) + 'k'

    #useful vars
    yMin=g0[1]
    yMax=600-g0[1]-20
    xMin=g0[0]
    xMax=800

    #vertical tick marks and labels
    for i in range(5):
        Line(Point(xMin-5, yMin+(yMax*(i/4))), Point(xMin+5, (yMin+(yMax*(i/4))))).draw(win)
        Text(Point(xMin/2, (yMax*(i/4))+10+yMin), labels[i]).draw(win)

    #horizontal tick marks and labels
    #markers are in the center of the bars
    #thanks bracketPairColoriser extension for making
    #what would otherwise be unreadable
    #slightly better
    for i in range(years):
        Line(Point(((i/years)*(xMax-xMin))+xMin+(((xMax-xMin)/years)/2), yMin-5), Point(((i/years)*(xMax-xMin))+xMin+(((xMax-xMin)/years)/2), yMin+5)).draw(win)
        Text(Point(((i/years)*(xMax-xMin))+xMin+(((xMax-xMin)/years)/2), yMin-15), i).draw(win)

    #make bars
    for i in range(years):
        r=Rectangle(Point((i/years)*(xMax-xMin)+xMin, yMin), Point(((i+1)/years)*(xMax-xMin)+xMin, (yMin+(yMax*(values[i]/initialVal)))))
        r.setFill(color_rgb(100, 160, 255))
        r.setWidth(2)
        r.draw(win)

    #I thought about making a custom button class
    #but that seemed kinda pointless as we're going to make one soon anyway
    #and besides, I've got a physics test to study for!
    #anyway, make a quit button:
    quitButton=Rectangle(Point(650, 500), Point(750, 570))
    quitButton.setFill(color_rgb(100, 160, 255))
    quitText=Text(Point(700, 535), 'Quit')
    quitButton.draw(win)
    quitText.draw(win)

    #wait for quit button to be clicked, then close window
    while True:
        p=win.getMouse()
        if p.getX()>650 and p.getX()<750 and p.getY()<570 and p.getY()>500:
            break

    win.close()

if __name__ == '__main__':
    main()