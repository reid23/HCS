'''
Author: Reid Dye

This file contains code to calculate the zeros of a quadratic function.
It then displays this information onscreen.
'''

from graphics import *
from math import *
import numpy as np

def main():
    #make window
    win=GraphWin('Quadratic', 800, 800)

    #write formula
    formula=Text(Point(400, 50), 'Standard Form: ax^2 + bx + c')
    formula.draw(win)

    #place text boxes
    ae=Entry(Point(200, 100), 7)
    be=Entry(Point(400, 100), 7)
    ce=Entry(Point(600, 100), 7)
    ae.draw(win)
    be.draw(win)
    ce.draw(win)

    #place text box labels
    at=Text(Point(200, 80), 'a coefficient')
    bt=Text(Point(400, 80), 'b coefficient')
    ct=Text(Point(600, 80), 'c coefficient')
    at.draw(win)
    bt.draw(win)
    ct.draw(win)

    #create calculate button and label
    calcButton=Rectangle(Point(350, 170), Point(450, 200))
    calcButton.setFill('blue')
    calcText=Text(Point(400, 185), 'Calculate')
    calcButton.draw(win)
    calcText.draw(win)

    #wait for button to be pressed
    while True:
        p=win.getMouse()
        if p.getX()>350 and p.getX()<450 and p.getY()<200 and p.getY()>170:
            break
    
    #get user's values
    a=float(ae.getText())
    b=float(be.getText())
    c=float(ce.getText())

    #change button to quit button
    calcText.setText('Quit')
    calcButton.setFill('red')

    #use quadratic formula
    try:
        zeros = [(-b+sqrt(b*b-4*a*c))/(2*a),(-b-sqrt(b*b-4*a*c))/(2*a)]
        for counter, _ in enumerate(zeros):
            zeros[counter]=zeros[counter]+1-1 #get rid of -0.0
        if zeros[0]==zeros[1]:
            zeros=[zeros[0]]
    
    #if there are no real coefficients
    except ValueError:
        zeros=None

    #display the output of the calculation
    zeroText=Text(Point(400, 300), text=f'Zeros: x = {str(zeros)[1:-1]}' if not not zeros else 'No Real Zeros')
    zeroText.draw(win)

    #wait for quit button to be clicked
    while True:
        p=win.getMouse()
        if p.getX()>350 and p.getX()<450 and p.getY()<200 and p.getY()>170:
            break

    win.close()

if __name__ == '__main__':
    main()