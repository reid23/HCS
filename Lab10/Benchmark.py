#%%
from time import time
from random import uniform
# from numba import njit
# from numba.core.errors import NumbaPendingDeprecationWarning
# import warnings
# warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

def timeSort(sort, iters, listLen):
    toSort=[uniform(0, 1) for _ in range(listLen)]
    start=time()
    for _ in range(iters):
        sort(toSort.copy())
    end=time()
    print(sort.__name__, 'finished')
    return end-start
#%%

def selectionSortSlow(l):
    for j in range(len(l)):
        minimum=2
        mindex=0
        for counter, i in enumerate(l[j:]):
            if i<minimum:
                minimum=i
                mindex=counter
        l[j], l[mindex+j] = l[mindex+j], l[j]


def selectionSort(l):
    for j in range(len(l)):
        cp=l[j:]
        mindex = cp.index(min(cp)) #use faster functions implemented in c
        l[mindex+j], l[j] = l[j], l[mindex+j]


#%%

def insertionSort(l):
    for i in range(len(l)):
        j=i
        while j>0:
            if l[j-1]>l[j]: #if it should be lower,
                l[j], l[j-1] = l[j-1], l[j] #swap
            else: #if it shouldn't be lower, don't swap.  we know list below is already sorted
                break
            j -= 1
        i+=1
    return l

# @njit
def insertionSortj(l):
    for i in range(len(l)):
        j=i
        while j>0:
            if l[j-1]>l[j]: #if it should be lower,
                l[j], l[j-1] = l[j-1], l[j] #swap
            else: #if it shouldn't be lower, don't swap.  we know list below is already sorted
                break
            j -= 1
        i+=1
    return l
# %%

#! CITE: https://en.wikipedia.org/wiki/Quicksort
def partition(l, low, high):
    center = l[(high + low)//2]
    high+=1
    low-=1

    while True:
        low+=1
        while l[low]<center: #make sure l[low] is greater than center
            low+=1
        high-=1
        while l[high]>center: #make sure l[high] is lower than center, if low is greater and high is lower then we need to swap them
            high-=1

        if low>=high: #if they're the same it's sorted/partitioned/whatever because we went throught the whole list and there were no swappable pairs
            return high
            
        l[low], l[high] = l[high], l[low] #swap high and low


def quickSort(l, low=-1, high=-1): 
    if low<0 or high<0:
        low, high = 0, len(l)-1
    if low<high: #base case
        p=partition(l, low, high)
        quickSort(l, low, p)
        quickSort(l, p+1, high)
    


# %%
a=[i for i in range(100000)][::-1]
def main():
    quickSort(a)

if __name__ == '__main__': main()

# %%
