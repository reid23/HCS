#import all math stuff
from math import *

#just pretend these inserted wherever I use them, alright?
#i'm tired and lazy
#i don't want to copy and paste them over and over
tanAng=lambda a0, a1: degrees(atan(a1/a0)) if not a0==0 else degrees(atan(inf))
# for above had to add if to catch division by zero
# works with np datatypes, just returns inf, but 
# not with python builtins
correctAng=lambda a: a if a>=0 else 360+a
norm=lambda a0, a1: sqrt((a0*a0)+(a1*a1))

def testScores():
    #intro line
    print('This function calculates some usefull numbers for you based on your test scores.')

    #get numberof tests
    tests = input('Welcome to the test center!  How many tests are there? ')
    tests = int(tests)
    
    #init vars
    maxScore=0
    minScore=inf
    corriendoAvg=0
    avg=0
    letterGrade=''

    #getting and calc-ing scores/stats
    for i in range(tests):
        #get new input
        inputString='Enter the score for test ' + str(i+1) + ': '

        #set curScore
        curScore=int(input(inputString))

        #check if the current score is a new max or min
        if curScore>maxScore:
            maxScore=curScore
        if curScore<minScore:
            minScore=curScore

        #add current score to running average
        #will divide by number of scores after the loop
        corriendoAvg+=curScore
    
    #calculate actual average
    avg=corriendoAvg/tests

    #use average to get letter grades.  Just lots of ifs.
    if avg<60:
        letterGrade='F'
    elif avg<70:
        letterGrade='D'
    elif avg<80:
        letterGrade='C'
    elif avg<90:
        letterGrade='B'
    elif avg>90:
        letterGrade='A'

    #print out output data
    print('Your high score was', maxScore)
    print('Your low score was', minScore)
    print('Your test average is', avg, '(This is in the', letterGrade,'range).')

def points():
    print('This function calculates some stuff based on two points')
    print() #newline

    #intro banner
    print('Welcome to the equation center!')
    
    #get inputs and assign them to variables
    #it's almost like a poor man's array
    a0,a1 = eval(input('Enter the coordinates of point A as x,y: '))
    b0,b1 = eval(input('Enter the coordinates of point B as x,y: '))


    #catch various corner cases:
    # if the points are the same
    if a1==b1 and a0==b0:
        equation=f'ambiguous, not enough data.'
        slope='ambiguous, not enough data'
    
    #if the x coordinates are equal
    #the line must be vertical
    elif a0==b0:
        slope='undefined'
        equation=f'x={a0}'

    #if the y coordinates are equal
    #the line must be horizontal
    elif a1==b1:
        slope=0
        equation=f'y={a1}'
    
    #else it's a normal line, and the slope 
    #and equation will be standard
    else:
        #calculate slope, dy/dx
        slope=(a1-b1)/(a0-b0)

        #mx+b get b, and round it
        b=round((-1*slope*a0)+a1, 2)

        #round the slope to two places
        slope=round(slope, 2)

        #make the y-intercept show the positive or negative sign
        b = b if b < 0 else '+' + str(b)

        #put everything together into the equation string
        equation = 'y='+str(slope)+'x'+str(b)


    #get angles with atan
    aAng= tanAng(a0,a1) if a0>0 else (tanAng(a0,a1))+180
    bAng= tanAng(b0,b1) if b0>0 else (tanAng(b0,b1))+180

    #fix the angles
    #they both have to be positive for subtracting them to work
    #because python doesn't inherently understand wrapping around
    #at 360 degrees
    #that'd be a cool challenge
    #class degreeAngle extends int
    #can you even do that?
    aAng=correctAng(aAng)
    bAng=correctAng(bAng)

    #find the difference of the angles (the angle between them)
    angle=bAng-aAng

    #correct the angle again because the subtraction
    #might have made some negative angles
    angle=correctAng(angle)

    #round the output
    angle=round(angle, 2)


    #print out all the numbers
    print('***************************')
    print(f'The slope of the line is {slope}.')
    print(f'The distance between the points is {round(norm(a0-b0, a1-b1),2)}') #the part in norm() is just poor mans vector subtraction
    print(f'The equation of the line is {equation}')
    print(f'The angle of rotation about the origin from A to B is {angle} degrees')


def leap():
    #intro print line
    print('this function determines whether any given year is a leap year or not.')

    #get the user's year input, and store it as a number
    year=input('Year: ')
    year=int(year)

    #figure out if it's a leap year:
    #divisible by 400 means automatically yup
    if year%400==0:
        output = 'is'
    #divisible by 100 means no because we already know our year
    #failed the 400 divisibility test
    elif year%100==0:
        output = 'is not'

    #same logic as above, if the program even got here, 
    #we know year%4 is the last criteria
    elif year%4==0:
        output = 'is'
    
    #if it failed all tests
    else:
        output = 'is not' 

    #print output
    print(year, output, 'a leap year.')


#for testing
if __name__ == '__main__':
    print('Leap:')
    leap()
    print('\n')
    print('Points:')
    points()
    print('\n')
    print('Scores:')
    testScores()

