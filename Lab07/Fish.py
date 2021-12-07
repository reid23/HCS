from graphics import*
from random import randrange
import math

class Fish:
    """Fish object that does fish things as specified in the lab"""
    NORTH, EAST, SOUTH, WEST = '000', '090', '180', '270'
    def __init__(self, xcoord, ycoord, flee = False, imgPath='fish1/fish___.png'):
        self.imgPath=imgPath
        self.position = [xcoord, ycoord]
        direction = randrange(1,5)
        if direction == 1: self.cardinalDirection = Fish.NORTH
        if direction == 2: self.cardinalDirection = Fish.EAST
        if direction == 3: self.cardinalDirection = Fish.SOUTH
        if direction == 4: self.cardinalDirection = Fish.WEST
    def setImage(self, image):
        "sets the image variable to an actual image object"
        self.img=image.clone()
    def getFleeMode(self):
        return self.
#MOVE FISH FIRST 
    def turn(self, sharkPosition):
        relativex = self.position[0] - sharkPosition[0]
        relativey = self.position[1] - sharkPosition[1]
        if abs(relativex) < 4 and abs(relativey) < 4:
            flee = True
        else:
            flee = False
            
        if flee == True:
            if abs(relativex) == abs(relativey):
                #flee random
                direction = randrange(1,3)
                if direction == 1:
                    if relativey < 0:
                        #the fish is below the shark
                        self.cardinalDirection = Fish.SOUTH
                    if relativey > 0:
                        #the fish is above the shark
                        self.cardinalDirection = Fish.NORTH
                if direction == 2:
                    #flee horizontal
                     if relativex < 0:
                        #fish is to the left of the shark
                        self.cardinalDirection = Fish.WEST
                     else:
                        #fish is to the right of the shark
                        self.cardinalDirection = Fish.EAST
            elif abs(relativex) > abs(relativey):
                if relativex < 0:
                    #fish is to the left of the shark
                    self.cardinalDirection = Fish.WEST
                else:
                    #fish is to the right of the shark
                    self.cardinalDirection = Fish.EAST
            else:
                if relativey < 0:
                    #the fish is below the shark
                    self.cardinalDirection = Fish.SOUTH
                if relativey > 0:
                    #the fish is above the shark
                    self.cardinalDirection = Fish.NORTH
        elif flee == False:
            #turns fish if near wall
            if self.position[0] == 0 and self.cardinalDirection == Fish.WEST:
                self.cardinalDirection = Fish.EAST
            if self.position[0] == 9 and self.cardinalDirection == Fish.EAST:
                self.cardinalDirection = Fish.WEST
            if self.position[1] == 0 and self.cardinalDirection == Fish.SOUTH:
                self.cardinalDirection = Fish.NORTH
            if self.position[1] == 9 and self.cardinalDirection == Fish.NORTH:
                self.cardinalDirection = Fish.SOUTH
                
        if self.cardinalDirection == Fish.NORTH: self.position[1] += 1
        if self.cardinalDirection == Fish.EAST: self.position[0] += 1
        if self.cardinalDirection == Fish.WEST: self.position[0] -= 1
        if self.cardinalDirection == Fish.SOUTH: self.position[1] -= 1

        if self.position[0] > 9:
            self.position[0] -= 10
        if self.position[0] < 0:
            self.position[0] += 10
        if self.position[1] > 9:
            self.position[1] -= 10
        if self.position[1] < 0:
            self.position[1] += 10
    def getPos(self):
        return self.position
    def getDirection(self):
        return self.cardinalDirection
    def getImgPath(self):
        return self.imgPath

#if fish are in each others way, the blocked fish wastes its turn. two fish never on same square        

        
