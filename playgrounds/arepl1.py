# a=[3,4,2,4,1,7,5]
class foo:
    def __init__(self, thing1, thing2, thing3):
        self.a=thing1
        self.b=thing2
        self.c=thing3
    def __repr__(self):
        return f'foo({self.a}, {self.b}, {self.c})'
    def __gt__(self, other):
        return self.b>other.b



a=[foo(1,2,3), foo(2,3,4), foo(3,4,5)]

print(a)

a.sort(reverse=True)

print(a)

a.sort(key=b)

print(a)