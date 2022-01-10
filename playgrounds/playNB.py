# %%
#! Mutable Default arguments

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


def bc(a, b, func):
    s_a = _shape(a)
    s_b = _shape(b)

    if len(s_a)


def _shape(a):
    shape = []
    while True:
        try:
            shape.append(len(a))
        except TypeError:
            break
        a=a[0]
    return tuple(shape)



#%%

