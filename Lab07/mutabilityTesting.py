from graphics import *
class C():
    def __init__(self):
        self.win=GraphWin()
        self.circle={'c':Circle(Point(100, 100), 50)}
    def getCircle(self, name):
        return self.circle[name]
    def setCircle(self, circle, name):
        self.circle[name].undraw()
        self.circle[name]=circle

c=C()

c.getCircle('c').draw(c.win)

c.win.getMouse()

c.getCircle('c').move(50, 50)

c.win.getMouse()

c.setCircle(Circle(Point(100, 100), 50), 'c')
c.getCircle('c').draw(c.win)

c.win.getMouse()