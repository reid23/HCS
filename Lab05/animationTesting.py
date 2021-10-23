from reidList import reidList as r
from graphics import *
from math import *
from random import randrange

corners=r(
    r(1,1,1),
    r(-1,1,1),
    r(-1,-1,1),
    r(1,-1,1),
    r(1,1,-1),
    r(-1,1,-1),
    r(-1,-1,-1),
    r(1,-1,-1),
)

one=r(0, 0, randrange(0, 360))
two=r(0, 90, randrange(0, 360))
three=r(-90, 0, randrange(0, 360))
four=r(90, 0, randrange(0, 360))
five=r(0, -90, randrange(0, 360))
six=r(0, 180, randrange(0, 360))


win=graphWin('animation testing', 1000, 1000)
win.setCoords(0,0,10,10)

def sort(arr):
    

def show(corners):
    #sort corners by z pos
    