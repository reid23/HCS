from graphics import *
from math import *
import numpy as np

'''
(4 pts) Write a program called QuadraticGUI.py that uses a GUI interface to calculate the solution(s) to a quadratic equation in standard form after the user enters coefficients. Your program should meet the following specifications:
It should have a Text line which contains the standard form of a quadratic equation.
It will have three user entry boxes (with labels) in which the user will enter values for a, b, and c (which can be any real number).
There should be a “button” that the user clicks in order to perform the calculation. The result of the calculation should either be “no real solutions” or one or two solutions in the form “x = ”. Solutions should be rounded to two decimal places.
After the results are displayed on the window, the previous “button” should now say “Quit” and close the window when it is clicked.
'''

win=GraphWin('Quadratic', 800, 800)

formula=Text(Point(400, 50), 'Standard Form: ax^2 + bx + c')
formula.draw(win)


ae=Entry(Point(200, 100), 7)
be=Entry(Point(400, 100), 7)
ce=Entry(Point(600, 100), 7)

ae.draw(win)
be.draw(win)
ce.draw(win)

at=Text(Point(200, 80), 'a coefficient')
bt=Text(Point(400, 80), 'b coefficient')
ct=Text(Point(600, 80), 'c coefficient')

at.draw(win)
bt.draw(win)
ct.draw(win)

calcButton=Rectangle(Point(350, 170), Point(450, 200))
calcButton.setFill('blue')
calcText=Text(Point(400, 185), 'Calculate')
calcButton.draw(win)
calcText.draw(win)

while True:
    p=win.getMouse()
    if p.getX()>350 and p.getX()<450 and p.getY()<200 and p.getY()>170:
        break

a=float(ae.getText())
b=float(be.getText())
c=float(ce.getText())

#show stuff
calcText.setText('Quit')
calcButton.setFill('blue')

try:
    zeros = [(-b+sqrt(b*b-4*a*c))/(2*a),(-b-sqrt(b*b-4*a*c))/(2*a)]
    for counter, _ in enumerate(zeros):
        zeros[counter]=zeros[counter]+1-1 #get rid of -0.0
    if zeros[0]==zeros[1]:
        zeros=[zeros[0]]
except ValueError:
    zeros=None

zeroText=Text(Point(400, 300), text=f'Zeros: {str(zeros)[1:-1]}' if not not zeros else 'No Real Zeros')
zeroText.draw(win)

while True:
    p=win.getMouse()
    if p.getX()>350 and p.getX()<450 and p.getY()<200 and p.getY()>170:
        break

win.close()