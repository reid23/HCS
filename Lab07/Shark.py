'''
Author: Reid Dye

This file contains the Shark class for the shark lab.
'''

from graphics import *
import numpy as np #only used for cleanliness
from random import randint
from numpy.core.numeric import Inf #only used for cleanliness
class Shark:
    def __init__(self, imgPath='images/Shark.png', pos=[7,2]):
        """constructor for Shark class

        Args:
            imgPath (str, optional): the path to the image. Defaults to 'Shark.png'.
            pos (list, optional): the initial position of this shark. Defaults to [7,2].
        """
        self.imgPath=imgPath
        self.pos=pos
        self.chasing=randint(1, 3)
        #collapse this if your ide allows it
        #it takes up a lot of space
        self.possibleMoves = [
            [0, 1], 
            [1, 1], 
            [1, 0], 
            [1, -1], 
            [0, -1], 
            [-1, -1], 
            [-1, 0], 
            [-1, 1],
            
            [2, 2], 
            [2, 0], 
            [2, -2], 
            [0, -2], 
            [-2, -2], 
            [-2, 0], 
            [-2, 2], 
            [0, 2],

            [2, 1],
            [2, -1],
            [-2, 1],
            [-2, -1],
            [1, 2],
            [1, -2],
            [-1, 2],
            [-1, -2]
        ]
    def _dist(self, a, b): 
        """finds the euclidian (L2) distance between two points.

        Args:
            a (list): a point in the form [x, y]
            b (list): another point in the form [x, y]

        Returns:
            float: the euclidean distance between a and b.
        """
        return np.linalg.norm(np.array(a)-np.array(b)) #sorry I'm lazy and didn't want to make a pythagorean kind of thing
    #takes in the shark and fish positions as 'a' and 'b' respectively and returns a magnitude of their proximity
    def _mindex(self, a):
        """utility method to find the index of the minimum value(s) in a list

        Args:
            a (list): the input list

        Returns:
            list: a list of the index/indeces of the minimum value(s).  Only longer than 1 element if there are multiple values tied for minimum.
        """
        curmin=Inf #np is useful here, could have used 100000000, but this is cleaner.
        output=[]
        for counter, i in enumerate(a):
            if i == curmin:
                output.append(counter)
            elif i < curmin:
                output=[counter]
                curmin = i
        return output
    
    def getGraphicsObjects(self):
        "returns a list of all graphics objects in this class"
        return [self.img]
    def getImgPath(self):
        "returns the path of the image representing this animal"
        return self.imgPath
    def getPos(self):
        "gets the coordinate position of this animal"
        return self.pos
    def getDirection(self):
        "gets the rotation of this animal"
        return '270' #always east because shark doesnt turn
    def setImage(self, image):
        "sets the image variable to an actual image object"
        self.img=image.clone()
    def setFleeMode(self, fleeMode):
        "sets the flee mode.  For compatability"
        pass
    def getFleeMode(self):
        "gets the flee mode. For compatability"
        return False
    def setChasing(self, fishPoses):
        "sets self.chasing given all of the fish positions"
        dists = [self._dist(self.pos, i) for i in fishPoses]
        if self.chasing-1 in self._mindex(dists): return
        self.chasing=self._mindex(dists)[randint(0, len(self._mindex(dists))-1)]+1
    def getChasing(self):
        "returns which fish this shark is chasing, either 1, 2, 3, or None"
        return self.chasing
    def turn(self, fishPoses):
        """runs through the Shark turn logic and returns the desired relative movement in the form [deltaX, deltaY]

        Args:
            fishPoses (list): a list of the positions of the fish.  in the form [[x,y] [x,y] [x,y]]

        Returns:
            list: the desired relative movement in the form [Dx, Dy]
        """
        self.setChasing(fishPoses)
        endPos=fishPoses[self.chasing-1]
        direction=[endPos[0]-self.pos[0], endPos[1]-self.pos[1]]

        if direction in self.possibleMoves: return [direction[0], direction[1]]
        if direction[1]==0: return [-2, 0] if direction[0]<0 else [2, 0]
        if direction[0]==0: return [0, -2] if direction[1]<0 else [0, 2]
        if direction[0]>0 and direction[1]>0: return [2, 2]
        if direction[0]<0 and direction[1]>0: return [-2, 2]
        if direction[0]>0 and direction[1]<0: return [2, -2]
        if direction[0]<0 and direction[1]<0: return [-2, -2]
    def setPos(self, movementInfo):
        """sets the shark's position given relative movement information

        Args:
            movementInfo (list): the relative movement, in the form [Dx, Dy]
        """
        self.pos[0] += movementInfo[0]
        self.pos[1] += movementInfo[1]
        if self.pos[0] == 0: self.pos[0] += 1
        if self.pos[0] == 11: self.pos[0] -= 1
        if self.pos[1] == 0: self.pos[1] += 1
        if self.pos[1] == 11: self.pos[1] -= 1
    def reset(self):
        """resets the position to the start position
        """
        self.pos = [7,2]
