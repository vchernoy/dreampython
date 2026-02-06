# Recursion. Dynamic Programming. Memoization

## When You Finally Learned Recursion in Python

What do all these functions do?
```py
def N(n):
    return N(n-1) + 1 if n > 0 else N(n+1) - 1 if n < 0 else 0
```
```py
def X(n):
    return X(n-1) + 'x' if n > 0 else ''
```
```py
def S(n):
    return S(n-1) + n if n > 0 else 0
```
```py
def LN(s):
    return LN(s[1:]) + 1 if s else 0
```
```py
def SM(values):
    return values[0] + SM(values[1:]) if values else 0
```
```py
def FC(n):
    return n * FC(n-1) if n > 0 else 1
```
```py
def PR(values):
    return values[0] * PR(values[1:]) if values else 1
```
```py
def MN(values):
    return min(values[0], MN(values[1:])) if len(values) > 1 else values[0]
```
```py
def PW(x, n):
    return x * PW(x, n-1) if n > 0 else 1 / PW(x, -n) if n < 0 else 1
```
```py
def AN(values):
    return bool(values) and (values[0] or AN(values[1:]))
```
```py
def INC(values):
    return [values[0]+1, *INC(values[1:])] if values else []
```
```py
def JN(words):
    return words[0] + ',' + JN(words[1:]) if len(words) > 1 else words[0]
```

When you learned tail recursion

Compare these variants with the similar ones above.
```py
def SM(values, acc=0):
    return acc if not values else SM(values[1:], acc+values[0])
```
```py
def FC(n, acc=1):
    return acc if n <= 1 else FC(n-1, acc=acc*n)
```
```py
def AN(values, acc=False):
    return acc if acc or not values else AN(values[1:], acc=bool(values[0]))
```
```py
def JN(words, acc=''):
    return acc if not words else JN(words[1:], acc=(f'{acc},' if acc else '') + words[0])
```

Tail recursion ⏤ is a type of recursion where the recursive call occurs as the very last command. Tail recursion is good because it can easily be converted to a simple loop. Some types of non-tail recursions can easily be converted to tail recursions.

There are also indirect recursions, when a function calls another, and that one calls the first (the call chain can be longer).

What are the Time and Space Complexities for each of these functions?

---

## LeetCode/Medium 77. Combinations

Recursion, dynamic programming, memoization, generators, Newton's binomial.

https://leetcode.com/problems/combinations/description/

> Given two integers n and k, return all possible combinations of k numbers chosen from the range `[1, n]`.
> 
> You may return the answer in any order.
> ```
> Input: n = 4, k = 2
> Output: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
> 
> Input: n = 4, k = 3
> Output: [[1,2,3], [1,2,4], [1,3,4], [2,3,4]]
> ```

The number of combinations is easily calculated via Binomial Coefficient: n! / (k! * (n-k)!).

How to see and use recursion?

Consider the first example: n = 4, k = 2.

Let's break down the expected answer:
```
[[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
```
Into two parts:
```
[[1,2], [1,3], [2,3]]
[[1,4], [2,4], [3,4]]
```
The first group ⏤ is all combinations of 2 numbers composed from `[1,2,3]`. That is, we reduce this case to the subproblem `n=3,k=2`.

Note that in the second group, all combinations contain a common element (4). So the second group can be obtained by attaching 4 to each combination from: `[[1], [2], [3]]`.

`[[1], [2], [3]]` ⏤ is all combinations of size 1, composed from `[1,2,3]`. That is, we arrive at the subproblem `n=3,k=1`.

Suppose the function `gen(n, k)`, which we need to write, can generate all combinations for parameters `(n, k)`. Approximate plan of action:

Generate all combinations, each consists of k numbers from the range 1 to n-1, that is, call `gen(n, k-1)`.

Generate all combinations, each consists of k-1 numbers from the range 1 to n-1 (`gen(n-1,k-1)`), but to each combination we "add" the number n.

The union of all combinations obtained in the previous two steps ⏤ this will be the answer for `gen(n, k)`.

```py
from functools import cache

def combine(n: int, k: int) -> list[list[int]]:
    @cache 
    def gen(n: int, k: int):
        if n < 0:
            return []
        if k == 0:
            return [[]]

        res = gen(n-1, k)            
        for t in gen(n-1, k-1):
            res.append([*t, n])
            
        return res

    return gen(n, k)
```
Since the function `gen` calls itself (recursively), we must handle edge cases: `k=0` or `n < 0`.

`[*t, n]` ⏤ unpacks the combination of k-1 numbers and adds the k-th number. For example, if `t=[1,2]` and `n=5`, then `[*t, n]` will create `[1,2,5]`.

`functools.cache` remembers the result of the function for each call, so as not to do repeated calculations for the same parameters. This is called Memoization.

In the next version, we make the following changes: handle other edge cases (for variety), use `tuple` instead of `list` for combinations, and most importantly: apply list comprehension.

```py
from functools import cache

def combine(n: int, k: int) -> list[list[int]]:
    @cache
    def gen(n: int, k: int):
        if k == 0 or n == k:
            return [tuple(range(1, k+1))]

        return gen(n-1, k) + [(*t, n) for t in gen(n-1, k-1)]

    return gen(n, k)
```
The function gen can be shortened to one, but long command:
```py
from functools import cache

def combine(n: int, k: int) -> list[list[int]]:
    @cache
    def gen(n: int, k: int):
        return gen(n-1, k) + [(*t, n) for t in gen(n-1, k-1)] if k not in (0, n) else [tuple(range(1, k+1))]
    return gen(n, k)
```

We can switch to lazy evaluation, the simplest way ⏤ is to use generators. 
But in this case, `@cache` should be removed. 
With a generator, Memoization won't work correctly (why?).

```py
def combine(n: int, k: int):
    def gen(n: int, k: int):
        if k == 0 or n == k:
            yield tuple(range(1, k+1))
            return

        for t in gen(n-1, k):
            yield t

        for t in gen(n-1, k-1):
            yield *t, n

    return list(gen(n, k))
```

Two for loops can be combined into one. Let's use the itertools.chain function, which concatenates several iterables into one:
```py
from itertools import chain

def combine(n: int, k: int):
    def gen(n: int, k: int):
        if k == 0 or n == k:
            yield tuple(range(1, k+1))
            return            

        for t in chain(gen(n-1, k), ((*t, n) for t in gen(n-1, k-1))):
            yield t
    return list(gen(n, k))
```

Use generator-expression. Now `gen` ⏤ is not a generator, but an ordinary function that returns a generator:

```py
from itertools import chain

def combine(n: int, k: int):
    def gen(n: int, k: int):
        if k == 0 or n == k:
            return (tuple(range(1, k+1)),)

        return chain(gen(n-1, k), ((*t, n) for t in gen(n-1, k-1)))
    return list(gen(n, k))
```
We can put everything in one line (what will we get?).

Actually, the standard library has the itertools.combinations function, which solves the given problem. We get a very simple solution:
```py
from itertools import combinations

def combine(n: int, k: int) -> list[tuple[int]]:
    return list(combinations(range(1, n+1), k))
```

---

## LeetCode/Hard 115. Distinct Subsequences

https://leetcode.com/problems/distinct-subsequences/

> Given two strings s and t, return the number of distinct subsequences of s which equals t.
> ```
> Input: s = "rabbbit", t = "rabbit"
> Output: 3
> ```

Three ways to get `rabbit` from `rabbbit`:

* **rabb**b**it**
* **rab**b**bit**
* **ra**b**bbit**

In other words, we remove some letters from s to get t. Our goal: count the number of ways to create s from t (by crossing out letters from s).
```
Input: s = "babgbag", t = "bag"
Output: 5
```
Five ways to get `bag` from `babgbag`:

* **ba**b**g**bag
* **ba**bgba**g**
* **b**abgb**ag**
* ba**b**gb**ag**
* babg**bag**

Consider the last example. Divide the answer into two groups:

Group #1 includes solutions where the first letter b is included in the solution.

* **ba**b**g**bag
* **ba**bgba**g**
* **b**abgb**ag**

Group #2 includes solutions where the first letter b is skipped.

* ba**b**gb**ag**
* babg**bag**

Actually, we split the problem into two subproblems.

Let `f(s, t)` ⏤ denote the number of solutions for the problem `(s, t)`. That is, `f(s, t)` should count all ways to get t from s.
Now let's count the number of solutions in each group separately.

* `f(s[1:], t[1:])` ⏤ we remove one letter from s and t, and solve the problem for the resulting strings. This will be the answer for group #1.
* `f(s[1:], t)` ⏤ we skip the first letter only in s. And this is the answer for group #2.

The sum of the two solutions gives the answer for `f(s, t)`. But we need to remember that group #1 can be reduced to the subproblem (`s[1:], t[1:]`) only if the first characters of both strings are equal.

```py
from functools import cache
from collections import Counter

def num_distinct(s: str, t: str) -> int:
    @cache 
    def f(s: str, t: str) -> int:
        if not t:
            return 1
        if len(s) < len(t):
            return 0
        r = f(s[1:], t)
        if s[0] == t[0]:
            r += f(s[1:], t[1:])
        return r

    return f(s, t) if Counter(s) >= Counter(t) else 0
```

* As in other examples, the inner function is based on recursion, which we described above.
* We must handle edge cases: if t is empty, then the answer is 1, and if t is longer than s, then the answer is 0.
* We remember (cache) computation results using the decorator: functools.cache (Memoization).
* Before starting recursion, we check if s contains all letters of t, otherwise immediately answer 0. For this purpose, multi-set works perfectly: `itertools.Counter`.

Can we do it in one line?

Of course, just a long one:

```py
from functools import cache
from collections import Counter

def num_distinct(s: str, t: str) -> int:
    @cache
    def f(s: str, t: str) -> int:
        return 1 if not t else \
            0 if len(s) < len(t) else \
                f(s[1:], t) + (s[0] == t[0] and f(s[1:], t[1:]))

    return f(s, t) if Counter(s) >= Counter(t) else 0
```
We used the short form if (or if-expression): `value1 if condition else value2`.

But applied it twice: `value1 if conditionA else value2 if conditionB else value3`.

Also used such a tricky notation: `x + (ok and y)`, which means `(x + y) if ok else x`.

Note that previous solutions at each step (call) skip one or two letters.

And thanks to Memoization, repeated calculations don't occur.

Therefore, the number of different calls is proportional to the number of combinations of all suffixes of s and t, that is O((len(s) + len(t))²).

But each call spends О(len(s) + len(t)) for removing the first letter. That is, we get a cubic algorithm.

Working with substrings can be eliminated, because to skip a character, it's not necessary to use slicing `[1:]`.

```py
from functools import cache
from collections import Counter

def num_distinct(s: str, t: str) -> int:
    @cache
    def f(i: int, j: int) -> int:
        return 1 if j == len(t) else \
            0 if len(s)-i < len(t)-j else \
                f(i+1, j) + (s[i] == t[j] and f(i+1, j+1))

    return f(0, 0) if Counter(s) >= Counter(t) else 0
```

Instead of s and t, we use indices i, j, each of which points to the beginning of the considered substring. This solution has quadratic Time Complexity.

It also becomes obvious that instead of Memoization, we can use Dynamic Programming, that is, instead of recursion, fill a table `len(s)`x`len(t)` with simple nested loops.

```py
from collections import Counter

def num_distinct(s: str, t: str) -> int:
    if Counter(s) < Counter(t):
        return 0

    F = [[0] * len(t) + [1] for _ in range(len(s)+1)]

    for i in range(len(s)-1, -1, -1):
        for j in range(len(t)-1, max(len(t)-len(s)+i, 0)-1, -1):
            F[i][j] = F[i+1][j] + (s[i] == t[j] and F[i+1][j+1])

    return F[0][0]
```

I think this is not a Hard level problem, but rather a solid Medium. Maybe next time I'll show a similar Medium level problem that is clearly harder than this task (and definitely deserves Hard).

---

## LeetCode/Medium 97. Interleaving String

https://leetcode.com/problems/interleaving-string/

> Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
> 
> Input:
> 
> * s1 = "aabcc",
> * s2 = "dbbca",
> * s3 = "aadbbcbcac"
>
> Output: True
> 
> Let's divide s1 and s2 into three and two parts respectively:
>
> * s1 = "aa" + "bc" + "c",
> * s2 = "dbbc" + "a".

Then we can get s3 like this:

* s3 = "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".

Input:
* s1 = "aabcc",
* s2 = "dbbca",
* s3 = "aadbbbaccc"

Output: False

Input:
* s1 = "",
* s2 = "",
* s3 = ""

Output: True

In other words, we need to divide s1 and s2 into pieces and, without changing the order, merge everything into one string to get s3. In case of success, return True. Counting all possible combinations is not required, it's enough to determine if a successful partition is possible.

Obviously, s3 should have a length equal to the sum of the lengths of s1 and s2. Moreover, s3 should consist of the same set of letters as s1 + s2. This can be easily implemented:

```py
    if Counter(s1) + Counter(s2) != Counter(s3):
        return False
```

It's also easy to notice that if s2 ⏤ is an empty string, then it's enough to compare for equality s1 == s3 ⏤ this will be needed in recursion.

Let the function f(s1, s2, s3) solve the given problem, that is, find a partition of s1 and s2 so that by joining all pieces, we get the string s3. But we require that in merging the partition pieces, the first piece must be chosen as a prefix of string s1.

If such a function were given, then the answer to the problem could be written like this:

```py
from functools import cache
from collections import Counter

def is_interleave(s1: str, s2: str, s3: str) -> bool:
    @cache
    def f(s1: str, s2: str, s3: str) -> bool:
        ...

    if Counter(s1) + Counter(s2) != Counter(s3):
        return False
    return f(s1, s2, s3) or f(s2, s1, s3)
```

We cut a prefix from s1, starting from length 1, iterate through all possible options until we find a prefix common to both s1 and s2. This can be written like this:

```py
        for i in range(min(len(s1), len(s3))):
            if s1[i] != s3[i]:
                return False
            ...
```

In case s1 and s2 have a common prefix of length i+1, we cut this prefix and check if for the new strings s1[i+1:], s2, s3[i+1:] we can find a partition:

```py
            if f(s2, s1[i+1:], s3[i+1:]):
                return True
```

Tricky recursion: the function f(s1, s2, s3) calls f(s2, s1[i+1:], s3[i+1:]). Parameters swapped places and this is not an error. Since f(s1, s2, s3) must take a prefix from string s1 (that is, from its first parameter), then f(s2, s1[i+1:], s3[i+1:]) will take a prefix from s2 (so we pass it as the first parameter).

Full code:

```py
from functools import cache
from collections import Counter

def is_interleave(s1: str, s2: str, s3: str) -> bool:
    @cache
    def f(s1: str, s2: str, s3: str) -> bool:
        if not s2:
            return s1 == s3
        for i in range(min(len(s1), len(s3))):
            if s1[i] != s3[i]:
                return False
            if f(s2, s1[i+1:], s3[i+1:]):
                return True
        return False

    if Counter(s1) + Counter(s2) != Counter(s3):
        return False
    return f(s1, s2, s3) or f(s2, s1, s3)
```

The parameters `s1`, `s2`, `s3` of function f shadow the parameters of function `is_interleave`. If, for convenience, we denote by `s1'`, `s2'`, `s3'` ⏤ the original parameters, then we can make the following statements:

* `s1` ⏤ is a suffix of `s1'`, similarly for `s2`, `s3`.
* `len(s3) == len(s1) + len(s2)`
* `s3 == s3'[-len(s1) - len(s2):]`
* `f(s1'[:len(s1)], s2'[:len(s2)], s3'[:len(s3)]) == True`

In other words, `s3` can be removed from the parameters of function f, and calculate it when needed:

```py
from functools import cache
from collections import Counter

def is_interleave(s1: str, s2: str, s3: str) -> bool:
    @cache
    def f(s1: str, s2: str) -> bool:
        if not s2:
            return s1 == s3[-len(s1):]
        for i in range(len(s1)):
            if s1[i] != s3[len(s3)-len(s1)-len(s2) + i]:
                return False
            if f(s2, s1[i+1:]):
                return True
        return False

    if Counter(s1) + Counter(s2) != Counter(s3):
        return False
    return f(s1, s2) or f(s2, s1)
```

This variant is more confusing, but makes it clear that exactly two parameters are important for recursion. This fact is important for analyzing Time & Space Complexities, as well as for further optimizations: switching to indices and Dynamic Programming. We'll skip these topics here.

The function f can be written in one, very long line, we'll have to format it (break into parts):

```py
from functools import cache
from collections import Counter
from itertools import takewhile

def is_interleave(s1: str, s2: str, s3: str) -> bool:
    @cache
    def f(s1: str, s2: str, s3: str) -> bool:
        if not s2:
            return s1 == s3
        return any(
            f(s2, s1[i+1:], s3[i+1:]) 
            for i in takewhile(
                lambda i: s1[i] == s3[i], 
                range(len(s1))
            )
        )

    return Counter(s1 + s2) == Counter(s3) and (f(s1, s2, s3) or f(s2, s1, s3))
```

The `itertools.takewhile` function iterates through iterables (in this case: indices i from `range(len(s1)))` as long as `s1[i] == s3[i]` holds). Then there's a generator expression that for each such index, calls `f(s2, s1[i+1:], s3[i+1:])`. The `any` function will stop and return True as soon as it gets the first True (recursive call).

Obviously, `if not s2` and `return` can also be combined into one command.

As I think, this problem has Hard complexity, at least, this problem is harder than 115 (Distinct Subsequences).


**LeetCode: two Medium level recursion problems in one line (counting and generating binary trees)**

---

## LeetCode/Medium 96. Unique Binary Search Trees

https://leetcode.com/problems/unique-binary-search-trees/

> Given an integer n, return the number of structurally unique BST's (binary search trees) with exactly n nodes of unique values from 1 to n.

We need to count the number of binary trees with n nodes.
* For n: 0 ⏤ answer: 1 (empty tree).
* For n: 1 ⏤ answer: 1 (one tree with one node).
* For n: 2 ⏤ answer: 2 (two symmetric trees).
* For n: 3 ⏤ answer: 5.

Let f(n) denote the number of trees with n nodes.

If the left subtree contains l nodes (0 ≤ l ≤ n-1), then the right subtree must contain n - l - 1 nodes.

Since in such a configuration:
* the number of all possible left subtrees: f(l),
* and the number of possible right subtrees: f(n - l - 1).
* then the number of trees of size n will be: f(l) * f(n - l - 1).

We iterate through all possible l, we get the recurrence relation:
* f(n) = sum(f(l) * f(n - l - 1))
* f(0) = 1

Write code, for convenience define the recursive function f internally:
```py
from functools import cache

def num_trees(n: int) -> int:
    @cache
    def f(n: int) -> int:
        if n == 0:
            return 1
        return sum(f(l) * f(n - l - 1) for l in range(n))

    return f(n)
```

Solution in one line!

Interesting fact, f(n) are Catalan numbers, which can be calculated as:

* C(n) = 2*(2*n-1)/(n+1) * C(n-1)
* C(0) = 1

Or in Python:
```py
def num_trees(n: int) -> int:
    def f(n: int) -> int:
        c = 1
        for i in range(1, n):
            c = 2 * (2*i + 1) * c // (i + 2)
        return c

    return f(n)
```
We can also write this function in one line:
```py
from functools import reduce

def num_trees(n: int) -> int:
    def f(n: int) -> int:
        return reduce(
            lambda c, i: 2 * (2*i + 1) * c // (i + 2), 
            range(1, n), 
            1
        )

    return f(n)
```
Catalan numbers can be expressed via binomial coefficients:
* C(n) = Binom(2*n, n) / (n+1)

Which can be obtained using the function: math.comb. We get the simplest and shortest solution:

```py
from math import comb

def num_trees(n: int) -> int:
    def f(n: int) -> int:
        return comb(2*n, n) // (n+1)

    return f(n)
```
---

## LeetCode/Medium 95. Unique Binary Search Trees II

https://leetcode.com/problems/unique-binary-search-trees-ii/

> Given an integer n, return all the structurally unique BST's (binary search trees), which have exactly n nodes of unique values from 1 to n. 
> Return the answer in any order.

This problem is a continuation of the previous one. Now our goal is to generate all binary trees of size n.

In the problem condition, BSTs are defined as follows:

```py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Let the function `f(beg, end)` be able to generate all BSTs whose node values are from `[beg..end]`.

Suppose the root of the tree contains value `val` (`beg ≤ val ≤ end`).

* Then all left trees left we generate by calling `f(beg, val-1)`,
* and all right trees right we create using `f(val+1, end)`.

Then for each `val`, `left`, `right` defined above, we can create a correct and unique tree:

* `TreeNode(val=val, left=left, right=right)`

We collect all variants in a list trees, which will be the result of f(beg, end):

```py
from functools import cache

def generate_trees(n: int) -> list[TreeNode|None]:
    @cache
    def f(beg: int, end: int) -> list[TreeNode|None]:
        if end - beg <= -1:
            return [None]

        trees = []
        for val in range(beg, end + 1):
            for left in f(beg, val-1):
                for right in f(val+1, end):
                    trees.append(
                        TreeNode(val=val, left=left, right=right)
                    )
        return trees

    return f(1, n)
```

The function f can be written in one line using list comprehension:

```py
from functools import cache

def generate_trees(n: int) -> list[TreeNode|None]:
    @cache
    def f(beg: int, end: int) -> list[TreeNode|None]:
        if end - beg <= -1:
            return [None]

        return [
            TreeNode(val, left, right)
            for val in range(beg, end + 1)
            for left in f(beg, val-1)
            for right in f(val+1, end)
        ]
    return f(1, n)
```

Using itertools.product we can replace two loops with one:

```py
from functools import cache
from itertools import product

def generate_trees(n: int) -> list[TreeNode|None]:
    @cache
    def f(beg: int, end: int) -> list[TreeNode|None]:
        if end - beg <= -1:
            return [None]

        return [
            TreeNode(val, left, right)
            for val in range(beg, end + 1)
            for left, right in product(f(beg, val-1), f(val+1, end))
        ]
    return f(1, n)
```
Obviously, the size of the list of all trees should be equal to the number of trees, that is, the two problems should have consistent results for the same value n:

* `len(generate_trees(n)) == num_trees(n)`

