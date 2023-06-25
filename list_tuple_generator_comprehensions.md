# List, Tuple, and Generator Comprehensions

## map/starmap vs. list/generator comprehension & zip (June 2)

Начинаем с импорта:
```py
from functools import partial
from itertools import starmap, repeat
import operator
```
* partial ⏤ позволяет у функций фиксировать параметры, например: partial(operator.add, 10) ⏤ это функция, которая добавляет 10, то есть аналог: lambda x: operator.add(10, х), ну или lambda x: 10 + х.
* repeat ⏤ генерирует значения по кругу, например, repeat(7) создаст бесконечную последовательность: 7, 7, 7,...
* starmap ⏤ аналог встроенной функции map, ниже объясняем разницу.

Допустим дан список целых чисел values и наша цель создать новый список square_values, который будет содержать квадраты значений первого списка. Пишем простой цикл:
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
Вычисляем квадраты, используя list comprehension:
```py
square_values = [v**2 for v in values]
print(square_values)
```
Вместо `v**2` можно использовать `pow(v, 2)` или `v*v`.

### Generators

Заменив квадратные скобки `[v**2 for ...]` на круглые (v**2 for ...), получим generator expression.
Чтобы посчитать квадраты чисел, нужно заставить генератор работать, например, конвертируя его в список:
```py
square_values = (v**2 for v in values)
print(list(square_values))
```
Генератор можно создать через функцию:
```py
def square(values):
    for v in values:
        yield v**2

square_values = square(values)
print(list(square_values))
```
Далее, будем подразумевать вызов функции print после каждого вычисления square_values.

### `map(func, iterable)`

map в каком-то смысле является аналогом generator comprehension.

Первый параметр ⏤ это функция, которую map применяет к компонентам второго параметра (iterable).
* map производит ленивые вычисления, map(lambda v: v**2, values) ⏤ это аналог: (v**2 for v in values) ⏤ lazy evaluation.
* list(map(lambda v: v**2, values)) ⏤ это аналог [v**2 for v in values], то есть производит список ⏤ eager evaluation.

Простое решение с map:
```py
square_values = map(lambda v: v**2, values)
```
Теперь попробуем обойтись без введения функций, через lambda. Такой хитрый вариант: используем partial + pow:
```py
square_values = map(partial(pow, exp=2), values)
```

### `map(func, iterable1, iterable2, ...)`

map может работать сразу с несколькими iterables. В этом случае map применяет функцию к значениям из всех последовательностей, а значит функция должна работать с несколькими аргументами. Вот два примера:
```py
square_values = map(operator.mul, values, values)
```
```py
square_values = map(operator.pow, values, repeat(2))
```
Попробуем проявить креативность и накидать ещё однострочных решений. Все они должны произвести тот же самый список квадратов оригинальных чисел.

### Generator + `zip(iterable1, iterable2, ...)`

Возвращаемся к generator expression, но добавляем zip.

zip группирует несколько последовательностей в одну, состоящую из tuples.

Проще всего это понять на примере:
```py
square_values = (v[0]*v[1] for v in zip(values, values))
```
Далее два примера, которые аналогичны применению map над двумя iterables, но используем generator expression + zip:
```py
square_values = (operator.mul(*v) for v in zip(values, values))
```
```py
square_values = (operator.pow(*v) for v in zip(values, repeat(2)))
```

## `starmap(func, iterable of tuples)` + `zip`

starmap ⏤ это аналог map, но умеет распаковывать кортежи (tuples) автоматически:
```py
square_values = starmap(operator.mul, zip(values, values))
```
```py
square_values = starmap(operator.pow, zip(values, repeat(2)))
```
### Что тут происходит?

Ну и два самых странных решения:

```py
square_values = map(operator.mul, *[values]*2)
```

```py
square_values = map(int(2).__rpow__, values)
```

Code: https://onlinegdb.com/N6qx5p-Da

---

## `filter` vs. list/generator comprehension (June 3))

Начинаем с импорта:

```py
from functools import partial
import operator
```

* `partial` ⏤ фиксирует аргументы у данной функции. \
Например: `partial(int.__and__, 1)` создаёт новую функцию, которая принимает один аргумент, скажем x, и вычисляет `1 & x`. \
Это аналог: `lambda x: int.__and__,(1, х)`, ну или ещё проще: `lambda x: 1 & х`.

* Напомним, что в данном случае речь идёт об двоичном, побитовом AND (Bitwise AND). \
Фактически оставляем самый младший бит в `x`, а остальные обнуляются. Это более хитрый способ посчитать: `x % 2`.

* `int.__and__` ⏤ это оператор Bitwise AND, определённый в классе int.

Допустим дан список целых чисел values. Цель ⏤ найти все нечётные числа и поместить их в новый список: odd_values.

Начнём с простого цикла:
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
Как и ранее накидаем как можно больше различных вариантов сделать то же самое. Например, используем короткую форму if и команду ...:
```py
odd_values = []
for v in values:
    odd_values.append(v) if v % 2 == 1 else ...

print(odd_values)
```
Интересный момент, команда ... является аналогом pass, но последняя, в данном случае, не работает. Есть идеи почему?

### Generator

Следующий способ решить задачу: создать generator. Это можно сделать легко: определяем функцию, и вместо append + return, используем yield:
```py
def odd_only(values):
    for v in values:
        if v % 2 == 1:
            yield v

odd_values = odd_only(values)
print(list(odd_values))
```
Если в предыдущих примерах odd_values ⏤ это уже был готовый список, то в последнем ⏤ odd_values содержит генератор. Чтобы получить реальные значения, нужно заставить генератор вычислить все значения. Именно поэтому в print мы используем list(odd_values).

Теперь используем генератор вместе с короткой формой команды if:
```py
def odd_only(values):
    for v in values:
        (yield v) if v % 2 == 1 else ...

odd_values = odd_only(values)
print(list(odd_values))
```
Заметили, что yield v взят в скобки? Почему?
Далее уже не будем повторять `print(list(odd_values))`.

### Generator Expression

Generator expressions очень похожи на list comprehension:
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
Все эти варианты эквиваленты:
* `v % 2` и `v & 1` одно и тоже;
* так же как и `v % 2 == 1` и `v & 1 == 1`. 
* Заметим, что if v % 2 эквивалентно `if v % 2 != 0`. А в данном случае, это то же самое, что `if v % 2 == 1`.

Если заменить круглые скобки (v for v ...) на квадратные [v for v ...], получим list comprehension.
Помним разницу между lazy evaluation и eager evaluation?

### filter(func, iterable)

`filter` является аналогом generator comprehension:
* `filter(func, iterable)` примерно равен:
* `(func(v) for v in iterable)`.

Предыдущие четыре варианта generator expressions можно переписать используя filter + lambda:
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

### filter и функция одного аргумента

Иногда функция для фильтра уже доступна, то есть можно сэкономить на `lambda`'s.
У каждого целого (int) есть методы `__rmod__` и `__and__`. Используем их:

```py
odd_values = filter(int(2).__rmod__, values)
```
```py
odd_values = filter(int(1).__and__, values)
```
Первых вариант аналогичен:
* `lambda x: x % 2`, а второй аналогичен:
* `lambda x: 1^x`.

### filter+partial

Воспользуемся двоичными операторами, у которых, с помощью partial, зафиксируем первый аргумент:
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

Комбинируем два предыдущих поста. Теперь наша цель ⏤ найти в списке values все нечётные числа и поместить их квадраты в sq_odd_values. Начнём с простого решения:
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
Далее используем короткую форму if:
```py
sq_odd_values = []
for v in values:
    sq_odd_values.append(v**2) if v % 2 == 1 else ...

print(sq_odd_values)
```
Переходим на вложенный list comprehension:
```py
sq_odd_values = [v**2 for v in [v for v in values if v % 2 == 1]]
print(sq_odd_values)
```
Можно сделать тоже самое, но без nested list comprehension:
```py
sq_odd_values = [v**2 for v in values if v % 2 == 1]
print(sq_odd_values)
```

### Generators

Помним, что в дух предыдущих постах мы вводили два генератора? Используем их композицию:
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
Оба генератора: square и odd_only принимают iterable и создают iterables. Получим ли тот же ответ для композиции: `odd_values(square(values))`?

Далее опустим print-команды.

Несложно заменить композицию генераторов одним:
```py
def square_odd(values):
    for v in values:
        (yield v**2) if v % 2 == 1 else ...

sq_odd_values = square_odd(values)
```

### Generator Expressions

Вложенные generator expressions и нет (по аналогии со списками):
```py
sq_odd_values = (v**2 for v in (v for v in values if v % 2 == 1))
```
```py
sq_odd_values = (v**2 for v in values if v % 2 == 1)
```

### `map`/`filter`

По аналогии с предыдущими двумя постами, используем lambda:
```py
sq_odd_values = map(lambda v: v**2, filter(lambda v: v % 2 == 1, values))
```
Или операторы:
```py
sq_odd_values = map(partial(pow, exp=2), filter(partial(operator.and_, 1), values))
```

Code in https://onlinegdb.com/FLDien5qE

---


## Пять способов создать slices in Python (May 20)

Возьмём для примера список, например из 6 слов (words). 
Нужно получить подсписок, например: все слова кроме первого. 
Или подсписок из каждого третьего слова. 
Или все слова с индексами между 2 и 4. 
Этого можно добиться разными способами.

### 1. words[beg:end:step]

Создаём подсписок через words[beg:end:step]. step может быть отрицательным, тогда получим обратный порядок. Этот способ создаёт совершенно новый список, копируя все элементы. Поэтому изменение words никак не влияет на созданный список.
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

То же самое можно добиться и при помощи list comprehension.
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

А это уже generator comprehension (используются круглые скобки). Фактически реальный подсписок создаётся только в последней строчке при конвертации генератора в список. В отличие от предыдущих примеров, изменения в words отобразятся и в tail!
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

Несколько похожий пример с использованием стандартной функции slice(). Эта функция очень похожа на range(), но slice не создаёт последовательность значений (не является iterable), а просто описывает индексы подсписка. Получаем shadow slice (как в предыдущем примере), но в момент вызова words[sliced] ⏤ создаётся список.
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

В последнем примере itertools.islice() возвращает итератор. Тоже вариант shadow slice. Изменения в оригинальном списке повлияют и на значения выдаваемые итератором.
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
