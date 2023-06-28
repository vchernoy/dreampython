# Recursion. Dynamic Programming. Memoization

## Когда наконец-то выучил рекурсию в Python

Что делают все эти функции?
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

Когда выучил хвостовую рекурсию (tail recursion)

Сравните эти варианты, с аналогичными выше.
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

Хвостовая рекурсия ⏤ это такой вид рекурсии, когда рекурсивный вызов происходит в качестве самой последней команды. Хвостовая рекурсия хороша тем, что её легко можно простым циклом. Некоторые виды не хвостовых рекурсий можно легко переделать в хвостовые.

Есть ещё косвенные рекурсии, это когда функция вызывает другую, а та, вызывает первую (цепочка вызовов может быть длиннее).

Какие Time и Space Complexities у каждой из этих функций?

---

## LeetCode/Medium 77. Combinations

Рекурсия, динамическое программирование, memoization, генераторы, бином Ньютона.

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

Количество комбинаций легко считается через Binomial Coefficient: n! / (k! * (n-k)!).

Как увидеть и использовать рекурсию?

Рассмотрим первый пример: n = 4, k = 2.

Разобьём ожидаемый ответ:
```
[[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
```
На две части:
```
[[1,2], [1,3], [2,3]]
[[1,4], [2,4], [3,4]]
```
Первая группа ⏤ это все комбинации из 2-х чисел, составленных из `[1,2,3]`. То есть сводим этот случай к подзадаче `n=3,k=2`.

Заметим, что у второй группы все комбинации содержат общий элемент (4). А значит вторую группу можно получить присоединив 4 к каждой комбинации из: `[[1], [2], [3]]`.

`[[1], [2], [3]]` ⏤ это все комбинации размера 1, составленных из `[1,2,3]`. То есть приходим к подзадаче `n=3,k=1`.

Допустим функция `gen(n, k)`, которую нам нужно написать, умеет генерировать все комбинации для параметров `(n, k)`. Примерный план действий:

Сгенерируем все комбинации, каждая состоит из k чисел из диапазона от 1 до n-1, то есть вызываем `gen(n, k-1)`.

Сгенерируем все комбинации, каждая состоит из k-1 чисел из диапазона от 1 до n-1 (`gen(n-1,k-1)`), но к каждой комбинации "добавим" число n.

Объединение всех комбинации полученных в предыдущих двух шагах ⏤ это и будет ответ для `gen(n, k)`.

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
Поскольку функция `gen` вызывает себя (рекурсивно), то обязательно нужно обработать крайние случаи: `k=0` или `n < 0`.

`[*t, n]` ⏤ распаковывает комбинацию из k-1 чисел и добавляет k-ое число. Например, если `t=[1,2]` и `n=5`, то `[*t, n]` создаст `[1,2,5]`.

`functools.cache` запоминает результат функции для каждого вызова, с тем, чтобы впоследствии не делать повторных вычислений для тех же параметров. Это называется Memoization.

В следующей версии делаем следующие изменения: обрабатываем другие крайние случаи (для разнообразия), для комбинаций используем `tuple` вместо `list`, и самое главное: применяем list comprehension.

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
Функцию gen можно сократить до одной, но длинной команды:
```py
from functools import cache

def combine(n: int, k: int) -> list[list[int]]:
    @cache
    def gen(n: int, k: int):
        return gen(n-1, k) + [(*t, n) for t in gen(n-1, k-1)] if k not in (0, n) else [tuple(range(1, k+1))]
    return gen(n, k)
```

Можно перейти на ленивые вычисления, самый простой способ ⏤ это использовать генераторы. 
Но в этом случае, `@cache` следует убрать. 
С генератором, Memoization не будет работать корректно (почему?).

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

Два цикла for можно объединить в один. Воспользуемся функцией itertools.chain, которая склеивает несколько iterables в один:
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

Используем generator-expression. Теперь `gen` ⏤ это не генератор, а обычная функция, которая возвращает генератор:

```py
from itertools import chain

def combine(n: int, k: int):
    def gen(n: int, k: int):
        if k == 0 or n == k:
            return (tuple(range(1, k+1)),)

        return chain(gen(n-1, k), ((*t, n) for t in gen(n-1, k-1)))
    return list(gen(n, k))
```
Можно всё впихнуть в одну строку (что получится?).

В действительности в стандартной библиотеке есть функция itertools.combinations, которая решает поставленную задачу. Получим очень простое решение:
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

Три способа из `rabbbit` получить `rabbit`:

* **rabb**b**it**
* **rab**b**bit**
* **ra**b**bbit**

Другими словами, удаляем некоторые буквы из s, чтобы получить t. Наша цель: подсчитать количество способов, создания s из t (путём вычеркивания букв из s).
```
Input: s = "babgbag", t = "bag"
Output: 5
```
Пять способов получить `bag` из `babgbag`:

* **ba**b**g**bag
* **ba**bgba**g**
* **b**abgb**ag**
* ba**b**gb**ag**
* babg**bag**

Рассмотрим последний пример. Разделим ответ на две группы:

В группу #1 включаем решения, в которых первая буква b включается в решение.

* **ba**b**g**bag
* **ba**bgba**g**
* **b**abgb**ag**

В группе #2 включаем решения, в которых первая буква b пропускается.

* ba**b**gb**ag**
* babg**bag**

Фактически мы разбили задачу на две подзадачи.

Обозначим за `f(s, t)` ⏤ количество решений для задачи `(s, t)`. То есть `f(s, t)` должна посчитать все способы получения t из s.
Теперь посчитаем количество решений в каждой группе отдельно.

* `f(s[1:], t[1:])` ⏤ откусываем по одной букве из s и t, и для полученных строк решаем задачу. Это и будет ответ для группы #1.
* `f(s[1:], t)` ⏤ пропускаем первую букву только в s. А это ответ для группы #2.

Сумма двух решений даёт ответ для `f(s, t)`. Но нужно помнить, что группу #1 можно свести к подзадаче (`s[1:], t[1:]`) только если первые символы обеих строк равны.

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

* Как и в других примерах, внутренняя функция основана на рекурсии, которую мы описали выше.
* Обязательно ставим обработку крайних случаев: если t пустая, то ответ 1, а если t длиннее s, то ответ 0.
* Запоминаем (кэшируем) результаты вычислений используя декоратор: functools.cache (Memoization).
* До запуска рекурсии проверяем, если s содержит все буквы t, иначе сразу ответ 0. Для этой цели отлично сработает multi-set: `itertools.Counter`.

Можно в одну строчку?

Конечно, только в длинную:

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
Использовали короткую форму if (или if-expression): `value1 if condition else value2`.

Но применили это дважды: `value1 if conditionA else value2 if conditionB else value3`.

Также использовали такую хитрую запись: `x + (ok and y)`, что означает `(x + y) if ok else x`.

Заметим, что предыдущие решения на каждом шаге (вызове) проскакивают одну-две буквы.

А благодаря Memoization, не происходит повторных вычислений.

Следовательно, количество различных вызовов пропорционально количеству комбинаций всех суффиксов s и t, то есть O((len(s) + len(t))²).

Но каждый вызов тратит О(len(s) + len(t)) для откусывания первой буквы. То есть получаем кубический алгоритм.

Работу с подстроками можно исключить, ведь, чтобы пропустить символ, совершенно не обязательно использовать slicing `[1:]`.

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

Вместо s и t, используем индексы i, j, каждый из которых указывает на начало рассматриваемой подстроки. Это решение имеет квадратичную Time Complexity.

Также становиться очевидным, что вместо Memoization можно использовать Dynamic Programming, то есть вместо рекурсии, заполнить табличку `len(s)`x`len(t)` простыми вложенными циклами.

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

Мне кажется это не уровня Hard проблема, а скорее твердый Medium. Может следующий раз покажу похожую проблему уровня Medium, которая явно тяжелее, чем эта задача (и точно потянет на Hard).

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
> Разделим s1 и s2 на три и две части соответственно:
>
> * s1 = "aa" + "bc" + "c",
> * s2 = "dbbc" + "a".

Тогда можно получить s3 так:

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

Другими словами, следует разделить s1 и s2 на кусочки и не меняя порядок слить всё в одну строку, чтобы получилась s3. В случае успеха, возвращаем True. Считать все возможные комбинации не требуется, достаточно определить, если успешное разбиение возможно.

Очевидно, что s3 должна иметь длину равную сумме длин s1 и s2. Более того s3 должна состоять из того же набора букв, что и s1 + s2. Это можно легко реализовать:

```py
    if Counter(s1) + Counter(s2) != Counter(s3):
        return False
```

Также легко заметить, что если s2 ⏤ пустая строка, то достаточно сравнить на равенство s1 == s3 ⏤ это нам понадобится в рекурсии.

Пусть функция f(s1, s2, s3) решает поставленную задачу, то есть ищет разбиение s1 и s2, чтобы соединив все кусочки, получилась строка s3. Но мы требуем, чтобы в сливании частей разбиения, первым кусочком был выбран префикс именно строки s1.

Если бы была дана уже такая функция, то ответ к задаче можно было бы записать так:

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

Отрезаем префикс у s1, начиная с длины 1, перебираем все возможные варианты, пока не найдёт префикс общий и к s1 и к s2. Это можно записать так:

```py
        for i in range(min(len(s1), len(s3))):
            if s1[i] != s3[i]:
                return False
            ...
```

В случае, если s1 и s2 имеют общий префикс длинны i+1, то отрезаем этот префикс и проверяем если для новых строк s1[i+1:], s2, s3[i+1:] можно найти разбиение:

```py
            if f(s2, s1[i+1:], s3[i+1:]):
                return True
```

Хитрая рекурсия: функция f(s1, s2, s3) вызывает f(s2, s1[i+1:], s3[i+1:]). Параметры поменялись местами и это не ошибка. Поскольку f(s1, s2, s3) обязана брать префикс у строки s1 (то есть у своего первого параметра), то f(s2, s1[i+1:], s3[i+1:]) будет уже брать префикс у s2 (поэтому передаём его первым параметром).

Весь код:

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

Параметры `s1`, `s2`, `s3` у функции f перекрывают параметры функции `is_interleave`. Если, для удобства, обозначим за `s1'`, `s2'`, `s3'` ⏤ оригинальные параметры, то можно сделать следующие утверждения:

* `s1` ⏤ суффикс `s1'`, аналогично для `s2`, `s3`.
* `len(s3) == len(s1) + len(s2)`
* `s3 == s3'[-len(s1) - len(s2):]`
* `f(s1'[:len(s1)], s2'[:len(s2)], s3'[:len(s3)]) == True`

Другими словами, `s3` можно убрать из параметров функции f, и вычислять его при необходимости:

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

Этот вариант более запутанный, но даёт понять, что для рекурсии важны именно два параметра. Это факт важен для анализа Time & Space Complexities, а также для дальнейших оптимизаций: перехода на индексы и Dynamic Programming. Мы эти темы тут опустим.

Функцию f можно записать в одну, очень длинную строку, придётся её отформатировать (разбить на части):

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

Функция `itertools.takewhile` пробегает по iterables (в данном случае: индексы i из `range(len(s1)))` то тех пор, пока выполняется `s1[i] == s3[i]`). Далее идёт generator expression, который для каждого такого индекса, вызывает `f(s2, s1[i+1:], s3[i+1:])`. Функция `any` остановится и вернёт True, как только получит первый True (вызов рекурсии).

Очевидно, что `if not s2` и `return` тоже можно объединить в одну команду.

Как мне кажется, эта задача имеет сложность Hard, по крайней мере, эта задача сложнее, чем 115 (Distinct Subsequences).


**LeetCode: две задачи уровня Medium на рекурсию в одну строчку (считаем и генерируем двоичные деревья)**

---

## LeetCode/Medium 96. Unique Binary Search Trees

https://leetcode.com/problems/unique-binary-search-trees/

> Given an integer n, return the number of structurally unique BST's (binary search trees) with exactly n nodes of unique values from 1 to n.

Нужно посчитать количество двоичных деревьев с n узлами.
* Для n: 0 ⏤ ответ: 1 (пустое дерево).
* Для n: 1 ⏤ ответ: 1 (одно дерево с одним узлом).
* Для n: 2 ⏤ ответ: 2 (два симметричных дерева).
* Для n: 3 ⏤ ответ: 5.

Пусть f(n) обозначает количество деревьев с n узлами.

Если левое поддерево содержит l узлов (0 ≤ l ≤ n-1), тогда правое поддерево должно содержать n - l - 1 узлов.

Поскольку в такой конфигурации:
* количество всевозможных левых поддеревьев: f(l),
* а количество возможных правых поддеревьев: f(n - l - 1).
* то количество деревьев размера n будет: f(l) * f(n - l - 1).

Перебираем все возможные l, получаем рекуррентное соотношение:
* f(n) = sum(f(l) * f(n - l - 1))
* f(0) = 1

Пишем код, для удобства определяем рекурсивную функцию f внутренней:
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

Решение в одну строчку!

Интересный факт, f(n) это числа Каталана, которые можно посчитать так:

* C(n) = 2*(2*n-1)/(n+1) * C(n-1)
* C(0) = 1

Или на Python:
```py
def num_trees(n: int) -> int:
    def f(n: int) -> int:
        c = 1
        for i in range(1, n):
            c = 2 * (2*i + 1) * c // (i + 2)
        return c

    return f(n)
```
Можно и эту функцию записать в одну строку:
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
Числа Каталана можно выразить через биномиальные коэффициенты:
* C(n) = Binom(2*n, n) / (n+1)

Которые можно получить с помощью функции: math.comb. Получаем самое простое и короткое решение:

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

Эта задача является продолжением предыдущей. Теперь наша цель генерировать все двоичные числа размера n.

В условии задачи, BST определены следующим образом:

```py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Пусть функция `f(beg, end)` умеет генерировать все BSTs значения в узлах которого значения из `[beg..end]`.

Допустим корень дерева содержит значение `val` (`beg ≤ val ≤ end`).

* Тогда все левые деревья left генерируем вызвав `f(beg, val-1)`,
* а все правые деревья right создаём с помощью `f(val+1, end)`.

Тогда для каждого `val`, `left`, `right` определённых выше, можно создать правильное и уникальное дерево:

* `TreeNode(val=val, left=left, right=right)`

Собираем все варианты в списке trees, которые у будет результатом работы f(beg, end):

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

Функцию f можно записать в одну строку используя list comprehension:

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

Используя itertools.product можно два цикла заменить одним:

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
Очевидно, что размер списка всех деревьев должен быть равен количеству деревьев, то есть две задачи должны иметь консистентные результаты для одинакового значения n:

* `len(generate_trees(n)) == num_trees(n)`
