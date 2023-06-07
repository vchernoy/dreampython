## Generators, Iterables, Callables

### The Art of Generators (May 15)

Синтаксически генераторы похожи как на функции, так и на списки и на кортежи. Создать генератор можно через определение функции, которая использует оператор yield. Следующая функция определяет генератор, который выдаёт три числа: 1, 10, 100.
```py
def gen_1_10_100():
    yield 1
    yield 10 
    yield 100 
```
Создаём генератор через вызов функции. Генерировать все значения можно через конвертацию генератора в list.
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
Тип объекта g ⏤ это generator. Конвертация в список даёт [1, 10, 100]. Может быть несколько неожиданно, но повторная конвертация выдаёт пустой список [].

Почему?

Ну, генератор выдал все, что было: 1, 10, 100. А дальше более нечего генерировать! Нужно создавать новый генератор!
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
Генератор можно передавать как параметр в функции, где ожидается получить последовательность значений. Проще, где работает список, может (но не обязательно!) сработать и генератор.
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
Генератор можно создать и через generator comprehension. Похоже на list comprehension, но в круглых скобках (...).
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
И такой генератор можно передать (не всегда!) в функции, где ожидается список:
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
Ещё больше generator comprehension:
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
И ещё:
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
Кстати, объект range(3) похож на генератор, но не является им. Списки, кортежи, генератор и range ⏤ это iterable объекты. Поэтому и похожи!
```py
print(f'{type(range(3))=}')
```
Output:
```
type(range(3))=<class 'range'>
```

Code in https://onlinegdb.com/uV9ygOawD

---


### Iterables -- Part 1 (May 15)

Из итерируемых объектов можно создать итератор, который позволяет пробежать по компонентам объекта в цикле for.
Лучше понять это на примерах. Берём список: [1, 10, 100]. Поскольку список являются iterable, из него можно создать итератор:
```py
it = iter([1, 10, 100])
```
Итератор неявно создаётся и используется в цикле for:
```py
for elem in [1, 10, 100]:
    print(elem)
```
На самом деле, нечасто приходится работать с итераторами напрямую. 
Понимать какой объект является iterable, может быть полезно, поскольку с такими объектами хорошо работает цикл for ⏤ как оператор, 
так и короткая форма (list/tuple/generator comprehension).
Один способ узнать, является ли объект iterable ⏤ это выяснить, есть ли у него метод `__iter__`. 
Этот метод используется итератором. Проверить наличие метода можно через hasattr:
```py
print(f"{hasattr([1, 10, 100], '__iter__')=}")
```
Output:
```
hasattr([1, 10, 100], '__iter__')=True
```
Иногда такой проверки будет недостаточно: метод вроде как есть, а его вызов завершается аварийно. Поэтому лучше создать итератор явно и ловить возможную аварийную ситуацию:
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
Теперь напишем вспомогательную функцию print_iterable_or_not, которая для каждого объекта из данной таблицы выведет на экран полезную информацию (тип объекта, если объект iterable, какие элементы находятся в объекте):
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
Выглядит громоздко, посмотрим как её использовать. Создаём таблицу из разных значений: списка, кортежа, множества, range и генератора. Всё это примеры iterable объектов и их можно легко использовать в цикле for.
Функция print_iterable_or_not должна определить их всех как iterable.
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
Для каждого объекта из таблицы, функция вывела информацию о типе (list, tuple, set, range, generator), подтвердила, что все они iterable (True), вывела на печать элементы этих объектов (0, 1, 2) и размер (3 элемента).
Генераторы можно создавать комбинацией из функции и yield. Другой способ ⏤ это использовать generator comprehension. Проверим, если любые генераторы являются iterable.
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
Так и вышло: все генераторы являются итерируемыми объектами (они кстати ещё являются и итераторами!).

Code: https://onlinegdb.com/hoEB0NXUG

---

### Iterables -- Part 2 (May 15)

Идём дальше: строки (str) и словари (dict) -- итерируемые. Строка итерируется по буквам, а словарь по своим ключам.
Более интересные примеры: классы-генераторы и файлы. Эти типы тоже итерируемые!
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
Строку можно представить как кортеж из букв, соответственно итерация по строке ⏤ работает так же как итерация по кортежу букв.

Словари содержат ассоциации между ключами и значениями. По умолчанию итерация по словарю пробегает по ключам. Чтобы пробежать по значениям, нужно воспользоваться методом: dict.values() или dict.items().

Класс-генератор работает примерно также, как и функция-генератор, но может содержать состояние. То есть, может генерировать разные последовательности значений.
Файл, открытый на чтение ⏤ это iterable, а значит чтение из файла можно производить с помощью цикла for.

Многие стандартные функции/классы генерируют последовательности, то есть они являются iterable. В модуле itertools можно найти много функций, которые являются iterable. Очень полезный модуль.

Многие стандартные функции/классы генерируют последовательности, то есть они являются iterable. В модуле itertools можно найти много функций, которые являются iterable. Очень полезный модуль.
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
Следующие две таблицы также содержат итерируемые объекты: пустые контейнеры и sole.
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

### Iterables -- Part 3 (May 15)

Настало время показать примеры объектов, которые не являются итерируемыми. В первую очередь это числа (целые, вещественные), булевские значения (True, False), и конечно None.

Никаких сюрпризов: по объектам типов int, float, bool, NoneType итерироваться в циле for не получится.
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
Функции, стандартные или определённые программистом, а также типы, классы и модули тоже не являются iterable.
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


### Callables (Aug 18)

В Python объект может быть Callable, то есть, его можно вызвать как обычную функцию.

Стандартная функция callable проверяет, является ли данный объект "вызываемым".

Очевидно, что любая функция, метод, в том числе внутренние и lambda — являются Callable.
Напишем простую программу и протестируем разные объекты на это свойство.
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
Функция add а также результат вызова mk_power_add(1) — эти примеры функций, которые просто суммируют два аргумента

То есть это примеры Callable, a значит callable(add) и callable(mk_power_add(1) вернёт True.

Также `callable(lambda a, b: a+b)` тоже вернёт True.

Далее приведём примеры статической функции (функция класса) и метода:
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
Обе функции `A.add` и `Power(1).add` суммируют два аргумента и являются Callable.

В следующем примере объекты двух классов являются Callable, 
поскольку у них реализован специальный скрытый метод `__call__`:

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

Вызовы `callable(Add())` и `callable(MkPowerAdd(1))` вернут True.

В следующем примере берём функцию с тремя аргументами, в которой фиксируем один аргумент, получим частичную функцию с двумя аргументами. Тоже Callable:
```py
def power_add(a: int, b: int, k: int): return a**k + b**k
```
Вызов `callable(functools.partial(power_add, k=1))` вернёт True.

Библиотечные функции `int.__add__`, operator.add — тоже Callable.

Движемся вперёд: для удобства зафиксируем степень k=1 и определим таблицу объектов для проверки на Callable:
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
Каждый объект по сути является аналогом операции +. Выполним вызов на аргументах a=12 и b=5 и проверим результат:
```py
a, b = 12, 5
```
```py
for func in tab:
    print(f'{callable(func)=}, {func.__name__}, {func(12, 5)=}')
```
Получим табличку:
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
