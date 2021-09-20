# notes
I split up the functions this time.  
Lab03.py contains the first functions I wrote to solve the problems.  I've added functionality to them, but the base algorithm (if you could even call it that) is the same. For this reason, Lab03Simple.py is somewhat cleaner code, or at least less cluttered code.  

I'm going to put the explanations for each function here because it's easier to read, and easier to type (don't have to make #s or deal with auto-complete).

## Lab03.py
### ```points(*points)```
Points takes any number of positional arguments, all 1D sequences with length 2.  If arguments are given, two must be given for the function to function correctly.  Points takes the first two points and calculates the slope of a line through them, the distance between them, the equation of the line through them, and the angle of rotation about the origin from the first to the second.  

If no arguments are given, points will use python's builtin input() function to get two points.  

If the user is so stubborn that they refuse to give any input, points will create two random points with coordinates between -1 and 1.  

The outputs of the calculations are printed out.  


### ```testScores(*scores)```
testScores takes any number of positional arguments, all integers from 0 to 100.  