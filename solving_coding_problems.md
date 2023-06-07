## Solving Coding Problems

### Фильтруем список списков (May 25)

Допустим дан список списков. Наша цель оставить только уникальные списки. Причём под уникальностью двух списков понимаем, что они состоят из одних и тех же элементов (порядок не важен).

Как это сделать?

Пример, дан список списков чисел.
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
После фильтрации, получим только "уникальные списки":
```py
unique = [
    [2, 7]
    [1, 2, 6],
    [1, 1, 7],
    [1, 2, 2, 3],
]
```
Почему?

Потому как по нашим условиям:

* [7, 2] и [2, 7] ⏤ не уникальны (состоят из одинаковых элементов, но в разном порядке).
* [6, 2, 1], [1, 2, 6], [1, 6, 2] ⏤ не уникальны.
* [1, 2, 2, 3] и [1, 2, 3, 2] ⏤ не уникальны.

Как оставить только уникальные элементы?

Список необязательно содержит уникальные элементы, а множество как раз таки гарантирует уникальность.

Но множество может хранить только hashable элементы, то есть например tuples, но не lists.

А элементы нашего списка ⏤ тоже списки!

Значит первый шаг: перевести все внутренние списки в tuples:
```py
set_of_values = set(tuple(values) for values in store)
```
Этого будет недостаточно, ведь такое множество уберёт уникальные элементы, только если они будут равны, например: [2,7] и [2,7]. Но посчитает уникальными списки: [7,2] и [2,7].

Решение: можно сначала отсортировать эти списки, а потом уже конвертировать в tuple. Получим:
```py
unique_as_set = set(tuple(sorted(values)) for values in store)
```
Используем set comprehension: множество формируется из элементов: tuple(sorted(values)).

Можно сделать то же самое через обычный цикл:
```py
unique_as_set = set()
for values in store:
    unique_as_set.add(tuple(sorted(values)))
```
Двигаемся дальше, мы достигли цели, теперь у нас только уникальные списки (вернее tuples). Но что если хотим перевести в оригинальный формат, то есть вместо set of tuples получить list of lists?

Теперь используем list comprehension:
```py
unique = [list(values) for values in unique_as_set]
``` 
То есть формируем список из элементов: list(values). Можно обычным циклом:
```py
unique = []
for values in unique_as_set:
    unique.append(list(values))
```
Можно всё сделать в один шаг:
```py
unique = [list(values) for values in set(tuple(sorted(values)) for values in store)]
```
Можно вывести всё на печать:
```py
print(f'{store=}')
print(f'{unique_as_set=}')
print(f'{unique=}')
```
Бонус: А если цель посчитать все уникальные списки?

Тогда вместо set используем Counter и кидаем в него отсортированные tuples:
```py
from collections import Counter

counted_values = Counter(tuple(sorted(b)) for b in values)

print(f'{counted_values=}')
```

Code: https://onlinegdb.com/o_MRBjNxP

---


### Ставим рейтинг списку слов (June 5)

Дан список слов, требуется узнать на каком месте будет положение каждого слова после сортировки списка (игнорируем регистр букв).

Решение:

В качестве примера берём слова из цитаты Линуса Товальдса:
```py
words = ['Talk', 'is', 'cheap', 'Show', 'me', 'the', 'code', 'by', 'Linus', 'Torvalds']
```
Конструируем массив отсортированных индексов:
```py
indexes = list(range(len(words)))

indexes.sort(key=lambda i: words[i].lower())
```
indexes[0] содержит индекс слова, которое после сортировки, должно находиться в положении 0.

В общем случае: после сортировки слов, на месте r будет находиться слово words[indexes[r]].

Параметр key в функции sort определяет ключ/свойство, согласно которому производится сортировка.

Создаём словарь ranks, который по индексу i выдаст рейтинг (положение) слова words[i]:
```py
ranks = {}
for r, i in enumerate(indexes):
    ranks[i] = r
```
А теперь конструируем список пар: слово и его позиция в отсортированном списке.
```py
ranked_words = []
for i, w in enumerate(words):
    ranked_words.append((w, ranks[i]))

print(ranked_words)
```

Вроде несложно. Можно сократить количество строк, используя разные list/dict comprehension. А в качестве упражнения, попробуем вместить весь код в одну строчку (это для тех, кто дотянет до конца!).

#### Applying List & Dict Comprehension vs. Map

Список indexes, а также словарь ranks и список ranked_words можно сконструировать каждый в одну строчку:
```py
indexes = sorted(range(len(words)), key=lambda i: words[i].lower())

ranks = {i: r for r, i in enumerate(indexes)}

ranked_words = [(w, ranks[i]) for i, w in enumerate(words)]
```
Можно первые две строчки объединить, но получим нечто неуклюжее.

Лучше ещё потренируемся в написании альтернативных решений. Словарь rank можно создать такими способами:
```py
ranks = dict(zip(indexes, range(len(words))))
```
```py
ranks = dict(map(reversed, enumerate(indexes)))
```

А результирующий список ranked_words, такими способами:
```py
ranked_words = list(zip(words, (ranks[i] for i in range(len(words)))))
```
```py
ranked_words = list(zip(words, map(ranks.get, range(len(words)))))
```
```py
ranked_words = [(words[i], ranks[i]) for i in range(len(words))]
```
Можно, конечно, избавиться от индексов:
```py
indexes = sorted(range(len(words)), key=lambda i: words[i].lower())

ranks = dict(map(reversed, enumerate(indexes)))

ranked_words = list(zip(words, map(ranks.get, range(len(words)))))
```
Или чисто технически объединить первые две строчки в одну:
```py
ranks = dict(map(reversed, enumerate(sorted(range(len(words)), key=lambda i: words[i].lower()))))

ranked_words = list(zip(words, map(ranks.get, range(len(words)))))
```

#### Альтернативное решение: ещё один `sort`

Но можно пойти несколько другим путём. Вот альтернативное решение:
```py
indexes = sorted(range(len(words)), key=lambda i: words[i].lower())

ranks = dict(zip(indexes, range(len(words))))

ranked_words = [(words[i], r) for i, r in sorted(ranks.items())]
```
После конструирования словаря `ranks`, преобразовываем его в список пар (индекс, ранк) и сортируем эту последовательность (по индексу). В результате получаем список пар `(0, r0)`, `(1, r1)`, ...

Стало сложнее, но можно заметить, что мы делаем лишний шаг: сам словарь `ranks` нам не нужен!

Проще сразу сортировать список пар из indexes:
```py
indexes = sorted(range(len(words)), key=lambda i: words[i].lower())

ranked_words = [(words[i], r) for i, r in sorted(zip(indexes, range(len(words))))]
```
Ну а теперь, можно и в одну строчку:
```
ranked_words = [(words[i], r) for i, r in sorted(zip(sorted(range(len(words)), key=lambda i: words[i].lower()), range(len(words))))]
```
На работе за такое "побьют"!!!

Code in https://onlinegdb.com/eMH7atQTP

---


### Nested Dictionary, Recursion, Set Comprehension, Generators (Aug 29)

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

Решение задачи состоит из двух частей:
1. Найти все слова в данной структуре данных.
2. Выбрать только уникальные из них.

Пробегаем по всем значениям словаря (ключи нам не важны).

Собираем, те которые являются простыми строками.

Рекурсивно обрабатываем значения, которые являются словарями.

Следующая функция реализует рекурсивную обработку:
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
В чём разница между `isinstance(value, dict)` и `type(value) == dict`?

Считаем количество копий для каждого найденного слова.

Оставляем только те, которые уникальны (количество копий == 1):
```py
from collections import Counter
```
```py
def find_unique(d: dict) -> set[str]:
    words = get_words(d)
    c = Counter(words)
    unique = set()
    for word, n in c.items():
        if n == 1:
            unique.add(word)

    return unique
```
Тесты:
```py
from collections import defaultdict
```
```py
dicts = (
    {10: 'hello', 20: 'hi'},
    {10: 'hello', 20: 'hi', 30: 'hi'},
    {10: 'hello', 20: 'hi', 30: {2: 'hi', 7: 'you'}},
    {10: 'hello', 20: 'hi', 30: defaultdict(str, {2: 'hi', 7: 'you'})},
)
```
```py
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
Рассмотрим разные улучшения

Используя set-comprehension, функцию find_unique можно реализовать в одну строчку:
```py
def find_unique(d: dict) -> set[str]:
    return {word for word, n in Counter(get_words(d)).items() if n == 1}
```
Чтобы избежать многократного создания списков (из-за рекурсивных вызовов) и копирования слов из списка в список, рекурсивная функция может просто добавлять все найденные слова в один и тот же список:
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
Рекурсивная обработка производится внутренней функцией, а внешняя фактически является обёрткой, чтобы сохранить ту же самую сигнатуру (определение).

В следующем варианте, вместо создания списка слов, который потенциально может быть очень длинным, используется ленивый поиск слов, через генератор.
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
Следующее решение сразу создаёт Counter, в котором подсчитываются копии каждого слова.
```py
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
Это наиболее оптимальное решение из всех рассмотренных

https://onlinegdb.com/ohW2_B63i

---


### LeetCode/Easy: Пять задач с решением в одну строчку (June 24)

#### 242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word formed by rearranging the letters of a different word, using all the original letters exactly once.
```py
def is_аnagram(s: str, t: str) -> bool:
    return sorted(list(s)) == sorted(list(t))
```
https://leetcode.com/problems/valid-anagram/

#### 169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
```py
def majority_еlement(nums: list[int]) -> int:
    return next(v for v,c in Counter(nums).items() if c > len(nums) // 2, None)
```
https://leetcode.com/problems/majority-element/

#### 229. Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊ n / 3 ⌋ times.
```py
def majority_elements(nums: list[int]) -> list[int]:
    return [v for v,c in Counter(nums).items() if c > len(nums) // 3]
```
https://leetcode.com/problems/majority-element-ii/

#### 217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array and return false if every element is distinct.
```py
def contains_dup(nums: list[int]) -> bool:
    return any(c >= 2 for c in Counter(nums).values())
```
```py
def contains_dup(nums: list[int]) -> bool:
    return max(Counter(nums).values()) >= 2
```
https://leetcode.com/problems/contains-duplicate/

#### 350. Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays.
```py
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    return (Counter(nums1) & Counter(nums2)).elements()
```
https://leetcode.com/problems/intersection-of-two-arrays-ii/

---


### Пять простых задач на структуры данных и рекурсию (Aug 19)

Параллельно будем использовать новый оператор match-case и сравним его с коротким if-else.

#### 1. Merge Two Sorted Lists

Given the heads of two sorted linked lists. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Дано определение списка (linked list):
```py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```
* https://leetcode.com/problems/merge-two-sorted-lists/

Решение:
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
Конструкция match-case довольно громоздка, но в данном случае добавляет ясности:
* Если один один из списков пустой, ответом является второй список.
* Если голова первого списка меньше головы второго, берём значение первого и сливаем оставшийся хвост со вторым списком.
* В случае, если голова второго меньше, то просто меняем их местами.

Вызов функции: `merge(list1, list2)`

Можно и в одну строчку, с использованием короткой формы if-else:
```py
def merge(p: ListNode|None, q: ListNode|None) -> ListNode|None:
    return (ListNode(p.val, merge(p.next, q)) if p.val <= q.val else merge(q, p)) if p and q else p or q
```
Задания:
* Два первых блока case можно объединить, как?
* Перепишите функцию с использованием обычного оператора if-elif-else.
* Решите задачу без рекурсии (используя цикл, будет длиннее).

#### 2. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth, which is the number of nodes along the longest path from the root node down to the farthest leaf node.

* https://leetcode.com/problems/maximum-depth-of-binary-tree/

Дано определение списка (linked list):
```py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
Решение:
```py
def depth(r: TreeNode|None) -> int:
    match r:
        case None:
            return 0
        case TreeNode(val=_, left=left, right=right):
            return max(depth(left), depth(right)) + 1
```
* Если дерево пустое, то ответ 0.
* Для не пустого дерева, его depth на единицу больше чем максимальная глубина среди его поддеревьев.

Вызываем функцию так: `depth(root)`

В одну строчку:
```py
def depth(r: TreeNode|None) -> int:
    return max(depth(r.left), depth(r.right)) + 1 if r else 0
```
Задания:
* Последний блок case замените на case _.
* Замените короткий if-else оператором if-elif-else.

#### 3. Same Tree

Given two binary trees, check if they are the same or not. Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

* https://leetcode.com/problems/same-tree/

Решение:
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
* Два пустых дерева -- идентичны.
* Если только одно из деревьев пустое, то они не идентичны.
* Два не пустых дерева идентичны, если значения в их корнях совпадают, а также идентичными являются их левые и правые поддеревья (попарно).

Стандартная функция all возвращает True если все значения равны True, фактически это то же самое что `... and ... and ...` .

Вызываем: `same(p, q)`

В одну строчку:
```py
def same(p: TreeNode|None, q: TreeNode|None) -> bool:
    return all((p.val == q.val, same(p.left, q.left), same(p.right, q.right))) if p and q else p == q == None
```
Задания:
* В первой функции, объедините второй и третий блоки case.
* Замените короткий if-else оператором if-elif-else.

#### 4. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

* https://leetcode.com/problems/symmetric-tree/

Решение:

Напишем функцию, которая проверяет если два данных дерева симметричны друг к другу:
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
* Два не пустые дерева симметричны, если их корни совпадают, левое поддерево первого дерева симметрично правому поддереву второго дерева, а также симметричны правое поддерево первого дерева и левое поддерево второго дерева.

Вызов функции: `not root or symmetric(root.left, root.right)`

В одну строчку:
```py
def symmetric(p: TreeNode|None, q: TreeNode|None) -> bool:
    return all((p.val == q.val, symmetric(p.left, q.right), symmetric(p.right, q.left))) if p and q else p == q == None
```
Задания:
* Объедините первые три блока case в один.
* Замените короткий if-else оператором if-elif-else.

#### 5. Path Sum

Given a binary tree and an integer target, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals target. A leaf is a node with no children.

* https://leetcode.com/problems/path-sum/

Решение:
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
В данном случае процесс matching более сложный, поскольку используется паттерн по объектам.
* Для узла-листа (второй case), ответ True только если target совпадает с его значением.
* Для общего случая проверяем левое и правое поддеревья.

Вызываем: `has_path(root, targetSum)`

В одну строчку:
```py
def has_path(r: TreeNode|None, target: int) -> bool:
    return (has_path(r.left, target - r.val) or has_path(r.right, target - r.val) if r.left or r.right else r.val == target) if r else False
```

Задания:
* Замените последний case на case _.
* Замените короткий if-else оператором if-elif-else.

---


### LeetCode Problem #9: Palindrome Number (May 17)

> Given an integer x, return True if x is a palindrome integer.
>
> An integer is a palindrome when it reads the same backward as forward.
>
> For example, 121 is a palindrome while 123 is not.

https://leetcode.com/problems/palindrome-number/

Рассмотрим несколько решений этой задачи.

Вы знали что s[::-1] ⏤ переворачивает строку (а также список и кортеж)? Сначала целое x конвертируем в строку s, а затем сравниваем строку с её перевертышем. Это самое простое решение:
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]
```
Необязательно сравнивать целую строку, можно сравнить префикс с перевернутым суффиксом:
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    return s[:len(s)//2] == s[:(len(s)-1)//2:-1]
```
То же самое, что и первое решение, но через итераторы. В данном случае, не создаём перевёртыш строки, а бежим по ней в обратном порядке (reversed). Функция zip умеет бегать одновременно по нескольким iterables. A функция all возвращает True, если не встречает ни одного False!
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    return all(a == b for a,b in zip(s, reversed(s)))
```
Похожее решение, но бегаем только по префиксу и суффиксу:
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    return all(s[i] == s[-i-1] for i in range(len(s)//2))
```
Простой цикл, без всяких comprehensions. Помним, что отрицательный индекс указывает на последние элементы?
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False
    return True
```
То же самое, только бегаем по префиксу и суффиксу:
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    for i in range(0, len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True
```
То же самое, только через цикл while:
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
То же самое, только короче:
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
А тут мы не переводим целое в строку. Младшие цифры x перекидываем в старшие цифры y. То есть y ⏤ это перевернутое целое от x:
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


### LeetCode/Medium #39: Combination Sum (May 25)

Дан массив различных целых чисел (candidates) и целевое целое число (target).

Вернуть все уникальные комбинации кандидатов, такие что сумма кандидатов в комбинации была равна target.

В комбинации кандидат может быть представлен любое количество раз.

Пример 1:
```
candidates = [2,3,6,7]
target = 7
```
Полученные комбинации: `[[2,2,3], [7]]`
* 7 = 7
* 7 = 2 + 2 + 3

Пример 2:
```
candidates = [2,3,5]
target = 8
```
Полученные комбинации: `[[2,2,2,2], [2,3,3], [3,5]]`
* 8 = 2 + 2 + 2 + 2
* 8 = 2 + 3 + 3
* 8 = 3 + 5

https://leetcode.com/problems/combination-sum/

Рассмотрим несколько решений этой задачи.

Функция combination_sum(candidates, target) будет использовать внутреннюю рекурсивную функцию: comb(k, target).

`comb(k, target)` возвращает такие все комбинации, которые суммируются в target и состоят только из первых k кандидатов.

Частные случаи:

* comb(0, 0) должна вернуть всего одно решение, пустое, поэтому: [[]].
* comb(0, target), если target -- не 0, то нет решений: [].

Посмотрите на разницу: есть одно пустое решение [[]] и нет решений вообще [].

Какие ещё частные случаи можно заметить?

* comb(1, target), если target равен candidates[0], то возвращаем: `[[target]]`. \
Действительно, если дан всего один кандидат, причём равный целевому числу, то получаем одну возможную комбинацию.

* comb(1, target), если target не равен candidates[0], то нет решений: [].

Общий случай:

`comb(k, target)` можно разбить на два случая:

1. если пропускаем кандидата под номером k-1 (не включаем его в комбинацию), то делаем рекурсивный вызов: `comb(k-1, target)` -- это часть решения.
2. если кандидат не превышает целевое число, пытаемся включить его в комбинацию. \
Делаем рекурсивный вызов: `comb(k, target-candidates[k-1])`. \
Раз включили в комбинацию, то цель уменьшилась на величину кандидата (`target-candidates[k-1]`). \
Мы не исключаем повторное использование кандидата, поэтому вызываем с параметром k, а не k-1.

Но это ещё не всё: ко всем комбинациям, которые суммируются в значение `target-candidates[k-1]`, добавляем один элемент (кандидата). Только тогда такая комбинация будет суммироваться именно в target.

К рекурсивной функции (`comb`), можно добавить кэширование вызовов: `@cache`.
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
Следующее решение несколько отличается от предыдущего.

Добавлен параметр tail, который собирает текущую комбинацию. Ещё одно отличие: рекурсивная функция добавляет полученную комбинацию в список, а не возвращает её. Ну и интенсивно используется tuple, а не list. Это даёт возможность кэшировать ответы.
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
А в следующем решении возвращаемся к спискам, также уменьшаем количество рекурсивных вызовов (заменяем циклом).

Самый хитрый момент состоит в том, что параметр tail может меняться, но когда и если это происходит, то мы копируем список, чтобы избежать порчи данных.

Тут уж кэширование не будет работать:
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
Остальные решения смотрите тут: https://onlinegdb.com/2S4gQRwbe

---


### LeetCode/Medium #75: Sort Colors (May 25)

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

Начнём с более простой задачи, когда присутствуют только два цвета: red (0) и white (1).

Один из способов отсортировать массив из 0 и 1: это запустить partition:

* Все 0 слева пропускаем, затем все 1 справа пропускаем.
* Если уперлись слева в 1, а справа в 0, то делаем swap.
* Повторяем процесс, пока не проверим все числа.

Теперь с тремя цветами:

* Делим массив так: слева собираем все 0, а справа все 1 и 2.
* Затем делим правую часть массива на 1 (идут в левую часть), а все 2.
```py
from typing import List

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

Ещё более простое решение: подсчитываем сколько 0, 1 и 2 в массиве.
Далее просто заполняем массив: сначала пойдут все 0, потом 1, а затем: 2.
```py
from collections import Counter
```
```py
def sort_colors1(nums: list[int]) -> None:
    c = Counter(nums)
    for i in range(len(nums)):
        nums[i] = 0 if i < c[0] else 1 if i < c[0] + c[1] else 2
```
Следующее решение похоже на предыдущее, но потенциально может быть несколько более быстрым:
```py
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


### Pig It — в одну строчку (Oct 25)

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

Функция `pig_it` перемешивает каждое слово в тексте: первая буква прыгает в конец слова, к которому добавляется суффикс 'ay'. При этом функция не трогает пунктуацию.

Сделаем несколько упрощающих предположений:

* Слова и знаки пунктуации разделены друг от друга ровно одним пробелом.
* В качестве знаков пунктуации допустимы только символы: `','`, `'.'`, `'!'`, `'?'`, `':'`, `';'`.
* Встречаются только одиночные знаки пунктуации (например, запрещён: `???` или `!?`).

#### Реализуем алгоритм по шагам:

Step 1: Как проверить, что данное слово, `w`, состоит только из знака пунктуации?
Можно это сделать следующими способами (результат проверки запоминаем в переменной):
```py
is_punctuation_mark = w == ',' or w == '.' or w == '!' or w == '?' or w == ':' or w == ';'
```
Делаем короче, через проверку в кортеже:
```py
is_punctuation_mark = w in (',', '.', '!', '?', ':', ';')
```
Проверяем, если слово находится среди элементов кортежа.

Поскольку строка — это фактически кортеж символов, то кортеж можно заменить строкой, а проверку наличия элемента в кортеже — заменим проверкой наличия символа в строке:
```py
is_punctuation_mark = w in ',.!?:;'
```
Лучше запомнить все знаки препинания в строковой переменной:
```py
punctuation_marks = ',.!?:;'
```
```py
is_punctuation_mark = w in punctuation_marks
```

Step 2: Если дано слово, `w` (не знак препинания), как из него получить `pigged_w`?
```py
pigged_w = w[1:] + w[0] + 'ay'
```

Сливаем вместе все символы начиная со второго, 
в конце добавляем первый символ слова и `'ay'`. 
Для суффикса введём переменную `suffix`:

```py
suffix = 'ay'
```
```py
pigged_w = w[1:] + w[0] + suffix
```

Step 3: Дано слово, w (без пробелов), если w — это знак препинания, то оставим w как есть, в противном случае, перетасуем буквы w согласно условию задачи. Запомним результат в переменной pigged_w:
```py
is_punctuation_mark = w in punctuation_marks
if is_punctuation_mark:
    pigged_w = w
else:
    pigged_w = w[1:] + w[0] + suffix
```

Step 4: Теперь разобьем текст на слова, и пробежимся по каждому слову:
```py
words = text.split()
for w in words:
    pass
```

Step 5: Получили цикл-for, который ничего не делает, 
но теперь у нас есть возможность обработать каждое слово из `text`:

```py
words = text.split()
for w in words:
    is_punctuation_mark = w in punctuation_marks
    if is_punctuation_mark:
        pigged_w = w
    else:
        pigged_w = w[1:] + w[0] + suffix
```

Step 6: Пока, мы ничего не делам со значениями `pigged_w`. 
Их следует запомнить в списке, скажем, `pigged_words`. 
Теперь все перемешанные слова можно соединить в `pigged_text`:

```py
pigged_words = []
words = text.split()
for w in words:
    ...

pigged_text = ' '.join(pigged_words)
```

Step 7: Соберём весь код в одной функции:

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

Получили желаемое решение. Теперь следует проверить корректность функции и покрыть её тестами (смотрите ниже). Тесты помогут не сломать решение во время оптимизации кода.

#### Refactoring

Сократим код, избавляясь от всех переменных, которые используются только в одном месте:

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

Перепишем команду-if через укороченное выражение-if:

```py
def pig_it(text):
    pigged_words = []
    for w in text.split():
        pigged_w = w if w in punctuation_marks else w[1:] + w[0] + suffix
        pigged_words.append(pigged_w)

    return ' '.join(pigged_words)
```

Избавляемся от `pigged_w`:

```py
def pig_it(text):
    pigged_words = []
    for w in text.split():
        pigged_words.append(w if w in punctuation_marks else w[1:] + w[0] + suffix)

    return ' '.join(pigged_words)
```

Чисто механически заменяем цикл-for и `append` на List Comprehension:

```py
def pig_it(text):
    pigged_words = [w if w in punctuation_marks else w[1:] + w[0] + suffix for w in text.split()]
    return ' '.join(pigged_words)
```

Избавляемся от `pigged_words`:

```py
def pig_it(text):
    return ' '.join([w if w in punctuation_marks else w[1:] + w[0] + suffix for w in text.split()])
```

Можно удалить скобки `[ ]`. Почему? Что поменялось?

```py
def pig_it(text):
    return ' '.join(w if w in punctuation_marks else w[1:] + w[0] + suffix for w in text.split())
```

Мы достигли решения в одну строчку (one-liner).

Иногда код коротких функций записывают на той же строке, сразу после определения функции (тут это излишне, но так иногда делают):

```py
def pig_it(text): return ' '.join(w if w in punctuation_marks else w[1:] + w[0] + suffix for w in text.split())
```

Можно также определять безымянные функции через lambda.

```py
pig_it = lambda text: ' '.join(w if w in punctuation_marks else w[1:] + w[0] + suffix for w in text.split())
```

Заметим, что запоминая lambda в переменной, фактически, даём ей имя. 
Большого смысла в этом нет, но такой код тоже можно встретить.

#### Testing

Группу тестов определяем в одной таблице. 
Для каждого теста указываем входное значение и ожидаемый результат:

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
Функция `test` запускает `pig_it` для каждого теста и сверяет полученный результат с ожидаемым значением.

Code: https://onlinegdb.com/PtHfV39vU
