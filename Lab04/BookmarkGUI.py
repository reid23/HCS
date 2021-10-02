from graphics import *
from time import sleep
'''
### specs
Create a 250 x 600 graphics window
Draw a design using at least one of each shape: Point, Line, Circle, Rectangle, Oval, and Polygon
Draw at least one graphics object using the clone method
Make your bookmark colorful by filling shapes that enclose space with different colors 
Remember that a user mouse click should close your window and end the program
'''

win=GraphWin("Bookmark", 250, 600)
win.setCoords(0,0,250,600)

point=Point(100,300)
line=Line(Point(50,500), Point(200,50))
rect=Rectangle(Point(10,40), Point(240,590))
innerRect=Rectangle(Point(150,150), Point(200,400))
oval=Oval(Point(15,400), Point(50,300))
circle=Circle(Point(200,200), 30)
poly1=Polygon(Point(20,50), Point(23,70), Point(50,75), Point(55, 60), Point(25, 45))
poly2=poly1.clone()

txt=Text(Point(125,30), "'Modern Art'")
secondtxt=Text(Point(125,20), 'Graphics.py on Computer')
thirdtxt=Text(Point(125,10), 'Reid Dye, 2021')

circle.setFill('green')
innerRect.setFill('blue')
oval.setFill('red')
poly1.setOutline('purple')
poly1.setFill('black')
poly2.move(150,450)
poly2.setFill('cyan')

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

p=Point(5,5)
p.draw(win)


win.getMouse()
import applescript
r=applescript.tell.app('System Events', 'get position of first window of application process "python"')
print(r.out)
win.close()
exit()


