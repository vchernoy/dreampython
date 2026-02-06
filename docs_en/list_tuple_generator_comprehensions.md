# List, Tuple, and Generator Comprehensions

## map/starmap vs. list/generator comprehension & zip (June 2)

Starting with imports:
```py
from functools import partial
from itertools import starmap, repeat
import operator
```
* partial ⏤ allows fixing parameters for functions, for example: partial(operator.add, 10) ⏤ is a function that adds 10, that is, an analog of: lambda x: operator.add(10, х), or lambda x: 10 + х.
* repeat ⏤ generates values in a loop, for example, repeat(7) creates an infinite sequence: 7, 7, 7,...
* starmap ⏤ analog of the built-in map function, we explain the difference below.

Suppose we have a list of integers values and our goal is to create a new list square_values that will contain the squares of the values from the first list. Write a simple loop:
```py
values = [10, 2, 7, 5, 4, 9, 1, 8]

square_values = []
for v in values:
    square_values.append(v**2)

print(square_values)
```
Output:
```
[100, 4, 49, 25, 16, 81, 1, 64]
```
Calculate squares using list comprehension:
```py
square_values = [v**2 for v in values]
print(square_values)
```
Instead of `v**2` we can use `pow(v, 2)` or `v*v`.

### Generators

Replacing square brackets `[v**2 for ...]` with round ones (v**2 for ...), we get a generator expression.
To calculate the squares of numbers, we need to make the generator work, for example, by converting it to a list:
```py
square_values = (v**2 for v in values)
print(list(square_values))
```
A generator can be created via a function:
```py
def square(values):
    for v in values:
        yield v**2

square_values = square(values)
print(list(square_values))
```
Further, we'll imply calling the print function after each calculation of square_values.

### `map(func, iterable)`

map in some sense is an analog of generator comprehension.

The first parameter ⏤ is a function that map applies to components of the second parameter (iterable).
* map produces lazy evaluation, map(lambda v: v**2, values) ⏤ is an analog of: (v**2 for v in values) ⏤ lazy evaluation.
* list(map(lambda v: v**2, values)) ⏤ is an analog of [v**2 for v in values], that is, produces a list ⏤ eager evaluation.

Simple solution with map:
```py
square_values = map(lambda v: v**2, values)
```
Now let's try to do without introducing functions, via lambda. Such a tricky variant: use partial + pow:
```py
square_values = map(partial(pow, exp=2), values)
```

### `map(func, iterable1, iterable2, ...)`

map can work with multiple iterables at once. In this case, map applies the function to values from all sequences, so the function must work with multiple arguments. Here are two examples:
```py
square_values = map(operator.mul, values, values)
```
```py
square_values = map(operator.pow, values, repeat(2))
```
Let's try to be creative and come up with more one-line solutions. All of them should produce the same list of squares of the original numbers.

### Generator + `zip(iterable1, iterable2, ...)`

Returning to generator expression, but adding zip.

zip groups several sequences into one, consisting of tuples.

Easiest to understand with an example:
```py
square_values = (v[0]*v[1] for v in zip(values, values))
```
Further, two examples that are analogous to applying map over two iterables, but using generator expression + zip:
```py
square_values = (operator.mul(*v) for v in zip(values, values))
```
```py
square_values = (operator.pow(*v) for v in zip(values, repeat(2)))
```

---

## `starmap(func, iterable of tuples)` + `zip`

starmap ⏤ is an analog of map, but can unpack tuples automatically:
```py
square_values = starmap(operator.mul, zip(values, values))
```
```py
square_values = starmap(operator.pow, zip(values, repeat(2)))
```
### What's happening here?

Well, and two of the strangest solutions:

```py
square_values = map(operator.mul, *[values]*2)
```

```py
square_values = map(int(2).__rpow__, values)
```

Code: https://onlinegdb.com/N6qx5p-Da

---

## `filter` vs. list/generator comprehension (June 3))

Starting with imports:

```py
from functools import partial
import operator
```

* `partial` ⏤ fixes arguments for a given function. \
For example: `partial(int.__and__, 1)` creates a new function that takes one argument, say x, and calculates `1 & x`. \
This is an analog of: `lambda x: int.__and__,(1, х)`, or even simpler: `lambda x: 1 & х`.

* Recall that in this case we're talking about binary, bitwise AND (Bitwise AND). \
Actually we keep the least significant bit in `x`, and the rest are zeroed. This is a trickier way to calculate: `x % 2`.

* `int.__and__` ⏤ is the Bitwise AND operator, defined in the int class.

Suppose we have a list of integers values. Goal ⏤ find all odd numbers and place them in a new list: odd_values.

Start with a simple loop:
```py
values = [10, 2, 7, 5, 4, 9, 1, 8]

odd_values = []
for v in values:
    if v % 2 == 1:
        odd_values.append(v)

print(odd_values)
```
Output:
```
[7, 5, 9, 1]
```
As before, let's come up with as many different ways to do the same thing. For example, use the short form if and the command ...:
```py
odd_values = []
for v in values:
    odd_values.append(v) if v % 2 == 1 else ...

print(odd_values)
```
Interesting point, the command ... is an analog of pass, but the latter, in this case, doesn't work. Any ideas why?

### Generator

The next way to solve the problem: create a generator. This can be done easily: define a function, and instead of append + return, use yield:
```py
def odd_only(values):
    for v in values:
        if v % 2 == 1:
            yield v

odd_values = odd_only(values)
print(list(odd_values))
```
If in previous examples odd_values ⏤ was already a ready list, then in the last one ⏤ odd_values contains a generator. To get real values, we need to make the generator calculate all values. That's exactly why in print we use list(odd_values).

Now use the generator together with the short form of the if command:
```py
def odd_only(values):
    for v in values:
        (yield v) if v % 2 == 1 else ...

odd_values = odd_only(values)
print(list(odd_values))
```
Notice that yield v is in parentheses? Why?
Further we won't repeat `print(list(odd_values))`.

### Generator Expression

Generator expressions are very similar to list comprehension:
```py
odd_values = (v for v in values if v % 2 == 1)
```
```py
odd_values = (v for v in values if v & 1 == 1)
```
```py
odd_values = (v for v in values if v % 2)
```
```py
odd_values = (v for v in values if v & 1)
```
All these variants are equivalent:
* `v % 2` and `v & 1` are the same;
* as well as `v % 2 == 1` and `v & 1 == 1`. 
* Note that if v % 2 is equivalent to `if v % 2 != 0`. And in this case, this is the same as `if v % 2 == 1`.

If we replace round brackets (v for v ...) with square ones [v for v ...], we get list comprehension.
Remember the difference between lazy evaluation and eager evaluation?

### filter(func, iterable)

`filter` is an analog of generator comprehension:
* `filter(func, iterable)` is approximately equal to:
* `(func(v) for v in iterable)`.

The previous four variants of generator expressions can be rewritten using filter + lambda:
```py
odd_values = filter(lambda x: x % 2 == 1, values)
```
```py
odd_values = filter(lambda x: x & 1 == 1, values)
```
```py
odd_values = filter(lambda x: x % 2, values)
```
```py
odd_values = filter(lambda x: x & 1, values)
```

### filter and a function of one argument

Sometimes the function for filtering is already available, that is, we can save on `lambda`'s.
Each integer (int) has methods `__rmod__` and `__and__`. Let's use them:

```py
odd_values = filter(int(2).__rmod__, values)
```
```py
odd_values = filter(int(1).__and__, values)
```
The first variant is analogous to:
* `lambda x: x % 2`, and the second is analogous to:
* `lambda x: 1^x`.

### filter+partial

Let's use binary operators, for which, with the help of partial, we fix the first argument:
```py
odd_values = filter(partial(int.__rmod__, 2), values)
```
```py
odd_values = filter(partial(int.__and__, 1), values)
```
```py
odd_values = filter(partial(operator.and_, 1), values)
```

Code: https://onlinegdb.com/HZDjuLk45

---

## `map`+`filter` vs. list/generator comprehension

Combining the two previous posts. Now our goal ⏤ find all odd numbers in the list values and place their squares in sq_odd_values. Start with a simple solution:
```py
from functools import partial
import operator
```
```py
values = [10, 2, 7, 5, 4, 9, 1, 8]
sq_odd_values = []
for v in values:
    if v % 2 == 1:
        sq_odd_values.append(v**2)

print(sq_odd_values)
```
Output:
```
[49, 25, 81, 1]
```
Further use the short form if:
```py
sq_odd_values = []
for v in values:
    sq_odd_values.append(v**2) if v % 2 == 1 else ...

print(sq_odd_values)
```
Move to nested list comprehension:
```py
sq_odd_values = [v**2 for v in [v for v in values if v % 2 == 1]]
print(sq_odd_values)
```
We can do the same thing, but without nested list comprehension:
```py
sq_odd_values = [v**2 for v in values if v % 2 == 1]
print(sq_odd_values)
```

### Generators

Remember that in the two previous posts we introduced two generators? Use their composition:
```py
def square(values):
    for v in values:
        yield v**2

def odd_only(values):
    for v in values:
       (yield v) if v % 2 == 1 else ...

sq_odd_values = square(odd_only(values))
print(list(sq_odd_values))
```
Both generators: square and odd_only take iterable and create iterables. Will we get the same answer for the composition: `odd_values(square(values))`?

Further we'll omit print commands.

It's not difficult to replace the composition of generators with one:
```py
def square_odd(values):
    for v in values:
        (yield v**2) if v % 2 == 1 else ...

sq_odd_values = square_odd(values)
```

### Generator Expressions

Nested generator expressions and not (by analogy with lists):
```py
sq_odd_values = (v**2 for v in (v for v in values if v % 2 == 1))
```
```py
sq_odd_values = (v**2 for v in values if v % 2 == 1)
```

### `map`/`filter`

By analogy with the previous two posts, use lambda:
```py
sq_odd_values = map(lambda v: v**2, filter(lambda v: v % 2 == 1, values))
```
Or operators:
```py
sq_odd_values = map(partial(pow, exp=2), filter(partial(operator.and_, 1), values))
```

Code in https://onlinegdb.com/FLDien5qE

---

## Five Ways to Create Slices in Python (May 20)

Let's take a list for example, for instance of 6 words (words). 
We need to get a sublist, for example: all words except the first. 
Or a sublist of every third word. 
Or all words with indices between 2 and 4. 
This can be achieved in different ways.

### 1. words[beg:end:step]

Create a sublist via words[beg:end:step]. step can be negative, then we get reverse order. This method creates a completely new list, copying all elements. Therefore, changing words doesn't affect the created list at all.
```py
words = ['GoTo', 'statement', 'considered', 'harmful', 'by', 'Wirth']
tail = words[1:]
words[-1] = words[-1].upper()
print(f'{words=}')
print(f'{tail=}')
```
Output:
```
words=['GoTo', 'statement', 'considered', 'harmful', 'by', 'WIRTH']
tail=['statement', 'considered', 'harmful', 'by', 'Wirth']
```
### 2. list comprehension + range(beg, end, step)

The same can be achieved using list comprehension.
```py
words = ['GoTo', 'statement', 'considered', 'harmful', 'by', 'Wirth']
tail = [words[i] for i in range(1, len(words))]
words[-1] = words[-1].upper()
print(f'{words=}')
print(f'{tail=}')
```
Output:
```
words=['GoTo', 'statement', 'considered', 'harmful', 'by', 'WIRTH']
tail=['statement', 'considered', 'harmful', 'by', 'Wirth']
```
### 3. generator comprehension + range

And this is already generator comprehension (round brackets are used). Actually, the real sublist is created only in the last line when converting the generator to a list. Unlike previous examples, changes in words will be reflected in tail!
```py
words = ['GoTo', 'statement', 'considered', 'harmful', 'by', 'Wirth']
tail = (words[i] for i in range(1, len(words)))
words[-1] = words[-1].upper()
print(f'{words=}')
print(f'{list(tail)=}')
```
Output:
```
words=['GoTo', 'statement', 'considered', 'harmful', 'by', 'WIRTH']
list(tail)=['statement', 'considered', 'harmful', 'by', 'WIRTH']
```

### 4. slice & words[slice(beg, end, step)]

A somewhat similar example using the standard slice() function. This function is very similar to range(), but slice doesn't create a sequence of values (is not iterable), but simply describes indices of a sublist. We get a shadow slice (as in the previous example), but at the moment of calling words[sliced] ⏤ a list is created.
```py
words = ['GoTo', 'statement', 'considered', 'harmful', 'by', 'Wirth']
sliced = slice(1, len(words))
print(f'{sliced=}')
words[-1] = words[-1].upper()
print(f'{words=}')
tail = words[sliced]
print(f'{tail=}')
```
Output:
```
sliced=slice(1, 6, None)
words=['GoTo', 'statement', 'considered', 'harmful', 'by', 'WIRTH']
tail=['statement', 'considered', 'harmful', 'by', 'WIRTH']
```
### 5. itertools.islice(words, beg, end, step)

In the last example, itertools.islice() returns an iterator. Also a shadow slice variant. Changes in the original list will affect the values produced by the iterator.
```py
import itertools

words = ['GoTo', 'statement', 'considered', 'harmful', 'by', 'Wirth']
tail = itertools.islice(words, 1, len(words))
words[-1] = words[-1].upper()
print(f'{words=}')
print(f'{list(tail)=}')
```
Output:
```
words=['GoTo', 'statement', 'considered', 'harmful', 'by', 'WIRTH']
list(tail)=['statement', 'considered', 'harmful', 'by', 'WIRTH']
```

Code: https://onlinegdb.com/0PnBp4y9n

