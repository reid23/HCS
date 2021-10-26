from graphics import *
from ReidList import ReidList as r

class ScoreCell():
    def __init__(self, center, label: str):
        """constructor for ScoreCell

        Args:
            center (Point object): the center point of the ScoreCell
            label (str): the label of the ScoreCell (the type of scoring to perform)
        """
        #assign vars and check stuff
        self.types=r('1s', '2s', '3s', '4s', '5s', '6s', 'bonus', 'three\nof a\nkind', 'four\nof a\nkind', 'full\nhouse', 'small\nstra-\night', 'large\nstra-\night', 'chance', 'yaht-\nzee', 'total')
        #input validation on the string one, because that's a little more open-ened
        assert self.types.exists(label), f'{label} is not a valid type of ScoreCell.\n Valid types are {self.types}'
        self.center=center
        self.boundary=Rectangle(Point(center.getX()-20, center.getY()-50), Point(center.getX()+20, center.getY()+50))
        self.line=Line(Point(center.getX()-20, center.getY()-20), Point(center.getX()+20, center.getY()-20))
        p=center.clone()
        p.move(0, 15)#move doesn't output anything, it's a mutator, so we need this to be in a separate line
        self.label=Text(p, label)
        #some useful flags
        #state machines OP
        self.locked=False
        self.yahtzeeUsed=False
        self.drawn=False
        #the score in the ScoreCell
        p.move(0, -50)
        self.value=Text(p, '-')
    def reset(self):
        """called at the end of every game.  Resets the scores.
        """
        self.locked=False
        self.yahtzeeUsed=False
        self.value.setTextColor('black')
        self.value.setText('-')

    def _calc(self, dice):
        """Internal method to generate the score from dice for itself

        Args:
            dice (ReidList): a list of numbers that is the output of the dice rolls

        Returns:
            int: the score calculated based on the dice
        """
    #should have used a switch here...
    #switch statements have been added in python 3.10!
    #very exciting
        label=self.label.getText()
        #for 1-6s it's just the number of them times 6
        if label=='1s':
            return dice.count(1)
        elif label=='2s':
            return dice.count(2)*2
        elif label=='3s':
            return dice.count(3)*3
        elif label=='4s':
            return dice.count(4)*4
        elif label=='5s':
            return dice.count(5)*5
        elif label=='6s':
            return dice.count(6)*6
        elif label=='three\nof a\nkind':
            c=dice.toCounter()
            for i in c:
                #if there were 3+ of this element, return the score
                if i(1) >= 3:
                    return sum(dice)
            #else return zero, else not needed because return stops execution
            return 0
                
        elif label=='four\nof a\nkind': #same as three of a kind
            c=dice.toCounter()
            for i in c:
                if i(1) >= 4:
                    return sum(dice)
            return 0

        elif label=='full\nhouse':
            c=dice.toCounter()
            if not(len(c)==2 or len(c)==1): #if theres more than two different values on the dice, it cant be a full house
                return 0
            if c(0)(1)==2 or c(0)(1)==3 or c(0)(1)==5:  #make sure it's not like {6:1, 1:5}, which would have two different dice, but not full house
                return 25
            return 0

        elif label=='small\nstra-\night':
            #check if any of the small straight conditions are met
            if dice.exists(r(1,2,3,4)) or dice.exists(r(2,3,4,5)) or dice.exists(r(3,4,5,6)):
                return 30
            return 0
                    
        elif label=='large\nstra-\night': #Same as small straight but with less conditions
            if dice.exists(r(1,2,3,4,5) or r(2,3,4,5,6)):
                return 40
            return 0
        elif label=='chance': #this one's pretty simple
            return sum(dice)
        elif label=='yaht-\nzee':
            #oh boy here we go
            #all this complexity is from the problem where this is the only cell where it can still score points
            #even if it's already been scored
            if len(dice.toCounter())==1 and self.value.getText()!='0': #first check if it's a yahtzee, and the score hasn't been used and is 0 (because then you can't score bonus pts)
                if self.yahtzeeUsed: #check if yahtzee has been scored already
                    if self.value.config['fill']=='black': #if this is the first of three rolls, then it will be black from last round, but if it's the second roll, it will a) be red and b) already have the 100 added
                        return int(self.value.getText())+100
                    else:
                        return int(self.value.getText())
                return 50
            return 0
        elif label=='total':
            pass #this is calculated externally
    #draw and undraw, just bundling again
    def draw(self, win):
        if self.drawn:
            self.undraw()
        self.line.draw(win)
        self.boundary.draw(win)
        self.label.draw(win)
        self.value.draw(win)
        self.drawn=True
    def undraw(self):
        self.line.undraw()
        self.boundary.undraw()
        self.label.undraw()
        self.value.undraw()
        self.drawn=False

    #getters and setters
    def setValue(self, val):
        self.value.setText(str(val))
    def getVal(self):
        return self.value.getText()
    def getName(self):
        return self.label.getText()
    def getLocked(self):
        return self.locked
    
    #basicallly Button.clicked() but for scorecells
    #i need my inheritance
    #Those books, incedentally, are great (The Inheritance Cycle)
    def inBounds(self, p):
        if abs(p.getX()-self.center.getX()) < 20 and abs(p.getY()-self.center.getY()) < 50:
            return True
        return False
    
    #make the score immutable in future rolls, except for yahtzee, becuase yahtzee is --awful-- special
    def lockScore(self):
        self.value.setTextColor('black')
        if self.label.getText()=='yaht-\nzee':
            if self.value.getText()=='0':
                self.locked=True #it means that yahtzee was scored as a zero
                return #skip the rest
            else:
                self.yahtzeeUsed=True
                self.locked=False
                return #if we're locking, and yahtzee is being used, the value is already correct, it's just red, but we fixed that in the first line, so its fine
        self.locked=True #for normal cells all we need to do is flip this var and set the color to black
    def prelimCalc(self, dice):
        """sets colors and values for a preliminary calculation for aiding the user's choice of cell

        Args:
            dice (ReidList): A list of the dice's numbers (ints)
        """
        if not self.getLocked():
            self.value.setText(str(self._calc(dice)))
            self.value.setTextColor('red')

    def notLock(self):
        """To be run if the scoreCell isn't being locked/scored this round.  Basically resets it, except for yahtzee, because yahtzee is --awful-- special
        """
        if self.label.getText()=='yaht-\nzee':
            #I definately 100% understand what all of this logic does
            #please don't ask me though
            #I did write it, I'm just not sure how
            #lots of trial and error, the way I write everything
            #aslfjsd;afjasdl;fjalgkjsd;afsdj5l;kadfjl;kad it's late
            if self.locked:
                self.value.setTextColor('black')
                return
            if self.value.getText()=='50' and self.yahtzeeUsed:
                self.value.setTextColor('black')
                return
            #for this line
            #please let me just use value.config[item]
            #there's no getColor() method, and I really don't want to create a separate variable to track it
            if int(self.value.getText())>=150 and self.value.config['fill']!='black':
                self.value.setText(str(int(self.value.getText())-100))
                self.value.setTextColor('black')
                return
            elif int(self.value.getText())>=150:
                return
        self.value.setTextColor('black')
        self.locked=False
        self.value.setText('-')