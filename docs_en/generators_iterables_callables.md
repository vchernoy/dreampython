# Generators, Iterables, Callables

## The Art of Generators (May 15)

Syntactically, generators are similar to both functions and lists and tuples. A generator can be created by defining a function that uses the yield operator. The following function defines a generator that yields three numbers: 1, 10, 100.
```py
def gen_1_10_100():
    yield 1
    yield 10 
    yield 100 
```
Create a generator by calling the function. Generate all values by converting the generator to a list.
```py
g = gen_1_10_100()
print(f'{type(g)=}')
print(f'{g=}')
print(f'{list(g)=}')
print(f'{list(g)=}')
```
Output:
```
type(g)=<class 'generator'>
g=<generator object gen_1_10_100 at 0x7f460e476ac0>
list(g)=[1, 10, 100]
list(g)=[]
```
The type of object g ⏤ is generator. Converting to a list gives [1, 10, 100]. It may be somewhat unexpected, but repeated conversion yields an empty list [].

Why?

Well, the generator yielded everything it had: 1, 10, 100. And then there's nothing more to generate! We need to create a new generator!
```py
g = gen_1_10_100()
print(f'{list(g)=}')
print(f'{list(g)=}')
```
Output:
```
list(g)=[1, 10, 100]
list(g)=[]
```
A generator can be passed as a parameter to functions where a sequence of values is expected. Simply, where a list works, a generator can (but not necessarily!) work too.
```py
g = gen_1_10_100()
print(f'{sum(g)=}')

g = gen_1_10_100()
print(f'{sum(1.01**x for x in g)=}')
```
Output:
```
sum(g)=111
sum(1.01**x for x in g)=4.819435954832733
```
A generator can also be created via generator comprehension. Similar to list comprehension, but in round brackets (...).
```py
g = (x for x in [1, 10, 100])
print(f'{type(g)=}')
print(f'{g=}')
print(f'{list(g)=}')
```
Output:
```
type(g)=<class 'generator'>
g=<generator object <genexpr> at 0x7f7033d93ac0>
list(g)=[1, 10, 100]
```
And such a generator can be passed (not always!) to functions where a list is expected:
```py
g = (x for x in [1, 10, 100])
print(f'{sum(g)=}')
print(f'{type(x for x in [1, 10, 100])=}')
print(f'{sum(x for x in [1, 10, 100])=}')
```
Output:
```
sum(g)=111
type(x for x in [1, 10, 100])=<class 'generator'>
sum(x for x in [1, 10, 100])=111
```
Even more generator comprehension:
```
g = (x for x in [1, 10, 100])
exp_g = (1.01**x for x in g)
print(f'{type(exp_g)=}')
print(f'{sum(exp_g)=}')
```
Output:
```
type(exp_g)=<class 'generator'>
sum(exp_g)=4.819435954832733
```
And more:
```py
exp_g = (1.01**x for x in gen_1_10_100())
print(f'{sum(exp_g)=}')

exp_g = (1.01**x for x in (10**i for i in range(3)))
print(f'{sum(exp_g)=}')
```
Output:
```
sum(exp_g)=4.819435954832733
sum(exp_g)=4.819435954832733
```
By the way, the range(3) object is similar to a generator, but is not one. Lists, tuples, generators and range ⏤ are iterable objects. That's why they're similar!
```py
print(f'{type(range(3))=}')
```
Output:
```
type(range(3))=<class 'range'>
```

Code in https://onlinegdb.com/uV9ygOawD

---


## Iterables ⏤ Part 1 (May 15)

From iterable objects, you can create an iterator, which allows iterating through the components of the object in a for loop.
Better to understand this with examples. Take a list: [1, 10, 100]. Since a list is iterable, an iterator can be created from it:
```py
it = iter([1, 10, 100])
```
An iterator is implicitly created and used in a for loop:
```py
for elem in [1, 10, 100]:
    print(elem)
```
Actually, you rarely have to work with iterators directly. 
Understanding which object is iterable can be useful, since the for loop works well with such objects ⏤ both as an operator, 
and in short form (list/tuple/generator comprehension).
One way to find out if an object is iterable ⏤ is to find out if it has the `__iter__` method. 
This method is used by the iterator. Check for the method using hasattr:
```py
print(f"{hasattr([1, 10, 100], '__iter__')=}")
```
Output:
```
hasattr([1, 10, 100], '__iter__')=True
```
Sometimes such a check will be insufficient: the method seems to exist, but its call ends in failure. Therefore, it's better to create an iterator explicitly and catch a possible failure:
```py
some_obj = [1, 10, 100]
try:
    iter(some_obj)
    print(f'{some_obj}: iterable')
except TypeError:
    print(f'{some_obj}: not iterable')
```
Output:
```
[1, 10, 100]: iterable
```
Now let's write a helper function print_iterable_or_not, which for each object from a given table will output useful information (object type, if the object is iterable, what elements are in the object):
```py
def print_iterable_or_not(tab):
    for obj in tab:
        print(f'object:   {obj}')
        print(f"type:     {type(eval(obj)).__name__}")

        try:
            iter(eval(obj))
            iterable = True
        except TypeError:
            iterable = False

        print(f"iterable: {iterable}")
        values = list(eval(obj)) if iterable else [eval(obj)]
        print(f'value(s): {", ".join(str(x).strip() for x in values)}')
        print(f'size:     {len(values)}')
        print()
```
Looks cumbersome, let's see how to use it. Create a table of different values: list, tuple, set, range and generator. All these are examples of iterable objects and they can be easily used in a for loop.
The print_iterable_or_not function should identify them all as iterable.
```py
print_iterable_or_not((
    '[0, 1, 2]',
    '(0, 1, 2)',
    '{0, 1, 2}',
    'range(3)',
    '(x for x in range(3))',
))
```
Output:
```
object:   [0, 1, 2]
type:     list
iterable: True
value(s): 0, 1, 2
size:     3

object:   (0, 1, 2)
type:     tuple
iterable: True
value(s): 0, 1, 2
size:     3

object:   {0, 1, 2}
type:     set
iterable: True
value(s): 0, 1, 2
size:     3

object:   range(3)
type:     range
iterable: True
value(s): 0, 1, 2
size:     3

object:   (x for x in range(3))
type:     generator
iterable: True
value(s): 0, 1, 2
size:     3
```
For each object from the table, the function output information about the type (list, tuple, set, range, generator), confirmed that they are all iterable (True), printed the elements of these objects (0, 1, 2) and size (3 elements).
Generators can be created by combining a function and yield. Another way ⏤ is to use generator comprehension. Let's check if any generators are iterable.
```py
def gen_1_10_100():
    yield 1
    yield 10
    yield 100

print_iterable_or_not((
    'gen_1_10_100()',
    '(x for x in [1, 10, 100])',
    '(x for x in gen_1_10_100())',
    '(10**i for i in range(3))',
))
```
Output:
```
object:   gen_1_10_100()
type:     generator
iterable: True
value(s): 1, 10, 100
size:     3

object:   (x for x in [1, 10, 100])
type:     generator
iterable: True
value(s): 1, 10, 100
size:     3

object:   (x for x in gen_1_10_100())
type:     generator
iterable: True
value(s): 1, 10, 100
size:     3

object:   (10**i for i in range(3))
type:     generator
iterable: True
value(s): 1, 10, 100
size:     3
```
So it turned out: all generators are iterable objects (they are also iterators by the way!).

Code: https://onlinegdb.com/hoEB0NXUG

---

## Iterables ⏤ Part 2 (May 15)

Going further: strings (str) and dictionaries (dict) ⏤ are iterable. A string iterates by letters, and a dictionary by its keys.
More interesting examples: generator classes and files. These types are also iterable!
```py
class Gen_1_10_100:
    def __iter__(self):
        yield 1
        yield 10
        yield 100

with open('hello.txt', 'w') as f:
    print('Hello', file=f)
    print('World', file=f)

print_iterable_or_not((
    '"hello"',
    '{0:"a", 1:"b", 2:"c"}',
    'Gen_1_10_100()',
    "open('hello.txt', 'r')",
))
```
Output:
```
object:   "hello"
type:     str
iterable: True
value(s): h, e, l, l, o
size:     5

object:   {0:"a", 1:"b", 2:"c"}
type:     dict
iterable: True
value(s): 0, 1, 2
size:     3

object:   Gen_1_10_100()
type:     Gen_1_10_100
iterable: True
value(s): 1, 10, 100
size:     3

object:   open('hello.txt', 'r')
type:     TextIOWrapper
iterable: True
value(s): Hello, World
size:     2
```
A string can be represented as a tuple of letters, accordingly iteration over a string ⏤ works the same as iteration over a tuple of letters.

Dictionaries contain associations between keys and values. By default, iteration over a dictionary iterates over keys. To iterate over values, you need to use the method: dict.values() or dict.items().

A generator class works approximately the same as a generator function, but can contain state. That is, it can generate different sequences of values.
A file opened for reading ⏤ is iterable, which means reading from a file can be done using a for loop.

Many standard functions/classes generate sequences, that is, they are iterable. In the itertools module you can find many functions that are iterable. A very useful module.

Many standard functions/classes generate sequences, that is, they are iterable. In the itertools module you can find many functions that are iterable. A very useful module.
```py
import itertools

print_iterable_or_not((
    'enumerate(["a", "b", "c"])',
    'reversed([0, 1, 2])',
    'zip(range(3), ["a","b","c"])',
    'itertools.product(range(3), repeat=2)',
    'itertools.permutations(range(3))',
))
```
The following two tables also contain iterable objects: empty containers and single elements.
```py
print_iterable_or_not((
    '[]',
    'tuple()',
    'set()',
    'range(0)',
    '(x for x in [])',
    '{}',
    '""',
))
```
```py
print_iterable_or_not((
    '[7]',
    '(7,)',
    '{7}',
    '(x for x in [7])',
    'range(7,8)',
    '{7:"abc"}',
    '"7"',
))
```
Code: https://onlinegdb.com/o6581Ooqw

---

## Iterables ⏤ Part 3 (May 15)

Time to show examples of objects that are not iterable. First of all, these are numbers (integers, real), boolean values (True, False), and of course None.

No surprises: you can't iterate over objects of types int, float, bool, NoneType in a for loop.
```py
print_iterable_or_not((
    '5',
    '5.5',
    'True',
    'None',
))
```
Output:
```
object:   5
type:     int
iterable: False
value(s): 5
size:     1

object:   5.5
type:     float
iterable: False
value(s): 5.5
size:     1

object:   True
type:     bool
iterable: False
value(s): True
size:     1

object:   None
type:     NoneType
iterable: False
value(s): None
size:     1
```
Functions, standard or defined by the programmer, as well as types, classes and modules are also not iterable.
```py
print_iterable_or_not((
    'len',
    'gen_1_10_100',
    'str',
    'Gen_1_10_100',
    'itertools',
))
```
Output:
```
object:   len
type:     builtin_function_or_method
iterable: False
value(s): <built-in function len>
size:     1

object:   gen_1_10_100
type:     function
iterable: False
value(s): <function gen_1_10_100 at 0x10ae35a60>
size:     1

object:   str
type:     type
iterable: False
value(s): <class 'str'>
size:     1

object:   Gen_1_10_100
type:     type
iterable: False
value(s): <class '__main__.Gen_1_10_100'>
size:     1

object:   itertools
type:     module
iterable: False
value(s): <module 'itertools' (built-in)>
size:     1
```

Code: https://onlinegdb.com/wq9VInL3Z

---

## Callables (Aug 18)

In Python, an object can be Callable, that is, it can be called like an ordinary function.

The standard callable function checks if a given object is "callable".

Obviously, any function, method, including built-in ones and lambda — are Callable.
Let's write a simple program and test different objects for this property.
```py
import operator
import typing
import functools
```
```py
def add(a: int, b: int) -> int: return a + b
```
```py
def mk_power_add(k: int) -> typing.Callable[[int, int], int]:
    def power_k_add(a: int, b: int): return a**k + b**k
    return power_k_add
```
The add function as well as the result of calling mk_power_add(1) — these are examples of functions that simply sum two arguments

That is, these are examples of Callable, so callable(add) and callable(mk_power_add(1)) will return True.

Also `callable(lambda a, b: a+b)` will also return True.

Further, we'll give examples of a static function (class function) and method:
```py
class A:
    @staticmethod
    def add(a: int, b: int) -> int: return a + b
```
```py
class Power:
    def __init__(self, k: int): self.k = k

    def add(self, a: int, b: int) -> int: return a**self.k + b**self.k
```
Both functions `A.add` and `Power(1).add` sum two arguments and are Callable.

In the following example, objects of two classes are Callable, 
since they implement a special hidden method `__call__`:

```py
class Add:
    def __init__(self):
        self.__name__ = f'{type(self).__name__}'

    def __call__(self, a: int, b: int) -> int: return a + b
```
```py
class MkPowerAdd:
    def __init__(self, k: int):
        self.k = k
        self.__name__ = f'{type(self).__name__}({self.k})'

    def __call__(self, a: int, b: int) -> int: return a**self.k + b**self.k
```

Calls `callable(Add())` and `callable(MkPowerAdd(1))` will return True.

In the following example, we take a function with three arguments, in which we fix one argument, we get a partial function with two arguments. Also Callable:
```py
def power_add(a: int, b: int, k: int): return a**k + b**k
```
Call `callable(functools.partial(power_add, k=1))` will return True.

Library functions `int.__add__`, operator.add — are also Callable.

Moving forward: for convenience, let's fix the power k=1 and define a table of objects to check for Callable:
```py
k = 1
```
```py
power1_add = functools.partial(power_add, k=k)
power1_add.__name__ = 'power1_add'
```
```py
tab = (
    int.__add__,
    operator.add,
    lambda a, b: a + b,
    add,
    mk_power_add(k),
    A.add,
    Power(1).add,
    MkPowerAdd(k),
    power1_add,
)
```
Each object is essentially an analog of the + operation. Let's execute a call on arguments a=12 and b=5 and check the result:
```py
a, b = 12, 5
```
```py
for func in tab:
    print(f'{callable(func)=}, {func.__name__}, {func(12, 5)=}')
```
We'll get a table:
```py
callable(func)=True, func=<lambda>, func(12, 5)=17
callable(func)=True, func=add, func(12, 5)=17
callable(func)=True, func=power_k_add, func(12, 5)=17
callable(func)=True, func=add, func(12, 5)=17
callable(func)=True, func=add, func(12, 5)=17
callable(func)=True, func=Add, func(12, 5)=17
callable(func)=True, func=MkPowerAdd(1), func(12, 5)=17
callable(func)=True, func=power1_add, func(12, 5)=17
```
The code is https://onlinegdb.com/TH9ry84dL

