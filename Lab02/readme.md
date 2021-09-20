# Hi!
I just wanted to explain a few of the things in this lab.
I wanted to write a gradient descent demo for AI club, and this fit perfectly with the vertex() function that was required.  I did this in two steps. But first, here's why I wrote the black box function classes.

## Black Box Functions
I wrote these because with a neural network, you can't just evaluate the gradient symbolically.  That's way too computationally expensive when you have a thousand-variable function.  Instead, we use backprop.  But we don't need to do that for a demo of gradient descent, and we don't have an actual network to propagate through, so this is my alternative.  With the blackBoxFunction classes, all you can do is evaluate the function at a value. You can't use any algebra to figure out the exact gradient.  I guess it's kind of like the opposite of sympy.

## blackBoxFunction and vertex()
My initial idea was to write vertex() such that it simply used gradient descent instead of -b/2a.  So I implemented this first, and that's why I used the name vertex() and not something more descriptive.  I thought this was the only one I was going to be writing.

## blackBoxFunctionMultiVariable and bigBoiVertex()
This was my second try.  I wanted to generalize the method to higher dimensions, so I wrote these.  It's pretty much the same idea.  The main reason for doing this is so that I could plot the surface with matplotlib or something, then plot the path that the algorithm followed in a few different scenarios.  This way, I could easily show how gradient descent can get trapped in valleys or on plateaus.  I haven't implemented that yet though.

### That's it. Sorry if this is way too much stuff. I just plopped it all into this file while building it all, and figured it couldn't hurt to turn in.