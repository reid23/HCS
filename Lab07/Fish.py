from graphics import*

from random import *

class Fish:
    NORTH, EAST, SOUTH, WEST = '000', '090', '180', '270'
    """Fish object that does fish things as specified in the lab"""
    def __init__(self, xcoord, ycoord, fishABC, flee = False):
        self.position = [xcoord, ycoord]
        direction = randrange(1,5)
        if direction == 1: self.cardinalDirection = '000'
        if direction == 2: self.cardinalDirection = '090'
        if direction == 3: self.cardinalDirection = '180'
        if direction == 4: self.cardinalDirection = '270'
        if fishABC == 'a':
            self.imageName = 'fisha___.png'
        if fishABC == 'b':
            self.imageName = 'fishb___.png'
        if fishABC == 'c':
            self.imageName = 'fishc___.png'
    def turn(sharkPosition):
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
                        self.cardinalDirection = '180'
                    if relativey > 0:
                        #the fish is above the shark
                        self.cardinalDirection = '000'
                if direction == 2:
                    #flee horizontal
                     if relativex < 0:
                        #fish is to the left of the shark
                        self.cardinalDirection = '270'
                     else:
                        #fish is to the right of the shark
                        self.cardinalDirection = '090'
            elif abs(relativex) > abs(relativey):
                if relativex < 0:
                    #fish is to the left of the shark
                    self.cardinalDirection = '270'
                else:
                    #fish is to the right of the shark
                    self.cardinalDirection = '090'
            else:
                if relativey < 0:
                    #the fish is below the shark
                    self.cardinalDirection = '180'
                if relativey > 0:
                    #the fish is above the shark
                    self.cardinalDirection = '000'
        elif flee == False:
            #turns fish if near wall
            if self.position[0] == 0 and self.cardinalDirection == '270':
                self.cardinalDirection = '090'
            if self.position[0] == 9 and self.cardinalDirection == '090':
                self.cardinalDirection = '270'
            if self.position[1] == 0 and self.cardinalDirection == '180':
                self.cardinalDirection = '000'
            if self.position[1] == 9 and self.cardinalDirection == '000':
                self.cardinalDirection = '180'
                
        if self.cardinalDirection == '000': self.position[1] += 1
        if self.cardinalDirection == '090': self.position[0] += 1
        if self.cardinalDirection == '270': self.position[0] -= 1
        if self.cardinalDirection == '180': self.position[1] -= 1

        if self.position[0] > 9:
            self.position[0] -= 10
        if self.position[0] < 0:
            self.position[0] += 10
        if self.position[1] > 9:
            self.position[1] -= 10
        if self.position[1] < 0:
            self.position[1] += 10
    def getPos(self):
        return Point(self.position[0], self.position[1])
    def getImgPath(self):
        return self.imageName
    def getRotation(self):
        return self.cardinalDirection
    def setImage(self, image):
        self.sprite = image
    def getFlee(self):
        return flee
    def getGraphicsObjects(self):
        return [self.sprite]
    

#Figure out how to handle image things
#integrate fish class with gui to finish
        
    

#if fish are in each others way, the blocked fish wastes its turn. two fish never on same square        

        
