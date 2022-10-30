# Dream on Python


### Способы форматирования строк в Python (May 4)

Следующий оператор выводит на печать текст без дополнительной обработки:
```py
print("In 2021 the GDP of America is $22.99T")
```
Получаем:
```
In 2021 the GDP of America is $22.99T
```
Допустим параметры (название страны, год и ВВП) заданы в переменных:
```py
year = 2021
country = 'America'
value = 22.99
```
Следующие способы формирования текста выдают тот же самый результат:
```py
print('In ' + str(year) + ' the GDP of ' + country + ' is $' + str(value) + 'T')
```
```py
print('In %d the GDP of %s is $%.2fT' % (year, country, value))
```
```py
print('In {} the GDP of {} is ${}T'.format(year, country, value))
```
```py
print('In {0} the GDP of {1} is ${2}T'.format(year, country, value))
```
```py
print('In {year} the GDP of {country} is ${value}T'.format(
    year=year, country=country, value=value
))
```
```py
data = {'year':year, 'country':country, 'value':value}
print('In {year} the GDP of {country} is ${value}T'.format(**data))
```
```py
print(f'In {year} the GDP of {country} is ${value}T')
```
Наиболее современным является именно последний вариант, который использует f-string (fast string).

Code in https://onlinegdb.com/xQG_uyOnrj

---

### Формирование однострочного и многострочного текста в Python (May 4)

Следующие четыре примера формируют однострочный текст:

```py
print('"There should be no such thing as boring mathematics." -- Dijkstra\'s quote')
```
```py
print("\"There should be no such thing as boring mathematics.\" -- Dijkstra's quote")
```
```py
print('"There should be no such thing \
as boring mathematics." \
-- Dijkstra\'s quote')
```
```py
print('"There should be no such thing '
      + 'as boring mathematics." '
      + "-- Dijkstra's quote")
```
Вывод на экран:
```
"There should be no such thing as boring mathematics." -- Dijkstra's quote
```

А следующие пять примеров формируют многострочный (точнее двухстрочный) текст:
```py
print('"There should be no such thing as boring mathematics." \n\t-- Dijkstra\'s quote')
```
```py
print("\"There should be no such thing as boring mathematics.\" \n\t-- Dijkstra's quote")
```
```py
quote = '"There should be no such thing as boring mathematics." \n\
\t-- Dijkstra\'s quote'
print(quote)
```
```py
print(""""There should be no such thing as boring mathematics."
    -- Dijkstra\'s quote""")
```
```py
quote = """"There should be no such thing as boring mathematics."
    -- Dijkstra\'s quote"""
print(quote)
```
Вывод на экран:
```
"There should be no such thing as boring mathematics."
    -- Dijkstra's quote
```
The code to play: https://onlinegdb.com/tVtkO7Mcc

---

### Знакомство с методами `str.split()` и `str.join()` (May 4)

Используем `split()`, чтобы поделить текст на слова.
* Например: `text.split(' ')` делит строку text используя разделитель `' '` (space). Метод возвращает список строк (list of str). 

А чтобы склеить слова, используем обратный метод: `join()`.
* Например, `' '.join(words)` соединит все слова из списка words в одну строку, склеивая их символом `' '`:

```py
quote = 'Simplicity is prerequisite for reliability.'
print(f"Dijkstra's quote: {quote}")

words = quote.split(' ')
print(f"Split using ' ':  {words}")

text = ' '.join(words)
print(f"Join using ' ':   {text}")
print()
```

Можно использовать композицию вызовов (вызвать метод на результате предыдущего метода):
```py
print(' '.join(quote.split()))
print(' '.join(words).split(' '))
print()
```
А теперь сравниваем, что результат работы двух функций производит оригинал:
```py
print(f'the produced text equals original quote: {text == quote}')
print()

print(f'" ".join(quote.split(" ")) == quote: {" ".join(quote.split(" ")) == quote}')

print(f'" ".join(words).split(" ") == words: {" ".join(words).split(" ") == words}')
```
Code to play: https://onlinegdb.com/l1GEcnq3s

---

### Операция `+` в Python (May 5)

В Python применять операцию `+` можно не только к числам, но и к строкам, спискам, и даже кортежам. Примеры:
```py
print(100 + 5)
print(100. + 5.)
print('100' + '5')
print([100] + [5])
print((100,) + (5,))
print()

print('Say' + ' 5 times hi')
print(['Say',] + [5, 'times', 'hi'])
print(('Say',) + (5, 'times', 'hi'))
print()
```
Результат программы:
```
105
105.0
1005
[100, 5]
(100, 5)

Say 5 times hi
['Say', 5, 'times', 'hi']
('Say', 5, 'times', 'hi')
```

Можно предыдущий скрипт оформить в виде таблички и цикла, который применит + к каждой паре значений из таблицы.
```py
tab = (
    (100, 5), 
    (100., 5.), 
    ('100', '5'), 
    ([100], [5]), 
    ((100,), (5,)),
)

for a, b in tab:
    c = a + b
    print(f'{a!r:6} + {b!r:4} = {c!r:8} -- type: {type(c).__name__}')

print()

tab = (
    ('Say', ' 5 times hi'),
    (['Say',], [5, 'times', 'hi']),
    (('Say',), (5, 'times', 'hi')),
)

for a, b in tab:
    c = a + b
    print(f'{a!r:8} + {b!r:18} = {c!r:25} -- type: {type(c).__name__}')
```

Получим вывод с указанием типов результатов (int, float, str, list, tuple):
```
100    + 5    = 105      -- type: int
100.0  + 5.0  = 105.0    -- type: float
'100'  + '5'  = '1005'   -- type: str
[100]  + [5]  = [100, 5] -- type: list
(100,) + (5,) = (100, 5) -- type: tuple

'Say'    + ' 5 times hi'      = 'Say 5 times hi'          -- type: str
['Say']  + [5, 'times', 'hi'] = ['Say', 5, 'times', 'hi'] -- type: list
('Say',) + (5, 'times', 'hi') = ('Say', 5, 'times', 'hi') -- type: tuple
```

Code to play with: https://onlinegdb.com/9Ej3RmaOu

---


### Unpacking in Python (May 9)

Допустим где-то определён список (list).
```py
t = ['say', 5, 'times', 'hi']
print(t)
```
Компоненты списка можно присвоить отдельным переменным, то есть распаковать, всего одной командой:
```py
do_that, how_many, times, what = t
print(do_that, how_many, times, what)

(do_that, how_many, times, what) = t
print(do_that, how_many, times, what)
```
Можно распаковать список во время вызова функции, например:
```py
print(*t)
```
Стандартная функция print() использует запаковку (packing) параметров, поскольку определена как: print(*objects, ...). То есть, в последней строчке, список вначале распаковывается, а внутри print() запаковывается.

Output:
```
['say', 5, 'times', 'hi']
say 5 times hi
say 5 times hi
say 5 times hi
```
Можно распаковывать отдельные компоненты списка:
```py
do_that, *how_many_times, what = t
print(do_that, how_many_times, what)
print(do_that, *how_many_times, what)

print()

do_that, *something = t
print(do_that, something)
print(do_that, *something)
```
Output:
```
say [5, 'times'] hi
say 5 times hi

say [5, 'times', 'hi']
say 5 times hi
```
Распаковка работает для кортежей (tuple) похожим образом. Для словарей есть свой тип (un-)packing.

Code: https://onlinegdb.com/NvuGy8Oo8

---

### Операция * в Python (May 11)

В Python умножать на число можно не только числа, но и строки, списки и кортежи. Умножение чего-либо на 4 означает сложить "это самое" четыре раза. Примеры:
```py
print(20 * 4)
print(20. * 4)
print('20' * 4)
print([20] * 4)
print((20,) * 4)
```
Output:
```
80
80.0
20202020
[20, 20, 20, 20]
(20, 20, 20, 20)
```
БОЛЕЕ СЛОЖНЫЕ ПРИМЕРЫ:
```py
print('say hi, ' * 3)
print('Hello my darling! ' * 2)
print(['Say', 2, 'times', 'hi'] * 2)
print(list(range(3)) * 2)
print(tuple(range(3)) * 2)
```
Output:
```
say hi, say hi, say hi, 
Hello my darling! Hello my darling! 
['Say', 2, 'times', 'hi', 'Say', 2, 'times', 'hi']
[0, 1, 2, 0, 1, 2]
(0, 1, 2, 0, 1, 2)
```
Code: https://onlinegdb.com/26vDswZYs

---

### Инициализируем многомерные массивы (lists) в Python правильно! (May 12)

Заполняем двухмерные массивы (3х2), нулями, True и последовательными числами:
```py
print([[0] * 3 for _ in range(2)])
print([[True] * 3 for _ in range(2)])
print([list(range(3)) for _ in range(2)])
```
Output:
```
[[0, 0, 0], [0, 0, 0]]
[[True, True, True], [True, True, True]]
[[0, 1, 2], [0, 1, 2]]
```
Кортежи кортежей, списки кортежей, списки списков:
```py
print((tuple('#'*i for i in range(3)),)*2)
print([tuple('#'*i for i in range(3))]*2)
print([['#'*i for i in range(3)]]*2)
```
Output:
```
(('', '#', '##'), ('', '#', '##'))
[('', '#', '##'), ('', '#', '##')]
[['', '#', '##'], ['', '#', '##']]
```
В последней команде print, массив (list) содержит вложенных список. Двухмерный массив строится при помощи оператора повторения * (repetition). Это может создать непредсказуемые проблемы.

Смотрим следующий пример:
```py
broken_grid = [list(range(3))] * 2
print(broken_grid)
broken_grid[0][0] = 100 
print(broken_grid)
```
Output:
```
[[0, 1, 2], [0, 1, 2]]
[[100, 1, 2], [100, 1, 2]]
```
Изменение в элементе (0,0) также изменило и значение в (1,0). В действительности broken_grid[0] и broken_grid[1] -- указывают на один и тот же список. Скорее всего это не то, что мы хотели получить.

Правильно инициализировать сложные массивы так:
```py
grid = [list(range(3)) for _ in range(2)]
print(grid)
grid[0][0] = 100 
print(grid)
```
Output:
```
[[0, 1, 2], [0, 1, 2]]
[[100, 1, 2], [0, 1, 2]]
```
Code: https://onlinegdb.com/bBCb2LO_u

---

### Operator `star` for lists and tuples:

#### List repetition:
```py
values = [2, 5, 13]
repeated_values = values * 2
print(repeated_values)
```
Output:
```
[2, 5, 13, 2, 5, 13]
```
#### Partial unpacking:
```py
x, y, z = values
print(x, y, z)

x, *yz = values
print(x, yz)
```
Output:
```
2 5 13
2 [5, 13]
```
#### Arguments unpacking:
```py
print(values)
print(*values)
```
Output:
```
[2, 5, 13]
2 5 13
```
#### Yet another argument unpacking:
```py
def impress(a, b, c):
    print(a, b, c)

impress(*values)
```
Output:
```
2 5 13
```
#### Functions with arbitrary number of positional argument:
```py
def impress_any(*args):
    print(args)

impress_any(x, y, z)
impress_any(*values)
```
Output:
```
(2, 5, 13)
(2, 5, 13)
```
https://onlinegdb.com/-8B_D1JMB

---

### The Art of Print (May 15)

#### Print string and list of its letters:
```py
s = 'hello world'
print(s)
print(list(s))
print(*list(s))
```
Output:
```
hello world
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
h e l l o   w o r l d
```
#### Print list with sep:
```py
print(*list(s), sep='')
print(*list(s), sep=',')
print(*list(s), sep=' ')
```
Output:
```
hello world
h,e,l,l,o, ,w,o,r,l,d
h e l l o   w o r l d
```
#### Apply str.join to list:
```py
print(''.join(list(s)))
print(','.join(list(s)))
print(' '.join(list(s)))
```
Output:
```
hello world
h,e,l,l,o, ,w,o,r,l,d
h e l l o   w o r l d
```
#### Apply str.join to str:
```py
print(''.join(s))
print(','.join(s))
print(' '.join(s))
```
Output:
```
hello world
h,e,l,l,o, ,w,o,r,l,d
h e l l o   w o r l d
```
#### Print f-strings:
```py
print(f'{s=}')
print(f'{list(s)=}')
print(f"{' '.join(s)=}")
```
Output:
```
s='hello world'
list(s)=['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
' '.join(s)='h e l l o   w o r l d'
```
Code in https://onlinegdb.com/nSMCNF6w1

---

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

### Iterable или не iterable? (May 15)

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
На самом деле, не часто приходится работать с итераторами напрямую. Понимать какой объект является iterable может быть полезно, поскольку с такими объектами хорошо работает цикл for ⏤ как оператор, так и короткая форма (list/tuple/generator comprehension).
Один способ узнать, является ли объект iterable ⏤ это выяснить, есть ли у него метод __iter__. Этот метод используется итератором. Проверить наличие метода можно через hasattr:
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

### Iterable или не iterable: Part 2, May 15

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
