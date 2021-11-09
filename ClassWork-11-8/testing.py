#%%
'''
def main():
    while True:
        year=input('Enter a year n, where 1900<n<2099: ')
        try:
            year=int(year)
        except ValueError as e:
            print('Error:\n', e)
            print('Please enter an integer.')
        else:
            if 1900<=year<=2099:
                break
            else:
                print('year was not in correct range')


    month='March'
    a=year%19
    b=year%4
    c=year%7
    d=((19*a)+24)%30
    e=((2*b)+(4*c)+(6*d)+5)%7
    easterDate=22+d+e

    if year in [1954, 1981, 2049, 2076]:
        year -= 7

    if easterDate>31:
        month='April'
        easterDate-=31
    print(easterDate, month, year)


main()
# %%
import numpy as np
import matplotlib.pyplot as plt
  
data = np.random.random(( 12 , 12 ))
plt.imshow( data , cmap = 'autumn' , interpolation = 'nearest' )
  
plt.title( "2-D Heat Map" )
plt.show()
'''
# %%
import cv2
from time import sleep
from matplotlib import pyplot as plt
img=cv2.imread('/Users/reiddye/Downloads/sharkPixelArt.jpeg')
img=cv2.resize(img, (40, 40))
cv2.imwrite('shark.jpg', img)

# %%
