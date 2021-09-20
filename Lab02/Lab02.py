'''
Reid Dye

This module contains 8 functions and 2 classes:
functions:
address(), unitVector(), vertex(), bigBoiVertex(), 
triangle(), triangleSimple(), vertexSimple(), and metric().
classes:
blackBoxFunction
    __init__()
    __call__()
    derivative()
blackBoxFunctionMultiVariable
    __init__()
    __call__()
    gradient()
    partialDeriv()

descriptions of function and arguments are at the top of each thing.

quick note:
I haven't been deleting any comments or print statments.
that said, I've been trying to learn vscode's debugging
tools, so there aren't many print statements.  but if there
are a lot of random comments or prints, this is why.

also, I didn't see a char per line limit this time,
so I haven't been as strict about the short lines.
Most code is under 75, but there are a few longer lines
and a few longer comments.

I may have gone a little overboard on this one ;)
actual functions start on line 547.
'''
#%%
#import block
from numba import njit  # speeeedification
import numpy as np  # linear algebra/vectors/better arrays
from copy import copy #because python's dumb
from math import * #for user inputs so they're not restricted to */+-%etc
from numpy import format_float_positional as ffp #just a long name



#%%
'''
unitVector()

unitVector takes one argument, a 1-D numpy array
of numbers, and returns another numpy array of
the same shape.

The output vector is the same direction as the 
input vector, but has length one.
'''
@njit #abt 3x faster, every bit counts
def unitVector(vec):

    #commenting this out because I don't want to clutter the output.
    #this function gets run a lot.
    #print('This function outputs a unit vector in the')
    #print('same direction as the input vector.')

    #find length of input vector
    magnitude=sqrt(np.sum(vec**2))

    #make sure we won't have any divide by zero errors
    assert not magnitude==0, 'Input Vector is zeros. Unit vector conversion failed.'

    #actually perform the calculation, and return the output.
    return vec/magnitude

#%%
'''
blackBoxFunctionMultiVariable (woah, this isn't java, maybe I should shorten that)

A 'black box' function holder that can be called at any number.  But
that's all it can do: be evaluated.  You can't do anything symbolically.
I guess it's kind of the opposite of sympy.
'''
class blackBoxFunctionMultiVariable:
    '''
    Constructor
    takes in self, the object to be constructed,
    vars, a 1-D list or numpy array of strings
    containing all of the variables used in the
    expression, and expression, a string containing
    a python-readable expression that describes
    the function.

    doesn't return anything, just creates the
    object
    '''
    def __init__(self, vars, expression):
        #commenting this out, like i said earlier
        #print('This function constructs a ')
        #print('blackBoxFunctionMultiVariable object')

        #assign object vars, simple
        self.vars = np.array(vars)
        self.expression = expression


    '''
    __call__ takes in two arguments: the object,
    and the inputs, a 1-D list of inputs for each
    variable.  

    It returns the output of the function given
    those inputs.

    This exists mostly so that you can do f(points)
    just like in math (notation wise)    
    '''
    #! huh the rectification problem seems to be here somewhere
    #!af sdljafls;kdfj adns;v7s;labfds; kl ;;fsdakfjla;djffdsk
    def __call__(self, inputs):  # inputs is list of vals for vars
        #I'm being so inconsistent about how much I trust the user
        #but whatever, this can't hurt, right?
        assert len(self.vars) == len(inputs)

        #make a copy so that we can put the numbers
        #into the expression for eval()
        newExpression = self.expression

        #iterate through the variables
        for i in list(zip(self.vars, inputs)):
            newExpression = newExpression.replace(
                i[0], '('+str(i[1])+')')  # assign vars inside the string
                #* AH HAH!  GOTCHA! FEEL MY WRATH OF PARENTHESES, STUPID BUG!
                #* it was problems when inputting negative numbers 
                #* and order of operations
                #* origional solution: 
                #* newExpression.replace(i[0], i[1])

            # origional origional solution:
            # eval(f'{i[0]}={i[1]}')
            # turns out eval doesn't work with assignment
            # statements or ifs/whiles/etc.

        # I'm too lazy to sanitize inputs so
        # please don't put any malicious code here
        # In other news, my favorite username is:
        # reid'); DROP TABLE users;--
        # thanks bobby tables

        # print(newExpression)
        
        #calculate output and return result
        return eval(newExpression)


    '''
    gradient()
    gradient takes two arguments, self (the object), and
    point, 1-D list of inputs for each variable.  it
    returns a numpy array with the same shape as the
    input.

    gradient computes the gradient of the function object
    it is called on at the point given.
    '''
    #this is instead of backprop
    #because we don't have an actual network in
    #this case to propagate backwards through
    def gradient(self, point):
        #commenting out again
        #print('This function calculates the gradient of')
        #print('the object it is called on at the point given.')

        #confirm numpification (fun word to say)
        #necessary so that .shape works
        #yes, I could have used len, but whatever
        point = np.array(point)

        #create empty output
        #for njit, so that we allocate space
        #then change the values instead of
        #appending values
        #I didn't end up using njit but 
        #I'm too lazy to change this back
        outputVector = np.zeros(point.shape)

        #iterate through vars, take partial with respect
        #to each of them
        #because gradient is just partials for each var
        for counter, var in enumerate(self.vars):
            # can't use append with njit
            # because compiled arrays aren't dynamically allocated
            # but this is the essence of what we're doing:
            # outputVector.append(self.partialDeriv(var, point))
            #? welp actually i gave up on jit because it turns out
            #? that this computation doesn't really take that long
            #? it takes a while if you're doing it millions of times
            #? but it's fine for this

            #take partial, and put it into the output
            outputVector[counter] = self.partialDeriv(var, point)

        #return output
        return outputVector

    '''
    partialDeriv()
    partialDeriv takes three arguments: self, the object
    it's being called on, var, a character, and point, a
    1-D list or numpy array with the same length as self.vars.
    partialDeriv returns one float value.

    partialDeriv computes the partial derivative of self
    at point with respect to var.
    '''
    #! BROKEN!!!! all negatives are rectified somewhere
    #*for future me if i forget the debugging I just did
    #*checkpoints, you know?
    #TODO debug!  Maybe ask
    def partialDeriv(self, var, point):
        #commenting out again
        #print('this function outputs the partial derivative of the')
        #print('function it was called on with respect to var at point.')


        point = list(point)  # confirming list, bc the way I edit it only works with lists
        
        #make tiny number
        #this is dx
        tinyNumber = 0.00000001


        #this figures out the index of the variable we're using
        # [0][0] because of np.where outputs tuple of np array of values of indexes
        index = np.where(self.vars == var)[0][0]

        #print(self.vars[index]) #* verified

        nudgedUpPoint = copy(point) #need to copy because python's memory allocation for lists is dumb

        #this is where we use index, we have to
        #nudge the right var
        #anyway, this creates a copy of the input point with var shifted a little
        #basically for taking deriv
        nudgedUpPoint[index] += tinyNumber
        #print(point)
        #print(nudgedUpPoint)


# where tinyNumber = h
#   lim    f(x+tinyNumber,y) - f(x,y)
#   h->0           tinyNumber

# ^ is partial deriv with respect to x
        #approximate derivative
        #not great, because tinyNumber != 0, but let's pretend it's a real limit

        #anyway here's the actual calculation and output part
        return (self(nudgedUpPoint)-self(point))/(tinyNumber) #TODO test this formula thoroughly



'''
blackBoxFunction
This function was a precursor to the other blackBoxFunction.
I initially built an algorithm to use gradient descent to find the vertex
of a single-variable function.  But this wasn't great as a demo
because you didn't actually need to find a gradient: there were
only two possible directions to move at each step.  But keeping it here
can't hurt, right?

Anyways, it's mostly the same as the other blackBoxFunction except
that it doesn't have a vars or user-made expression variable.  It only works
with polynomials, and thus just stores a list of the coefficients in order
of decreasing degree.  
'''
class blackBoxFunction:
    '''
    Constructor
    the constructor takes two arguments: 
    self, and constants, a list of floats.

    The constants should be the coefficients
    for all of the terms of the polynomial in
    order of decreasing degree.
    '''
    def __init__(self, constants):
        #commenting out again
        #print('This function creates an instance of blackBoxFunction')

        #create a counter for for loop
        #didn't use enumerate() because we
        #need to go from high to low
        #bc the user inputs coefficients from
        #high degree to low degree
        counter = len(constants)-1

        #init output, also an instance var
        #the way this works is like this:
        #say the desired polynomial is
        #x^3 + 3x^2 - 5x + 2
        #then self.expressions would be
        #['(1*x)**3', '3*(x**2)', '5*(x**1)', '2*(x**0)']
        self.expressions = []

        #loop through constants and build the longhand function string
        for i in constants:
            #create a new term
            self.expressions.append(f'{i}*(x**{counter})')
            
            #decrement the degree each time
            counter -= 1


    '''
    __call__
    like the other blackBoxFunction, this is 
    mostly for aesthetic purposes and could
    be replaced by any old object method.

    __call__ takes two arguments, self, and x,
    a float value.

    __call__ returns the output of the function
    given the input x.
    '''
    def __call__(self, x):
        #commenting out again
        #print('this function evaluates self given this input x.')

        #init output var so we can += to it
        output = 0

        #loop through each section of expressions
        for i in self.expressions:

            #add that part of the expression to the output sum
            output += eval(i)

        #output the output
        return output

    '''
    A note about how this class works:
    I'm creating a string and eval()ing it
    because that way the object can work 
    with an arbitrary number of terms in 
    the polynomial.
    '''
    
    
    '''
    derivative()
    Derivative takes two arguments: self, 
    an instance of blackBoxFunction, 
    and x, a float.

    derivative returns the derivative of
    self at x.
    '''
    def derivative(self, x):
        #commenting out again
        #print('this function returns the derivative of self at x.')

        #init tinyNumber, our dx
        tinyNumber = 0.0000000001

        #compute approx derivative and return output
        return (self(x+tinyNumber)-self(x))/tinyNumber

#%%

'''
bigBoiVertex() (yes, I'm going crazy)

this takes no arguments and returns nothing.
it uses python's builtin input() method to
gather user data defining a function, then
it uses gradient descent to find a minimum
or maximum.  It tries to find the global
min/max, but it's not great at that, for 
the simple reason that gradient descent
isn't a great algorithm for finding global
mins/maxes, at least for simple functions.
'''
#why did i call it this
#debugging is making me go insane
def bigBoiVertex():
    #commenting this out again
    #print(u'This function uses gradient descent to find a minimum/maximum of an n-variable function that the user inputs.  n \u2208 \u2124')

    #print some info about inputs
    print('some info:')
    print('Only one output allowed.  All math modules are allowed.  \nIf you want an accurate value, make sure a max/min value actually exists.')

    #get input
    expression=input('Input the expression defining your \nfunction in a python-readable way: ')
    variables=input('Input all variables used in \nyour function separated by commas: ').split(',')
    minimize=True if input('Do you want to minimize or maximize the function?  (min/max): ')=='min' else False
    guess=input('Guess, in tuple format (optional, defaults to random): ')  #I'm going with tuple because... uh... parentheses are used in math for coordinates ;)
    
    #a random thing that will be useful later
    numVars=len(variables)

    #add default guess functionality
    guess=np.array(eval(guess)) if not guess=='' else np.random.rand(numVars)

    #create function object
    f=blackBoxFunctionMultiVariable(variables, expression)
    
    #set initial learning rate
    learningRate=1000

    #iteratively find min/max with gradient descent
    while learningRate>0.0001: #doing it based on lr and not gradient vec len to reduce chance of finding local 'trap' valleys
        #calculate gradient at current guess
        grad = f.gradient(guess)
        #print(guess, grad)
        
        
        #I'm too lazy to implement momentum so
        #this will have to do

        #prevent division by zero in a bad way
        #also convert the gradient vector to a unit vector
        try:
            grad=unitVector(grad)
        except AssertionError:
            grad=unitVector(np.random.rand(numVars))
        #now that the vector is length 1, to get a vector of arbitrary length, we just multiply the components by the desired length.
        
        #flip the gradient if we're descending
        if minimize:
            grad=np.negative(grad)
        

        #get new guess by adding a distance of learningRate 
        #to our current guess
        guess=(grad*learningRate)+guess

        #decrease the learning rate by 5 percent
        learningRate*=0.95


    #get the output values from guess and make them pretty
    #idk why but if these lines are put directly into the fstrings it breaks
    outputInput = [ffp(i, 3, trim='k') for i in guess] #must use for loop bc ffp only works on scalars
    outputOutput = ffp(f(guess), 3, trim='k')

    #print the output
    print(
        f'The global minimum/maximum is approximately ({outputInput}, {outputOutput})')

#%%

'''
vertex()

vertex takes no arguments and returns nothing.

vertex uses python's builtin input() function to
gather coefficient data from the user about a
polynomial, then uses a simple gradient descent-like
algorithm to find the global minimum or maximum, depending
on the leading coefficient.

vertex then prints out the result.
'''
def vertex():
    #commenting out again
    #print('this function uses input() to find the')
    #print("vertex of the user's function using gradient descent.")


    # get function parameters with input()
    print('Only functions with even degrees are allowed.')
    params = [float(x) for x in input(
        'Enter all coefficients, in order from highest to lowest order, separated by commas:').split(',')]

    #use leading coefficient to figure out minimization or maximization
    #not great because if the user inputs extra coefficients at the front
    #which are zeroes, it doesn't know that.  But I couldn't figure out a
    #way for this to work with an arbitrary number of leading 0s.
    #so this will work for now
    if params[0] > 0:
        minimize = True
    else:
        minimize = False

    #create function object
    func = blackBoxFunction(params)

    # oh yeah it's gradient descent time
    #set starting learning rate
    learningRate = 1000  # can't hurt to start high

    #set starting guess
    guess = 0  # start at 0

    #iterate through descending the function
    while learningRate > 0.0001:  # around 315 iters
        
        #evaluate the function at current guess
        atGuess = func(guess)

        ###*Calculate which way to step
        # this fake derivative strategy works because this is only 2d.  there are only two possible directions, not infinite.
        # little steps to get a vauge idea of the derivative
        aboveGuess = func(guess+(learningRate/10))
        # little steps to get a vauge idea of the derivative
        belowGuess = func(guess-(learningRate/10))
        if minimize == True:
            if atGuess < aboveGuess and atGuess < belowGuess:  # if guess is the best
                learningRate *= 0.95
                continue
            elif aboveGuess < atGuess and aboveGuess < belowGuess:
                guess += learningRate
                learningRate *= 0.95
                continue
            elif belowGuess < atGuess and belowGuess < aboveGuess:
                guess -= learningRate
                learningRate *= 0.95
                continue
        else:
            if atGuess > aboveGuess and atGuess > belowGuess:  # if guess is the best
                learningRate *= 0.95
                continue
            elif aboveGuess > atGuess and aboveGuess > belowGuess:
                guess += learningRate
                learningRate *= 0.95
                continue
            elif belowGuess > atGuess and belowGuess > aboveGuess:
                guess -= learningRate
                learningRate *= 0.95
                continue
        #whew that was a lot of ifs
        #basically what that did was find which direction, left or right, to
        #move the guess in order to better minimize/maximize the function.  
    
    #get output values from guess and make them look pretty
    #idk why but if I put these inside the fstring it breaks
    #oh well I don't need to understand it for it to work lol
    outputInput=ffp(guess, 6, trim='k')
    outputOutput=ffp(guess, 6, trim='k')

    #print the result
    print(
        f'The global minimum/maximum is approximately ({outputInput}, {outputOutput})')

#%%
'''
address()

address take no arguments and returns nothing.
It uses python's builtin input() function to
gather data about the user, then displays that
information in a standard format.
'''
def address():
    #get all the inputs
    street = input('Enter your street address: ')
    city = input('Enter your city: ')
    state = input('Enter your state abbreviation: ')
    zipCode = input('Enter your zip code: ')
    birthMonth = input('Enter your birth month: ')
    birthDay = input('Enter your birth day: ')
    birthYear = input('Enter your birth year: ')
    areaCode = input('Enter your area code: ')
    phoneNumber = input('Enter your phone number: ')
    #print out the output
    print(f'''
**************************************************
Your Address:
{street}
{city}, {state}   {zipCode}
Your Birthday: {birthMonth}-{birthDay}-{birthYear}
Your Phone Number: ({areaCode}) {phoneNumber}
    ''')

#%%
'''
triangle()
triangle takes one argument, n, an integer.
it then prints out the first n triangular numbers plus zero.
'''

def triangle(n):
    print('This function prints out the first n triangular numbers, including zero.')

    #must use np to add one to eliminate starting at zero easily
    print(str([0]+[sum(np.array(range(i))+1) for i in np.array(range(n))+1])[1:-1])
    # idk why i just did that
    # i kinda hate things that show 'clean' code as everything crammed into one line
    # it looks nice but it's soooo hard to read
    # haha good thing I don't have to read it anymore now that it works
    # it also does the exact same thing as triangleSimple()


#%%
'''
traingleSimple()
triangleSimple does the same thing as triangle
in practically the same way.  it's just easier
to read

like most things, the first thing that's written
is most often the worst.  That's what triangle() is.

This is much better.
'''
def triangleSimple(n):
    print('This function prints out the first n triangular numbers, including zero.')
    #main loop
    #bc we need to show all of the triangular numbers
    #up to n, not just n
    #n+1 bc range starts at 0
    for i in range(n+1):
        output=0 #reset output

        #loop through natural numbers and sum them
        #n+1 for the same reason
        for j in range(i+1):

            #add the current number to the output
            output += j
            for k in range(0):
                #ummmm
                #so i can get ijk
                #actually screw quaternions
                #almost as bad as nested for loops
                pass
        #print out this iteration's triangular number
        print(output, end=', ')
    
    #new line, so the next thing printed doesn't 
    #come right after the nubmers
    print()
    #ahhhh so much less claustrophobic
    #than traingle()
    #and still pretty compact
    #only 5 lines of actual code

#%%    
def vertexSimple():
    print('This function finds the coefficients of a quadratic function.')

    #print instructions
    print('Please enter the coefficients of f(x)=ax^2+bx+c:')

    #get inputs and make them into numbers
    a=float(input('Coefficient A: '))
    b=float(input('Coefficient B: '))
    c=float(input('Coefficient C: '))

    #do the calculations, this is just math
    x= (-1*(b/(2*a)))
    y= (a*(x**2)) + (b*x) + c

    #print output
    print('***************************')
    print('Your vertex is at (', end='')
    print(x+1-1, end='') #plus and minus one eliminates negative zeros
    print(', ', end='')
    print(y+1-1, end='')
    print(').')

#%%
'''
metric()
metric takes no arguments and returns nothing.

metric takes three user inputted values and converts them
metric units.  The usefullness of this 
calculator is... questionable.

In other news, I discovered wikipedia truly does
have a page for everything.  Here's a list of humorous units:

https://en.wikipedia.org/wiki/List_of_humorous_units_of_measurement
(ctrl-click!)  That's a fun read.
'''

def metric():
    #i'm assuming this is the intro print line
    print('Welcome to the Metric Conversion Center.')

    #get inputs 
    time=eval(input('Please input a length in yards: '))
    speed=eval(input('Please input a speed in furlongs per fortnight: '))
    volume=eval(input('Please input a volume in barn-megaparsecs: '))

    #print outputs
    print('*******************************')
    print('Your length is', time*0.9144, 'meters.')
    print('Your speed is', speed*0.1663, 'yoctometers per zeptosecond.')
    print('Your volume is', volume*3.0856, 'milliliters')
#%%

# for testing
# triangle()
# vertex()
# address()
# bigBoiVertex()
#   LOOK HERE BC IT'S REALLY HARD TO JUST THINK OF A MULTIVARIABLE TEST FUNCTION
#   a good test function: x³ - 2x² + y³ - 2 y² + x⁶ + y⁶
#   aka (x**3)-(2*(x**2))+(y**3)-(2*(y**2))+(x**6)+(y**6)
#   Graph: https://www.geogebra.org/3d/nkbdfzfq
#   (minimize the function)

# triangleSimple()
# vertexSimple()

if __name__ == '__main__':
    print('Triangle, from zero to 10:')
    for i in range(11):
        triangle(i)
    print('triangleSimple, from zero to 10:')
    for i in range(11):
        triangleSimple(i)
    print('Address:')
    address()
    print('Metric:')
    metric()
    print('vertexSimple:')
    vertexSimple()
    print('gradient descent single variable vertex:')
    vertex()
    print('gradient descent multivariate vertex:')
    bigBoiVertex()
    
# %%