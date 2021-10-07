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
        #do with X11
        pass
else:
    #windows not implemented yet
    #to be fair neither is haiku, FreeBSD, TempleOS, or most other things
    #you could use win32gui
    #or an ahk script with WinGetPos
    raise NotImplementedError("Windows, or whatever else you're using,  is not supported yet.")


#sleep(5)
#getWinPos()
win.getMouse()
getWinPos()

win.getMouse()
win.close()
exit()
