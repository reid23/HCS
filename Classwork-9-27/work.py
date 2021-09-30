#%%
from graphics import *

#%%
def gui():
    win=GraphWin(width=500,height=500, autoflush=False)
    
    p1=Point(80,40)
    p1.draw(win)

    p2=Point(130,180)
    p2.draw(win)

    r=Rectangle(p1,p2)
    r.setFill('blue')
    r.draw(win)

    label=Text(Point(105,110),'Blue Rectangle')
    label.draw(win)
# %%
class pltThing(Image, )