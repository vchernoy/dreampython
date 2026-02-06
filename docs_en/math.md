# Math

## Basics of Time/Space Complexity

EXAMPLE 1

The function takes a list of numbers and squares each one.
```py
def apply_square(nums: list[float]) -> None:
    for i in range(len(nums)):
        nums[i] = nums[i]**2
```
Note that the function returns nothing, but simply changes its argument, that is, the function has a side-effect, and it is not a pure-function.

How long will the function run, and how much additional memory does it use for its work?

It's quite difficult to calculate directly in seconds and bytes, but usually this is not required.

The answer needs to be given in terms of dependence on the size of input parameters, using asymptotic notation.

This function takes a list, say of size n (=len(nums)) and contains a loop that will execute n iterations.

Each iteration involves a group of elementary operations, the number and execution time of which (almost) does not depend on the size of the input data.

We conclude that the loop execution time (and the function itself) is proportional to n (or proportional to input size).

This is written as:

* Time Complexity: $\mathcal{O}(n)$,
* where $n$ is the input size

$\mathcal{O}$ (or big-$\mathcal{O}$) ⏤ is a form of asymptotic notation.

For example, if
* $f(n) = 5 \cdot n + 1000$

We can write:
* $f(n) = \mathcal{O}(n)$

That is, $f(n)$, as $n$ grows, grows no faster than linearly with $n$.
* $g(n) = 10$

We can write:
* $g(n) = \mathcal{O}(n)$

Although obviously $g(n)$ ⏤ is a constant function, and doesn't grow at all.

That is, $\mathcal{O}(n)$ ⏤ is some upper bound on the growth rate.

More precisely we could write:
* $g(n) = \mathcal{O}(1)$

That is, $g(n)$ grows approximately like an ordinary (any!) constant.

Besides $\mathcal{O}()$ other notations are also used, for example: $\mathcal{\Omega}()$, $\mathcal{\Theta}()$, $\mathcal{o}()$ ⏤ we'll talk about them some other time.

What about memory?

The function (almost) doesn't use additional memory.

Even if $n$ (list size) is huge, the requests for additional memory (besides input) for this function won't grow.

So we have:
* Space Complexity: $\mathcal{O}(1)$

EXAMPLE 2
```py
def squares_of1(nums: list[float]) -> list[float]:
    squares = []
    for num in nums:
        squares.append(num**2)
    return squares
```

This is a pure-function, no side-effects.

The function creates a new list that contains the squares of the received list.

Due to additional memory, space complexity is proportional to the size of nums.

* Time Complexity: $\mathcal{O}(n)$,
* Space Complexity: $\mathcal{O}(n)$,
* where $n$ is len(nums)

Execution time is $\mathcal{O}(n)$ since append execution time almost doesn't depend on the length of the list to which a new element is added.

More precisely: sometimes append works very long ($\mathcal{O}(n)$), but in most cases quickly ($\mathcal{O}(1)$).

On average, for n operations, we get that append works $\mathcal{O}(1)$.

A more precise phrase: amortized averaged time is $\mathcal{O}(1)$.

We can say the following:

Time and Space Complexity is proportional to the input size.

The algorithm runs in linear time and space.

EXAMPLE 3:
```py
def squares_of2(nums: list[float]) -> list[float]:
    squares = []
    for num in nums:
        squares = squares + [num**2]
    return squares
```

The function uses list concatenation instead of append.

And this significantly slows down the loop, because list-concatenation always works proportionally to the size of the concatenated lists.

On each iteration, the list (and time) gradually grows to $\mathcal{O}(n)$.

Number of iterations $n$, multiply by $\mathcal{O}(n)$, and we get: $\mathcal{O}(n^2)$.

* Time Complexity: $\mathcal{O}(n^2)$.
* Space Complexity: $\mathcal{O}(n)$.
* The algorithm runs in polynomial time and space.

The function requires a lot of memory, constantly creating an ever longer list.

That is, the total memory request size will also be $\mathcal{O}(n^2)$.

But since temporary lists are not used in future iterations, the runtime system will delete them.

Therefore, strictly speaking, Space Complexity: $\mathcal{O}(n)$.

Note that if instead of:
```py
        squares = squares + [num**2]
```
we use
```py
        squares += [num**2]
```
or
```py
        squares.extend(num**2)
```
then the execution time would be the same as for append (in example 2).

EXAMPLE 4

The same as example 2, but using List Comprehension.
```py
def squares_of3(nums: list[float]) -> list[float]:
    return [num**2 for num in nums]
```
This fundamentally doesn't change the algorithm's behavior:
* Time Complexity: $\mathcal{O}(n)$
* Space Complexity: $\mathcal{O}(n)$

The algorithm runs in linear time and space.

EXAMPLE 5:
```py
def squares_of4(nums: list[float]) -> list[float]:
    squares = []
    for num in nums:
        squares.append(num)

    for i in range(len(nums)):
        squares[i] = squares[i]**2

    return squares
```    
The first loop copies all elements into a new list.

The second loop squares them.
* Time Complexity: $\mathcal{O}(n) + \mathcal{O}(n) = \mathcal{O}(n)$
* Space Complexity: $\mathcal{O}(n)$

As we can see, although practically the function changed, it will likely be less efficient, but from an asymptotic point of view nothing changed.

The algorithm runs in linear time and space.

EXAMPLE 6
```py
def squares_of5(nums: list[float]) -> list[float]:
    squares = nums[:]
    apply_square(squares)
    return squares
```
Also first we copy the list (but without a loop), and then call the apply_square function (from example 1).

The result is the same, each of these operations takes $\mathcal{O}(n)$.

* Time Complexity: $\mathcal{O}(n) + \mathcal{O}(n) = \mathcal{O}(n)$
* Space Complexity: $\mathcal{O}(n)$
* The algorithm runs in linear time and space.

---

## A Bit of Algebra

### $\mathcal{O}(1)$
* $1000 = \mathcal{O}(1)$
* $1000 \cdot \mathcal{O}(1) = \mathcal{O}(1)$
* $\mathcal{O}(1) \cdot \mathcal{O}(1) = \mathcal{O}(1)$
* $1000 / n = \mathcal{O}(1)$
* $\mathcal{O}(n) / n = \mathcal{O}(1)$

### $\mathcal{O}(n)$
* $\mathcal{O}(n) + \mathcal{O}(n) = \mathcal{O}(n)$
* $1000 \cdot \mathcal{O}(n) = \mathcal{O}(n)$
* $\mathcal{O}(1000 \cdot n) = \mathcal{O}(n)$
* $\mathcal{O}(1) \cdot \mathcal{O}(n) = \mathcal{O}(n)$
* $\mathcal{O}(n) + \mathcal{O}(1) = \mathcal{O}(n)$
* $n \cdot \mathcal{O}(1) = \mathcal{O}(n)$
* $1000 \cdot n + 1000 \cdot \mathcal{O}(n) + 1000 \cdot n \cdot \mathcal{O}(1) = \mathcal{O}(n)$

### $\mathcal{O}(n^2)$
* $100  \cdot  n^2 + 100 \cdot n + 1000 = \mathcal{O}(n^2)$
* $n \cdot \mathcal{O}(n) + n^2  \cdot \mathcal{O}(1) = \mathcal{O}(n^2)$
* $\mathcal{O}(n) \cdot \mathcal{O}(n) = \mathcal{O}(n^2)$
* $1000 \cdot n^2 = \mathcal{O}(n^2)$ 

### $\mathcal{O}(n^3)$
* $n^2 \cdot \mathcal{O}(n) = \mathcal{O}(n^3)$
* $\mathcal{O}(n) \cdot \mathcal{O}(n) \cdot \mathcal{O}(n) = \mathcal{O}(n^3)$
* $4\cdot n^3 + 1000 \cdot n^2 + 10^30 = \mathcal{O}(n^3)$

