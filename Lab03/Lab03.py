#imports
import numpy as np
from numpy import format_float_positional as ffp
from numpy.linalg import norm
import warnings
from math import *
import random


#utils for points()
#description in readme
tanAng=lambda a: degrees(atan(a[1]/a[0]))
correctAng=lambda a: a if a>=0 else 360+a


def points(*points):
    #intro line
    print('This function calculates a bunch of stuff about the two points you input.')

    with warnings.catch_warnings(): #warnings?  what warnings?
        warnings.simplefilter("ignore") #if it doesn't stop the program, it doesn't matter lol

        print('Welcome to the equation center!')

        #check if points were given as args
        if not not points:
            a=np.array(points[0])
            b=np.array(points[1])

            #like when you dial into the zoom call, it
            #automatically puts in the meeting id
            print(f'Enter the coordinates of point A as x,y: {str(a)[1:-1]}')
            print(f'Enter the coordinates of point B as x,y: {str(b)[1:-1]}')
        else:
            #get input if needed
            a = np.array(input('Enter the coordinates of point A as x,y: ').split(','))
            b = np.array(input('Enter the coordinates of point B as x,y: ').split(','))

        #if the user forgets to give args
        #use random inputs to screw with them instead of throwing a handy error
        if a==np.array(['']) or b==np.array(['']):
            a=[random.uniform(-1,1) for _ in [0,0]] #heyyy it's a little shorter
            b=[random.uniform(-1,1), random.uniform(-1,1)]
            print(f'Enter the coordinates of point A as x,y: {str(a)[1:-1]}')
            print(f'Enter the coordinates of point B as x,y: {str(b)[1:-1]}')


        #convert to floats
        a, b = a.astype(np.float), b.astype('float')

        #calculate slope
        #we don't need to worry abt zeroDivisionError bc numpy is smrt
        #when doing 1/0, numpy takes the limit as the denominator goes to 0
        #instead of actually zero
        #so it just raises a warning and returns inf, which is perfect
        slope=(a[1]-b[1])/(a[0]-b[0])

        #if slope is undefined
        if abs(slope)==inf:
            slope='undefined'
            equation=f'x={a[0]}'

        #if line is horiz
        elif slope==0:
            equation=f'y={a[1]}'

        # if points are the same
        #have to do sum/2 to avoid 'The truth value of an array with more than one element is ambiguous.'
        elif sum(a==b)/2:
            equation=f'ambiguous, not enough data.'
            slope='ambiguous, not enough data'
        
        #if the line isn't normal
        #ie if the user isn't a hypothetical cs teacher trying to find corner cases
        else:
            c=ffp((-1*slope*a[0])+a[1], sign=True, precision=2, trim='k')
            slope=ffp(slope, precision=2, trim='k')
            equation = f'y={slope}x{c}'
        
        #first try, didn't work with angles in the 3rd and 4th quadrants
        # angle=np.dot(a,b)
        # lenA=norm(a)
        # lenB=norm(b)

        # angle=degrees(acos(angle/(lenA*lenB)))

        #get angles with atan
        #don't have to check for dividing by zero in tanAng
        #because using np datatypes dividing by 
        #zero just returns inf (the limit)
        aAng= tanAng(a) if a[0]>0 else (tanAng(a))+180
        bAng= tanAng(b) if b[0]>0 else (tanAng(b))+180

        #get rid of negative angles
        aAng=correctAng(aAng)
        bAng=correctAng(bAng)

        #calc angle and round
        angle=bAng-aAng
        angle=ffp(angle, precision=2, trim='k')
        #np.format_float_positional is just round() on steroids that returns a string.
        #it's seriously great
        #there's so many options!

        #print output stuffs
        print('***************************')
        print(f'The slope of the line is {slope}')
        print(f'The distance between the points is {ffp(norm(a-b), precision=2)}')
        print(f'The equation of the line is {equation}')
        print(f'The angle of rotation about the origin from A to B is {angle} degrees')

def testScores(*scores):
    #intro line
    print('This function calculates a bunch of stats about your test scores')
    #define all the letters
    #clunky but more line-efficient than a bunch of ifs
    scoreLetters = {0:'F', 1:'F', 2:'F', 3:'F', 4:'F', 5:'F', 6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}

    #check if scores were given as args
    if not not scores:
        scores=np.array(scores)  #tuples.  Nasty things.  Won't have 'em in the house.
        print('Welcome to the test center! How many tests are there?', len(scores))
    
    else:
        #get input if needed
        tests = input('Welcome to the test center!  How many tests are there? ')
        tests = int(tests)

        #make sure it won't break
        assert tests > 0, 'Minimum input is 1 score.'

        #init scores var
        #appending is hard to type and computationally slow
        scores = np.zeros(tests)

        #get input and put it in scores
        for counter, _ in enumerate(scores):
            score = int(input(f'Enter the score for test {counter + 1}: '))
            assert score >= 0, 'Negative scores are not allowed.'
            scores[counter]=score
    
    #print outputs
    print('Your high score was', scores[np.argmax(scores)])
    print('Your low score was', scores[np.argmin(scores)])
    print('Your test average is', np.average(scores), '(This is in the', scoreLetters[np.average(scores)//10],'range).')
    print('The standard deviation of your scores is', np.std(scores))  #I find the naming of this function somewhat unfortunate


def leap(*year):
    # using *year so that it's optional

    # I know that we're only supposed 
    # to accept positive integers, 
    # but i figured positive integers 
    # represented as strings were fine 
    # because that's how it would 
    # be with input()

    # not not just sees if something is there
    # ie if the input has already been given (as arg)
    # there's def better ways to do this but
    # not not is just amusing
    if not not not not not not not not not not not year:
        manual=True #flag for later to show year was input with input()
        year=input('Year: ')
        year=np.array([year])
    else:
        manual=False
        year=np.array(year)
    print(year)
    panic=False
    for counter, i in enumerate(year):
        try:
            year[counter]=float(year[counter])

            #quick fix bc idk what's going on
            #but year seems to be trying to keep the origional
            #datatype after the assignment above?  idk.
            #anyway it works now so *shrug*
            year=np.array(year, dtype=float)
        except ValueError:
            panic=True
    
    #all of the nasties above (and the line below)
    #are just so that I can have a custom error message
    #i had to catch all of the float() errors an use panic
    #and this is also why I'm using year%1 
    #instead of type(year)=int
    
    #make sure it works if multiple values are inputted
    for i in year:
        if panic==True:
            break
        if not i%1==0:
            panic==True
        if not i>=0:
            panic=True

    #raise error if input is wrong
    assert panic==False, f'Invalid input, expected a positive integer but received {year}'

    #actually figure out if it's a leap year
    output=np.zeros(year.shape)
    for counter, i in enumerate(year):
        if i%400==0:
            output[counter] = True
        elif i%100==0:
            output[counter] = False
        elif i%4==0:
            output[counter] = True
        else:
            output[counter] = False

    #print/return output
    if manual:
        print(f"{int(year[0])} {'is' if output[0] else 'is not'} a leap year.")
    else:
        return output
