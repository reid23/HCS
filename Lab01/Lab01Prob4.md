## Allowed Operations:

ADD A B C – Adds the contents of memory location A and B and put the result in C. Your CPU will allow you have C equal A or B, if you wish.\
STORE X A – Writes the value X to memory location A

<br></br>

### Problem A

```python
w=3
x=4
y=6
z=w+x+y
```
<br></br>

Soln:

```
store 3 1
store 4 2
store 6 3
add 1 2 0
add 0 3 0
```
<br></br>

### Problem B

``` python
z=0
x=5
for i in range(x):
    z=z+x
```
<br></br>

Soln:

```
store 0 0
store 5 1
add 0 1 0
add 0 1 0
add 0 1 0
add 0 1 0
add 0 1 0
```
<br></br>

### Problem C

Rewrite question A's solution in binary

``` 
001 011 001
001 100 010
001 110 011
000 001 010 000
000 000 011 000
```