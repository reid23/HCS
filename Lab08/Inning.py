class Inning:
    def __init__(self, number, team):
        self.runs = 0
        self.log = f'\nInning {number} - {team}'
        self.outs = 0
        self.bases = [0,0,0]
    def _shiftBit(self, bit, register:list):
        s_o = register[-1]
        register[:] = [bit]+register #have to do [:] to re assign elements instead of re assigning "register" pointer
        register[:] = register[:-1]
        return s_o
    def addPlay(self, play, player):
        self.log+=f"\n{player} {['struck out', 'singled', 'doubled', 'tripled', 'homered'][play]}"
        if play==0:
            self.outs+=1
            return False if self.outs>=3 else True

        for i in range(play):
            a=self._shiftBit(player if i==0 else 0, self.bases)
            if a!=0: self.log += f' ({a} scored)'
            self.runs+=1 if not not a else 0
        return True

    def getSummary(self):
        return self.log
    def getRuns(self):
        return self.runs
