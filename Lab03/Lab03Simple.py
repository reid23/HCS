from math import *

#just pretend these are functions, alright?
#i'm tired and lazy
tanAng=lambda a0, a1: degrees(atan(a1/a0)) if not a0==0 else degrees(atan(inf))
# for above had to add if to catch division by zero
# works with np datatypes, just returns inf, but 
# not with python builtins
correctAng=lambda a: a if a>=0 else 360+a
norm=lambda a0, a1: sqrt((a0*a0)+(a1*a1))

def testScores():
    tests = input('Welcome to the test center!  How many tests are there? ')
    tests = int(tests)
    
    #init vars
    maxScore=0
    minScore=inf
    corriendoAvg=0
    avg=0
    letterGrade=''
    for i in range(tests):
        inputString='Enter the score for test ' + str(i+1) + ': '
        curScore=int(input(inputString))
        if curScore>maxScore:
            maxScore=curScore
        if curScore<minScore:
            minScore=curScore
        corriendoAvg+=curScore
    
    avg=corriendoAvg/tests

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


    print('Your high score was', maxScore)
    print('Your low score was', minScore)
    print('Your test average is', avg, '(This is in the', letterGrade,'range).')

def points():
    print('Welcome to the equation center!')
    a0,a1 = eval(input('Enter the coordinates of point A as x,y: '))
    b0,b1 = eval(input('Enter the coordinates of point B as x,y: '))

    if a1==b1 and a0==b0:
        equation=f'ambiguous, not enough data.'
        slope='ambiguous, not enough data'
    elif a0==b0:
        slope='undefined'
        equation=f'x={a0}'
    elif a1-b1==0:
        slope=0
        equation=f'y={a1}'
    else:
        slope=(a1-b1)/(a0-b0)
        b=round((-1*slope*a0)+a1, 2)
        slope=round(slope, 2)
        b = b if b < 0 else '+' + str(b)
        equation = 'y='+str(slope)+'x'+str(b)


    #get angles with atan
    aAng= tanAng(a0,a1) if a0>0 else (tanAng(a0,a1))+180
    bAng= tanAng(b0,b1) if b0>0 else (tanAng(b0,b1))+180

    aAng=correctAng(aAng)
    bAng=correctAng(bAng)


    angle=bAng-aAng
    angle=round(angle, 2)
    angle=correctAng(angle)

    print('***************************')
    print(f'The slope of the line is {slope}.')
    print(f'The distance between the points is {round(norm(a0-b0, a1-b1),2)}') #the part in norm() is just poor mans vector subtraction
    print(f'The equation of the line is {equation}')
    print(f'The angle of rotation about the origin from A to B is {angle} degrees')


def leap():
    year=input('Year: ')
    year=int(year)
    if year%400==0:
        output = 'is'
    elif year%100==0:
        output = 'is not'
    elif year%4==0:
        output = 'is'
    else:
        output = 'is not' 
    print(year, output, 'a leap year.')

if __name__ == '__main__':
    print('Leap:')
    leap()
    print('\n')
    print('Points:')
    points()
    print('\n')
    print('Scores:')
    testScores()

#%%

