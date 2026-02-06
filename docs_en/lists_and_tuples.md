# Lists & Tuples

## Unpacking in Python (May 9)

Suppose a list is defined somewhere.
```py
t = ['say', 5, 'times', 'hi']
print(t)
```
List components can be assigned to separate variables, that is, unpacked, with just one command:
```py
do_that, how_many, times, what = t
print(do_that, how_many, times, what)

(do_that, how_many, times, what) = t
print(do_that, how_many, times, what)
```
You can unpack a list during a function call, for example:
```py
print(*t)
```
The standard print() function uses parameter packing, since it's defined as: print(*objects, ...). That is, in the last line, the list is first unpacked, and inside print() it's packed.

Output:
```
['say', 5, 'times', 'hi']
say 5 times hi
say 5 times hi
say 5 times hi
```
You can unpack individual list components:
```py
do_that, *how_many_times, what = t
print(do_that, how_many_times, what)
print(do_that, *how_many_times, what)

print()

do_that, *something = t
print(do_that, something)
print(do_that, *something)
```
Output:
```
say [5, 'times'] hi
say 5 times hi

say [5, 'times', 'hi']
say 5 times hi
```
Unpacking works for tuples (tuple) in a similar way. For dictionaries there's its own type of (un-)packing.

Code: https://onlinegdb.com/NvuGy8Oo8

---

## Initialize Multidimensional Arrays (lists) in Python Correctly! (May 12)

Fill two-dimensional arrays (3x2) with zeros, True, and consecutive numbers:
```py
print([[0] * 3 for _ in range(2)])
print([[True] * 3 for _ in range(2)])
print([list(range(3)) for _ in range(2)])
```
Output:
```
[[0, 0, 0], [0, 0, 0]]
[[True, True, True], [True, True, True]]
[[0, 1, 2], [0, 1, 2]]
```
Tuples of tuples, lists of tuples, lists of lists:
```py
print((tuple('#'*i for i in range(3)),)*2)
print([tuple('#'*i for i in range(3))]*2)
print([['#'*i for i in range(3)]]*2)
```
Output:
```
(('', '#', '##'), ('', '#', '##'))
[('', '#', '##'), ('', '#', '##')]
[['', '#', '##'], ['', '#', '##']]
```
In the last print command, the array (list) contains a nested list. A two-dimensional array is built using the repetition operator * (repetition). This can create unpredictable problems.

Look at the following example:
```py
broken_grid = [list(range(3))] * 2
print(broken_grid)
broken_grid[0][0] = 100 
print(broken_grid)
```
Output:
```
[[0, 1, 2], [0, 1, 2]]
[[100, 1, 2], [100, 1, 2]]
```
Changing element (0,0) also changed the value at (1,0). 
In fact, broken_grid[0] and broken_grid[1] ⏤ point to the same list. 
This is probably not what we wanted to get.

Correctly initialize complex arrays like this:
```py
grid = [list(range(3)) for _ in range(2)]
print(grid)
grid[0][0] = 100 
print(grid)
```
Output:
```
[[0, 1, 2], [0, 1, 2]]
[[100, 1, 2], [0, 1, 2]]
```
Code: https://onlinegdb.com/bBCb2LO_u

---

## Operator `star` for lists and tuples:

### List repetition:
```py
values = [2, 5, 13]
repeated_values = values * 2
print(repeated_values)
```
Output:
```
[2, 5, 13, 2, 5, 13]
```
### Partial unpacking:
```py
x, y, z = values
print(x, y, z)

x, *yz = values
print(x, yz)
```
Output:
```
2 5 13
2 [5, 13]
```
### Arguments unpacking:
```py
print(values)
print(*values)
```
Output:
```
[2, 5, 13]
2 5 13
```
### Yet another argument unpacking:
```py
def impress(a, b, c):
    print(a, b, c)

impress(*values)
```
Output:
```
2 5 13
```
### Functions with arbitrary number of positional argument:
```py
def impress_any(*args):
    print(args)

impress_any(x, y, z)
impress_any(*values)
```
Output:
```
(2, 5, 13)
(2, 5, 13)
```
https://onlinegdb.com/-8B_D1JMB

---

## The Art of Print (May 15)

### Print string and list of its letters:
```py
s = 'hello world'
print(s)
print(list(s))
print(*list(s))
```
Output:
```
hello world
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
h e l l o   w o r l d
```
### Print list with sep:
```py
print(*list(s), sep='')
print(*list(s), sep=',')
print(*list(s), sep=' ')
```
Output:
```
hello world
h,e,l,l,o, ,w,o,r,l,d
h e l l o   w o r l d
```
### Apply str.join to list:
```py
print(''.join(list(s)))
print(','.join(list(s)))
print(' '.join(list(s)))
```
Output:
```
hello world
h,e,l,l,o, ,w,o,r,l,d
h e l l o   w o r l d
```
### Apply str.join to str:
```py
print(''.join(s))
print(','.join(s))
print(' '.join(s))
```
Output:
```
hello world
h,e,l,l,o, ,w,o,r,l,d
h e l l o   w o r l d
```
### Print f-strings:
```py
print(f'{s=}')
print(f'{list(s)=}')
print(f"{' '.join(s)=}")
```
Output:
```
s='hello world'
list(s)=['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
' '.join(s)='h e l l o   w o r l d'
```
Code in https://onlinegdb.com/nSMCNF6w1

