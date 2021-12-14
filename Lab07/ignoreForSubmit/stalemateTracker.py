class stalemateTracker:
    def __init__(self):
        self.states={}
    def addState(self, fishPoses, fishRots, sharkPos):
        state=[*fishPoses, *fishRots, sharkPos] #unzipping is for flattening
        try:
            self.states[state]+=1
        except KeyError:
            self.states[state]=1
    def checkStalemate(self, repetitions=3):
        if max(self.states.values())>=repetitions:
            return True
        return False
    