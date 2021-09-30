'''
Reid Dye
Test 01
HCS-A
23 September 2021
'''
#%%
from math import *

#%%
def prob19():
    x=eval(input('Enter a number: '))
    if x % 2 == 0:
        if x % 4 == 0:
            y='a'
        elif x % 4 != 0:
            y='b'
    elif x % 2 != 0:
        y='c'
    
    print(y)


#%%
def prob20():
    #import numpy as np
    #output=np.array([i for i in range(101, 1000, 2)])
    #output=sum(output**2)/len(output)
    #print(output)
    output=0
    for i in range(101, 1000, 2):
        output += i**2
    
    print(output/450)


# %%
def prob21():
    spider=input('Word to replace spider: ')
    water=input('Word to replace water: ')
    spout=input('Word to replace spout: ')
    rain=input('Word to replace rain: ')
    print('The Itsy-Bitsy', spider, 'crawled up the', water, spout+',')
    print('Down came the', rain, 'and washed the', spider, 'out!')

#%%
def prob22():
    # all possible permutations of a, b, and c:
    # abc, acb, bca, bac, cba, cab
    # nvm don't need to test all of those because the inputs
    # are given pre-sorted
    a,b,c = eval(input('Enter the three side lengths, from least to greatest, separated by commas: '))
    
    #unneeded
    #a=np.array([a,b,c])
    #a,b,c=np.sort(a)

    if a+b<=c:
        raise ValueError('Side Lengths do not form a valid triangle')

    if a==b==c:
        triangleType = 'equilateral'
    elif a!=b!=c!=a:
        triangleType = 'scalene'
    else:
        triangleType = 'isosceles'
    
    s=(a+b+c)/2

    area=round(sqrt(s*(s-a)*(s-b)*(s-c)), 2)

    print("The triangle's area is", area, 'units^2.')
    print('The triangle is a', triangleType, 'triangle.')


if __name__=='__main__':
    print('problem 19:')
    prob19()
    print('\nProblem 20')
    prob20()
    print('\nProblem 21')
    prob21()
    print('\nProblem22')
    prob22()