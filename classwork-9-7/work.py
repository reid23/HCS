#%%
import numpy as np
from math import *
#%%
def mtok(miles):
    return miles*1.60934

mtok(5)
#%%
def countdown(n):
    print(str([i for i in np.array(list(range(n))[::-1])+1])[1:-1])

for i in range(6):
    countdown(i)
# %%
def bill(rate, mins, sms):
    calls=4
    texts=5
    return rate+(mins*4)+(sms*5)

print(bill(5,2,2))
# %%
def sumOfStuff():
    numbers=[]
    output=0
    n=input('the number: ')
    for i in list(n):
        numbers.append(int(i)**2)
    print(sum(numbers))

sumOfStuff()
# %%
