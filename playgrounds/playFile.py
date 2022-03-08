from functools import cache
from numba import njit
from time import time

def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

@cache
def fibc(n):
    if n<=2:
        return 1
    return fibc(n-1) + fibc(n-2)


@njit
def fibj(n):
    if n<=2:
        return 1
    return fibj(n-1) + fibj(n-2)
#fibj(3) #do the compiling

startTime=time()
print(fibc(100))
print(time()-startTime)