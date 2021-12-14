'''
Author: Derik Liu

The fish class contains all of the positional and directional info for fish objects
as well as an image identity for image retrieval.
The class also contains methods encompassing all necessary fish movement logic.
'''


from random import randrange
import math

class Fish:
    NORTH, EAST, SOUTH, WEST = '000', '090', '180', '270'
    """Fish object that does fish things as specified in the lab"""
    def __init__(self, xcoord, ycoord, fishABC, flee=False):
        #fish constructor: a fish object has a coordinate pair position,
        #a fish name designation a,b,c and a randomly assigned direction (N,E,S,W)
        #as well as a few of status variables (flee, isAlive etc.)
        self.position = [xcoord, ycoord]
        direction = randrange(1,5)
        if direction == 1: self.cardinalDirection = Fish.NORTH
        if direction == 2: self.cardinalDirection = Fish.EAST
        if direction == 3: self.cardinalDirection = Fish.SOUTH
        if direction == 4: self.cardinalDirection = Fish.WEST
        if fishABC == 'a':
            self.imgPath = 'images/fisha___.png'
        if fishABC == 'b':
            self.imgPath = 'images/fishb___.png'
        if fishABC == 'c':
            self.imgPath = 'images/fishc___.png'
        self.flee=flee
        self.isAlive = True
    def turn(self, sharkPosition):
        """Turn(coordinate pair shark position): runs the logic and changes the stored position of the
        fish by a single square"""
        
        if not self.isAlive:
            return
        relativex = self.position[0] - sharkPosition[0]
        relativey = self.position[1] - sharkPosition[1]
        if math.sqrt(relativex * relativex + relativey * relativey) <= 3:
            #flee logic could use tuning - how close should the fish actually be
            self.flee = True
        else:
            self.flee = False
            
        if self.flee == True:
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
        elif self.flee == False:
            #turns fish if near wall
            if self.position[0] == 1 and self.cardinalDirection == Fish.WEST:
                self.cardinalDirection = Fish.EAST
            if self.position[0] == 10 and self.cardinalDirection == Fish.EAST:
                self.cardinalDirection = Fish.WEST
            if self.position[1] == 1 and self.cardinalDirection == Fish.SOUTH:
                self.cardinalDirection = Fish.NORTH
            if self.position[1] == 10 and self.cardinalDirection == Fish.NORTH:
                self.cardinalDirection = Fish.SOUTH
        #changes fish position based on its current direction
        #(if there's no flee mode or other special circumstance
                
        if self.cardinalDirection == Fish.NORTH: self.position[1] += 1
        if self.cardinalDirection == Fish.EAST: self.position[0] += 1
        if self.cardinalDirection == Fish.WEST: self.position[0] -= 1
        if self.cardinalDirection == Fish.SOUTH: self.position[1] -= 1

        #at the end of the movement, if the fish is fleeing, the flee mode movements
        #may take it off the 10,10 grid. the position of the fish is checked, and off-grid
        #values are made to wrap around
        if self.flee == True:
            if self.position[0] > 10 and self.cardinalDirection == Fish.EAST:
                self.position[0] -= 10
            if self.position[0] < 1 and self.cardinalDirection == Fish.WEST:
                self.position[0] += 10
            if self.position[1] > 10 and self.cardinalDirection == Fish.NORTH:
                self.position[1] -= 10
            if self.position[1] < 1 and self.cardinalDirection == Fish.SOUTH:
                self.position[1] += 10

    def getPos(self):
        return self.position
    def getDirection(self):
        return self.cardinalDirection
    def getImgPath(self):
        return self.imgPath
    def setImage(self, image):
        "sets the image variable to an actual image object"
        self.img=image.clone()
    def getFleeMode(self):
        return self.flee
    def getGraphicsObjects(self):
        return [self.img]
    def setPos(self, pos):
        self.position[0] = pos[0]
        self.position[1] = pos[1]
    def setDirection(self, rot):
        self.cardinalDirection = rot
    def eaten(self):
        "fish that are eaten are moved to coordinate 100,100 for the remainder of the game"
        self.position = [100,100]
        self.isAlive = False
    def alive(self):
        return self.isAlive
    def reset(self):
        "resets status variables and reassigns a random direction at the start of each new round"
        self.isAlive = True
        self.position = [1,1]
        direction = randrange(1,5)
        if direction == 1: self.cardinalDirection = Fish.NORTH
        if direction == 2: self.cardinalDirection = Fish.EAST
        if direction == 3: self.cardinalDirection = Fish.SOUTH
        if direction == 4: self.cardinalDirection = Fish.WEST
        
        
        
