'''
Author: Reid Dye

a palindrome checker
'''

#import block
from graphics import *
from Button import Button

###* create all objects 
#make window
win=GraphWin('palindrome checker', 600, 220)

#instructions for above the text box
instructions=Text(Point(300, 25), 'Please Present Possibly Pithy Palidrome Proposals Promptly:')
instructions.draw(win)

#text box
e=Entry(Point(300, 50), 50)
e.draw(win)

#output/result message
result=Text(Point(300, 90), '_')

#the three buttons
quitB=Button(win, Point(150, 150), 100, 30, 'Quit')
tryAgain=Button(win, Point(300, 150), 100, 30, 'Try Again')
test=Button(win, Point(450, 150), 100, 30, 'Test')

#activating them (except tryAgain because it shouldnt be activated)
quitB.activate()
test.activate()

#init a tracker for how many times the user has failed in a row
failsInARow=0

###* Main loop
while True:
    '''
    pseudocode:
    
    wait for test to be clicked and for there to be text in the box
    deactivate test, activate tryAgain, clear entry box
    then check if its a palindrome and display the result
    if it's not a palindrome then add one to failsInARow

    wait for tryAgain to be clicked
    activate test, deactivate tryAgain, erase message
    '''
    #get first mouse click
    p=win.getMouse()
    if quitB.clicked(p): #quit functionality
        exit()
    elif test.clicked(p):
        inputString=e.getText()
        if inputString=='':
            continue #we can do this instead of a smaller loop because there's nothing outside of this main if statement (nothing that *must* run every loop)
        inputString=inputString.lower() #get rid of captials

        #iterate through the input and replace anything that's not a-z with a ?
        for c in inputString:
            if 97<=ord(c)<=122: #97 is 'a' and 122 is 'z'
                pass
            else:
                # we must do this instead of just removing the char because the for loop works based on the 
                # index in the string so if we take out characters then it might skip some while looping
                inputString=inputString.replace(c, '?')
            
        #remove all the ?s
        inputString=inputString.replace('?', '')

        isPalindrome = inputString==inputString[::-1] #actually check if it's a palendrome

        #set the result text and show the result
        result.setText(f"{e.getText()} {'is' if isPalindrome else 'is not'} a palindrome")
        result.draw(win)

        #add to fails counter if needed
        if isPalindrome:
            failsInARow=0
        else:
            failsInARow+=1

        #set button activation
        #trying the property() function, seems pretty cool
        #flexibility of setting instance vars, with more input validation!
        #* test.act, tryAgain.act = False, True
        #unfortunately that's a little harder to read
        #so I'll just stick with this
        test.deactivate()
        tryAgain.activate()

        #if the user's bad
        if failsInARow==3:
            break

        #wait for the try again button (or quit button) to be clicked
        while True:
            p=win.getMouse()
            if quitB.clicked(p):
                exit()
            elif tryAgain.clicked(p):
                break

        #reset stuff
        test.activate()
        tryAgain.deactivate()
        result.undraw()
        e.setText('')


#if the user failed three in a row, then do all of this

#failed message
Text(Point(300, 115), 'You have failed 3 attempts in a row.  Please quit.').draw(win)

#deactivate everything except quit
tryAgain.deactivate()
test.deactivate()

#wait for quit button to be clicked
while True:
    p=win.getMouse()
    if quitB.clicked(p):
        exit()

