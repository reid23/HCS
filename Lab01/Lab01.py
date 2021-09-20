'''
Author: Reid Dye

This module contains the answers for Lab01.
airport(), madLibs(), and sumOfEven().

It also contains loading() and associated functions,
which display a loading animation while the
program waits for Very Super Important 
Essential Calculations to be finished during madLibs().

Finally, it contains sumOfEvenSimple() and madLibsSimple()
which are bare-bones implementations of the required specs
that use no concepts outside of those already covered in class.

For testing, if you run this file, it executes all functions
except madLibsSimple because that is functionally identical 
to madLibs.  When imported as a module, this does not occur.

Actual assignment code starts on line 85.
'''

#imports
from time import sleep #for delays
import sys # for loading animation
from threading import Thread #for running loading animation concurrently with other stuff
import numpy as np  #for Very Super Important Essential Calculations


#declaration of done, to use later
done=False

# This function defines the loading animation.  
# It stops when finish() is called.
# Thanks Saahil for the idea to do this
# Arguments:
#   cycle: a 1-d list of strings of equal length.
#       These are the frames of the animation.
#   interval: a value, the time between frames of
#       the animation.
def loading(cycle, interval):

    # so that it can be stopped from another thread, 
    # it references a 'flag' variable
    global done 
    done=False
    
    counter=0

    #loop through and show the characters in cycle
    while done==False:

        #ensure the index is always one of the characters
        counter=counter%len(cycle)  
        char=cycle[counter]

        #\r is basically 'go back to start of the line'
        sys.stdout.write('\rloading ' + char) 
        sys.stdout.flush()
        sleep(interval)
        counter += 1
    sys.stdout.write('\nDone')


# here's some fun animations. 
# Source: 
# https://stackoverflow.com/questions/2685435/cooler-ascii-spinners
# (the answer by mpen)
# Copied the lists from here: 
# https://jsbin.com/tofehujixe/1/edit?js,output
# The ones listed below are my favorites:
block=['▁','▃','▄','▅','▆','▇','█','▇','▆','▅','▄','▃']
blockInterval=0.1
bouncyBar=['[=       ]','[==      ]','[===     ]',
    '[ ===    ]','[  ===   ]','[   ===  ]','[    === ]',
    '[     ===]','[      ==]','[       =]','[        ]',]
bouncyBarInterval=0.17
spinnyBar=['|','/','-','\\']
spinBarInterval=0.2
spinnyBox=["◰","◳","◲","◱"]
boxInterval=0.17
clocks=["🕛 ","🕐 ","🕑 ","🕒 ","🕓 ","🕔 ","🕕 ","🕖 ","🕗 ","🕘 ","🕙 ","🕚 "] 
clocksInterval=0.1 #coldplay, anyone?
moon=["🌑 ","🌒 ","🌓 ","🌔 ","🌕 ","🌖 ","🌗 ","🌘 "]
moonInterval=0.1

#must be threaded so it can play animation concurrently with another process
animationThread=Thread(target=loading, args=[moon,moonInterval]) 

def startAnimation():  #this function starts the animation.  super simple
    animationThread.start()

def finish():
    global done
    done=True
    sleep(0.3) #sleep a little longer than the sleep in the animation to
               #make sure that can finish before the story is printed out


#! here's the start of the actual required functions.

#* AIRPORT
# This function takes no arguments and returns nothing.
# when called, it prints out the airport code for 
# San Carlos Airport using 7x7 grids of asterisks 
# for each letter.
def airport():
    print('This function displays an ascii representation of SQL.')

    #print out the thing
    #idk what else to comment, it's literally that simple
    print("""
    * * *          * * *        *          
  *              *       *      *          
  *            *           *    *          
    * * *      *           *    *          
          *    *        *  *    *          
          *      *       *      *          
    * * *          * * *   *    * * * * *  
  (it's pronounced sequel)""") 
  #speaking of pronunciation, is it twopul or tupple?
  #Don't say toopuleeeee


#* MADLIBS
# this function takes no arguments and returns nothing.
# When called, it uses the inbuilt input() function to get user input and 
# create a madlibs story. This is then printed.
# I copied the story from the internet, I hope that's not plagiarism. 
# it's not the graded part of the assignment, right?
def madLibs():
    print('This function asks for input, then displays a madlibs story.')

    #Get inputs, and store them in answers:
    answers = {} #dict because then there aren't a million variables.  Also it adds length so my mega-line can be longer ;)
    answers['adj1']=input('Adjective:')
    answers['adj2']=input('Adjective:')
    answers['bird']=input('A type of bird: ')  #* TWEEEEET
    answers['room']=input('A room in your house: ')
    answers['verb1']=input('A verb (past tense): ')
    answers['verb2']=input('Verb: ')
    answers['name']=input('A name: ')
    answers['noun1']=input('Noun: ')
    answers['liquid']=input('A liquid: ')
    answers['verb3']=input('Verb that ends in -ing: ')
    answers['verb5']=input('Verb that ends in -ing (again): ')
    answers['bodyPart']=input('Body part: ')
    answers['noun2']=input('Plural noun: ')
    answers['noun3']=input('noun: ')
    answers['verb4']=input('another past tense verb: ')
    answers['place']=input('a place: ')

    #haha want to see a mega line?
    #it does work, try it!
    #696 chars, big brain time
    #what a nightmare
    #answers['adj1'], answers['adj2'], answers['bird'], answers['room'], answers['verb1'], answers['verb2'], answers['name'], answers['noun1'], answers['liquid'], answers['verb3'], answers['verb5'], answers['bodyPart'], answers['noun2'], answers['noun3'], answers['verb4'], answers['place'] = input('Adjective:'), input('Adjective:'), input('A type of bird: '), input('A room in your house: '), input('A verb (past tense): '), input('Verb: '), input('A name: '), input('Noun: '), input('A liquid: '), input('Verb that ends in -ing: '), input('Verb that ends in -ing (again): '), input('Body part: '), input('Plural noun: '), input('noun: '), input('another past tense verb: '), input('a place: ')

    startAnimation()#make loading animation

    #it's loading, so we have be computing something lol.
    #This computation is vitally important to the success of this function
    #So essential, in fact, that it is almost the whole purpose of the
    #function
#yes, I could have used a sleep, but how fun is that?
    for i in range(50000): #should take 5-8s
        x=np.random.rand(100,100)
        y=np.random.rand(100,100)
        z=np.matmul(x,y)
    finish()
    print('') #new line

    #display the story, with all the goodies inside
    print(f'''
    It was a {answers['adj1']}, cold November day.  
    I woke up to the {answers['adj2']} smell of {answers['bird']} roasting
    in the {answers['room']} downstairs. I {answers['verb1']} 
    down the stairs to see if I could help {answers['verb2']} the dinner.
    My mom said, “See if {answers['name']} needs a fresh 
    {answers['noun1']}.” So I carried a tray of glasses full of 
    {answers['liquid']} into the {answers['verb3']} room.  
    When I got there, I couldn’t believe my {answers['bodyPart']}!
    There were {answers['noun2']} {answers['verb5']} on the 
    {answers['noun3']}! I was so surprised that I {answers['verb1']} the 
    {answers['liquid']} at {answers['name']}. I couldn't handle 
    the unexpectedness of what I saw, so I {answers['verb4']} and 
    ran all the way to {answers['place']}.
    ''')

#* SUM OF EVEN
# This function takes three arguments (n, printed, returned) and returns 
# either a string or nothing, depending on the arguments.
# When called, the function prints, returns, or just calculates
# the sum of the first n even numbers.
# if the input is negative, it sums the first |n| negative numbers.
# printed is whether it prints the output, returned is whether 
# it returns the output.
# Arguments: 
#   n: an integer, the number of evens.
#   printed: a bool, defining whether the output should be printed.
#       defaults to true. 
#   returned: a bool, defining whether the output should be 
#       returned.  Defaults to true
def sumOfEven(n, printed=True, returned=False):
    print('This function calculates the sum of the first n even numbers.')

    # init a variable where we will store the running sum
    output = 0

    # try except to catch invalid input
    try:
        #*expanded version, because it's hard to comment the condensed version
        '''
        # loop x times
        for i in range(n):
            # j defines the j'th even number, the number that 
            # we're adding to sum this iteration.
            # we need to add one because the list that this 
            # loop is iterating through (that range returns)
            # starts at zero, not one, and our even numbers start
            # at 2, not zero.
            j = i+1
            # multiply by 2 (to convert even-number-index to 
            # actual even number), Then add to sum
            output += j*2
        '''

        #* and here's the condensed version:
        # output = sum([2*(i+1) for i in range(n)])

        # The only difference between this and the previous loop
        # is that this places all values in a list first, then
        # sums that loop instead of taking a running sum.

        # and here's the version that accounts for negative inputs
        # not clean and neat, but it works
        if n>=0:
            output = sum([2*(i+1) for i in range(n)])
        else:
            # gets abs(n) output, then negates it because 
            # that'll be the same as the abs(n) negative even numbers
            output = -1*sum([2*(i+1) for i in range(-1*n)])


    except TypeError:  #if theres text or a float inputted, range() throws a typeError
        #print out the error
        if printed==True:
            print(
                (f'The input {n} produced an invalid '
                'result. Only integers are allowed.'))
        if returned==True:
            return (f'The input {n} produced an invalid '
                    'result. Only integers are allowed.')
        #skip printing the last line because it makes no sense in this case
        return
    # print output in human legible format
    if printed==True:
        print(f'The sum of the first {n} even numbers is {output}.')
    if returned==True:
        return f'The sum of the first {n} even numbers is {output}.'

# I'm worried about the line between additional creativity and using 
# concepts not already covered in the class, so here are simple 
# versions of the functions.
# Arguments:
#   n: the number of evens to sum
def sumOfEvenSimple(n):
    print('This function calculates the sum of the first n even numbers.')
    output=0
    evenNum=2
    for i in range(n):
        output=output+evenNum
        evenNum=evenNum+2
    print('The sum of the first', n, 'even numbers is', output, '.')

def madLibsSimple():
    print('This function asks for input, then displays a madlibs story.')

    #Get inputs, and store them as variables:
    adj1=input('Adjective:')
    adj2=input('Adjective:')
    bird=input('A type of bird: ')  #* TWEEEEET
    room=input('A room in your house: ')
    verb1=input('A verb (past tense): ')
    verb2=input('Verb: ')
    name=input('A name: ')
    noun1=input('Noun: ')
    liquid=input('A liquid: ')
    verb3=input('Verb that ends in -ing: ')
    verb5=input('Verb that ends in -ing (again): ')
    bodyPart=input('Body part: ')
    noun2=input('Plural noun: ')
    noun3=input('noun: ')
    verb4=input('another past tense verb: ')
    place=input('a place: ')
    

    #display the story, with all the goodies inside
    print('It was a ' + str(adj1) + ', cold November day.')  
    print('I woke up to the ' + str(adj2) + ' smell of ' + str(bird) + ' roasting ')
    print('in the ' + str(room) + ' downstairs. I ' + str(verb1) + ' ')
    print('down the stairs to see if I could help ' + str(verb2) + ' the dinner.  ')
    print('My mom said, “See if ' + str(name) + ' needs a fresh ' + str(noun1) + '.”  ')
    print('So I carried a tray of glasses full of ' + str(liquid) + ' into ')
    print('the ' + str(verb3) + ' room.  When I got there, I couldn’t believe ')
    print('my ' + str(bodyPart) + '!  There were ' + str(noun2) + ' ' + str(verb5) + ' on the ' + str(noun3) + '!')
    print('I was so surprised that I ' + str(verb1) + ' the ' + str(liquid) + ' at ' + str(name) + '.')
    print("I couldn't handle the unexpectedness of what I saw, so I ")
    print('' + str(verb4) + ' and ran all the way to ' + str(place) + '.')

#for testing purposes
#if the file is run, these demos will also run
if __name__ == '__main__':  #so that if its imported as a module it will work as expected.
    print('testing all functions')
    print('Airport:')
    airport()
    print('sumOfEven:')
    print(f'sumOfEven(-2): {sumOfEven(-2, False, True)}')
    print(f'sumOfEven(-1): {sumOfEven(-1, False, True)}')
    print(f'sumOfEven(0): {sumOfEven(0, False, True)}')
    print(f'sumOfEven(1): {sumOfEven(1, False, True)}')
    print(f'sumOfEven(2): {sumOfEven(2, False, True)}')
    print(f'sumOfEven(3.657): {sumOfEven(3.657, False, True)}')
    # the simple ones have to be printed on another line because I can't 
    # add return vs print functionality
    print(f'sumOfEvenSimple(0): ')
    print(sumOfEvenSimple(0))
    print(f'sumOfEvenSimple(1): ')
    print(sumOfEvenSimple(1))
    print(f'sumOfEvenSimple(2): ')
    print(sumOfEvenSimple(2))
    print(f'sumOfEvenSimple(3): ')
    print(sumOfEvenSimple(3))
    print(f'sumOfEvenSimple(4): ')
    print(sumOfEvenSimple(4))
    print('madlibs:')
    madLibs()  #last because takes a while