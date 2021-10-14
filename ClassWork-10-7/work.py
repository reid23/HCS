#CLASSES!


class foo:
    #docstring
    #help(thing) returns this
    #can also be seen in the ide when coding
    """class example!
        has typical methods and stuff
    """
    #constructor:
    def __init__(self, var):
        """constructor; create foo object

        Args:
            var ([float]): the instance variable you want to set
        """
        #instance variable
        self.var=var

    #method
    def bar(self):
        """foo.bar()
            prints hi and self.var
        """
        print('hi', self.var)

    #output of repr(foo)
    #should be callable to create self
    def __repr__(self):
        return f'foo({self.var})'

    #human readable 
    def __str__(self):
        return f'<foo object> var={self.var}'

    #getters and setters
    def getVar(self):
        """foo.getVar()

        Returns:
            var: self.var
        """
        return self.var
    
    def setVar(self, var):
        """foo.setVar(var)
           sets self.var to var

        Args:
            var (float): the value to set self.var to
        """
        self.var=var

f=foo(100)
f.bar()

print(repr(f))
print(str(f))
