from graphics import *
import numpy as np
from random import randint
from numpy.core.numeric import Inf
class Shark:
    def __init__(self, imgPath='Shark.png', pos=[7,2], draw=True):
        self.imgPath=imgPath
        self.pos=pos
        self.chasing=None
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
            [0, 2]
        ]
    def _dist(a, b): return list(np.linalg.norm(np.array(a)-np.array(b)))
    def _mindex(a):
        curmin=Inf
        output=[]
        for counter, i in enumerate(a):
            if i == curmin:
                output.append(counter)
            elif i < curmin:
                output=[counter]
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
    def setChasing(self, *fishPoses):
        "sets self.chasing given all of the fish positions"
        xs, ys = zip(*fishPoses)
        if min(xs)>2 or min(ys)>2: 
            self.chasing=None
            return
        dists = [self._dist(self.pos, i) for i in fishPoses]
        if self.chasing-1 in self._mindex(dists): return
        self.chasing=self._mindex(dists)[randint(1, len(self._mindex(dists)))]+1
    def getChasing(self):
        "returns which fish this shark is chasing, either 1, 2, 3, or None"
        return self.chasing
    def turn(self, *fishPoses):
        self.setChasing(*fishPoses)
        endPos=fishPoses[self.chasing-1]
        direction=[endPos[0]-self.pos[0], endPos[1]-self.pos[0]]

        if direction in self.possibleMoves: return (direction[0], direction[1])
        if direction[1]==0: return (2, 0) if direction[0]<0 else (0, 2)
        if direction[0]==1: return (2, 0) if direction[0]<0 else (2, 0)
        if direction[0]>0 and direction[1]>0: return (2, 2)
        if direction[0]<0 and direction[1]>0: return (-2, 2)
        if direction[0]>0 and direction[1]<0: return (2, -2)
        if direction[0]<0 and direction[1]<0: return (-2, -2)
