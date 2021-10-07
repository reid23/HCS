# notes
Welp, here's lab 4.  I didn't add much to this one.  
The documentation is in each file; these are just misc notes.

I also wanted to say that I've started using github to sync my stuff across devices... Definitely not because I've run out of room in dropbox.

Anyway, if I forget to submit something, it's probably there.  https://github.com/reid23/HCS
Just leaving this here, hopefully it will never be used, but I tend to be forgetful :|

# Pentagon
I spent a bunch of time trying to get the lines to follow the mouse in this, and ultimately decided it was impossible, or at least not worth my time.  The problem (as usual :|) was that it's super hard to do anything non-gui-based on macs.  I couldn't figure out a way to get the window location.  I could get the cursor location in global coordinates using pyautogui, but then needed to subtract the graphWin's coordinates to get the spot where I should put the actual objects.  Here's what I tried:

## Looking through the graphics library
I dug through the graphics library to see where it got the coordinates from GraphWin.getMouse() from, but I found nothing.  It seems that the handling for the mouse is built into tkinter somewhere, because GraphWin.update() isn't defined in graphics.py, so it must be in the superclass of GraphWin, which is tk.Canvas.  I've never used tkinter before, so I pretty much gave up here.  I did also look through the toWorld() function, and the transformation class, but I didn't find anything that helped there.

## computer vision
I also tried doing a knn-style thing where I just computed the euclidean distance between a small image (the window's top, with the title) and sections of a screenshot with the same shape.  But even with numba speedification, that was exceedingly slow.

The kernel.npy function is the portion of screenshot I used; if you do np.load and then plt.imshow() you can see that it is a few pixels of a screenshot of the title bar of the GraphWin on my mac.

## Applescript
I found out that I could get window positions using applescript, and tried implementing this in several ways.  If you run GetWinPos.applescript while there's a GraphWin open, it will return the coordinates.  However, the issue arises when you try to run this file from python.  I tried the appscript library, the applescript library, and straight up running the file from terminal with subprocess.popen(), but no matter what I did, the script would just give me the spinny beach ball.  It seems that it only works if the applescript process is separate from the python process?  I don't know.


## Partial success (?)
I figured out how to do it on linux and (in theory, don't have a windows machine to test on) windows, but because you're grading on a mac, I decided that it wasn't worth my time to go through the process of implementing that.  So PentagonGUI.py is the remaining skeleton of my failed attempt to improve pentagon.  
Throughout this adventure, I also learned a lot about regular expressions, and the myths are true!  It *is* like a cat jumped on my keyboard.  
> Some people, when confronted with a problem, think "I know, I'll use a regex."  
> Now they have two problems.

# PentagonGUI2
This one's the actual implementation.  I took the liberty of using numpy instead of a ten billion (ok, more like log(ten billion)) variables to store all of the numbers; please have mercy.  It just let me get all of the stuff easily without having to type a lot of lines.  Like getting the xs and ys from the points in two lines instead of ten. And letting me do the math in one line instead of one line per point.

The one thing I added was making the button actually work!  I just said to only close the window if the mouse click was in the button.

# QuadraticGUI
I... May have used lists again.  But its coordinates, they have to be in pairs!  Yes, I could have used two variables and not changed anything, but I *really* don't want to rewrite it.  Thanks.

# AutoDepMPL
This was just to hash out the general format of the autodep program, and to see what a graph could look like.  It just uses matplotlib to plot the depreciation instead of manually doing it.  Much cleaner.

# AutoDepGUI
The actual implementation.  I did use numpy again, and in this case I would have to do it differently without arrays.  But I don't want to implement that because I'm busy this week, spent too much time trying to get my pentagon thing to work, and have a physics test to study for, so here's how I would do it in ~~english~~ code which can be 'compiled' using OpenAI Codex.

It's all the same until line 52, at which point things start to change.
First, I would create all of the graph axes, and the y axis tick marks and labels, manually.
Then I would make a large loop that loops [years] times.  Every time, it would add a new box, tick mark, and label, and calculate the box size in the accumulator format.  
Basically, I'd have to put everything in one big loop instead of kind of sequentially like it is now.
