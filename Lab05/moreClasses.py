#%%
from graphics import *

#%%
class button():
    def __init__(self, center, xSize=70, ySize=20, text:str, color='white', lineColor='black', draw=False):
        self.center=center
        self.boundary=Rectangle(Point(center.getX()-(xSize/2), center.getY()-(ySize/2)), Point(center.getX()+(xSize/2), center.getY()+(ySize/2)))
        self.boundary.setColor(color)
        self.boundary.setOutline(lineColor)
        self.text=Text(center, text)
        if draw:
            self.draw()
        def draw(self, GraphWin):
            self.boundary.draw(GraphWin)
            self.text.draw(GraphWin)

#%%
class Dye():
    def __init__(self, center, size=50, sides=6):
        """constructor for the dye class

        Args:
            center (Point object): the center point of the die
            size (int, optional): the side length of the square around the dye. Defaults to 50.
            sides (int, optional): The number of faces on the die. Defaults to 6.
        """
        self.center=center
        self.size=50
        self.sides=6
        self.border=Rectangle(Point(center.getX()-(size/2), center.getY()-(size/2)), Point(center.getX()+(size/2), center.getY()+(size/2)))
    def roll(self):
        pass

#%%
#should have done this earlier
#going to learn lists soon anyways :(
# but it'll be useful for this lab, i guess
class reidList():
    def __init__(self, *elements, length=-1):
        """constructor for reidList

        Args:
            *elements: the elements to put in the list
            length (int): the length of the list.  If given, this will override the *elements and initialize a list of zeros.
        """
        self.curElement=0 #for iterating
        if not length == -1:
            self.len=length
            for i in range(length):
                exec(f'self.element{i}=0')
        else:
            self.len=len(elements)
            for counter, i in enumerate(elements):
                theString='self.elements'+str(counter)+'='+repr(i)
                exec(f'self.elements{counter}={repr(i)}')

    def __repr__(self):
        output='reidList('
        for i in range(self.len):
            output+=f'{self.getElement(i)}'
            if not (self.len-1)==i:
                output+=','
        output+=')'
        return output

    def __str__(self):
        output='<reidList Object> ['
        for i in range(self.len):
            output+=f'{self.getElement(i)}'
            if not (self.len-1)==i:
                output+=','
        output+=']'
        return output

    def __iter__(self):
        return self
    
    def __next__(self):
        self.lastElement=self.len-1
        if self.curElement <= self.lastElement:
            self.curElement+=1
            return self.getElement(self.curElement-1)
        raise StopIteration


    def getElement(self, element):
        if element>=0:
            return eval(f'self.elements{element}')
        else:
            #for getting from the end of the list
            return eval(f'self.elements{self.len+element}')


    def setElement(self, element, value):
        exec(f'self.elements{element}={repr(value)}')

    def append(self, value):
        #because indexed at zero, self.len is always one plus the last element
        exec(f'self.elements{self.len}={repr(value)}')
        self.len+=1

    def getRange(self, start: int, stop: int, step=1):
        output=reidList()
        for i in range(start, stop, step):
            output.append(self.getElement(i))
        return output

    #bubblesort
    #not most efficient, but pretty easy
    def sort(self):
        output=eval(repr(self))
        for i in range(output.len):
            for j in range(output.len-i):
                a = output.getElement(j)
                if a != output.getElement(-1):
                    b=output.getElement(j+1)
                    if a>b:
                        output.setElement(j, b)
                        output.setElement(j+1, a)
        return output

    def __len__(self):
        return self.len

    def __add__(self, y):
        """defines how reidLists are added

        Args:
            y (int or float, or other reidList with the same shape): the variable to be added.  If it's a single value, it must be the same 
        """
        if type(y)==int or type(y)==float or type(y)==str:
            output=reidList(length=self.len)
            for i in range(self.len):
                output.setElement(i, self.getElement(i)+y)
        else:
            #in this case it's another reidList object
            assert len(y)==len(self), 'arrays are different shapes, computation could not be completed'
            output=reidList(length=self.len)
            for i in range(self.len):
                output.setElement(i, self.getElement(i)+y.getElement(i))
        return output
    
    def __sub__(self, y):
        """defines how reidLists are subtracted.  Same as __add__

        Args:
            y (int, float, str, or other reidList with the same shape): the thing to be added.  if it's a single value, it must be the same type as the reidList elements

        Returns:
            output (reidList): the result of the calculation
        """
        if type(y)==int or type(y)==float or type(y)==str:
            output=reidList(length=self.len)
            for i in range(self.len):
                output.setElement(i, self.getElement(i)-y)
        else:
            #in this case it's another reidList object
            assert len(y)==len(self), 'arrays are different shapes, computation could not be completed'
            output=reidList(length=self.len)
            for i in range(self.len):
                output.setElement(i, self.getElement(i)-y.getElement(i))
        return output
    def __mul__(self, y):
        if type(y)==int or type(y)==float or type(y)==str:
            output=reidList(length=self.len)
            for i in range(self.len):
                output.setElement(i, self.getElement(i)*y)
        else:
            #in this case it's another reidList object
            assert len(y)==len(self), 'arrays are different shapes, computation could not be completed'
            output=reidList(length=self.len)
            for i in range(self.len):
                output.setElement(i, self.getElement(i)*y.getElement(i))
        return output
    def __truediv__(self, y):
        if type(y)==int or type(y)==float or type(y)==str:
            output=reidList(length=self.len)
            for i in range(self.len):
                output.setElement(i, self.getElement(i)/y)
        else:
            #in this case it's another reidList object
            assert len(y)==len(self), 'arrays are different shapes, computation could not be completed'
            output=reidList(length=self.len)
            for i in range(self.len):
                output.setElement(i, self.getElement(i)/y.getElement(i))
        return output
    def __floordiv__(self, y):
        """defines floor division, works elementwise

        Args:
            y (int, float, or reidList): the thing to divide by

        Returns:
            output (reidList): the quotient
        """
        if type(y)==int or type(y)==float:
            output=reidList(length=self.len)
            for i in range(self.len):
                output.setElement(i, self.getElement(i)//y)
        else:
            #in this case it's another reidList object
            assert len(y)==len(self), 'arrays are different shapes, computation could not be completed'
            output=reidList(length=self.len)
            for i in range(self.len):
                output.setElement(i, self.getElement(i)//y.getElement(i))
        return output
    def __pow__(self, y):
        if type(y)==int or type(y)==float:
            output=reidList(length=self.len)
            for i in range(self.len):
                output.setElement(i, self.getElement(i)**y)
        else:
            #in this case it's another reidList object
            assert len(y)==len(self), 'arrays are different shapes, computation could not be completed'
            output=reidList(length=self.len)
            for i in range(self.len):
                output.setElement(i, self.getElement(i)**y.getElement(i))
        return output
    def __eq__(self, y):  #equivalent to a.all()
        if type(y)==int or type(y)==float or type(y)==str or type(y)==bool:
            for i in range(self.len):
                if not self.getElement(i)==y:
                    return False
        else:
            #in this case it's another reidList object
            for i in range(self.len):
                if not self.getElement(i)==y.getElement(i):
                    return False
        return True #if it's not returned by now

    #all right
    #that's all I'm doing for now
    #maybe in the future I'll add eq, >, <, etc. that work by returning a bool array
    #but not for now
    #and we'll probably learn about lists soon
    #also better support for multi-dimensional arrays would be nice but
    #again--numpy coming soon, hopefully
# %%
