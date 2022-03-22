# Lab 10
So... I went a little overboard on this one.

For benchmark, I tried to implement all of the sorts in Rust first, then port them over to python. I've been learning rust for an outside project, and I figured it would be a nice way to learn that while also improving my understanding of the sorts. I'm writing another summer program application right now, so I added pretty much everything to this lab that I could rationalize before working on that.

## Benchmark (rust)
This is the rust implementation.  It's compiled for my computer, but I think it will work for yours as well, unless you have one of those new ARM chips. There's a bunch of stuff, just run `./path/to/benchmark -h` (or whatever the right path is).  You might have to `chmod +x` if it's not executable by default.

## Benchmark
For `Benchmark.py`, I used a bunch of libraries we haven't used as a class, so it won't run if you don't have `numpy`, `matplotlib`, and `numba` installed. These aren't for doing the actual specs; all of the printing to shell and sorting and timing would work with just normal (non-numpy) lists, but it would be much slower without numba, wouldn't make pretty graphs at the end, and you'd have to comment everything out.

To change how long the longest list length is, you can change the `length` variable at the top of `main`. It will sort up to lists of length $2^{length+1}$.  I found that, even with numba, 14 was about as high as I could tolerate while debugging.  Without numba, the max was 11 or 12.  
If you want to try running it without numba, you can uncomment line 25, which overwrites the `@njit` decorator to not do anything.

When running with numba, there is also a one or two second initialization delay after you answer the questions.  This is because numba's just-in-time compilation is, by definition, only done when needed.  So I call all of the sorts in the beginning to make numba compile all of them before the benchmarking starts, preventing the compilation from messing with the data.

One thing to be aware of is that `Benchmark.py` saves the timing data (if you tell it to) to the relative path `data/times.npy`, so you need a `data` folder in the same library that you're running `Benchmark.py` from.

## Profiling

I also included `callgraph.svg`, which is just a really cool graphic of the results from running cprofile on `Benchmark.py`.  It turns out that cprofile is pretty much useless, because it doesn't tell you anything deeper than the function level (like it just says "bubbleSort is slow!"), but it's still a really interesting graph because you can see the real flow of the program.  I also used `line_profiler`, which ended up being much more helpful because it give times line-by-line, but it doesn't have fancy gui.

## ConvertBase

This file has a bunch of redundant functions.  Briefly:
- `toTen` is never used, it's just an expanded version of the algorithm in `cvtr`
- `toStr`, `toTenR`, and `cvtrBig` are together the equivalent of `cvtr`, except that `toTenR` is recursive while the implementation in `cvtr` is not (because you can't cram everything in one line if it has to call another function)
- `cvtr`, the monster, is equal in size and mysticality to the monster group (hence its name).  Seriously, I have no clue how or why I did this.  Every error was just "there's an error on this line!  Good luck, have fun!"  But it works, so whatever.
- `main` contains all of the input validation and printing, and calls `cvtr`.

The purpose of this was that I wanted to put all of the conversion into as little lines as possible. Because Paul said he did it in four lines.  Yes, mine is unreadable and unending spaghetti while his is four actually sane lines, but mine is still one line.  Was it painful?  Yes.  Was it helpful to me in any way?  No.  But was it still worth it anyway?  No, it definitely wasn't.  I have no idea why I did this.