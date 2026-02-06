# LeetCode/Hard 239: Sliding Window Maximum

## Sliding Window Maximum: Part 1

https://leetcode.com/problems/sliding-window-maximum/

> You are given an array of integers nums. 
> There is a sliding window of size k, moving from the very left of the array to the right. 
> You can only see the k numbers in the window. 
> Each time the sliding window moves right by one position.
> 
> Return the max sliding window.
> ```
> Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
> Output: [3,3,5,5,6,7]
> ```

* The first window consists of numbers: `[1,3,-1]`, and the maximum: 3.
* Next window: `[3,-1,-3]`, maximum of this window: also 3.
* Third window: `[-1,-3,5]`, maximum: 5. etc.
* Last window: `[3,6,7]`, and its maximum: 7.

We collect all 6 maximums and return as a list: `[3,3,5,5,6,7]`.

In Python, this problem is easy to solve if you don't pay attention to Performance.
The simplest solution that will work poorly for large nums:

```py
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    window: list[int] = []
    max_sliding_win: list[int] = []

    for i in range(len(nums)):
        window.append(nums[i])
        if i >= k:
            window.remove(nums[i-k])

        if i >= k-1:
            max_sliding_win.append(max(window))

    return max_sliding_win
```
`window` — is the current window, on each iteration we add a new element. And if the window size exceeds k, then we remove the first element.

If the window has size k, then we calculate its maximum and write it to `max_sliding_win`.

* Time Complexity: O(n²)

Where n is the size of nums.

Number of iterations: n, and (almost) on each iteration we calculate the maximum and remove the first element, which requires O(n).

As a result, we get: n∙O(n) = O(n²).

Actually, for this problem there is a faster solution, only O(n log n), and this is a huge improvement, since it will practically work like O(n).

And indeed, this problem is marked in LeetCode as Hard and requires a more efficient solution than what we wrote above.

Unfortunately, Python doesn't have reasonable standard tools to implement an O(n log n) solution.

Yes, with Python you can fail on this question, even if you roughly know how to solve it.

If interested, in the continuation there will be:
* consider an example of ADT (abstract data types) applied to this problem;
* write faster (but not optimal) solutions to this problem in Python: O(n √n);
* implement an optimal solution using other programming languages: C++, Java, Rust;
* find out which programming languages will be most effective for this problem,
* and which programming languages will be inefficient, like Python.

----

## Sliding Window Maximum. Part 2: ADT

ADT, abstract data type — is a description of a data structure in terms of operations that can be performed with this data.

ADT defines operations, not how they should be implemented.

In the Sliding Window Maximum problem, we need some container, let's call it MaxWindow, which can contain numbers and supports the following operations:
* add a number;
* remove a given number;
* calculate the maximum.

For these purposes, we used a specific data structure, Python's list, and operations on it: append, remove, max.
Formally, we need a data type (class) with the following methods:

```py
class MaxWindow:
    def add(self, val: int):
        pass

    def remove(self, val: int):
        pass

    def max(self) -> int:
        pass
```

We can add @abstractmethod to the methods, emphasizing that this is still a description, without implementation.

For this abstract type, we can write a concrete implementation (even several). Use, for example, a standard list:

```py
class MaxArray:
    def __init__(self):
        self.values = []

    def add(self, val: int):
        self.values.append(val)

    def remove(self, val: int):
        self.values.remove(val)

    def max(self) -> int:
        return max(self.values)
```

This container, obviously, can do all operations that ADT MaxWindow defines.

Time Complexity:
* add: O(1)
* remove: O(m)
* max: O(m)

Where m is the number of elements in MaxArray.

We can rewrite the solution using this container (instead of list):

```py
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    window = MaxArray()
    max_sliding_win: list[int] = []

    for i in range(len(nums)):
        window.add(nums[i])
        if i >= k:
            window.remove(nums[i-k])
        if i >= k-1:
            max_sliding_win.append(window.max())

    return max_sliding_win
```

Actually, little has changed, and that's good, now we have the ability to implement other containers with the same operations. At the same time, the solution (code) will remain almost unchanged.

### Time Complexity

The two solutions, based on list and MaxWindow, differ little. But let's do a more precise analysis (for best-case and worst-case).

* The first k iterations of the loop call only add, and therefore each iteration executes in O(1).
* The next n-k iterations call all three methods (add, remove, max), so each iteration executes in O(k).

Time Complexity of the entire loop (and solution): k∙O(1) + (n-k)∙O(k) = O(k∙(n - k)).

* If k is very small (k << n), then we get O(k∙n).
* If k doesn't depend on n (k = const, k = O(1)), then we get a linear solution: O(n).
* If k is very close to n, so that k = n - O(1), then we also get: O(n).

That is, if the window size is either very small, or almost as large as nums, the solution will work quickly (linearly with the size of nums).

#### The Best Case Time Complexity: O(n).

In worst-case scenarios, when k is proportional to n (k ~ n, k = O(n)), for example, k = n / 2, we get:

#### The Worst Case Time Complexity: O(n²).

If we can implement a container (with ADT MaxWindow operations) with faster operations, then we can improve Time Complexity for the solution as a whole.

---

## Sliding Window Maximum. Part 3: Slow Solutions in Python

Recall that the remove and max operations of the MaxArray class require O(m) time, and only add executes in O(1). We can speed up max to O(1) if we sort all elements after each container change:

```py
class SortedArray:
    def __init__(self):
        self.values: list[int] = []

    def add(self, val: int):
        self.values.append(val)
        self.values.sort()

    def remove(self, val: int):
        self.values.remove(val)
        self.values.sort()

    def max(self) -> int:
        return self.values[-1]
```

But then add will lose its speed:

Time Complexity:
* add: O(m)
* remove: O(m)
* max: O(1)

Where m is the number of elements in the container.

To use SortedArray in the `max_sliding_window` function, we need to replace
```py
    window = MaxArray()
```
with
```py
    window = SortedArray()
```

And everything will work, since both classes have the same set of methods, that is, implement the same ADT (abstract data type) MaxWindow.

Note that general sorting over arbitrary data requires O(m log m). But in our case, before each call to sort(), the container elements are already almost sorted. Python uses the TimSort sorting method, which works O(m) for a sorted or almost sorted array

Actually, for real data sizes, log m grows so slowly that in practice we can assume:
O(m log m) = О(m)

Unfortunately, SortedArray won't improve the execution time of `max_sliding_window`.

Can we do better?

We need a data structure that can keep elements in (almost) sorted order, quickly add/remove and find the maximum. Such properties are possessed by Searching Trees and MaxHeap.

Python standard doesn't have trees, but there is MinHeap. To make Max from Min, we invert values (5 becomes -5):

```py
import heapq

class MaxHeap:
    def __init__(self):
        self.values: list[int] = []

    def add(self, val: int):
        heapq.heappush(self.values, -val)

    def remove(self, val: int):
        self.values.remove(-val)
        heapq.heapify(self.values)

    def max(self) -> int:
        return -self.values[0]
```

Time Complexity:
* add: O(log m)
* remove: O(m)
* max: O(1)

In the remove method, we don't know how to quickly remove an element from the heap, we have to remove as from a regular list in O(m). Actually, this is just a limitation of the specific Heap implementation in Python. If we implement our own MaxHeap, we can remove in O(log m) if we know the position of the element to remove. And this can be achieved using dict.

With such an implementation, operations add and remove will take O(log m), and max will be very fast: О(1). And then the execution time of `max_sliding_window` will significantly improve, to O(n log k).

The idea is good, but definitely not in 15 minutes: you need to know how to implement MaxHeap on trees (not arrays) and combine with `dict`.

The same Time Complexity can be achieved using Searching Trees, but they are not available in Python standard, and their implementation is also non-trivial.

We'll continue fighting with Python in the next post.

---

## Sliding Window Maximum. Part 4: Dancing with a Tambourine in Python

Note that, as in a standard set, we don't care about the order of elements in the container. But unlike set, we need to preserve all duplicates. Actually, we're talking about Multiset.

In Python, Multiset can be implemented using Counter (created based on dict), which will count the number of copies of each value. A very useful data structure.
```py
import collections

class MaxCount:
    def __init__(self):
        self.counts: collections.Counter[int] = collections.Counter()

    def add(self, val: int):
        self.counts[val] += 1

    def remove(self, val: int):
        self.counts[val] -= 1
        if self.counts[val] == 0:
            del self.counts[val]

    def max(self) -> int:
        return max(self.counts.keys())
```
Time Complexity:
* add: O(1)
* remove: O(1)
* max: O(m)

This approach also doesn't improve the speed of `max_sliding_window`, but can give some ideas about how to improve the speed of the max method.

### Buckets

In the problem condition, it's stated that number values are in the range from -10,000 to 10,000. Let's divide this range into 200 buckets, each covering a range of 100 values.

* Bucket with index 0: -10,000..-9,901
* Bucket with index 1: -9,900..-9,801
* Bucket with index 2: -9,800..-9,701
* ...
* Bucket with index 100: 0..99
* Bucket with index 101: 100..199
* ...
* Bucket with index 199: 9,900..9,999
* Bucket with index 200: 10,000..10,099

Actually there will be one more bucket (201), but that's not important.

Finding the maximum value consists of two steps:
1. find a non-empty bucket with maximum index and
2. find the maximum in that bucket.

```py
import collections

class BucketCount:
    def __init__(self):
        self.MIN = -10 ** 4
        self.MAX = 10 ** 4
        self.CAP = 100
        self.NUM_BUCKETS = (self.MAX - self.MIN + self.CAP) // self.CAP

        self.buckets: tuple[collections.Counter[int], ...] \
            = tuple(collections.Counter() for _ in range(self.NUM_BUCKETS))

    def add(self, val: int):
        idx = (val - self.MIN) // self.CAP
        self.buckets[idx][val] += 1

    def remove(self, val: int):
        idx = (val - self.MIN) // self.CAP
        self.buckets[idx][val] -= 1

        if self.buckets[idx][val] == 0:
            del self.buckets[idx][val]

    def max(self) -> int:
        for idx in range(self.NUM_BUCKETS - 1, -1, -1):
            if self.buckets[idx]:
                return max(self.buckets[idx])
```

Average Case Time Complexity
* add: O(1)
* remove: O(1)
* max: O(b + m / b)

Where b is the number of buckets.

The function f(b) = b + m / b takes a minimum value at b = m / b, that is, when b = √m.

We can't choose b dynamically, but knowing the problem conditions, we can choose b = O(√n).

Then Time Complexity of the `max_sliding_window` function will be:
* O(n √n),

Which is noticeably better than previous solutions (О(n²)).

Since by the problem condition m ≤ n ≤ 100,000, the number of buckets should be approximately 200-400. The best value can be found experimentally (by tests).

All previous solutions failed on long tests:

> Time Limit Exceeded.

And only this solution passes all tests.

**Task:** the standard collections package contains many different classes. For example, there is deque, which can be used in our problem. Take MaxArray and replace list with deque.

What will be the Time Complexity for the resulting container (let's call it MaxDeque)? Will there be an improvement in Time Complexity for `max_sliding_window`?

In the next parts, we'll see how dinosaur languages like C++ perform on this problem.

---

## Sliding Window Maximum. Part 5: C++ Rules

### C++

Simple, concise and fast solution in C++ in just 15 lines:

```cpp
#include <set>
#include <vector>

std::vector<int> max_sliding_window(std::vector<int>& nums, int k) {
    std::multiset<int> window;
    std::vector<int> max_sliding_win;

    for (int i = 0; i < nums.size(); i++) {
        window.insert(nums[i]);
        if (i >= k) {
            window.erase(window.find(nums[i-k]));
        }
        if (i >= k-1) {
            max_sliding_win.push_back(*window.rbegin());
        }
    }
    return max_sliding_win;
}
```

* Time Complexity: О(n log k)

The C++ standard library provides the `multiset` container, based on BST (Binary Search Tree).

Multiset allows duplicates, and gives access to elements in O(log m), where m is the number of elements in `multiset`.

Time Complexity of the C++ solution is much better than the fast Python solution (О(n log k) vs O(n √n)). Moreover, the C++ solution is about 3 times shorter than the Python solution.

**Did this surprise you?**

### Rust

Rust is a direct competitor to C++, also used for systems development and focused on code execution speed.

Rust doesn't offer Multiset in the standard library, but for our purposes we can use BTreeMap, which is also based on BST.

The solution looks more cumbersome, due to value conversion (can be made prettier?) and counting copies of values.

```rust
use std::vec::Vec;
use std::collections::BTreeMap;

pub fn max_sliding_window(nums: Vec<i32>, _k: i32) -> Vec<i32> {
    let k = _k.try_into().unwrap();
    let mut window = BTreeMap::new();
    let mut max_sliding_win = Vec::new();

    for i in 0..nums.len() {
        window.entry(nums[i]).and_modify(|c| *c += 1).or_insert(1);
        if i >= k {
            let j = i - k;
            window.entry(nums[j]).and_modify(|c| *c -= 1);
            if *window.get(&nums[j]).unwrap() == 0 {
                window.remove(&nums[j]);
            }
        }
        if i >= k - 1 {
            max_sliding_win.push(*window.iter().next_back().unwrap().0);
        }
    }
    return max_sliding_win;
}
```

### Java

In the Java standard library, you can find the TreeMap container, based on BST. We implement the same approach used in Rust.

```java
import java.util.List;
import java.util.ArrayList;
import java.util.SortedMap;
import java.util.TreeMap;

public int[] maxSlidingWindow(int[] nums, int k) {
    List<Integer> maxSlidingWin = new ArrayList<>();
    SortedMap<Integer, Integer> window = new TreeMap<>();

    for (int i = 0; i < nums.length; i++) {
        window.compute(nums[i], (key, c) -> c != null ? c+1 : 1);
        if (i >= k) {
            window.compute(nums[i-k], (key, c) -> c > 1 ? c-1 : null);
        }
        if (i >= k-1) {
            maxSlidingWin.add(window.lastKey());
        }
    }
    return maxSlidingWin.stream().mapToInt(x -> x).toArray();
}
```

* Time Complexity: O(n log k)

