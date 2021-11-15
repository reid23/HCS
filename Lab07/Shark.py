from graphics import *
class Shark:
    def __init__(self, imgPath='Shark___.png', pos=[7,2], draw=True):
        self.imgPath=imgPath
        self.pos=pos
    def getGraphicsObjects(self):
        return self.img
    def getImgPath(self):
        return self.imgPath
    def getPos(self):
        return self.pos
    def setImage(self, image):
        self.img=image.clone()
