from SharkGUI import Gui
from Shark import Shark
from Fish import Fish
from Button import Button
import os

print(os.listdir())

s=Shark()
a=Fish(5,5)
b=Fish(6,6)
c=Fish(7,8)

start=Button(3, -1, 0.2, 0.5, 'start')
move=Button(5, -1, 0.2, 0.5, 'move')
quit=Button(7, -1, 0.2, 0.5, 'quit')
msgbox=Button(8, -1, 0.2, 1, '[empty message]')

g=Gui(s, a, b, c, start, quit, move, None, None, None, msgbox, drawButtons=True, drawEntries=True, drawMsgBox=True)
g.drawGrid()
g.getMouse()

g.moveChasingBox([5,5])
g.draw(Gui.CHASINGBOX)
g.getMouse()

g.moveAnimal(Gui.SHARK, [-2, -2])
g.getMouse()

g.undraw(Gui.FISHA)
g.getMouse()