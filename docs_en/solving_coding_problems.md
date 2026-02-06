# Solving Coding Problems

## Filtering a List of Lists (May 25)

Suppose we have a list of lists. Our goal is to keep only unique lists. By uniqueness of two lists, we mean that they consist of the same elements (order doesn't matter).

How to do this?

Example, given a list of lists of numbers.
```py
store = [
    [7, 2],
    [2, 7],
    [6, 2, 1],
    [1, 1, 7],
    [1, 2, 6],
    [1, 6, 2],
    [2, 2, 1, 3],
    [1, 2, 2, 3],
]
```
After filtering, we get only "unique lists":
```py
unique = [
    [2, 7],
    [1, 2, 6],
    [1, 1, 7],
    [1, 2, 2, 3],
]
```
Why?

Because according to our conditions:

* `[7, 2]` and `[2, 7]` ⏤ are not unique (consist of the same elements, but in different order).
* `[6, 2, 1]`, `[1, 2, 6]`, `[1, 6, 2]` ⏤ are not unique.
* `[1, 2, 2, 3]` and `[1, 2, 3, 2]` ⏤ are not unique.

How to keep only unique elements?

A list doesn't necessarily contain unique elements, but a set guarantees uniqueness.

But a set can only store hashable elements, that is, for example tuples, but not lists.

And the elements of our list ⏤ are also lists!

So the first step: convert all inner lists to tuples:
```py
set_of_values = set(tuple(values) for values in store)
```
This won't be enough, because such a set will remove unique elements only if they are equal, for example: [2,7] and [2,7]. But will consider lists unique: [7,2] and [2,7].

Solution: we can first sort these lists, and then convert to tuple. We get:
```py
unique_as_set = set(tuple(sorted(values)) for values in store)
```
We use set comprehension: the set is formed from elements: tuple(sorted(values)).

We can do the same thing through a regular loop:
```py
unique_as_set = set()
for values in store:
    unique_as_set.add(tuple(sorted(values)))
```
Moving forward, we've achieved our goal, now we have only unique lists (well, tuples). But what if we want to convert to the original format, that is, instead of set of tuples get list of lists?

Now we use list comprehension:
```py
unique = [list(values) for values in unique_as_set]
``` 
That is, we form a list from elements: list(values). Can use a regular loop:
```py
unique = []
for values in unique_as_set:
    unique.append(list(values))
```
We can do everything in one step:
```py
unique = [list(values) for values in set(tuple(sorted(values)) for values in store)]
```
We can print everything:
```py
print(f'{store=}')
print(f'{unique_as_set=}')
print(f'{unique=}')
```
Bonus: What if the goal is to count all unique lists?

Then instead of set we use Counter and throw sorted tuples into it:
```py
from collections import Counter

counted_values = Counter(tuple(sorted(b)) for b in values)

print(f'{counted_values=}')
```

Code: https://onlinegdb.com/o_MRBjNxP

---

## Ranking a List of Words (June 5)

Given a list of words, we need to find the position of each word after sorting the list (ignoring letter case).

Solution:

As an example, we take words from Linus Torvalds' quote:
```py
words = ['Talk', 'is', 'cheap', 'Show', 'me', 'the', 'code', 'by', 'Linus', 'Torvalds']
```
Construct an array of sorted indices:
```py
indexes = list(range(len(words)))

indexes.sort(key=lambda i: words[i].lower())
```
indexes[0] contains the index of the word that, after sorting, should be at position 0.

In general: after sorting words, at position r will be the word words[indexes[r]].

The key parameter in the sort function determines the key/property according to which sorting is performed.

Create a dictionary ranks, which by index i will give the rank (position) of word words[i]:
```py
ranks = {}
for r, i in enumerate(indexes):
    ranks[i] = r
```
And now construct a list of pairs: word and its position in the sorted list.
```py
ranked_words = []
for i, w in enumerate(words):
    ranked_words.append((w, ranks[i]))

print(ranked_words)
```

Seems simple. We can reduce the number of lines using different list/dict comprehensions. And as an exercise, let's try to fit all the code in one line (this is for those who make it to the end!).

### Applying List & Dict Comprehension vs. Map

The indexes list, as well as the ranks dictionary and ranked_words list can each be constructed in one line:
```py
indexes = sorted(range(len(words)), key=lambda i: words[i].lower())

ranks = {i: r for r, i in enumerate(indexes)}

ranked_words = [(w, ranks[i]) for i, w in enumerate(words)]
```
We can combine the first two lines, but we'll get something clumsy.

Better to practice writing alternative solutions. The rank dictionary can be created in these ways:
```py
ranks = dict(zip(indexes, range(len(words))))
```
```py
ranks = dict(map(reversed, enumerate(indexes)))
```

And the resulting ranked_words list, in these ways:
```py
ranked_words = list(zip(words, (ranks[i] for i in range(len(words)))))
```
```py
ranked_words = list(zip(words, map(ranks.get, range(len(words)))))
```
```py
ranked_words = [(words[i], ranks[i]) for i in range(len(words))]
```
We can, of course, get rid of indices:
```py
indexes = sorted(range(len(words)), key=lambda i: words[i].lower())

ranks = dict(map(reversed, enumerate(indexes)))

ranked_words = list(zip(words, map(ranks.get, range(len(words)))))
```
Or purely technically combine the first two lines into one:
```py
ranks = dict(map(reversed, enumerate(sorted(range(len(words)), key=lambda i: words[i].lower()))))

ranked_words = list(zip(words, map(ranks.get, range(len(words)))))
```

### Alternative Solution: Another `sort`

But we can go a somewhat different way. Here's an alternative solution:
```py
indexes = sorted(range(len(words)), key=lambda i: words[i].lower())

ranks = dict(zip(indexes, range(len(words))))

ranked_words = [(words[i], r) for i, r in sorted(ranks.items())]
```
After constructing the `ranks` dictionary, we convert it to a list of pairs (index, rank) and sort this sequence (by index). As a result, we get a list of pairs `(0, r0)`, `(1, r1)`, ...

It became more complex, but we can notice that we're doing an extra step: the `ranks` dictionary itself is not needed!

Simpler to immediately sort the list of pairs from indexes:
```py
indexes = sorted(range(len(words)), key=lambda i: words[i].lower())

ranked_words = [(words[i], r) for i, r in sorted(zip(indexes, range(len(words))))]
```
Well, and now, we can do it in one line:
```
ranked_words = [(words[i], r) for i, r in sorted(zip(sorted(range(len(words)), key=lambda i: words[i].lower()), range(len(words))))]
```
At work, they'll "beat" you for this!!!

Code in https://onlinegdb.com/eMH7atQTP

---

## Nested Dictionary, Recursion, Set Comprehension, Generators (Aug 29)

Problem: Given a nested dictionary, in which each value is either a word or another dictionary (of the same type).

Write a function that finds all unique words in this dictionary.
```py
def find_unique(d: dict) -> set[str]
```
Examples:
* Input: `{1: hello, 2: hi, 3: hi}` \
Output: `{hello}`
* Input: `{10: hello, 20: hi, 30: {2: hi, 7:you}}` \
Output: `{hello, you}`

The solution consists of two parts:
1. Find all words in this data structure.
2. Select only unique ones.

We iterate through all values of the dictionary (keys are not important to us).

Collect those that are simple strings.

Recursively process values that are dictionaries.

The following function implements recursive processing:
```py
def get_words(d: dict) -> list[str]:
    words = []
    for value in d.values():
        if isinstance(value, dict):
            words.extend(get_words(value))
        else:
            words.append(value)

    return words
```
What's the difference between `isinstance(value, dict)` and `type(value) == dict`?

Count the number of copies for each found word.

Keep only those that are unique (number of copies == 1):
```py
from collections import Counter

def find_unique(d: dict) -> set[str]:
    words = get_words(d)
    c = Counter(words)
    unique = set()
    for word, n in c.items():
        if n == 1:
            unique.add(word)

    return unique
```
Tests:
```py
from collections import defaultdict

dicts = (
    {10: 'hello', 20: 'hi'},
    {10: 'hello', 20: 'hi', 30: 'hi'},
    {10: 'hello', 20: 'hi', 30: {2: 'hi', 7: 'you'}},
    {10: 'hello', 20: 'hi', 30: defaultdict(str, {2: 'hi', 7: 'you'})},
)

for d in dicts:
    print(find_unique(d))
```
Output:
```
{'hello', 'hi'}
{'hello'}
{'hello', 'you'}
{'hello', 'you'}
```
Let's consider different improvements

Using set-comprehension, the find_unique function can be implemented in one line:
```py
def find_unique(d: dict) -> set[str]:
    return {word for word, n in Counter(get_words(d)).items() if n == 1}
```
To avoid repeatedly creating lists (due to recursive calls) and copying words from list to list, the recursive function can simply add all found words to the same list:
```py
def get_words(d: dict) -> list[str]:
    words = []

    def get_all(d: dict) -> None:
        for value in d.values():
            if isinstance(value, dict):
                get_all(value)
            else:
                words.append(value)

    get_all(d)

    return words
```
Recursive processing is done by an inner function, and the outer one is actually a wrapper to preserve the same signature (definition).

In the next variant, instead of creating a list of words, which can potentially be very long, lazy word search is used, through a generator.
```py
from typing import Iterator

def get_words(d: dict) -> Iterator[str]:
    for value in d.values():
        if isinstance(value, dict):
            for v in get_words(value):
                yield v
        else:
            yield value
```
The following solution immediately creates a Counter, in which copies of each word are counted.
```py
from collections import Counter

def get_words(d: dict) -> Counter:
    c = Counter()

    def get_all(d: dict) -> None:
        for value in d.values():
            if isinstance(value, dict):
                get_all(value)
            else:
                c[value] += 1

    get_all(d)

    return c
```
```py
def find_unique(d: dict) -> set[str]:
    return {word for word, n in get_words(d).items() if n == 1}
```
This is the most optimal solution of all considered

https://onlinegdb.com/ohW2_B63i

---

## LeetCode/Easy: Five Problems with One-Line Solutions (June 24)

### LeetCode 242. Valid Anagram

https://leetcode.com/problems/valid-anagram/

> Given two strings s and t, return true if t is an anagram of s, and false otherwise.
> 
> An Anagram is a word formed by rearranging the letters of a different word, using all the original letters exactly once.

```py
def is_аnagram(s: str, t: str) -> bool:
    return sorted(list(s)) == sorted(list(t))
```

### LeetCode 169. Majority Element

https://leetcode.com/problems/majority-element/

> Given an array nums of size n, return the majority element.
> 
> The majority element is the element that appears more than ⌊n / 2⌋ times.
```py
from collections import Counter

def majority_еlement(nums: list[int]) -> int:
    return next((v for v,c in Counter(nums).items() if c > len(nums) // 2), None)
```

### LeetCode 229. Majority Element II

https://leetcode.com/problems/majority-element-ii/

> Given an integer array of size n, find all elements that appear more than ⌊ n / 3 ⌋ times.

```py
from collections import Counter

def majority_elements(nums: list[int]) -> list[int]:
    return [v for v,c in Counter(nums).items() if c > len(nums) // 3]
```

### LeetCode 217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate/

> Given an integer array nums, return true if any value appears at least twice in the array and return false if every element is distinct.

```py
from collections import Counter

def contains_dup(nums: list[int]) -> bool:
    return any(c >= 2 for c in Counter(nums).values())
```
```py
from collections import Counter

def contains_dup(nums: list[int]) -> bool:
    return max(Counter(nums).values()) >= 2
```

### LeetCode 350. Intersection of Two Arrays II

https://leetcode.com/problems/intersection-of-two-arrays-ii/

> Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays.

```py
from collections import Counter

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    return (Counter(nums1) & Counter(nums2)).elements()
```

---

## LeetCode/Easy: Five Problems on Data Structures and Recursion (Aug 19)

In parallel, we'll use the new match-case operator and compare it with short if-else.

### LeetCode 21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

> Given the heads of two sorted linked lists. 
> Merge the two lists into one sorted list. 
> The list should be made by splicing together the nodes of the first two lists.

Given definition of a list (linked list):
```py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

Solution:

```py
def merge(p: ListNode|None, q: ListNode|None) -> ListNode|None:
    match p, q:
        case p, None:
            return p
        case None, q:
            return q
        case p, q if p.val <= q.val:
            return ListNode(p.val, merge(p.next, q)) 
        case p, q:
            return merge(q, p)
```
The match-case construct is quite verbose, but in this case adds clarity:
* If one of the lists is empty, the answer is the second list.
* If the head of the first list is less than the head of the second, we take the value of the first and merge the remaining tail with the second list.
* In case the head of the second is less, we simply swap them.

Function call: `merge(list1, list2)`

Can also be done in one line, using the short form if-else:
```py
def merge(p: ListNode|None, q: ListNode|None) -> ListNode|None:
    return (ListNode(p.val, merge(p.next, q)) if p.val <= q.val else merge(q, p)) if p and q else p or q
```
Tasks:
* The first two case blocks can be combined, how?
* Rewrite the function using the regular if-elif-else operator.
* Solve the problem without recursion (using a loop, will be longer).

### LeetCode 104. Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

> Given the root of a binary tree, return its maximum depth, which is the number of nodes along the longest path from the root node down to the farthest leaf node.

Given definition of a list (linked list):
```py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
Solution:
```py
def depth(r: TreeNode|None) -> int:
    match r:
        case None:
            return 0
        case TreeNode(val=_, left=left, right=right):
            return max(depth(left), depth(right)) + 1
```
* If the tree is empty, then the answer is 0.
* For a non-empty tree, its depth is one more than the maximum depth among its subtrees.

Call the function like this: `depth(root)`

In one line:
```py
def depth(r: TreeNode|None) -> int:
    return max(depth(r.left), depth(r.right)) + 1 if r else 0
```
Tasks:
* Replace the last case block with case _.
* Replace the short if-else with the if-elif-else operator.

### LeetCode 100. Same Tree

https://leetcode.com/problems/same-tree/

> Given two binary trees, check if they are the same or not. 
> Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Solution:
```py
def same(p: TreeNode|None, q: TreeNode|None) -> bool:
    match p, q:
        case None, None:
            return True
        case p, None if p is not None:
            return False
        case None, q if q is not None:
            return False
        case p, q:
            return all((p.val == q.val, same(p.left, q.left), same(p.right, q.right)))
```

* Two empty trees ⏤ are identical.
* If only one of the trees is empty, then they are not identical.
* Two non-empty trees are identical if the values in their roots match, and their left and right subtrees are also identical (pairwise).

The standard all function returns True if all values equal True, actually this is the same as `... and ... and ...` .

Call: `same(p, q)`

In one line:
```py
def same(p: TreeNode|None, q: TreeNode|None) -> bool:
    return all((p.val == q.val, same(p.left, q.left), same(p.right, q.right))) if p and q else p == q == None
```
Tasks:
* In the first function, combine the second and third case blocks.
* Replace the short if-else with the if-elif-else operator.

### LeetCode 101. Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

> Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Solution:

Let's write a function that checks if two given trees are symmetric to each other:
```py
def symmetric(p: TreeNode|None, q: TreeNode|None) -> bool:
    match p, q:
        case None, None:
            return True
        case p, None if p is not None:
            return False
        case None, q if q is not None:
            return False
        case _:
            return all((p.val == q.val, symmetric(p.left, q.right), symmetric(p.right, q.left)))
```
* Two non-empty trees are symmetric if their roots match, the left subtree of the first tree is symmetric to the right subtree of the second tree, and also symmetric are the right subtree of the first tree and the left subtree of the second tree.

Function call: `not root or symmetric(root.left, root.right)`

In one line:
```py
def symmetric(p: TreeNode|None, q: TreeNode|None) -> bool:
    return all((p.val == q.val, symmetric(p.left, q.right), symmetric(p.right, q.left))) if p and q else p == q == None
```
Tasks:
* Combine the first three case blocks into one.
* Replace the short if-else with the if-elif-else operator.

### LeetCode 112. Path Sum

https://leetcode.com/problems/path-sum/

> Given a binary tree and an integer target, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals target. 
> A leaf is a node with no children.

Solution:
```py
def has_path(r: TreeNode|None, target: int) -> bool:
    match r:
        case None:
            return False
        case TreeNode(val=val, left=None, right=None):
            return val == target
        case TreeNode(val=val, left=left, right=right):
            return has_path(left, target-val) or has_path(right, target-val)
```
In this case, the matching process is more complex, since object pattern matching is used.
* For a leaf node (second case), the answer is True only if target matches its value.
* For the general case, we check the left and right subtrees.

Call: `has_path(root, targetSum)`

In one line:
```py
def has_path(r: TreeNode|None, target: int) -> bool:
    return (has_path(r.left, target - r.val) or has_path(r.right, target - r.val) if r.left or r.right else r.val == target) if r else False
```

Tasks:
* Replace the last `case` with `case _`.
* Replace the short `if-else` with the `if-elif-else` operator.

---

## LeetCode/Easy 9: Palindrome Number (May 17)

https://leetcode.com/problems/palindrome-number/

> Given an integer x, return True if x is a palindrome integer.
>
> An integer is a palindrome when it reads the same backward as forward.
>
> For example, 121 is a palindrome while 123 is not.

Let's consider several solutions to this problem.

Did you know that `s[::-1]` ⏤ reverses a string (as well as a list and tuple)? First convert integer x to string s, and then compare the string with its reverse. This is the simplest solution:
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]
```
We don't have to compare the entire string, we can compare the prefix with the reversed suffix:
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    return s[:len(s)//2] == s[:(len(s)-1)//2:-1]
```
The same as the first solution, but through iterators. In this case, we don't create a reversed string, but iterate through it in reverse order (reversed). The zip function can iterate through several iterables simultaneously. And the all function returns True if it doesn't encounter a single False!
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    return all(a == b for a,b in zip(s, reversed(s)))
```
Similar solution, but we iterate only through the prefix and suffix:
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    return all(s[i] == s[-i-1] for i in range(len(s)//2))
```
Simple loop, without any comprehensions. Remember that negative index points to the last elements?
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False
    return True
```
The same, but we iterate only through the prefix and suffix:
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    for i in range(0, len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True
```
The same, but through a while loop:
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
```
The same, but shorter:
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    i = 0
    while i < len(s)//2:
        if s[i] != s[-i-1]:
            return False
        i += 1
    return True
```
And here we don't convert the integer to a string. We move the lower digits of x to the higher digits of y. That is, y ⏤ is the reversed integer from x:
```py
def is_palindrome(x: int) -> bool:
    y, z = 0, x
    while z > 0:
        y = 10*y + z % 10
        z //= 10            
    return y == x
```
Code: https://onlinegdb.com/ghcfGOncm

---

## LeetCode/Medium 39: Combination Sum (May 25)

https://leetcode.com/problems/combination-sum/

> Given an array of distinct integers (candidates) and a target integer (target).
>
> Return all unique combinations of candidates such that the sum of candidates in the combination equals target.
>
> A candidate may appear in the combination any number of times.
>
> Example 1:
>```
> candidates = [2,3,6,7]
> target = 7
>```
> Obtained combinations: `[[2,2,3], [7]]`
> * 7 = 7
> * 7 = 2 + 2 + 3
>
> Example 2:
> ```
> candidates = [2,3,5]
> target = 8
> ```
> Obtained combinations: `[[2,2,2,2], [2,3,3], [3,5]]`
> * 8 = 2 + 2 + 2 + 2
> * 8 = 2 + 3 + 3
> * 8 = 3 + 5

Let's consider several solutions to this problem.

The combination_sum(candidates, target) function will use an internal recursive function: `comb(k, target)`.

`comb(k, target)` returns all such combinations that sum to target and consist only of the first k candidates.

Special cases:

* comb(0, 0) should return only one solution, empty, so: [[]].
* comb(0, target), if target ⏤ is not 0, then there are no solutions: [].

Look at the difference: there is one empty solution [[]] and no solutions at all [].

What other special cases can we notice?

* comb(1, target), if target equals candidates[0], then we return: `[[target]]`. \
Indeed, if given only one candidate, and it equals the target number, then we get one possible combination.

* comb(1, target), if target is not equal to candidates[0], then there are no solutions: [].

General case:

`comb(k, target)` can be split into two cases:

1. if we skip candidate number k-1 (don't include it in the combination), then we make a recursive call: `comb(k-1, target)` ⏤ this is part of the solution.
2. if the candidate doesn't exceed the target number, we try to include it in the combination. \
We make a recursive call: `comb(k, target-candidates[k-1])`. \
Since we included it in the combination, the target decreased by the candidate's value (`target-candidates[k-1]`). \
We don't exclude repeated use of the candidate, so we call with parameter k, not k-1.

But that's not all: to all combinations that sum to `target-candidates[k-1]`, we add one element (the candidate). Only then will such a combination sum exactly to target.

To the recursive function (`comb`), we can add call caching: `@cache`.
```py
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    def comb(k: int, target: int) -> list[list[int]]:
        if k == 0:
            if target == 0:
                return [[]]
            return []

        res = list(comb(k-1, target))
        if candidates[k-1] <= target:
            res.extend(c + [candidates[k-1]] for c in comb(k, target-candidates[k-1]))
        return res

    return comb(len(candidates), target)
```
The following solution differs somewhat from the previous one.

Added parameter tail, which collects the current combination. Another difference: the recursive function adds the obtained combination to a list, rather than returning it. And tuple is used intensively, not list. This gives the ability to cache answers.
```py
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    def comb(k: int, target: int, tail: tuple[int]):
        if k == 0:
            if target == 0:
                res.append(tail)
            return

        comb(k-1, target, tail)
        if candidates[k-1] <= target:
            comb(k, target-candidates[k-1], tail + (candidates[k-1],))    

    comb(len(candidates), target, tuple())
    return res
```
And in the next solution we return to lists, also reduce the number of recursive calls (replace with a loop).

The trickiest moment is that the tail parameter can change, but when and if this happens, we copy the list to avoid data corruption.

Here caching won't work:
```py
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    def comb(k: int, target: int, tail: list[int]):
        if k == 0:
            if target == 0:
                res.append(tail)
            return        

        comb(k-1, target, tail)
        tail = tail[:]
        while candidates[k-1] <= target:
            tail.append(candidates[k-1])
            target -= candidates[k-1]
            comb(k-1, target, tail)

    comb(len(candidates), target, [])
    return res
```
See other solutions here: https://onlinegdb.com/2S4gQRwbe

---

## LeetCode/Medium 75: Sort Colors (May 25)

https://leetcode.com/problems/sort-colors/

> Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
> 
> We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
> 
> You must solve this problem without using the library's sort function.
> 
> Example 1:
> 
> Input: nums = [2,0,2,1,1,0]
> Output: [0,0,1,1,2,2]
> 
> Example 2:
> 
> Input: nums = [2,0,1]
> Output: [0,1,2]

Let's start with a simpler problem, when only two colors are present: red (0) and white (1).

One way to sort an array of 0s and 1s: run partition:

* Skip all 0s on the left, then skip all 1s on the right.
* If we hit a 1 on the left and a 0 on the right, then we swap.
* Repeat the process until we check all numbers.

Now with three colors:

* Divide the array like this: collect all 0s on the left, and all 1s and 2s on the right.
* Then divide the right part of the array into 1s (go to the left part) and all 2s.

```py
def sort_colors0(nums: list[int]) -> None:
    def partition(beg, end, left):
        i = beg
        j = end
        while True:
            while i < j and nums[i] == left:
                i += 1
            while i < j and nums[j-1] != left:
                j -= 1

            if i == j:
                break

            nums[i], nums[j-1] = nums[j-1], nums[i]
        return i

    mid = partition(0, len(nums), 0)
    partition(mid, len(nums), 1)
```

An even simpler solution: count how many 0s, 1s, and 2s are in the array.
Then simply fill the array: first all 0s, then 1s, and then: 2s.
```py
from collections import Counter

def sort_colors1(nums: list[int]) -> None:
    c = Counter(nums)
    for i in range(len(nums)):
        nums[i] = 0 if i < c[0] else 1 if i < c[0] + c[1] else 2
```
The following solution is similar to the previous one, but potentially can be somewhat faster:
```py
from collections import Counter

def sort_colors2(nums: list[int]) -> None:
    c = Counter(nums)
    for i in range(c[0]):
        nums[i] = 0

    for i in range(c[0], c[0]+c[1]):
        nums[i] = 1

    for i in range(c[0]+c[1], len(nums)):
        nums[i] = 2
```
Code to play: https://onlinegdb.com/P2hNkRMdH

---

## Pig It — in One Line (Oct 25)

> Problem: Write a function `pig_it` that on the given text, 
> moves the first letter of each word to the end of it, 
> then adds `'ay'` to the end of the word.
> 
> It must leave punctuation marks untouched.
>
> Examples:
> 
> * `pig_it('Pig latin is cool')`
> * returns: `igPay atinlay siay oolcay`
> 
> 
> * `pig_it('Hello world !')`
> * returns: `elloHay orldway !`

The `pig_it` function shuffles each word in the text: the first letter jumps to the end of the word, to which the suffix 'ay' is added. At the same time, the function doesn't touch punctuation.

Let's make several simplifying assumptions:

* Words and punctuation marks are separated from each other by exactly one space.
* Only the following characters are allowed as punctuation marks: `','`, `'.'`, `'!'`, `'?'`, `':'`, `';'`.
* Only single punctuation marks occur (for example, `???` or `!?` are forbidden).

### Implementing the algorithm step by step:

Step 1: How to check that a given word, `w`, consists only of a punctuation mark?
We can do this in the following ways (remember the check result in a variable):
```py
is_punctuation_mark = w == ',' or w == '.' or w == '!' or w == '?' or w == ':' or w == ';'
```
Make it shorter, through checking in a tuple:
```py
is_punctuation_mark = w in (',', '.', '!', '?', ':', ';')
```
Check if the word is among the elements of the tuple.

Since a string is actually a tuple of characters, we can replace the tuple with a string, and replace checking for an element in a tuple — with checking for a character in a string:
```py
is_punctuation_mark = w in ',.!?:;'
```
Better to remember all punctuation marks in a string variable:
```py
punctuation_marks = ',.!?:;'
```
```py
is_punctuation_mark = w in punctuation_marks
```

Step 2: If given a word, `w` (not a punctuation mark), how to get `pigged_w` from it?
```py
pigged_w = w[1:] + w[0] + 'ay'
```

Merge together all characters starting from the second, 
at the end add the first character of the word and `'ay'`. 
For the suffix, let's introduce variable `suffix`:

```py
suffix = 'ay'
```
```py
pigged_w = w[1:] + w[0] + suffix
```

Step 3: Given a word, w (without spaces), if w is a punctuation mark, then leave w as is, otherwise, shuffle the letters of w according to the problem condition. Remember the result in variable pigged_w:
```py
is_punctuation_mark = w in punctuation_marks
if is_punctuation_mark:
    pigged_w = w
else:
    pigged_w = w[1:] + w[0] + suffix
```

Step 4: Now let's split the text into words, and iterate through each word:
```py
words = text.split()
for w in words:
    pass
```

Step 5: We got a for-loop that does nothing, 
but now we have the ability to process each word from `text`:

```py
words = text.split()
for w in words:
    is_punctuation_mark = w in punctuation_marks
    if is_punctuation_mark:
        pigged_w = w
    else:
        pigged_w = w[1:] + w[0] + suffix
```

Step 6: So far, we're not doing anything with the `pigged_w` values. 
We should remember them in a list, say, `pigged_words`. 
Now all shuffled words can be joined into `pigged_text`:

```py
pigged_words = []
words = text.split()
for w in words:
    ...

pigged_text = ' '.join(pigged_words)
```

Step 7: Let's put all the code in one function:

```py
punctuation_marks = ',.!?:;'
suffix = 'ay'
```
```py
def pig_it(text):
    pigged_words = []
    words = text.split()
    for w in words:
        is_punctuation_mark = w in punctuation_marks
        if is_punctuation_mark:
            pigged_w = w
        else:
            pigged_w = w[1:] + w[0] + suffix

        pigged_words.append(pigged_w)

    pigged_text = ' '.join(pigged_words)
    return pigged_text
```

We got the desired solution. Now we should check the correctness of the function and cover it with tests (see below). Tests will help not break the solution during code optimization.

### Refactoring

Let's shorten the code, getting rid of all variables that are used only in one place:

```py
def pig_it(text):
    pigged_words = []
    for w in text.split():
        if w in punctuation_marks:
            pigged_w = w
        else:
            pigged_w = w[1:] + w[0] + suffix

        pigged_words.append(pigged_w)

    return ' '.join(pigged_words)
```

Rewrite the if command through a shortened if-expression:

```py
def pig_it(text):
    pigged_words = []
    for w in text.split():
        pigged_w = w if w in punctuation_marks else w[1:] + w[0] + suffix
        pigged_words.append(pigged_w)

    return ' '.join(pigged_words)
```

Get rid of `pigged_w`:

```py
def pig_it(text):
    pigged_words = []
    for w in text.split():
        pigged_words.append(w if w in punctuation_marks else w[1:] + w[0] + suffix)

    return ' '.join(pigged_words)
```

Purely mechanically replace the for-loop and `append` with List Comprehension:

```py
def pig_it(text):
    pigged_words = [w if w in punctuation_marks else w[1:] + w[0] + suffix for w in text.split()]
    return ' '.join(pigged_words)
```

Get rid of `pigged_words`:

```py
def pig_it(text):
    return ' '.join([w if w in punctuation_marks else w[1:] + w[0] + suffix for w in text.split()])
```

We can remove the brackets `[ ]`. Why? What changed?

```py
def pig_it(text):
    return ' '.join(w if w in punctuation_marks else w[1:] + w[0] + suffix for w in text.split())
```

We've achieved a one-line solution (one-liner).

Sometimes code of short functions is written on the same line, right after the function definition (here it's excessive, but sometimes it's done this way):

```py
def pig_it(text): return ' '.join(w if w in punctuation_marks else w[1:] + w[0] + suffix for w in text.split())
```

We can also define nameless functions via lambda.

```py
pig_it = lambda text: ' '.join(w if w in punctuation_marks else w[1:] + w[0] + suffix for w in text.split())
```

Note that by storing lambda in a variable, we're actually giving it a name. 
There's not much point in this, but such code can also be encountered.

### Testing

We define a group of tests in one table. 
For each test, we specify the input value and expected result:

```py
def test():
    table = (
        ('', ''),
        (';', ';'),
        ('; . , :', '; . , :'),
        ('a', 'aay'),
        ('Pig latin is cool', 'igPay atinlay siay oolcay'),
        ('Hello world !', 'elloHay orldway !'),
    )

    for text, expected in table:
        pigged_text = pig_it(text)
        print(f'{pigged_text = }, {pigged_text == expected = }')
```

```py
test()
```
The `test` function runs `pig_it` for each test and compares the obtained result with the expected value.

Code: https://onlinegdb.com/PtHfV39vU

---

## LeetCode/Medium: Five Problems: Sort vs. Heap

### LeetCode 215. k-th largest element in an array

https://leetcode.com/problems/kth-largest-element-in-an-array/

> Given an integer array nums and an integer k, return the k-th largest element in the array. 
> Note that it is the k-th largest element in the sorted order, not the kth distinct element.
> 
> ```
> Input: nums = [3,2,1,5,6,4], k = 2
> Output: 5
> ```

The problem requires finding the k largest elements in a list. We give each solution a name. 
In subsequent problems, we'll apply similar approaches, and names will help navigate between different methods:

**Sorting**

Sort the list and take the last k elements:

```py
def find_klargest(nums: list[int], k: int) -> int:
    return sorted(nums)[-k]
```

* Time Complexity: O(n log n)
* Space Complexity: O(n)

**Heap + nlargest**

The Heap data structure is used in problems where PriorityQueue is required or for partial data sorting. 
In Python, MinHeap is in the `heapq` library. 

There's also the `nlargest` function, which can find the `k` largest elements in an iterable faster, 
than standard sorting, provided that `k` is significantly smaller than the number of elements in the list.

```py
import heapq

def find_klargest(nums: list[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]
```

* Time Complexity: O(n + k log n)
* Space Complexity: O(n)

**CountingSort**

By the problem condition, the range of values of each number is significantly smaller than the number of numbers in the list. 
So, we can speed up sorting: use the counting method.

```py
from collections import Counter

def find_klargest(nums: list[int], k: int) -> int:
    count = Counter(nums)
    for num in sorted(count.keys(), reverse=True):
        if count[num] >= k:
            return num

        k -= count[num]
```

* Time Complexity: O(n)
* Space Complexity: O(n)

**MaxHeap + heapify**

We can use Heap directly. We need MaxHeap, but `heapq` only has MinHeap. 
For each number in the list, we change the sign to the opposite ⏤ this trick allows working with MinHeap as MaxHeap. 

The `heapify` function creates a MinHeap, that is, partially sorts the data. 
At index 0 we'll get the smallest element, which will essentially be the largest in the original list (if we change the sign to the opposite).

```py
import heapq

def find_klargest(nums: list[int], k: int) -> int:
    ordered = [-num for num in nums]
    heapq.heapify(ordered)
    for _ in range(k-1):
        heapq.heappop(ordered)

    return -ordered[0]
```

* Time Complexity: O(n + k log n)
* Space Complexity: O(n)

**k-MinHeap**

This time we use MinHeap, in which we limit the size to `k`. 
Add elements one by one to the heap, if after adding, the heap size exceeds `k`, remove the minimum element. 
At the end, the heap will contain the `k` largest numbers.

```py
import heapq

def find_klargest(nums: list[int], k: int) -> int:
    ordered = []
    for num in nums:
        heapq.heappush(ordered, num)
        if len(ordered) > k:
            heapq.heappop(ordered)

    return ordered[0]
```
 
* Time Complexity: O(k log n)
* Space Complexity: O(k)

### LeetCode 347. Top k frequent elements

https://leetcode.com/problems/top-k-frequent-elements/

> Given an integer array nums and an integer k, return the k most frequent elements. 
> You may return the answer in any order.
> 
> ```
> Input: nums = [1,1,1,2,2,3], k = 2
> Output: [1,2]
> ```

We need to return the k most frequently occurring elements.

**Sorting**

The `sorted` method can be passed a sort key. 
That is, instead of comparing `x` and `y`, the `sorted` function will compare `count[x]` and `count[y]`:

```py
from collections import Counter

def top_kfrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    ordered = sorted(count.keys(), key=count.get)
    return ordered[-k:]
```

* Time Complexity: O(n log n)
* Space Complexity: O(n)

**Heap + nlargest**

```py
import heapq
from collections import Counter

def top_kfrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

* Time Complexity: O(n + k log n)
* Space Complexity: O(n)

**MaxHeap + heapify**

The heapify function doesn't have a `key` parameter. To force sorting numbers by their frequency (repetition), we create a MinHeap from pairs `(-c, num)`. 
As a result, heapify will perform sorting by `-c`.

```py
import heapq
from collections import Counter

def top_kfrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    ordered = [(-c, num) for num, c in count.items()]
    heapq.heapify(ordered)
    return [heapq.heappop(ordered)[1] for _ in range(k)]
```

* Time Complexity: O(n + k log n)
* Space Complexity: O(n)

**k-MinHeap**

```py
import heapq
from collections import Counter

def top_kfrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    ordered = []
    for num, c in count.items():
        heapq.heappush(ordered, (c, num))
        if len(ordered) > k:
            heapq.heappop(ordered)

    return [num for _, num in ordered]
```

* Time Complexity: O(n log k)
* Space Complexity: O(n)

### LeetCode 1985. Find the k-th largest integer in the array

https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

> You are given an array of strings nums and an integer `k`. 
> Each string in nums represents an integer without leading zeros.
> 
> Return the string that represents the k-th largest integer in nums.
> 
> Duplicate numbers should be counted distinctly. 
> For example, if nums is `['1', '2', '2']`, 
> * `'2'` is the first largest integer, 
> * `'2'` is the second-largest integer, and 
> * `'1'` is the third-largest integer.
> 
> ```
> Input: nums = ['3', '6', '7', '10'], k = 4
> Output: '3'
> ```
> 
> Explanation: The numbers in nums sorted in non-decreasing order are `['3', '6', '7', '10']`. 
> The 4th largest integer in nums is `'3'`.

We need to find the k-th largest number, represented as a string.

**Sorting**

Set the `key=int` parameter, which will force sorted to sort strings according to their numeric representations (otherwise the data will be sorted lexicographically, as in dictionaries).

```py
def klargest_num(nums: list[str], k: int) -> str:
    return sorted(nums, key=int)[-k]
```

* Time Complexity: O(n log n)
* Space Complexity: O(n)

**Heap + nlargest**

```py
import heapq

def klargest_num(nums: list[str], k: int) -> str:
    return heapq.nlargest(k, nums, key=int)[-1]
```
* Time Complexity: O(n + k log n)
* Space Complexity: O(n)

**MaxHeap + heapify**

Again we create a heap from pairs `(-int(w), w)`, which actually creates a MaxHeap sorting strings w according to their numeric representations:

```py
import heapq

def klargest_num(nums: list[str], k: int) -> str:
    ordered = [(-int(w), w) for w in nums]
    heapq.heapify(ordered)
    for _ in range(k-1):
        heapq.heappop(ordered)

    return ordered[0][1]
```

* Time Complexity: O(n + k log n)
* Space Complexity: O(n)

**k-MaxHeap**

```py
import heapq

def klargest_num(nums: list[str], k: int) -> str:
    ordered = []
    for w in nums:
        heapq.heappush(ordered, (int(w), w))
        if len(ordered) > k:
            heapq.heappop(ordered)

    return ordered[0][1]
```

* Time Complexity: O(n log k)
* Space Complexity: O(k)

### LeetCode 973. K closest points to origin

https://leetcode.com/problems/k-closest-points-to-origin/

> Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, 
> return the `k` closest points to the origin `(0, 0)`.
> 
> The distance between two points on the X-Y plane is the Euclidean distance (i.e., `√[(x1 - x2)^2 + (y1 - y2)^2]`).
> 
> ```
> Input: points = [[1,3],[-2,2]], k = 1
> Output: [[-2,2]]
> ```

We need to find k points closest to the center of the plane `O(0,0)`.

**Sorting**

Sort points `(x,y)` by the square of their distance to point `O`: `x**2 + y**2`:

```py
def kclosest(points: list[list[int]], k: int) -> list[list[int]]:
    return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]
```

* Time Complexity: O(n log n)
* Space Complexity: O(n)

**Heap + nsmallest**

For the nlargest function there's an analogous one: nsmallest, which finds the smallest elements:

```py
import heapq

def kclosest(points: list[list[int]], k: int) -> list[list[int]]:
    return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
```

* Time Complexity: O(n + k log n)
* Space Complexity: O(n)

**MinHeap + heapify**

```py
import heapq

def kclosest(points: list[list[int]], k: int) -> list[list[int]]:
    ordered = [(p[0]**2 + p[1]**2, p) for p in points]
    heapq.heapify(ordered)
    return [heapq.heappop(ordered)[1] for _ in range(k)]
```

* Time Complexity: O(n + k log n)
* Space Complexity: O(n)

**k-MaxHeap**

```py
import heapq

def kclosest(points: list[list[int]], k: int) -> list[list[int]]:
    ordered = []
    for p in points:
        heapq.heappush(ordered, (-p[0]**2 - p[1]**2, p))
        if len(ordered) > k:
            heapq.heappop(ordered)

    return [p[1] for p in ordered]
```

* Time Complexity: O(n log k)
* Space Complexity: O(k)

### LeetCode 692. Top k frequent words

https://leetcode.com/problems/top-k-frequent-words/description/

> Given an array of strings words and an integer `k`, return the `k` most frequent strings.
>
> Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
> 
> ```
> Input: words = ['i', 'love', 'leetcode', 'i', 'love', 'coding'], k = 2
> Output: ['i', 'love']
> ```

We need to find the `k` most frequently occurring words. 
If two words have the same number of repetitions, prefer the one that comes lexicographically. 
Sort the result.

**Sorting**

Count the number of repetitions of each word. 
As a key for sorting words w, use the pair: `(-count[w], w)`. 
Actually sort by number of repetitions (from larger to smaller), and then sort lexicographically.

```py
from collections import Counter

def top_kfrequent_words(words: list[str], k: int) -> list[str]:
    count = Counter(words)
    return sorted(count.keys(), key=lambda w: (-count[w], w))[:k]
```

* Time Complexity: O(n log n)
* Space Complexity: O(n)

**Heap + nsmallest**

```py
import heapq
from collections import Counter

def top_kfrequent_words(words: list[str], k: int) -> list[str]:
    count = Counter(words)
    return heapq.nsmallest(k, count.keys(), key=lambda w: (-count[w], w))
```

* Time Complexity: O(n + k log n)
* Space Complexity: O(n)

**MinHeap + Heapify**

```py
import heapq
from collections import Counter

def top_kfrequent_words(words: list[str], k: int) -> list[str]:
    count = Counter(words)
    ordered = [(-c, w) for w, c in count.items()]
    heapq.heapify(ordered)
    return [heapq.heappop(ordered)[1] for _ in range(k)]
```

* Time Complexity: O(n + k log n)
* Space Complexity: O(n)

**k-MaxHeap**

Unfortunately, getting MaxHeap from MinHeap by changing the sign to the opposite won't work, since we have two sorting criteria here. 
There's no way to specify `key`. 
The option remains to create a wrapper class, where we'll specify the correct comparison method. 
For the wrapper class, we use `dataclass` with fields `w` (word) and `c` (number of repetitions of `w`):

```py
import dataclasses

@dataclasses.dataclass
class O:
    w: str
    c: int

    def __lt__(self, other):
        return (-self.c, self.w) >= (-other.c, other.w)
```

```py
import heapq
from collections import Counter

def top_kfrequent_words(words: list[str], k: int) -> list[str]:
    count = Counter(words)
    ordered = []
    for w, c in count.items():
        heapq.heappush(ordered, O(w,c))
        if len(ordered) > k:
            heapq.heappop(ordered)

    return [o.w for o in sorted(ordered, reverse=True)]
```

* Time Complexity: O(n log k)
* Space Complexity: O(n)

**Notes:**
* Time/Space Complexity are somewhat simplified for problems where we work with strings.
* These problems can also be solved in other ways: QuickSelect, as well as using sorted-containers (not in the standard library).

