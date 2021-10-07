#the easy way lol


import matplotlib.pyplot as plt
from graphics import *
from math import *
import numpy as np
#import io  //was trying to import the mpl plot into a graphWin but that didn't work out
#import cv2


def main():
    win=GraphWin('AutoDep', 800, 300)

    valueInput=Entry(Point(250, 70), 10)
    yearInput=Entry(Point(550, 70), 10)
    valueText=Text(Point(250, 50), 'Initial Value')
    yearText=Text(Point(550, 50), 'Time Since Purchase (Y)')

    valueInput.draw(win)
    yearInput.draw(win)
    valueText.draw(win)
    yearText.draw(win)

    calcButton=Rectangle(Point(350, 170), Point(450, 200))
    calcButton.setFill('blue')
    calcText=Text(Point(400, 185), 'Calculate')
    calcButton.draw(win)
    calcText.draw(win)

    while True:
        p=win.getMouse()
        if p.getX()>350 and p.getX()<450 and p.getY()<200 and p.getY()>170:
            break

    initialVal=float(valueInput.getText())
    years=int(yearInput.getText())+1

    values=np.zeros(years)
    values[0]=initialVal

    for i in range(years):
        if i==0:
            continue
        values[i]=values[i-1]*0.85

    plt.bar(range(years), values, width=1, align='edge')
    plt.xlim(0, years)

    plt.show()

if __name__ == '__main__':
    main()