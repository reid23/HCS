#%%
import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
# %%
img=cv2.imread('Shark.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)
for counter, i in enumerate(img):
    for counter2, j in enumerate(i):
        if not ((np.array_equal(img[counter][counter2], np.array([255,255,255]))) or (np.array_equal(img[counter][counter2], np.array([0,0,0])))):
            #print(img[counter][counter2])
            img[counter][counter2][0]=250
            #img[counter][counter2][1]-=50
            img[counter][counter2][2]-=150
        
            #print(img[counter][counter2])
            #print()
        
plt.imshow(img)
plt.show()
# %%

from SharkGUI import *
g=Gui(None, None, None, None, None, None, None, None, None, None, None)

# %%

np.save('all_possible_fish_start_positions.npy', a)