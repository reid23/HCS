#%%
from math import *

def circRad(area):
    return sqrt(area/pi)
# %%
def quadFormula(a,b,c):
    try:
        oneSide=(-b+sqrt((b**2)-(4*a*c)))/(2*a)
    except:
        oneSide='NaN'
    try:
        otherSide=(-b+sqrt((b**2)-(4*a*c)))/(2*a)
    except:
        otherSide='NaN'

    return oneSide, otherSide
# %%
