from Lab02 import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

f=blackBoxFunctionMultiVariable(['x','y'], '(x**3)-(2*(x**2))+(y**3)-(2*(y**2))+(x**6)+(y**6)')

arr=np.arange(-1.65, 1.66, 0.4)

length=len(arr)

X = np.array(list(arr)*length)
Y = np.repeat(arr, length)

print(X.shape, X.shape)

Z = []

for i in arr:
    for j in arr:
        Z.append(f([j,i]))

Z=np.array(Z)




fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_trisurf(X, Y, Z, linewidth=0, antialiased=False, alpha=0.5)

#do gradient descent
learningRate=1.7
guess=np.array([-0.01,1.5])
xGuesses=[]
yGuesses=[]
zGuesses=[]
#iteratively find min/max with gradient descent
while learningRate>0.2: #doing it based on lr and not gradient vec len to reduce chance of finding local 'trap' valleys\
    xGuesses.append(guess[0])
    yGuesses.append(guess[1])
    zGuesses.append(f(guess))
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
    
    #flip the gradient cause we're descending
    grad=np.negative(grad)
    

    #get new guess by adding a distance of learningRate 
    #to our current guess
    guess=(grad*learningRate)+guess
    #decrease the learning rate by 5 percent
    learningRate*=0.93


#get the output values from guess and make them pretty
#idk why but if these lines are put directly into the fstrings it breaks
outputInput = [ffp(i, 3, trim='k') for i in guess] #must use for loop bc ffp only works on scalars
outputOutput = ffp(f(guess), 3, trim='k')

ax.scatter(np.array(xGuesses), np.array(yGuesses), np.array(zGuesses))
ax.plot(np.array(xGuesses), np.array(yGuesses), np.array(zGuesses))
ax.view_init(70,0)
plt.show()