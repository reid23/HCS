#moving this to a different file because
#it's taking up a bunch of space
#and also now I can do import ReidList as r

#should have done this earlier
#going to learn lists soon anyways :(
# but it'll be useful for this lab, i guess
#it would also be nice to have a dict class
#but that is definately way too much work

from graphics import *
class ReidList():
    def __init__(self, 
        e0=None, 
        e1=None, 
        e2=None, 
        e3=None, 
        e4=None, 
        e5=None, 
        e6=None, 
        e7=None, 
        e8=None, 
        e9=None, 
        e10=None, 
        e11=None, 
        e12=None, 
        e13=None, 
        e14=None, 
        e15=None, 
        e16=None, 
        e17=None, 
        e18=None, 
        e19=None, 
        e20=None, 
        e21=None, 
        e22=None, 
        e23=None, 
        e24=None, 
        e25=None, 
        e26=None, 
        e27=None, 
        e28=None, 
        e29=None, 
        e30=None, 
        e31=None, 
        e32=None, 
        e33=None, 
        e34=None, 
        e35=None, 
        e36=None, 
        e37=None, 
        e38=None, 
        e39=None, 
        e40=None, 
        e41=None, 
        e42=None, 
        e43=None, 
        e44=None, 
        e45=None, 
        e46=None, 
        e47=None, 
        e48=None, 
        e49=None, 
        e50=None, 
        e51=None, 
        e52=None, 
        e53=None, 
        e54=None, 
        e55=None, 
        e56=None, 
        e57=None, 
        e58=None, 
        e59=None, 
        e60=None, 
        e61=None, 
        e62=None, 
        e63=None, 
        e64=None, 
        e65=None, 
        e66=None, 
        e67=None, 
        e68=None, 
        e69=None, 
        e70=None, 
        e71=None, 
        e72=None, 
        e73=None, 
        e74=None, 
        e75=None, 
        e76=None, 
        e77=None, 
        e78=None, 
        e79=None, 
        e80=None, 
        e81=None, 
        e82=None, 
        e83=None, 
        e84=None, 
        e85=None, 
        e86=None, 
        e87=None, 
        e88=None, 
        e89=None, 
        e90=None, 
        e91=None, 
        e92=None, 
        e93=None, 
        e94=None, 
        e95=None, 
        e96=None, 
        e97=None, 
        e98=None, 
        e99=None, length=-1):
        """constructor for ReidList

        Args:
            *elements: the elements to put in the list
            length (int): the length of the list.  If given, this will override the *elements and initialize a list of zeros.
        """
        self.curElement=0 #for iterating
        if not length == -1:
            self.len=length
            for i in range(length):
                exec(f'self.elements{i}=0')
        else:
            '''
            self.len=len(elements)
            for counter, i in enumerate(elements):
                theString='self.elements'+str(counter)+'='+repr(i)
                exec(f'self.elements{counter}={repr(i)}')
            '''
            self.len=0
            for i in range(100):
                if eval(f'e{i}')==None: continue
                self.len+=1
                exec(f"self.elements{i}=e{i}")
    def loop(self, func):
        """an alternative to making this class iterable.  

        Args:
            func (function): the function to be executed.  In the form func(listInput, counterInput)
        """
        counter=0
        for i in range(self.len):
            func(self.get(i), counter)
            counter+=1

    def __repr__(self):
        output='ReidList('
        for i in range(self.len):
            output+=repr(self.get(i))
            if not (self.len-1)==i:
                output+=','
        output+=')'
        return output

    def __str__(self):
        output='['
        for i in range(self.len):
            output+=f'{self.get(i)}'
            if not (self.len-1)==i:
                output+=','
        output+=']'
        return output

    def __iter__(self):
        self.curElement=0
        return self
    
    def __next__(self):
        self.lastElement=self.len-1
        if self.curElement <= self.lastElement:
            self.curElement+=1
            return self.get(self.curElement-1)
        raise StopIteration

    #cause I'm lazy
    def __call__(self, element):
        return self.get(element)


    #yes, I could have used __getitem__(), but
    #I'm lazy and that's unneeded
    #this works fine, and __call__ is good enough
    #I'm not optimizing for speed or anything, adding a scalar to an m-d array has complexity O(n^m)
    #and you know what we say in P&D:
    # > Good enough, is!
    def get(self, element):
        try: #for more useful errors
            if element>=0:
                return eval(f'self.elements{element}')
            else:
                #for getting from the end of the list
                return eval(f'self.elements{self.len+element}')
        except AttributeError:
            raise IndexError(f'List index out of range. element {element} does not exist in list of length {self.len}.')

    def set(self, element, value):
        if element >=0:
            pass
        else:
            element=self.len+element  
        exec(f'self.elements{element}={repr(value)}')

    def append(self, value):
        #because indexed at zero, self.len is always one plus the last element
        exec(f'self.elements{self.len}=value')
        self.len+=1

    def getRange(self, start: int, stop: int, step=1):
        output=ReidList()
        for i in range(start, stop, step):
            output.append(self.get(i))
        return output

    def vecMatMul(self, mat):
        output=ReidList(length=self.len)
        assert len(mat)==self.len, 'matrix had incorrect shape.'
        counter=0
        for i in mat:
            output=output+(i*self.get(counter))
            counter += 1
        return output

    def exists(self, x):
        t=type(x)
        if t==int or t==str or t==float or t==bool:
            for i in self:
                if x==i:
                    return True
            return False
        else:
            for i in x:
                if not self.exists(i):
                    return False
        return True
    #bubblesort
    #not most efficient, but pretty easy
    def sort(self):
        output=eval(repr(self))
        for i in range(len(output)-1):
            for j in range(len(output)-i-1):
                if output(j) > output(j+1) :
                    outputJ=output(j) #because we can't do multiple assignment with ReidList elements
                    output.set(j, output(j+1))
                    output.set(j+1, outputJ)
        return output
    
    def count(self, x):
        """Count how many elements of self are equal to x, y

        Args:
            x (any): the value to match

        Returns:
            int: the number of values equal to x in self.
        """
        output=0
        for i in self:
            if i==x:
                output+=1
        return output
    

    #like collections.Counter
    def toCounter(self):
        """outputs a list that's formatted like a dict with the equivalent purpose of collections.Counter.

        Returns:
            ReidList: the output list.
        """
        ordered=self.sort()
        output=ReidList()
        counted=ReidList()
        for i in ordered:
            if counted.exists(i):
                output.set(-1, output(-1)+ReidList(0, 1))
            else:
                counted.append(i)
                output.append(ReidList(i, 1))
        return output
                
    def delElement(self, element):
        while element<self.len-1:
            exec(f'self.elements{element}=self.get({element+1})')
            element+=1
        exec(f'del(self.elements{element})')
        self.len-=1
        

    def __len__(self):
        return self.len

    def __add__(self, y):
        """defines how ReidLists are added

        Args:
            y (int or float, or other ReidList with the same shape): the variable to be added.  If it's a single value, it must be the same 
        """
        if type(y)==int or type(y)==float or type(y)==str:
            output=ReidList(length=self.len)
            for i in range(self.len):
                output.set(i, self.get(i)+y)
        else:
            #in this case it's another ReidList object
            assert len(y)==len(self), 'arrays are different shapes, computation could not be completed'
            output=ReidList(length=self.len)
            for i in range(self.len):
                output.set(i, self.get(i)+y.get(i))
        return output
    
    def __sub__(self, y):
        """defines how ReidLists are subtracted.  Same as __add__

        Args:
            y (int, float, str, or other ReidList with the same shape): the thing to be added.  if it's a single value, it must be the same type as the ReidList elements

        Returns:
            output (ReidList): the result of the calculation
        """
        if type(y)==int or type(y)==float or type(y)==str:
            output=ReidList(length=self.len)
            for i in range(self.len):
                output.set(i, self.get(i)-y)
        else:
            #in this case it's another ReidList object
            assert len(y)==len(self), 'arrays are different shapes, computation could not be completed'
            output=ReidList(length=self.len)
            for i in range(self.len):
                output.set(i, self.get(i)-y.get(i))
        return output
    def __mul__(self, y):
        if type(y)==int or type(y)==float or type(y)==str:
            output=ReidList(length=self.len)
            for i in range(self.len):
                output.set(i, self.get(i)*y)
        else:
            #in this case it's another ReidList object
            assert len(y)==len(self), 'arrays are different shapes, computation could not be completed'
            output=ReidList(length=self.len)
            for i in range(self.len):
                output.set(i, self.get(i)*y.get(i))
        return output
    def __truediv__(self, y):
        if type(y)==int or type(y)==float or type(y)==str:
            output=ReidList(length=self.len)
            for i in range(self.len):
                output.set(i, self.get(i)/y)
        else:
            #in this case it's another ReidList object
            assert len(y)==len(self), 'arrays are different shapes, computation could not be completed'
            output=ReidList(length=self.len)
            for i in range(self.len):
                output.set(i, self.get(i)/y.get(i))
        return output
    def __floordiv__(self, y):
        """defines floor division, works elementwise

        Args:
            y (int, float, or ReidList): the thing to divide by

        Returns:
            output (ReidList): the quotient
        """
        if type(y)==int or type(y)==float:
            output=ReidList(length=self.len)
            for i in range(self.len):
                output.set(i, self.get(i)//y)
        else:
            #in this case it's another ReidList object
            assert len(y)==len(self), 'arrays are different shapes, computation could not be completed'
            output=ReidList(length=self.len)
            for i in range(self.len):
                output.set(i, self.get(i)//y.get(i))
        return output
    def __pow__(self, y):
        if type(y)==int or type(y)==float:
            output=ReidList(length=self.len)
            for i in range(self.len):
                output.set(i, self.get(i)**y)
        else:
            #in this case it's another ReidList object
            assert len(y)==len(self), 'arrays are different shapes, computation could not be completed'
            output=ReidList(length=self.len)
            for i in range(self.len):
                output.set(i, self.get(i)**y.get(i))
        return output
    def __eq__(self, y):  #equivalent to a.all()
        if type(y)==int or type(y)==float or type(y)==str or type(y)==bool:
            for i in range(self.len):
                if not self.get(i)==y:
                    return False
        elif y==None:
            return False #if we'e got here... it can't be None.  Because self exists.
        else:
            #in this case it's another ReidList object
            for i in range(self.len):
                if not self.get(i)==y.get(i):
                    return False
        return True #if it's not returned by now

    #all right
    #that's all I'm doing for now
    #maybe in the future I'll add eq, >, <, etc. that work by returning a bool array
    #but not for now
    #and we'll probably learn about lists soon
    #also better support for multi-dimensional arrays would be nice but
    #again--numpy coming soon, hopefully
# %%
if __name__=='__main__':
    print(ReidList(5,5,5,1,1).sort())
    print(ReidList(1,5,2,5,7).sort())