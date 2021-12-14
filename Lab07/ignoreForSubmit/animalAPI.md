each animal should have the following methods:  

1. The constructor.  It takes a string, the path of the image, and the intial position.  Maybe also a flee variable
```python 
def __init__(self, imgPath='fish/fish____.png', pos=[7,2], draw=True, flee=False):
    pass
```

2. getGraphicsObjects(self): should return a list of all objects that make up an object.
```python 
def getGraphicsObjects(self): return [self.img, self.fleeModeIndicator, self.randomGraphicsObjectIJustMadeUp]
```

3. getImgPath(self)  
returns a string representing the path for the animal's image, but with ___ instead of the numbers in the actual path.

4. getPos(self)  
returns an list representing the animal's current position in the grid, in the form [x, y]

5. getRot(self)  
returns the current rotation: '000', '090', '180', or '270'

6. setImage(self, image)  
sets self.img to a copy of image.

7. setFleeMode(self, fleeMode)  
sets the flee mode

8. getChasing(self)
gets who the shark is chasing.  ```pass``` or ```return None``` for fish.

9. turn(self, sharkPos)
returns a relative movement, and sets flee mode correctly.   
example return:

```python
self.setFleeMode(True)
return [1,1]
```

sharkRunner should, after each turn, use SharkGUI to check each fish's flee mode, then draw or undraw the flee mode indicator.