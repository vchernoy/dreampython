# String Internals

## What Are Strings? ⏤ Part 1 (Oct 17)

Python has a built-in data type: str (string). Strings are used to represent text, words, and individual characters. For example: `'Hello World!'` is a constant string (has type str).

A string is a sequence of characters of finite length.

### Strings in C ('71), Oberon ('89)

In previous-generation programming languages, such as C (1971) and Oberon (1989), strings had minimal support (from the language side). Usually strings were represented as arrays of characters, and a special character with code 0 was used to mark the end of a string.

In Python, this can be represented as a list (list), which can be partially filled with characters.

Want to count the length of a string?

We iterate through the character array until we encounter the special "end of string" character.

Strings could be modified, since a string is simply an array of characters (list in Python).

### Strings in Java ('95), Golang ('09), Python ('91)

New-generation programming languages, such as Java (1995), Golang (2009), and Python (1991), introduce a separate "string" type (String in Java, string in Golang, str in Python).
In new languages, strings are usually made immutable (immutable/unmodifiable), which makes working with them more convenient (why?).

This is done in Python, Golang, and Java (and many other places).

### Custom string implementation based on tuples

What if Python didn't have the str type, could we implement our own "strings"?

With some caveats and limitations, yes, though we wouldn't get the same convenience as with the built-in str type.

To introduce new types, Python uses the class definition construct. The simplest way to implement a string in Python is using a tuple of characters — yes, we still need individual characters.

Why use a tuple instead of a list?

Lists can be modified, but tuples cannot, just like standard strings, so tuple fits us more organically.

Let's call our string type: TStr, the prefix "T" comes from the word "tuple", meaning we're making strings based on tuples.

Let's start by defining the TStr class, introducing a constructor (`__init__`) and a method (`__len__`):

```py
class TStr:
    def __init__(self, chars: str = '') -> None:
        self.chars = tuple(chars)

    def __len__(self) -> int:
        return len(self.chars)
```

Objects of the TStr class contain an attribute chars (characters) — which contains individual characters in a tuple.

The `__len__` method counts the length of the string, which equals the length of the tuple (`self.chars`). Defining the `__len__` method allows using TStr objects in the len function, for example, this code will now work correctly:

```py
s = TStr('Hello World!')
print(len(s))

s = TStr()
print(len(s))
```

Output:

```text
12
0
```

Unfortunately, attempting to print TStr objects using print will fail:

```py
s = TStr('Hello')
print(s)
print(s.chars)
```

Output:

```text
<__main__.TStr object at 0x7fb5f424abe0>
('H', 'e', 'l', 'l', 'o')
```

The first print implicitly tries to convert TStr to type str. This can be fixed by defining the `__str__` method:

```py
    def __str__(self) -> str:
        return ''.join(self.chars)
```

The `__str__` method merges all characters from the tuple (`self.chars`) into a normal string (of type str). Now we get:

```text
Hello
('H', 'e', 'l', 'l', 'o')
```

Of course, in a hypothetical Python without the str type, the `__str__` method would be different, so this is another necessary assumption we make for convenience.

Recall that built-in strings (str) allow many operations, for example:
merging, repetition, extracting individual characters or substrings by indices.

* Strings can be compared and used as keys in dictionaries.
* Strings have many methods, such as startswith, endswith, find, replace, etc.

All of this can be implemented in TStr and it will work like standard str.

To be continued.

Code: [OnlineGDB](https://onlinegdb.com/PEyCCALh0)

---

## What Are Strings? ⏤ Part 2 (Oct 19)

In part 1, we started implementing the TStr class (strings) based on tuples (tuples of characters). Here's what we already have:

```py
class TStr:
    def __init__(self, chars: str = '') -> None:
        self.chars = tuple(chars)

    def __len__(self) -> int:
        return len(self.chars)

    def __str__(self) -> str:
        return ''.join(self.chars)
```

The next method `__repr__` creates a string representation of the object.
Note that the `__str__` method is called by the str function, and `__repr__` is called by `repr`.
This is another case where we can't do without standard strings:

```py
    def __repr__(self) -> str:
        return f'{type(self).__name__}("{self}")'
```

Now the following code will work correctly (try it without `__repr__`):

```py
hello = TStr('Hello')
world = TStr('World!')
space = TStr(' ')

print([hello, space, world])
```

Output:

```py
[TStr("Hello"), TStr(" "), TStr("World!")]
```

### TStr concatenation & repetition

The following methods are necessary for string concatenation and repetition.

```py
    def __add__(self, s) -> 'TStr':
        return TStr(self.chars + s.chars)

    def __mul__(self, n: int) -> 'TStr':
        return TStr(n * self.chars)

    def __rmul__(self, n: int) -> 'TStr':
        return TStr(n * self.chars)
```

Note that these operations are based on tuples, that is, they use (delegate) the corresponding operations on tuple: concatenation and repetition.

Example where these methods are used:

```py
print(hello + space + world)
print(world * 3)
print(3 * world)
```

Output:

```text
Hello World!
World!World!World!
World!World!World!
```
The `__add__` method is called where the + operator (concatenation) is applied to TStr objects, and `__mul__` and `__rmul__` are called where the * operator (repetition) is applied to TStr and int.

### TStr comparison

Want to compare TStr objects, as regular strings allow? Want to sort lists of TStr? Then we need to add the following methods:

```py
    def __eq__(self, x: object) -> bool:
        return self.chars == x.chars

    def __lt__(self, x: 'TStr') -> bool:
        return self.chars < x.chars

    def __le__(self, x: 'TStr') -> bool:
        return self == x or self < x
```

* `__eq__` is called by the `==` operation,
* `__lt__` is called by the `<` operation,
* `__le__` is called by the `<=` operation.

Now let's apply sorting:

```py
words = [world, hello]
words.sort()
print(words)
```

Output:

```py
[TStr("Hello"), TStr("World!")]
```

### Hashable TStr in `set` & `dict`

To be able to use TStr in set and dict (as a key), we need to make TStr "hashable", that is, add:
```py
    def __hash__(self) -> int:
        return hash(self.chars)
```
The `__hash__` method is called by the `hash` function, which we apply in `__hash__`, 
but already to values of type tuple (`self.chars`) — again delegating functionality to tuple.
Now we can create a set of TStr, as standard str allows:
```py
print(set(words))
```
Output:

```py
{TStr("Hello"), TStr("World!")}
```

Try using TStr as keys in `dict` — it should work.
And then remove `__hash__`, what happens?

### `TStr[i]`, `TStr[beg:end:step]`, iteration over `TStr`

Now let's provide access to individual characters by index, as standard strings allow:

```py
    def __getitem__(self, i: int) -> 'TStr':
        return TStr(self.chars[i])
```

This code will work:

```py
print([hello[0], hello[-1], hello[1:3], hello[:-1], hello[:], hello[::-1]])
```

Output:

```py
[TStr("H"), TStr("o"), TStr("el"), TStr("Hell"), TStr("Hello"), TStr("olleH")]
```

Negative indices work wonderfully, and even substring extraction (slices) works. Step and reversal also work. Magic! Again we delegated functionality to tuple! How close strings and tuples really are.

The following code also works thanks to `__getitem__`:

```py
print(list(hello))
print(list(reversed(hello)))
```

Output:

```py
[TStr("H"), TStr("e"), TStr("l"), TStr("l"), TStr("o")]
[TStr("o"), TStr("l"), TStr("l"), TStr("e"), TStr("H")]
```

### Iterating over characters (TStr became an enumerable type)

```py
for ch in hello:
    print(repr(ch))
```

Output:

```py
TStr("H")
TStr("e")
TStr("l")
TStr("l")
TStr("o")
```

We can iterate over characters and join them:

```py
import functools
res = functools.reduce(lambda x,y: x+y, hello, TStr())
print(repr(res))
```

Output:

```py
TStr("Hello")
```

To be continued...

Code: [OnlineGDB](https://onlinegdb.com/2ohZlESkI_)

---

## What Are Strings? ⏤ Part 3 (Oct 20)

In parts 1 and 2, we implemented part of the TStr class:

```py
class TStr:
    def __init__(self, chars: str = '') -> None:
        self.chars = tuple(chars)

    def __len__(self) -> int:
        return len(self.chars)

    def __str__(self) -> str:
        return ''.join(self.chars)

    def __repr__(self) -> str:
        return f'{type(self).__name__}("{self}")'

    def __add__(self, s) -> 'TStr':
        return TStr(self.chars + s.chars)

    def __mul__(self, n: int) -> 'TStr':
        return TStr(n * self.chars)

    def __rmul__(self, n: int) -> 'TStr':
        return TStr(n * self.chars)

    def __eq__(self, x: object) -> bool:
        return self.chars == x.chars

    def __lt__(self, x: 'TStr') -> bool:
        return self.chars < x.chars

    def __le__(self, x: 'TStr') -> bool:
        return self == x or self < x

    def __hash__(self) -> int:
        return hash(self.chars)

    def __getitem__(self, i: int) -> 'TStr':
        return TStr(self.chars[i])
```

### String slicing in Python vs. Java

Thanks to the `__getitem__` method, we can extract individual characters (`s[i]`) or substrings (`s[beg:end:step]`) from strings.
In Python, slicing can be used for strings, as well as for lists and tuples.
Despite the fact that strings and slicing are present in both Python and Java and Golang, slicing functionality is implemented differently.
More precisely, different optimizations are made.

For example, in Java, when creating a substring, characters are not copied to a new string. Instead, the created substring simply points to the same character array used in the original string.

In Python, slicing honestly copies all characters to a new string.

Sometimes Java's approach will work better, and sometimes Python's approach will work better. However, different approaches don't change the correctness of slicing — it's just a matter of optimization for specific cases.

Imagine that we're given a very long string from which we create a short substring (slice). What will happen in Java and Python?

### `s.find(x)` vs. `x in s`

If we implement the `s.find(x)` method (returns the index of substring `x` in `s`, or -1 if substring `x` is not found in `s`),
then we can get the `x in s` operation for free
(which delegates the check to the `__contains__` method):

```py
    def find(self, x: 'TStr') -> int:
        return next((i for i in range(len(self)-len(x)+1) if self[i:i+len(x)] == x), -1)
```

```py
    def __contains__(self, x: 'TStr') -> bool:
        return self.find(x) >= 0
```

Now this code will work:

```py
hello = TStr('Hello')
world = TStr('World!')
space = TStr(' ')
hello_world = hello + space + world
```

```py
for w in hello, space, world, space+hello:
    print(hello_world.find(w))
```

```py
for w in hello, space, world, space+hello:
    print(w in hello_world)
```

Output:

```text
0
5
6
-1
```

```text
True
True
True
False
startswith & endswith
```

Let's add methods:

```py
    def startswith(self, prefix: 'TStr') -> bool:
        return self[:len(prefix)] == prefix

    def endswith(self, suffix: 'TStr') -> bool:
        return self[-len(suffix):] == suffix
```

And check:

```py
for w in hello, space, world, hello+space:
    print(hello_world.startswith(w))
```

```py
for w in world, hello, space, space+world:
    print(hello_world.endswith(w))
```

Output:

```text
True
False
False
True
```

```text
True
False
False
True
```

### `s.replace(old, new)`

The `replace` method is implemented through recursion, we get very simple code:

```py
    def replace(self, old: 'TStr', new: 'TStr') -> 'TStr':
        k = self.find(old)
        return self[:k] + new + self[k+len(old):].replace(old, new) if k >= 0 else self
```

Example:

```py
print(hello_world.replace(TStr('l'), TStr('L')*3))
```

Output:

```text
HeLLLLLLo WorLLLd!
```

Code: [OnlineGDB](https://onlinegdb.com/0CqoCkOm-)

---

## What Are Strings? ⏤ Part 4 (Oct 23)

In previous parts, part of the TStr class (strings based on tuples) was implemented. Here's what we got:

```py
class TStr:
    def __init__(self, chars: str = '') -> None:
        self.chars = tuple(chars)

    def __len__(self) -> int:
        return len(self.chars)

    def __str__(self) -> str:
        return ''.join(self.chars)

    def __repr__(self) -> str:
        return f'{type(self).__name__}("{self}")'

    def __add__(self, s) -> 'TStr':
        return TStr(self.chars + s.chars)

    def __mul__(self, n: int) -> 'TStr':
        return TStr(n * self.chars)

    def __rmul__(self, n: int) -> 'TStr':
        return TStr(n * self.chars)

    def __eq__(self, x: object) -> bool:
        return self.chars == x.chars

    def __lt__(self, x: 'TStr') -> bool:
        return self.chars < x.chars

    def __le__(self, x: 'TStr') -> bool:
        return self == x or self < x

    def __hash__(self) -> int:
        return hash(self.chars)

    def __getitem__(self, i: int) -> 'TStr':
        return TStr(self.chars[i])

    def find(self, x: 'TStr') -> int:
        return next((i for i in range(len(self) - len(x) + 1) if self[i:i + len(x)] == x), -1)

    def __contains__(self, x: 'TStr') -> bool:
        return self.find(x) >= 0

    def startswith(self, prefix: 'TStr') -> bool:
        return self[:len(prefix)] == prefix

    def endswith(self, suffix: 'TStr') -> bool:
        return self[-len(suffix):] == suffix

    def replace(self, old: 'TStr', new: 'TStr') -> 'TStr':
        k = self.find(old)
        return self[:k] + new + self[k+len(old):].replace(old, new) if k >= 0 else self
```

Now let's consider how to implement the `join` method. We want the following code to work:

```py
space = TStr(' ')
words = [TStr('hello'), TStr('my'), TStr('dear'), TStr('friend')]

print(repr(space.join(words)))
print(repr(space.join([TStr('hello')])))
print(repr(space.join([])))

print(repr(TStr(':').join([TStr('hello')]*5)))
```

Output:

```text
TStr("hello my dear friend")
TStr("hello")
TStr("")
TStr("hello:hello:hello:hello:hello")
```

The `join` method accumulates all characters in the `res` list (has type: `list[str]`),
which is finally converted to a tuple and passed to the TStr constructor:

```py
    def join(self, sequence: Iterable['TStr']) -> 'TStr':
        res: list[str] = []
        for word in sequence:
            if res:
                res.extend(self.chars)

            res.extend(word.chars)

        return TStr(tuple(res))
```

[code snippet](https://github.com/vchernoy/dreampython/blob/f310f4678e5bbacb72541d19a9104835a268210c/string_internals/tstr.py#LL54C1-L63C1)

Here we have a problem, since `__init__` expects a string, not a tuple. Let's fix `__init__`:

```py
    def __init__(self, chars: str | tuple[str] = ()) -> None:
        self.chars = chars if type(chars) == tuple else tuple(chars)
```

Let's clarify, during the execution of the method call: `space.join(words)`, in the `for` loop,

* `self` is `space`,
* `sequence` is `words`, and
* `word` is the elements of `words` (`sequence`).

If we assume that the list of words can be huge,
then the `join` method will allocate a huge list of characters (larger than the sum of all characters in all words).
Then a tuple will be created from the list, which will be part of the result (TStr).
Actually, we wasted memory on the list, since we need a tuple.
Can we improve?

The following version uses a generator (the `yield_chars` function):

```py
import itertools
```

```py
   def join21(self, sequence: Iterable['TStr']) -> 'TStr':
        def yield_chars():
            for word in sequence:
                yield self.chars
                yield word.chars

        return TStr(tuple(
            itertools.chain.from_iterable(
                itertools.islice(
                    yield_chars(),
                    1,
                    None)
            )
        ))
```

We can also do it in one, but very long, line:

```py
    def join(self, sequence: Iterable['TStr']) -> 'TStr':
        return TStr(tuple(
            itertools.chain.from_iterable(
                t.chars for t in itertools.islice(
                    itertools.chain.from_iterable(zip(itertools.repeat(self), sequence)),
                    1,
                    None
                )
            )
        ))
```
Other methods (from str) can be added (to TStr) without much trouble, some will be more complex, and some simpler.

What else distinguishes strings in different languages, besides the ability to modify and optimizations?

The main task of strings is to support text, which, in fact, can contain not only English, but also other different languages.

The question of how to correctly encode letters of different alphabets (Cyrillic, Chinese, Hebrew) is the most important and difficult task. Approaches to encodings vary among different languages, there's even a difference in approaches between Python 2 and Python 3. That's right, strings in Python 2 are not compatible with strings in Python 3.

Code: [OnlineGDB](https://onlinegdb.com/o_vdN5LO7)

