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



# %%
