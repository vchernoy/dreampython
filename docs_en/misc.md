# Misc

## Fascinating Symmetry with Turtle (Oct 17) 

What do you think the following algorithm will draw?

1. Draw an equilateral triangle.
2. Draw a point anywhere inside the triangle.
3. Draw the next point in the middle between the current point and a randomly chosen vertex of the triangle.
4. Repeat the last step (3) infinitely.

Gradually a fractal of nested triangles will be created.

Let's try to display this in Python. For graphics we'll use the fun turtle module (turtle).

This is the same Turtle that children learn programming with. 

The turtle can perform the following operations:

* `down`/`up`: lower or raise the tail
* `left`/`right`: turn left or right
* `forward`: jump forward
* `setpos`: jump to a certain position

The main thing is that if the turtle moves with its tail down, it leaves a trace (draws).

Let's start writing code.

Import the turtle and the random number module (random) — we need to choose a vertex randomly):

```py
import random, turtle

side = 600
vertexes = []
```

* `side` — length of the triangle side, and
* `vertexes` — list of coordinates of the three vertices of the triangle.

Set maximum speed, tail and fill color, and jump to the starting position:

```py
turtle.speed(0)
turtle.color('red', 'yellow')
turtle.up()
turtle.setpos(-side / 2, side / 2)
turtle.down()
```

Now let's draw the triangle, and remember all its vertices in the vertexes list:

```py
turtle.begin_fill()

for _ in range(3):
    turtle.forward(side)
    turtle.right(120)
    vertexes.append(turtle.pos())

turtle.end_fill()
```
Three times we do the following: jump forward (along the triangle side), turn 120 degrees (create an interior angle: 180 - 120 = 60), and remember the triangle vertex in vertexes.

* `begin_fill`/`end_fill` — allow filling the triangle with some color — this is optional, you can remove these calls.

Before entering the infinite loop, create three variables:

* `total_dots` — for counting drawn points (this is optional).
* `x`, `y` — position of the current point (we'll start with 0,0)

```py
total_dots = 0
x = y = 0
while True:
    v_x, v_y = vertexes[random.randint(0, 2)]
    x = (x + v_x) / 2
    y = (y + v_y) / 2
```

* `randint(0, 2)` generates a random integer from 0 to 2 (inclusive) — that is, randomly choose a vertex.

Next in the same loop, draw a point with diameter 3 in blue:

```py
    turtle.up()
    turtle.setpos(x, y)
    turtle.down()
    turtle.dot(3, 'blue')
```

Update the statistics of drawn points and output to console every thousand (this is optional to do).

```py
    total_dots += 1
    if total_dots % 1000 == 0:
        print(f'total dots drawn: {total_dots}')
```
That's it! Run from PyCharm and wait, 5 minutes, or maybe an hour.... By 10,000 points the picture turns out quite nice.

Meditation!

Code: https://onlinegdb.com/qrT12YxnT

---

## What's New in Python 3.10 (May 22)

To demonstrate some old and new features, let's write functions for working with arithmetic expressions represented as nested lists.

Examples:

* `[+, 10, 20, 30]` represents `(10 + 20 + 30)`, which equals: 60.
* `[*, 5, 10, [+, 10, 20]]`, which means: `(5 * 10 * (10 + 20))`, and this equals: 1500.

The first element of the list is the operation (`+`, `*`, you can also introduce: `min`, `max`, etc.), followed by operands to which this operation is applied. 
Moreover, each operand can also represent an arithmetic expression represented as a list.

Let's start with a class that defines allowed operators (`+`, `*`, `min`, `max`).

```py
class OP:
    def __init__(self, name: str, apply: Callable[[Iterable], Any]):
        self.name = name
        self.apply = apply

    def __repr__(self) -> str:
        return self.name
```

```py
class Ops:
    ADD = OP('+', sum)
    MUL = OP('*', 
             lambda values: functools.reduce(operator.mul, values, 1))
    MIN = OP('min', min)
    MAX = OP('max', max)
```

We could do without `OP`, `Ops`, and instead of `ADD`, `MUL`, `MIN`, `MAX`, use `'+'`, `'-'`, `'min'`, `'max'`. 
But our approach somewhat reduces the probability of making errors in expression descriptions.

As a working arithmetic expression, let's take the following:

```py
expr = [
    Ops.MUL,
    5,
    20,
    5,
    [Ops.ADD, 10, 20],
    [Ops.MIN, 5, 15, 25]
]
```

It represents: `(5 * 20 * 5 * (10 + 20) * min(5, 15, 25)`, which equals 75000.

Writing a function that calculates such expressions is not difficult:

```py
def calc(expr: Sequence|int|float) -> int|float:
    try:
        return expr[0].apply(
            calc(expr[i]) for i in range(1, len(expr))
        )
    except TypeError:
        return expr
```

Recall that `expr[0]` contains the operator (for example, `Ops.ADD`), if of course `expr` ⏤ is a `Sequence` (`list` is a `Sequence`).

The function performs calculations recursively ⏤ this is a natural approach, since expressions are also defined recursively.

For each operand, the function calls itself. 
If the operand turned out not to be a `Sequence` (but has a simple type: `int`, `float`), then an error is generated, which is handled in `try-except`. 
A simple operand is returned as is (`return expr`).

In Python 3.10, notation for type union was introduced: `int|float`, which means: `int` or `float`. 
In previous versions of Python, you would have to write: `Union[int, float]`.

Let's try to calculate the expression:

```py
print(f'{expr=}')
print(f'{calc(expr)=}')
```

Output:

```
expr=[*, 5, 20, 5, [+, 10, 20], [min, 5, 15, 25]]
calc(expr)=75000
```

Surprisingly, writing a function that converts such expressions to normal format is somewhat more complex:

```py
def to_str(expr: Sequence|int|float) -> str:
    try:
        op = expr[0]
        match op:
            case OP(name='+'|'*', apply=_):
                joiner = f' {op} '
                maybe_func = ''
            case _:
                joiner = ', '
                maybe_func = f'{op}'
        return f'{maybe_func}({joiner.join(to_str(expr[i]) for i in range(1, len(expr)))})'
    except TypeError:
        return str(expr)
```
The principle is the same: recursion iterates through operands. 
But here we use the new `match-case` construct (introduced in Python 3.10).

Note that `[+, 5, 10]` and `[min, 5, 10]` should be displayed completely differently: `(5 + 10)` versus `min(5, 10)`. 
Therefore case branches are used. 
In the end we reduce to calling `joiner.join(to_str(expr[i]) for i in range(1, len(expr)))`.

The `str.join()` call combines all operands, either through the operator (for example: `' + '`) or with commas (`', '`).

The `match-case` command ⏤ is an extended (more readable?) variant of the good old command: `if-elif-else`.

Since `to_str(expr)` ⏤ is a correct arithmetic expression, it can be calculated using the standard function: `eval()`. 
It's convenient to use this to check that `to_str` and `calc` ⏤ produce consistent results.

```py
print(f'{to_str(expr)=}')
print(f'{eval(to_str(expr))=}')
print(f'{calc(expr)==eval(to_str(expr))=}')
```

Output:

```
to_str(expr)='(5 * 20 * 5 * (10 + 20) * min(5, 15, 25))'
eval(to_str(expr))=75000
calc(expr)==eval(to_str(expr))=True
```

Code: [https://onlinegdb.com/Q9M1jLNIo]

