import os
import platform
import re
import warnings
from time import sleep
import subprocess
import applescript
import numpy as np
import pyautogui
from graphics import *

'''
### specs:
(4 pts) Write a program called PentagonGUI.py that creates an 800 x 600 pixel window, then allows the user 
to generate a pentagon by clicking on the location of the vertices (like the Triangle.py example in the 
book). Then the program should calculate the area, in “square pixels,” of that pentagon (hint: think about 
splitting it into triangles) and show this area as a text object on your window. You can assume that the 
user will click on the vertices in the order they want to be connected and that the pentagon will be 
convex. When finished, you should display a ”quit button” and have the window close after a mouse click. 
'''

win=GraphWin('Pentagon',600,800)
rect=Rectangle(Point(0,0), Point(100,200))
rect.draw(win)
win.flush()
kernel=np.load('kernel.npy')

#get window location
#differs based on os
print(platform.platform())
re.search(r'^Darwin.*', platform.platform())

if (not not re.search(r'^Darwin.*|^macOS.*', platform.platform()))==True:
    #mac
    #make sure appscript is installed
    def getWinPos():
        p=subprocess.Popen(['osascript','GetWinPos.applescript'])
        print(p)
        
elif (not not re.search(r'^Linux.*', platform.platform()))==True:
    if not re.search(r'.*bionic$', platform.platform()):
        warnings.warn('This code is only tested on Ubuntu Bionic.')
    #linux!
    def getWinPos():
        pass
else:
    #windows not implemented yet
    #to be fair neither is haiku, FreeBSD, TempleOS, or most other things
    #you could probably use some python library or
    #or an ahk script with WinGetPos []
    raise NotImplementedError("Windows, or whatever else you're using,  is not supported yet.")


#sleep(5)
#getWinPos()
win.getMouse()
getWinPos()

win.getMouse()
win.close()
exit()
