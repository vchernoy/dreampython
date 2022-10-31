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

---

### Iterable или не iterable: Part 3 (May 15)

Настaло время показать примеры объектов, которые не являются итерируемыми. В первую очередь это числа (целые, вещественные), булевские значения (True, False), и конечно None.

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
Функции, стандартные или определённые програмистом, а также типы, классы и модули тоже не являются iterable.
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


### Mortgage Calculator: namedtuple, custom types, operator overloading (May 16)

Возьмём учебный пример: подсчет процентов и выплат по fixed-rate mortage. Допустим цена дома $500,000, начальный взнос: 20%. Это можно выразить следующим кодом на Python:
```py
home_price = USD * 500000
down_payment = home_price * 0.2
mortgage = home_price - down_payment

print(f'{home_price=}')
print(f'{down_payment=}')
print(f'{mortgage=}')

loan_to_value = mortgage / home_price

print(f'{loan_to_value=:.1%}')
```
Тут мы заодно посчитали LTV, который в данном примере составит: 80% (ну раз первый взнос: 20%).

Мы тут пока не определили USD, но можно догадаться, речь про $1, а значит USD * 500000 означает: $500,000.
Недостающий кусок кода разберём чуть позже, а пока посмотрим на вывод данного кода.

Output:
```
home_price=$500,000.00
down_payment=$100,000.00
mortgage=$400,000.00

loan_to_value=80.0%
```
Магическим образом числа форматируются как цены, хотя сама команда print этого вроде не делает.
Определим, что ссуда берётся под 5% годовых на 30 лет. Пересчитываем в проценты за один месяц. Также вводим понятие amortization term которое означает срок ссуды в количестве месяцев:
```py
mortgage_rate = 0.05
monthly_rate = (1 + mortgage_rate) ** (1 / 12) - 1

print(f'{mortgage_rate=:.1%}')
print(f'{monthly_rate=:.3%}')

mortgage_term = 30
amortization_term = mortgage_term * 12
```
Output:
```
mortgage_rate=5.0%
monthly_rate=0.407%
```
Теперь считаем считаем выплаты как по процентам так и возврат по ссуде. Вычисления скрыты в функции, которую разберём чуть позже.
```py
monthly_interest, monthly_principle = payment(mortgage, amortization_term, monthly_rate)
monthly_payment = monthly_interest + monthly_principle
print(f'{monthly_interest=}')
print(f'{monthly_principle=}')
print(f'{monthly_payment=}')
```
Output:
```py
monthly_interest=$1,629.65
monthly_principle=$490.57
monthly_payment=$2,120.22
```
Опять магия: цены форматируются корректно!

#### Функция `payment()`

А вот и недостающая функция подсчёта выплат по ссуде:
```py
def payment(balance: Dollar, term: int, rate: float) -> Tuple[Dollar, Dollar]:
    interest = balance * rate
    principle = interest / ((1 + rate) ** term - 1)

    return interest, principle
```
Считает по известным формулам и возвращает пару (tuple): оплата процентов и возврат ссуды. В сумме получим (месячный) платёж. На самом деле, этой функции всё равно, речь про месяцы или года. Используются абстрактные: balance, term, rate!
Упрощая, допустим баланс по ссуде $400К, годовой процент: 5%, ссуда на 30 лет, то функция payment($400,000, 30, 5%) посчитает:
```py
interest = $400,000 * 5% = $20,000
principle = $20,000 / (1.05^30 - 1) = $6,020
```
Общий платёж (за год): $5,000 + $1,505 = $26,020.

В терминах целых годов, ответ будет не совсем верный. Более правильным будет сделать пересчёт по месяцам. Именно поэтому вы вызываем эту функцию как payment($400,000, 12*30, 0.407%).
Заметим, что функция имеет аннотацию к типам и для balance указан тип Dollar, который мы пока нигде не определили.

#### Тип `Dollar`

Dollar ⏤ это класс, который наследует все поля и свойства другого типа collections.namedtuple. Можно и без наследования обойтись, но namedtuple является очень полезным типом, с которым следует познакомиться.

Тип namedtuple позволяет определить наименованные кортежи. Как раз Dollar ⏤ это кортеж из всего одной но именованной компоненты: amount. Как и обычные tuple, namedtuple тоже является неизменяемым ⏤ ещё одно полезное свойство.

Можно конечно же использовать namedtuple напрямую, например так:
```py
Dollar = namedtuple('Dollar', 'amount', defaults=(1,))
```
Тут мы определяем новый тип: неизменяемый именованный кортеж с полем amount (со значением по умолчанию: 1). Но этого недостаточно, если хотим производить арифметические операции с объектами типа Dollar.

Поэтому Dollar наследует поле amount и свойства immutability, но определяет свои операторы. 
Например:
* __mul__() помогает переопределить оператор умножения значения типа Dollar на некое число. Результатом умножения будет значение типа Dollar.

Это позволяет писать такой код: Dollar(500) * 10 ⏤ получим: Dollar(5000).

* Метод __add__() позволяет писать такой код: Dollar(500) + Dollar(80) ⏤ получим: Dollar(580).

* Метод __truediv__() позволяет считать:
```py
Dollar(500) / Dollar(10) = 50 или
Dollar(500) / 50 = Dollar(10).
```
* Метод __str__() красиво форматирует объекты типа Dollar, тут и появляется: $5,000 вместо 5000.

```py
from collections import namedtuple
```
```py
class Dollar(namedtuple('Dollar', 'amount', defaults=(1,))):
    def __mul__(self, other: Union[int, float]) -> 'Dollar':
        return Dollar(self.amount * other)

    def __truediv__(self, other: Union[int, float, 'Dollar']) -> 'Dollar':
        return self.amount / other.amount \
        if type(other) == Dollar \
        else Dollar(self.amount / other)

    def __add__(self, other: 'Dollar') -> 'Dollar':
        return Dollar(self.amount + other.amount)

    def __sub__(self, other: 'Dollar') -> 'Dollar':
        return Dollar(self.amount - other.amount)

    def __str__(self) -> str:
        return f'${self.amount:,.2f}' \
        if self.amount >= 0 \
        else f'-${-self.amount:,.2f}'

    def __repr__(self) -> str:
        return str(self)
```
Теперь можно ввести недостающий доллар:
```py
USD = Dollar(1)
```
Code: https://onlinegdb.com/EySDwsUIo

---

### Декораторы в Python (May 17)

Покажем, как к некой функции добавить дополнительные свойства без того, чтобы менять её код. Пусть, например, у нас есть функция:
```py
def test_func(x, y):
    ...
```
Один из простых способов достичь этого ⏤ это написать декоратор. В качестве примера, можно создать decorator, который при вызове функции печатает входные параметры и возвращаемое значение.

Чтобы применить декоратор, скажем log_call, к функции test_func, нужно декорировать последнюю специальным образом, добавив @log_call перед определением функции:
```py
@log_call
def test_func(x, y):
    print('I am doing some magic!')
    print(f'I am using the parameters: {x=}, {y=}')
    print('Biggest magic has done.')
    return 'done'
```
Эффект от декоратора проявится при вызове функции test_func:
```py
print(test_func(10, 'hi'))
```
Output:
```
test_func(10,hi)
I am doing some magic!
I am using the parameters: x=10, y='hi'
Biggest magic has done.
test_func: done
done
```
Первая и предпоследняя строки печатаются самим декоратором log_call, который реализован следующим образом:
```py
def log_call(some_func):
    def call_it(*args):
        print(f'{some_func.__name__}({",".join(str(arg) for arg in args)})')
        ret = some_func(*args)
        print(f'{some_func.__name__}: {ret}')
        return ret

    return call_it
```
Как видим, декоратор log_call ⏤ это функция, которая принимает на вход другую функцию (some_func). Декоратор оборачивает вызов some_func в другую функцию call_it, которая как раз и выводит на экран
* имя вызванной (декодируемой) функции:some_func.__name__,
* переданные параметры: ",".join(str(arg) for arg in args) и
* результирующее значение: ret.

Заметим, что call_it() запаковывает все полученные параметры в tuple: args. А далее, распаковывает кортеж при передаче параметров в функцию some_func().

Code: https://onlinegdb.com/kML69mab7

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
Не обязательно сравнивать целую строку, можно сравнить префикс с перевернутым суффиксом:
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    return s[:len(s)//2] == s[:(len(s)-1)//2:-1]
```
Тоже самое, что и первое решение, но через итераторы. В данном случае, не создаём перевёртыш строки, а бежим по ней в обратном порядке (reversed). Функция zip умеет бегать одновременно по нескольким iterables. A функция all возвращает True, если не встречает ни одного False!
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
Тоже самое, только бегаем по префиксу и суффиксу:
```py
def is_palindrome(x: int) -> bool:
    s = str(x)
    for i in range(0, len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True
```
Тоже самое, только через цикл while:
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
Тоже самое, только короче:
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

### Декораторы в Python: Part 2 (May 18)

Рассмотрим ещё один простой декоратор: @cache. Этот decorator запоминает результат вызова функции и при повторном вызове с такими же параметрами использует сохранённое значение.

Передаваемые в функцию параметры используются как ключ в словаре cached, который сохраняет возвращаемые значения.
```py
def cache(some_func):
    cached = {}

    def call_it(*args):
        if args in cached:
            return cached[args]
        ret = some_func(*args)
        cached[args] = ret
        return ret

    return call_it
```
Теперь, если мы декорируем функцию двумя декораторами: @cache и @log_call следующим образом:
```py
@cache
@log_call
def test_func(x, y):
    print('I am doing some magic!')
    print(f'I am using the parameters: {x=}, {y=}')
    print('Biggest magic has done.')
    return 'done'
```
то при повторных вызовах функции test_func:
```py
print(test_func(10, 'hi'))
print(test_func(10, 'hi'))
```
на экране получим следующее:
```
test_func(10,hi)
I am doing some magic!
I am using the parameters: x=10, y='hi'
Biggest magic has done.
test_func: done
done
done
```
Результат второго вызова ⏤ всего лишь одна строка: done. Декоратор запомнил ответ (done) и просто вернул его при повторном вызове.

Если произведём вызов функции с другими параметрами, то функция исполнится, как и ожидается:
```py
print(test_func(10, 'hello'))
```
Output:
```
test_func(10,hello)
I am doing some magic!
I am using the parameters: x=10, y='hello'
Biggest magic has done.
test_func: done
done
```
Декоратор @cache ещё иногда называется “memoize” (или "memoization"). Чаще всего его можно встретить для рекурсивных функций. Например, напишем функцию, вычисляющую числа Фибоначчи:
```py
@cache
@log_call
def fib(n: int) -> int:
    return fib(n - 1) + fib(n - 2) if n >= 2 else n
```
Функцию можно по желанию декорировать @cache и/или @log_call.

Без мемоизации вызов fib(5) произведёт огромное количество повторяющихся рекурсивных вызовов, попробуйте fib(5) с и без @cache. Фактически @cache многократно уменьшает время выполнения функции при больших n.

Вернёмся к декоратору @log_call, и добавим индентацию (сдвиг "принтов" вправо) в зависимости от глубины рекурсивных вызовов:
```py
def log_call(some_func):
    depth = [0]
    def call_it(*args):
        indent = 't' * depth[0]
        print(f'{indent}{some_func.__name__}({",".join(str(arg) for arg in args)})')
        depth[0] += 1
        try:
            ret = some_func(*args)
            print(f'{indent}{some_func.__name__}: {ret}')
            return ret
        finally:
            depth[0] -= 1

    return call_it
```
В переменой depth (да, тут используем список из одного элемента, почему так?) сохраняем глубину рекурсивного вызова. От depth зависит сдвиг вправо (индентация).

Оператор try-finally для учебного примера не обязателен, но тут мы хотим показать, что при любой аварии нужно вернуть depth на прежнее значение. Попробуйте убрать try-finally и искусственно добавить вызов исключительной ситуации (например поделите на 0) ⏤ в результате индентация сломается.

Применяем оба декоратора к fib():
```py
print(f'{fib(5)=}')
print(f'{fib(5)=}')
```
Output:
```
fib(5)
	fib(4)
		fib(3)
			fib(2)
				fib(1)
				fib: 1
				fib(0)
				fib: 0
			fib: 1
		fib: 2
	fib: 3
fib: 5
fib(5)=5
fib(5)=5
```
Видим как работает индентация. Также видно, что повторный вызов приводит к немедленному ответу!
В модуле functools можно найти стандартные декораторы. Например, там уже реализован @functools.cache: https://docs.python.org/3/library/functools.html

Code: https://onlinegdb.com/zYm7xeYeg

---

### Пять способов создать slices in Python (May 20)

Возьмём для примера список, например из 6 слов (words). Нужно получить подсписок, например: все слова кроме первого. Или подсписок из каждого третьего слова. Или все слова с индексами между 2 и 4. Этого можно добиться разными способами.

#### 1. words[beg:end:step]

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
#### 2. list comprehension + range(beg, end, step)

Тоже самое можно добиться и при помощи list comprehension.
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
#### 3. generator comprehension + range

А это уже generator comprehension (используются круглые скобки). Фактически реальный подсписок создаётся только в последней строчек при конвертации генератора в список. В отличие от предыдущих примеров, изменения в words отобразятся и в tail!
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

#### 4. slice & words[slice(beg, end, step)]

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
#### 5. itertools.islice(words, beg, end, step)

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

----


### Что нового в Python 3.10 (May 22)

Для демонстрации некоторых старых и новых возможностей, напишем функции работы с арифметическими выражениями, представленными в виде вложенных списков.

Примеры:
* `[+, 10, 20, 30]` представляет (10 + 20 + 30), что равно: 60.
* `[*, 5, 10, [+, 10, 20]]`, что означает: (5 * 10 * (10 + 20)), и это равно: 1500.

Первым элементом списка идёт операция (+, *, можно ещё ввести: min, max, и т.д.), за которой идут операнды, к которым применяется эта операция. Причём каждый операнд может представлять тоже арифметическое выражение, представленное списком.

Начнём с класса, который определяет допустимые операторы (+, *, min, max).
```py
class OP:
    def __init__(self, name: str, apply: Callable[[Iterable], Any]):
        self.name = name
        self.apply = apply

    def __repr__(self) -> str:
        return self.name
```
```py
class Ops:
    ADD = OP('+', sum)
    MUL = OP('*', 
             lambda values: functools.reduce(operator.mul, values, 1))
    MIN = OP('min', min)
    MAX = OP('max', max)
```
Можно было бы обойтись и без OP, Ops, а вместо ADD, MUL, MIN, MAX, использовать '+', '-', 'min', 'max'. Но наш подход несколько снижает вероятность сделать ошибки в описании выражений.

В качестве рабочего арифметического выражения возьмём следующее:
```py
expr = [
    Ops.MUL,
    5,
    20,
    5,
    [Ops.ADD, 10, 20],
    [Ops.MIN, 5, 15, 25]
]
```
Оно представляет: (5 * 20 * 5 * (10 + 20) * min(5, 15, 25), что равно 75000.

Функцию, которая вычисляет такие выражения, написать несложно:
```py
def calc(expr: Sequence|int|float) -> int|float:
    try:
        return expr[0].apply(
            calc(expr[i]) for i in range(1, len(expr))
        )
    except TypeError:
        return expr
```
Напомним, что expr[0] содержит оператор (например, Ops.ADD), если конечно expr ⏤ это Sequence (list является Sequence).

Функция производит вычисления рекурсивно ⏤ это естественный подход, поскольку выражения тоже определены рекурсивно.

Для каждого операнда, функция вызывает сама себя. Если операнд оказался не Sequence (а имеет простой тип: int, float), то генерируется ошибка, которая обрабатывается в try-except. Простой операнд возвращается как есть (return expr).

В Python 3.10 было введено обозначения для объединения типов: int|float, что означает: или int или float. В предыдущих версиях Python пришлось бы писать так: Union[int, float].
Пробуем вычислить выражение:
```py
print(f'{expr=}')
print(f'{calc(expr)=}')
```
Ouput:
```
expr=[*, 5, 20, 5, [+, 10, 20], [min, 5, 15, 25]]
calc(expr)=75000
```
На удивление написать функцию, которая переводит такие выражения в обычный формат несколько сложнее:
```py
def to_str(expr: Sequence|int|float) -> str:
    try:
        op = expr[0]
        match op:
            case OP(name='+'|'*', apply=_):
                joiner = f' {op} '
                maybe_func = ''
            case _:
                joiner = ', '
                maybe_func = f'{op}'
        return f'{maybe_func}({joiner.join(to_str(expr[i]) for i in range(1, len(expr)))})'
    except TypeError:
        return str(expr)
```
Принцип тот же: рекурсия пробегается по операндам. Но тут мы используем новую конструкцию match-case (введена в Python 3.10).

Заметим, что `[+, 5, 10]` и `[min, 5, 10]` должны отобразиться совершенно по разному: (5 + 10) против min(5, 10). Поэтому используются ветки case. В конце-концов сводим к вызову `joiner.join(to_str(expr[i]) for i in range(1, len(expr)))`.

Вызов `str.join()` объединяет все операнды, или через оператор (например: ' + ') или запятыми (', ').

Команда match-case ⏤ это расширенный (более читаемый?) вариант старой доброй команды: if-elif-else.

Поскольку `to_str(expr)` ⏤ это правильное арифметическое выражение, его можно посчитать используя стандартную функцию: eval(). Удобно этим воспользоваться, чтобы проверить, что to_str и calc ⏤ выдают согласованные результаты.
```py
print(f'{to_str(expr)=}')
print(f'{eval(to_str(expr))=}')
print(f'{calc(expr)==eval(to_str(expr))=}')
```
Output:
```
to_str(expr)='(5 * 20 * 5 * (10 + 20) * min(5, 15, 25))'
eval(to_str(expr))=75000
calc(expr)==eval(to_str(expr))=True
```

Code: https://onlinegdb.com/Q9M1jLNIo

---
