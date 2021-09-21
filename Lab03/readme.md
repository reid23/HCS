# Notes
I split up the functions into different files this time.  

Lab03.py contains the first functions I wrote to solve the problems.  I've added functionality to them, but the base algorithm (if you could call it that) is the same. For this reason, Lab03Simple.py is somewhat cleaner code, or at least less cluttered code.  

I'm going to put the explanations for each function here because it's easier to read, and easier to type (don't have to make #s or deal with auto-complete).  

Additionally, I'm still a little unclear about the expectations on commenting.  I've done the max commenting for Lab03Simple, but gone a little lighter on Lab03.  Are there any concrete/quantitative requirements on comments?  

# Lab03.py
## `points(*points)`
Calculates the slope of a line through them, the distance between them, the equation of the line through them, and the angle of rotation about the origin from the first to the second.  

Parameters:
- `*points` : Two 1D, length-2 numpy ndarrays or python lists representing the input points of the function in the form [x0,y0], [x1,y1].  If no arguments are given, points will use python's builtin input() function to get two points.  If the user is so stubborn that they refuse to give any input, points will create two random points with coordinates between -1 and 1.  

Returns:
- Nothing All outputs are printed. 


## `testScores(*scores)`
Finds the min, max, average, standard deviation, and the average letter grade for a set of test scores.  

Parameters:
- `*scores` : any number of integers from 0 to 100.  These are the test scores.  If none are given, testScores will use input() to get scores.

Returns: 
- Nothing. All outputs are printed.

## `leap(*years)`
Calculates whether a year is a leap year.  

Parameters:
- `*years` : any number of positive integers.  These are the input years.  If none are given, leap will use input() to gather a single year.

Returns:
- `output` : a numpy ndarray of boolean values, representing whether each input value is a leap year or not.
- If no arguments were given, `output` is printed instead of returned.

## `tanAng(a)`
Calculates the angle vector in degrees using atan.  Range is [-90, 90]

Parameters:
- `a` : A numpy ndarray with shape (2,) representing the input vector in <x,y> form.

Returns:
- `null` : A numpy scalar, the angle of the vector.

## `corrrectAng(a)`
Converts negative angles to their positive counterparts.

Parameters:
- `a` : an angle, in degrees.  Float or int.

Returns:
- `null` : an angle, in degrees.  Float or int, based on input

# Lab03Simple.py
## `testScores()`
Finds the min, max, average, and average letter grade for a set of test scores.

Parameters:
- None.  All input is through input().  Scores must be integers between 0 and 100.

Returns:
- Nothing. all output is printed.

## `points()`
Calculates the slope of a line through any two points, the distance between them, the equation of the line through them, and the angle of rotation about the origin from the first to the second. 

Parameters:
- None.  All input is through input().  Input must be integers.

Returns:
- Nothing. all output is printed.

## `leap()`
Determines whether a year is a leap year or not.

Parameters:
- None.  All input is through input().  Input must be a positive integer.

Returns:
- Nothing. all output is printed.

## `tanAng(a0, a1)`
Calculates the angle of the vector <a0,a1> using atan. Range is [-90, 90].

Parameters:
- `a0` : Float or int.  The x coordinate of the input vector.
- `a1` : Float or int.  The y coordinate of the input vector.

Returns: 
- `null` : Float or int.  The angle of the vector, in degrees.

## `correctAng(a)`
Converts a negative angle to its positive counterpart.

Parameters:
- `a` : Float or int.  The input angle. (degrees)

Returns:
- `null` : Float or int.  The corrected, positive angle. (degrees)


## `norm(a0, a1)`
Calculates the euclidean norm (magnitude) of a 2D input vector.

Parameters:
- `a0` : Float or int.  The x coordinate of the input vector.
- `a1` : Float or int.  The y coordinate of the input vector.

Returns:
- `null` : Float or int.  The 2-norm of the input.
