from SharkGUI import *
from Shark import *
s=Shark()
a=Shark(pos=[7,4])
b=Shark(pos=[8,3])
c=Shark(pos=[2,7])

g=Gui(s, a, b, c, None, None, None, None, None, None, None, drawButtons=False, drawEntries=False, drawMsgBox=False)
g.drawGrid()
g.getMouse()

g.moveChasingBox([5,5])
g.draw(Gui.CHASINGBOX)
g.getMouse()

g.moveAnimal(Gui.SHARK, [-2, -2])
g.getMouse()

g.undraw(Gui.FISHA)
g.getMouse()