'''
Author: Reid Dye

This file contains the classwork for 8/30.
'''
#%%
def greeting(name):
    print(f'Hi {name}!  How are you today?')

def even(n):
    output = [2*(i) for i in range(n)] #change (i) to (i+1) to start at 2 instead of 0
    print(str(output)[1:-1]) #convert to str, then remove the brackets (first and last char)

def inputGreeting():
    name=input("What's your name?")
    print(f'Hi {name}!  How are you today?')

def inputEven():
    n=int(input('How many evens should I print? (int)')) #need into to convert string to number
    output = [2*(i) for i in range(n)] #change (i) to (i+1) to start at 2 instead of 0
    print(str(output)[1:-1]) #convert to str, then remove the brackets (first and last char)
# %%
