#%%
class dynamicFuncs:
    def __init__(self):
        self.remembered = {}
    def fib(self, n):
        try:
            return self.remembered[n]
        except KeyError:
            if n<=2:
                self.remembered[n] = 1
                return 1
            self.remembered[n] = +self.fib(n-2)+self.fib(n-1)
            return self.remembered[n]
        

def fibNaive(n):
    if n<=2:
        return 1
    return fibNaive(n-2)+fibNaive(n-1)


#%%
import random
def sorted(l):
    for counter, i in enumerate(l):
        if counter==0:
            continue
        if i<l[counter-1]:
            return False
    return True

def bogosort(l):
    while not sorted(l):
        random.shuffle(l)
    return l

#%%
def fact(n):
    out = 1
    for i in range(n):
        out *= i+1
    return out

def factr(n):
    if n==1:
        return 1
    return factr(n-1)*n

#%%
from numba import njit
from functools import cache, lru_cache

def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

@njit
def fibj(n):
    if n<=2:
        return 1
    return fibj(n-1) + fibj(n-2)

fibj(3)

@cache
def fibc(n):
    if n<=2:
        return 1
    return fibc(n-1) + fibc(n-2)


@lru_cache(10)
def fiblc(n):
    if n<=2:
        return 1
    return fiblc(n-1) + fiblc(n-2)

def fibi(n):
    nums = []
    for i in range(n):
        if i<=2:
            nums.append(1)
        else:
            nums.append(nums[-1]+nums[-2])
    return nums[-1]

#%%
#* 1/24 - OOD
class Class:
    def __init__(self, name, teacher, roster):
        self.name=name
        self.teacher=teacher
        self.roster=roster
    def takeAttendence(self, whoIsHere):
        allPresent=True
        for student in self.roster:
            if student in whoIsHere:
                pass
            else:
                allPresent=False
        return allPresent
    def meeting(self):
        self.teachLesson()
    def teachLesson(self, lesson):
        return f"yay! here's the lesson: {lesson}"

class Club(Class):
    def __init__(self, name, teacher, studentLeader, roster):
        super().__init__(name, teacher, roster)
        self.studentLeader=studentLeader
    def meeting(self):
        self.doActivity()
    def doActivity(self):
        self.teachLesson(f'funClubActivity with club {self.name}')


class AIClub(Club):
    def __init__(self, name, teacher, studentLeader, roster, studentPythonSkills=None):
        super().__init__(name, teacher, studentLeader, roster)
        print(super().super())
        self.studentPythonSkills=studentPythonSkills



#%%
from numba import njit, jit

@jit(nopython=True)
def ncat(a, b):
    return a+b

def ccat(a, b):
    return a+b


#%%
class foo:
    def __init__(self, num):
        self.num=num
    def __lt__(self, other):
        return self.num<other

print(foo(5)<5)


#%%
class point:
    x: float
    y: float

print(point(1,1))
d = {'one':1, 'two':2, 'three':3}
a = list(d.items())

a.sort(key=lambda a:a[1], reverse=True)

print(a)

# %%
#! Mutable Defafult arguments

def foo(n, l=[]):
    l.append(n)
    return l

print(foo(5))
print(foo(6))
print(foo(7))

def bar(n, l=None):
    if l==None: #default l to empty list, without using mutable default arguments.  because that creates problems.
        l = []
    
    l.append(n)
    return l

print(bar(5))
print(bar(6, [1,2,3,4,5]))
print(bar(7))


# %%
#! file methods

with open('data.data', 'r') as file:
    for line in file:
        print(line, end = '')
# %%
def add(a, b):
    return a+b

def mult(a, b):
    return a*b

def _shape(a):
    shape = []
    while True:
        try:
            shape.append(len(a))
        except TypeError:
            break
        a=a[0]
    return tuple(shape)

def bc(A, B, func):
    a=A.copy()
    b=B.copy()

    s_a = _shape(a)
    s_b = _shape(b)
    if len(s_a)<len(s_b):
        while len(_shape(a))<len(s_b):
            a=[a]
    elif len(s_b)<len(s_a):
        while len(_shape(b))<len(s_a):
            b=[b]
    s_a = _shape(a)
    s_b = _shape(b)

    s_a_r = list(s_a)
    s_b_r = list(s_b)

    s_a_r.reverse()
    s_b_r.reverse()

    for counter, i in enumerate(s_a_r):
        if i==s_b_r[counter]: continue
        elif i==1:
            exec(f'a{"[0]"*counter} = [a{"[i]"*counter}[0] for j in range({s_b_r[counter]})]')
        elif s_b_r[counter]==1:
            pass
        else:
            raise ValueError(f'Operands could not be broadcast together with shapes {_shape(A)} and {_shape(B)}')

    print(_shape(a), _shape(b))

    print(s_a, s_b)

def stretch(arr, axis, len):
    pass





#%%
import numpy as np
def zeroes(shape):
    output=[]
    shape.reverse()
    for i in range(shape[0]): output.append(0)
    for i in shape[1:]:
        output=[output for i in range(i)]
    return output

def bc(A, B, func):
    a=A.copy()
    b=B.copy()

    s_a = _shape(a)
    s_b = _shape(b)
    if len(s_a)<len(s_b):
        while len(_shape(a))<len(s_b):
            a=[a]
    elif len(s_b)<len(s_a):
        while len(_shape(b))<len(s_a):
            b=[b]
    s_a = _shape(a)
    s_b = _shape(b)

    s_a_r = list(s_a)
    s_b_r = list(s_b)

    s_a_r.reverse()
    s_b_r.reverse()

    for counter, i in enumerate(s_a_r):
        if i==s_b_r[counter]: continue
        elif i==1:
            exec(f'a{"[0]"*counter} = [a{"[i]"*counter}[0] for j in range({s_b_r[counter]})]')
        elif s_b_r[counter]==1:
            pass
        else:
            raise ValueError(f'Operands could not be broadcast together with shapes {_shape(A)} and {_shape(B)}')

    print(_shape(a), _shape(b))

    print(s_a, s_b)

#%%
def stretch(arr, axis, len):
    for i, _ in enumerate(eval(f'arr{"[0]"*axis}')):
        print(f'arr{("[0]"*axis)+"["+str(i)+"]"}=[arr{("[0]"*axis)+"["+str(i)+"]"} for _ in range(len)]')
        print("["+str(i)+"]")
        exec(f'arr{("[0]"*axis)+"["+str(i)+"]"}=[arr{("[0]"*axis)+"["+str(i)+"]"} for _ in range(len)]', locals(), locals())
    #waaaaa

class lrst:
    def __init__(self, *shape):
        self.dims=[lrst(*shape[1:]) if len(shape)>1 else 0 for _ in range(shape[0])]
        print(self.dims)




#%%
import numpy as np

def zeroes(shape):
    output=[]
    shape.reverse()
    for i in range(shape[0]): output.append(0)
    for i in shape[1:]:
        output=[output for i in range(i)]
    return output



# %%
