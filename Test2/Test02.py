from graphics import *
from random import randrange
'''
specs:
1. open a 500x400 window
2. draw a circle in the middle of the window, with a 50px radius
3. the circle must be entirely blue
4. the window should close with a mouse click
5. the function should not run with the file (no if __name__ == '__main__':)
'''
def prob17():
    w, h = 500, 400 #variables for adaptability
    win=GraphWin(width=w, height=h)
    circle=Circle(Point(w/2, h/2), 50)
    circle.setFill('blue')
    circle.setOutline('blue')
    circle.draw(win)

    win.getMouse()
    win.close()
    
    #don't need to del() all the objects
    #because scope
    #it won't interfere elsewhere

class Truck():
    def __init__(self, make: str, model: str):
        """constructor for a truck object.

        Args:
            make (str): the make of the truck. Ex 'toyota'.
            model (str): the model of the truck.  Ex 'tacoma'.
        """
        self.make=make
        self.model=model

    def __str__(self):
        return self.make + ' ' + self.model
    
    def __repr__(self):
        return 'Truck(' + "'" + self.make + "'" + ', ' + "'" + self.model + "'" + ')'

    #getters and setters
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    
    def setMake(self, make: str):
        self.make=make
    def setModel(self, model: str):
        self.model=model

def prob18():
    print('Testing all truck methods.  If error is encountered, execution will be halted as normal.')
    t=Truck('Toyota', 'Tacoma')
    t.getMake()
    t.getModel()
    t.setMake('Toyota')
    t.setModel('Tacoma')
    str(t)
    repr(t)

    print('All methods executed successfully, now verifying their outputs.')

    if not t:
        print("Test failed. Ran Truck('Toyota', 'Tacoma'), expected an output, received", t)
        return #exit the function, test failed
    if not str(t)=='Toyota Tacoma':
        print("Test failed. with t=Truck('Toyota', 'Tacoma'), evaluated str(t). \nExpected 'Toyota Tacoma', but received", str(t))
        return
    try:
        reprTestTruck=eval(repr(t))
    except:
        print('Test failed: eval(repr(<truck object>)) returned an error.')


    if not t.getMake()=='Toyota':
        print("Test failed. with t=Truck('Toyota', 'Tacoma'), evaluated t.getMake. \nExpected 'Toyota', but received", t.getMake())
        return
    
    if not t.getModel()=='Tacoma':
        print("Test failed. with t=Truck('Toyota', 'Tacoma'), evaluated t.getMake. \nExpected 'Tacoma', but received", t.getModel())
        return
    
    t.setMake('Ford')
    t.setModel('F-150')

    if not t.getMake()=='Ford':
        print("Test failed. with t=Truck('Toyota', 'Tacoma'), evaluated t.setMake('Ford'). \nExpected t.getMake() to return 'Ford', but received", t.getMake())
        return
    if not t.getModel()=='F-150':
        print("Test failed. with t=Truck('Toyota', 'Tacoma'), evaluated t.setModel('F-150'). \nExpected t.getModel() to return 'F-150', but received", t.getModel())
        return
    
    #yay if it's gotten this far, that means it works!
    print('''
    ===================================================
    ~~~~~~~~~~~~~~~~~All tests passed!~~~~~~~~~~~~~~~~~
    ===================================================
    ''')

def prob19():
    w, h = 400, 400
    win=GraphWin('Try to click on the Target!', w, h)

    p1=Point(200, 200)
    p2=Point(250, 270)
    target=Rectangle(p1, p2)
    target.setFill('red')
    target.setOutline('red')

    targetText=Text(target.getCenter(), 'Target')

    scoreBoardOutline=Rectangle(Point(w-100, 0), Point(w, 100))
    scoreBoardLine=Line(Point(w-50, 0), Point(w-50, 100))
    hitsText=Text(Point(w-75, 25), 'Hits')
    missesText=Text(Point(w-25, 25), 'Misses')

    hits=Text(Point(w-75, 75), '0')
    misses=Text(Point(w-25, 75), '0')
    
    hits.draw(win)
    misses.draw(win)
    scoreBoardLine.draw(win)
    hitsText.draw(win)
    missesText.draw(win)
    scoreBoardOutline.draw(win)
    targetText.draw(win)
    target.draw(win)

    while True:
        p=win.getMouse()
        if 200<p.getX()<250 and 200<p.getY()<270:
            hits.setText(str(int(hits.getText())+1))
        else:
            misses.setText(str(int(misses.getText())+1))
        if int(hits.getText())==10 or int(misses.getText())==10:
            break
    Text(Point(100, 100), 'Game over - Click anywhere to quit').draw(win)
    win.getMouse()
    win.close()
if __name__ == '__main__':
    prob19()