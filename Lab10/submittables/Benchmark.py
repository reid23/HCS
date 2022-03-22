'''
Author: Reid Dye

This file runs five different sorting algorithms and compares their performance.
'''


# actually needed for sorting
from time import time
from random import uniform

# for fun stuffs
from numba import njit #for going faster because I'm not waiting for hours every time
from numba.core.errors import NumbaPendingDeprecationWarning #because warnings nasty
import warnings
from matplotlib import pyplot as plt #pretty graphs
import sys
import os
import numpy as np #for saving data (I'm not waiting for it every time!)

# who needs warnings anyway
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

#! uncomment to turn off numba jit compilation
# def njit(func): return func


def timeSort(sort, iters, listLen):
    times = []
    for _ in range(iters):
        toSort=[uniform(0, 1) for _ in range(listLen)]
        start=time()
        sort(toSort.copy())
        times.append((time()-start) * 1000)

    print(f'{sort.__name__} finished {iters} sorts of length-{listLen} lists')
    return [min(times), max(times), sum(times)/len(times)]

def selectionSortSlow(l): #more elementary, theoretically faster
    for j in range(len(l)):
        minimum=2
        mindex=0
        for counter, i in enumerate(l[j:]):
            if i<minimum:
                minimum=i
                mindex=counter
        l[j], l[mindex+j] = l[mindex+j], l[j]

#ok technically this one is O(n^3), but it's faster because index() and min() are implemented in C
@njit
def selectionSort(l):
    for j in range(len(l)):  # everything is wrapped again so O(n) again
        cp=l[j:]             # slicing is O(k); k:=len of slice; so this is O(n).  but it's just added so doesn't matter for overall
        mindex = cp.index(   # index is O(n)
                    min(cp)) #   min is O(n)
        l[mindex+j], l[j] = l[j], l[mindex+j] # O(1), because getting and setting are all O(1)



@njit
def insertionSort(l):
    for i in range(len(l)):
        for j in range(i, 0, -1):
            a=l[j] #declare vars for this to minimize lookups
            #accessing a list is O(1) but it's still slow
            b=l[j-1]
            if b>a:
                l[j] = b
                l[j-1] = a
            else:
                break

@njit
def bubbleSort(l):
    length = len(l)
    for i in range(length):
        for j in range(length-i-1): # -1 to prevent l[j+1] from being out of bounds
            a=l[j]
            b=l[j+1]
            if a>b:
                l[j]=b #swap
                l[j+1]=a




#source: cobbled together from https://en.wikipedia.org/wiki/Merge_sort
#couldn't figure out how to make this one in-place though, so i just did the sketchy wrapper function trick

def mergeSort(l):
    l=mergeSortMain(l)

@njit
def mergeSortMain(l):
    length = len(l)
    if length<=1: return l

    mid = length//2;
    lin = l[:mid]
    rin = l[mid:]
    left, right = mergeSortMain(lin), mergeSortMain(rin)
    return merge(lin, rin)

@njit
def merge(l, r):
    merged = []
    lpos, rpos = 0, 0
    llen, rlen = len(l), len(r)
    while lpos<llen and rpos<rlen:
        if l[lpos] > r[rpos]:
            merged.append(r[rpos])
            rpos += 1
        else:
            merged.append(l[lpos])
            lpos += 1
        
    if lpos==llen: #if left got to the end first
        return merged+r[rpos:]
    return merged+l[lpos:]

# CITE: https://en.wikipedia.org/wiki/Quicksort
@njit
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

@njit
def quickSort(l, low=-1, high=-1): 
    if low<0 or high<0:
        low, high = 0, len(l)-1
    if low<high: #base case
        p=partition(l, low, high)
        quickSort(l, low, p)
        quickSort(l, p+1, high)
    


# for nicer looks
class shutUp:
    def __enter__(self): #no init default constructor is fine
        sys.stdout = open(os.devnull, 'w') #shove printed stuff into /dev/null where it can go to live happily every after
    def __exit__(self, *args): #python passes some random stuff at the end of a with statement?  idk it doesn't throw errors anymore
        sys.stdout = sys.__stdout__ #set back to normal


def main():
    length = 14

    runSorts = input("Do you want to actually run the sorts (as opposed to loading old data)? [y/N] ") #n assumed as default
    if 'y' in runSorts.lower():
        runSorts = True
        saveSorts = input("Do you want to save the timing data? [Y/n] ")# y assumed the default
        if 'n' in saveSorts.lower():
            saveSorts = False
        else:
            saveSorts = True
    else:
        runSorts = False
        saveSorts = False
    

    if runSorts:
        print("initializing...")

        with shutUp(): #make all this stuff not print anything
            #compile everything for numba!
            bubbleSort([5,4,3,2,1])
            selectionSort([5,4,3,2,1])
            insertionSort([5,4,3,2,1])
            mergeSort([5,4,3,2,1])
            quickSort([5,4,3,2,1])
            timeSort(bubbleSort, 10, 10)
            timeSort(selectionSort, 10, 10)
            timeSort(insertionSort, 10, 10)
            timeSort(mergeSort, 10, 10)
            timeSort(quickSort, 10, 10)

        #gather data
        print("starting sorts!\n")
        b = np.array([np.array(timeSort(bubbleSort,    10, 2**(i+1))) for i in range(3, length)])
        s = np.array([np.array(timeSort(selectionSort, 10, 2**(i+1))) for i in range(3, length)])
        i = np.array([np.array(timeSort(insertionSort, 10, 2**(i+1))) for i in range(3, length)])
        m = np.array([np.array(timeSort(mergeSort,     10, 2**(i+1))) for i in range(3, length)])
        q = np.array([np.array(timeSort(quickSort,     10, 2**(i+1))) for i in range(3, length)])
        data = np.array([b,s,i,m,q])
        if saveSorts:
            np.save('data/times.npy', data)
    else:
        data = np.load('data/times.npy')

    # data is shape (5, 11, 3)
    # 5 sorts x 11 list lengths x 3 numbers per trial


    fig = plt.figure()
    gs = fig.add_gridspec(5, hspace=0)
    ax = gs.subplots(sharex=True, sharey=False)

    plt.suptitle("Time take (ms) vs list length\nblue: min, green: avg, orange: max")


    x=[2**(i+1) for i in range(3, length)]
    for i in range(len(data)):
        ax[i].plot(x, data[i], marker='o')
        ax[i].set_xscale("log", base=2)
        ax[i].label_outer()
    ax[0].set_title("bubble sort", y=1.0, pad= -14)
    ax[1].set_title("selection sort", y=1.0, pad= -14)
    ax[2].set_title("insertion sort", y=1.0, pad= -14)
    ax[3].set_title("merge sort", y=1.0, pad= -14)
    ax[4].set_title("quick sort", y=1.0, pad= -14)

    for i in range(3, length):
        print(f"Size of List: 2^{i+1}")
        print("Results (times in ms):\n")

        print("Sort method          Fastest         Slowest         Average")
        print("-----------          -------         -------         -------")
        print(f"Bubble              {str(data[0][i-3][0])[:10]}      {str(data[0][i-3][1])[:10]}      {str(data[0][i-3][2])[:10]}")
        print(f"Selection           {str(data[1][i-3][0])[:10]}      {str(data[1][i-3][1])[:10]}      {str(data[1][i-3][2])[:10]}")
        print(f"Insertion           {str(data[2][i-3][0])[:10]}      {str(data[2][i-3][1])[:10]}      {str(data[2][i-3][2])[:10]}")
        print(f"Merge               {str(data[3][i-3][0])[:10]}      {str(data[3][i-3][1])[:10]}      {str(data[3][i-3][2])[:10]}")
        print(f"Quick               {str(data[4][i-3][0])[:10]}      {str(data[4][i-3][1])[:10]}      {str(data[4][i-3][2])[:10]}")
        print()

    plt.show()



if __name__ == '__main__': 
    main()

# %%
