'''
Reid Dye
palindrome checker
'''

#import block
from graphics import *
from Button import Button

#set up window
win=GraphWin('palindrome checker', 600, 220)

instructions=Text(Point(300, 25), 'Please Present Possibly Pithy Palidrome Proposals Promptly:')
instructions.draw(win)

e=Entry(Point(300, 50), 50)
e.draw(win)


quitB=Button(win, Point(150, 150), 100, 30, 'Quit')
tryAgain=Button(win, Point(300, 150), 100, 30, 'Try Again')
test=Button(win, Point(450, 150), 100, 30, 'Test')

quitB.activate()
test.activate()

win.getMouse()

failsInARow=0

while failsInARow<3:
    '''
    pseudocode:
    
    wait for test to be clicked and for there to be text in the box
    deactivate test, activate tryAgain, clear entry box
    then check if its a palindrome and display the result
    if it's not a palindrome then add one to failsInARow

    wait for tryAgain to be clicked
    activate test, deactivate tryAgain, erase message
    
    
    '''
    p=win.getMouse()
    if quitB.clicked(p):
        exit()
    if test.clicked(p):
        inputString=e.getText()
        if inputString=='':
            continue

        inputString=inputString.lower()
        for c in inputString:
            if 97<=ord(c)<=122:
                pass
            else:
                inputString=inputString.replace(c, '?')
        inputString=inputString.replace('?', '')

        isPalindrome = inputString==inputString[::-1]


'''
out of loop pseudocode


'''

