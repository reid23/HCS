from graphics import *
from ReidList import ReidList as r
class Button():
    """A button class for the graphics library
        This is just a container for a box and some text that can be clicked.
        So it's not a graphicsObject, even though some methods may be similar.
        It's just a collection of graphicsObjects
    """
    def __init__(self, center, text: str = "Button", size=r(70,20), color='white', lineColor='black', draw=False, win=None):
        """constructor for a button

        Args:
            center (Point object): the center point of the button
            text (str, optional): the label on the button. Defaults to "Button"
            size (reidList, optional): the (x,y) dimensions of the button, in px. Defaults to r(70,20).
            color (str, optional): the background color of the button. Defaults to 'white'.
            lineColor (str, optional): the color of the border of the button. Defaults to 'black'.
            draw (bool, optional): Whether to draw the button upon initialization. Defaults to False.
            win ([type], optional): the GraphWin to use when drawing, if not passed in draw(), or when drawn upon intialization. Defaults to None.
        """
        self.center=center.clone() #center is a point object
        self.boundary=Rectangle(Point(center.getX()-(size(0)/2), center.getY()-(size(1)/2)), Point(center.getX()+(size(0)/2), center.getY()+(size(1)/2)))
        self.boundary.setFill(color)
        self.boundary.setOutline(lineColor)
        self.text=Text(center, text)
        self.win=win
        self.size=size
        self.drawn=False
        if draw:
            self.draw(win)
            self.drawn=True
    #draw method
    def draw(self, win=None):
        if not win:
            #if win is provided update the default win
            win=self.win
        if self.drawn:
            #avoid 'object is already draw' errors
            self.undraw()
        #draw everything
        self.boundary.draw(win)
        self.text.draw(win)
        self.drawn=True
        self.win=win
    def undraw(self):
        #don't need to worry about it already being drawn because
        #GraphicsObject.undraw() already handles this
        self.boundary.undraw()
        self.text.undraw()
        self.drawn=False

    #move function, just bundles boundary.move() and text.move() and center.move()
    def move(self, dx, dy):
        self.boundary.move(dx,dy)
        self.text.move(dx,dy)
        self.center.move(dx, dy)
    def moveAbs(self, x, y):
        #calculate absolute movement
        curPos=r(self.center.getX(), self.center.getY())
        endPos=r(x,y)
        movement=endPos-curPos
        #just use self.move() to move it
        self.move(movement(0), movement(1))
    def setSize(self, x, y):
        self.size=r(x,y)
        self.boundary.undraw() #avoid a rectangle with no pointer referencing it, or at least just make it so we can't see these phantom rectangles
        self.boundary=Rectangle(Point(self.center.getX()-(self.size(0)/2), self.center.getY()-(self.size(1)/2)), Point(self.center.getX()+(self.size(0)/2), self.center.getY()+(self.size(1)/2)))
        #redraw thing if needed
        if self.drawn:
            self.draw()
    def waitClick(self, win=None, outputAsList=True):
        """wait for a click and return the clicked point

        Args:
            win (GraphWin object, optional): the graphwin to wait for a click in. defaults to none, will use self.win.
            outputAsList (bool, optional): whether to output as reidList or as Point object. Defaults to True (reidList).

        Returns:
            point: Point object or reidList describing the clicked point
        """
        #update self.win if needed
        if not win:
            win=self.win
        
        #while true to wait for a click
        while(True):
            p=win.getMouse()
            l=r(p.getX(), p.getY()) #convert to list so I don't have to type getX() and getY() a million times
            if self.boundary.getP1().getX()<l(0)<self.boundary.getP2().getX() and self.boundary.getP1().getY()<l(1)<self.boundary.getP2().getY():
                break #break out of list and continue if the click was in the button
        #return the list or the point
        if outputAsList:
            return l
        else:
            return p
    def clicked(self, point):
        """Button.clicked():
            Determine if a point is within a button.

        Args:
            point (Point object): The input point

        Returns:
            bool: Whether or not the point is contained within self.
        """
        #basically waitClick without the while
        l=r(point.getX(), point.getY())
        if self.boundary.getP1().getX()<l(0)<self.boundary.getP2().getX() and self.boundary.getP1().getY()<l(1)<self.boundary.getP2().getY():
            return True
        return False