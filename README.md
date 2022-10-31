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

### Backend на FastAPI: mortgage calculator (May 23)

В папке `webapptest` создадим проект. Там сохраним:
* файл `main.py` и
* каталог `venv` (`virtualenv`).

В первую очередь устанавливаем необходимые библиотеки. Скопируйте в терминал следующую команду:
```sh
venv/bin/pip install "fastapi[all]" "uvicorn[standard]"
```
Проверить, что там установилось можно командой:
```sh
venv/bin/pip list
```

#### `main.py` и запуск WEB-сервиса:

Создаём backend и регистрируем API. Декораторы помним?
```py
import fastapi

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return 'loan calculator'
```
Декоратор `@app.get("/")` устанавливает удалённую точку вызова для функции read_root(), которая просто возвращает строку (ничего хитрого!).

Запускаем сервис локально, например, на порту 8000:
```sh
venv/bin/uvicorn main:app --reload --port 8000
```
Output:
```
INFO:     Will watch for changes in these directories: ['/Users/slava/PycharmProjects/webapptest']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [29735] using watchgod
INFO:     Started server process [29737]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
Если всё хорошо, пусть бежит!

Теперь через webbrowser можно вызвать функцию read_root, набрав следующий URL:

http://127.0.0.1:8000/

В браузере должно появиться:
```
"loan calculator"
```
Мы только что запустили минимальный WEB service (backend)!

#### Loan Calculator

Уже знакомы с именованными кортежами? Объекты LoanPayments будут содержать информацию о выплатах за определённый срок. Например за один месяц, год, весь период и т.д.:
```py
import collections
```
```py
LoanPayments = collections.namedtuple(
    'LoanPayments',
    [
        'interest',
        'principle',
        'paid',
        'balance_left',
        'payments_done',
    ],
)
```
Создать объект этого типа можно так:
```py
loan_payments = LoanPayments(
    interest=1000,
    principle=2000,
    paid=1000+2000,
    balance_left=100000 - 3000,
    payments_done=1,
)
```
Основная функция, которая считает выплаты по кредиту на заданном интервале:
```py
def payment(balance: float, term: int, rate: float, payments: int = 1) -> LoanPayments:

    print(f'payment({balance=}, {term=}, {rate=}: {payments=})')

    total_interest, total_principle = 0, 0
    for _ in range(payments):
        interest = balance * rate
        principle = interest / ((1 + rate) ** term - 1)

        total_interest += interest
        total_principle += principle

        balance -= principle
        term -= 1

    return LoanPayments(
        interest=round(total_interest, 2),
        principle=round(total_principle, 2),
        paid=round(total_interest+total_principle, 2),
        balance_left=round(balance, 2),
        payments_done=payments,
    )
```
Входные параметры для функции:
* balance: размер долга по ссуде, например: 100000 ($100К).
* term: оставшееся количество выплат, например: 30 * 12 (30 лет).
* rate: кредитная ставка за один взнос.
* payments: количество взносов, можно например указать: 1 (месяц), 12 (год), 120 (10 лет) или term (за всё время).

Добавляем API:
```py
@app.get("/amortization_loan/")
def amortization_loan(balance: float, months_left: int, annual_rate: float, months_to_pay: int = 1):

    annual_rate *= 0.01
    rate = (1 + annual_rate) ** (1 / 12) - 1

    monthly = payment(balance, months_left, rate, 1)
    annual = payment(balance, months_left, rate, 12)
    total = payment(balance, months_left, rate, months_left)
    paid = payment(balance, months_left, rate, months_to_pay)

    return {
        'monthly': monthly._asdict(),
        'annual': annual._asdict(),
        'total': total._asdict(),
        'paid': paid._asdict(),
    }
```
Теперь в браузере можно указать такой URL:

http://127.0.0.1:8000/amortization_loan/?balance=100000&months_left=360&annual_rate=5&months_to_pay=120

Что означает: вызвать функцию amortization_loan с параметрами:
* balance=100000 ($100К);
* months_left=360 (ссуда на 30 лет);
* annual_rate=5 (5% годовых);
* months_to_pay=120 (интересуют выплаты за 10 лет).

В браузере получим ответ в виде JSON:
```json
{"monthly":{"interest":407.41,"principle":122.64,"paid":530.06,"balance_left":99877.36,"payments_done":1},"annual":{"interest":4855.52,"principle":1505.14,"paid":6360.66,"balance_left":98494.86,"payments_done":12},"total":{"interest":90819.87,"principle":100000.0,"paid":190819.87,"balance_left":0.0,"payments_done":360},"paid":{"interest":44675.09,"principle":18931.53,"paid":63606.62,"balance_left":81068.47,"payments_done":120}}
```
Новый API добавлен, сервис loan calculator работает!

Следующий шаг можно пропустить:

#### Форматирование JSON

JSON можно красиво отформотрировать с помощью вызова модуля: python3 -m json.tool. Запускаем в терминале следующую команду:
```sh
echo '{"monthly":{"interest":407.41,"principle":122.64,"paid":530.06,"balance_left":99877.36,"payments_done":1},"annual":{"interest":4855.52,"principle":1505.14,"paid":6360.66,"balance_left":98494.86,"payments_done":12},"total":{"interest":90819.87,"principle":100000.0,"paid":190819.87,"balance_left":0.0,"payments_done":360},"paid":{"interest":44675.09,"principle":18931.53,"paid":63606.62,"balance_left":81068.47,"payments_done":120}}' | python3 -m json.tool
```
Output:
```json
{
    "monthly": {
        "interest": 407.41,
        "principle": 122.64,
        "paid": 530.06,
        "balance_left": 99877.36,
        "payments_done": 1
    },
    "annual": {
        "interest": 4855.52,
        "principle": 1505.14,
        "paid": 6360.66,
        "balance_left": 98494.86,
        "payments_done": 12
    },
    "total": {
        "interest": 90819.87,
        "principle": 100000.0,
        "paid": 190819.87,
        "balance_left": 0.0,
        "payments_done": 360
    },
    "paid": {
        "interest": 44675.09,
        "principle": 18931.53,
        "paid": 63606.62,
        "balance_left": 81068.47,
        "payments_done": 120
    }
}
```
* За месяц заплатим: $530;
* за год: $6,360;
* за все 30 лет: $190,819;
* за 10 лет: $63,606.

#### Interactive API docs

FastAPI также генерирует точку вызова для интерактивного API. Пока бежит ваш сервис, наберите в браузере следующий URL:

http://127.0.0.1:8000/docs

Должна генерироваться страница для вызова двух функций: `Root Read` и `Amortization Loan`.

Кликаем на стрелочки и далее на "Try it out" и "Execute"!

Получили очень простой UI, через который можно взаимодействовать с сервисом

Full Code: https://onlinegdb.com/7FLyB8K7P

See https://fastapi.tiangolo.com/

---

### LeetCode #39: Combination Sum (Medium Level) (May 25)

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
def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    def comb(k: int, target: int) -> List[List[int]]:
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
def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    def comb(k: int, target: int, tail: Tuple[int]):
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
def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    def comb(k: int, target: int, tail: List[int]):
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

Можно сделать тоже самое через обычный цикл:
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

### LeetCode #75: Sort Colors (Medium) (May 25)

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

def sort_colors0(nums: List[int]) -> None:
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
def sort_colors1(nums: List[int]) -> None:
    c = Counter(nums)
    for i in range(len(nums)):
        nums[i] = 0 if i < c[0] else 1 if i < c[0] + c[1] else 2
```
Следующее решение похоже на предыдущее, но потенциально может быть несколько более быстрым:
```py
def sort_colors2(nums: List[int]) -> None:
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

### map/starmap vs. list/generator comprehension & zip (June 2)

Начинаем с импорта:
```py
from functools import partial
from itertools import starmap, repeat
import operator
```
* partial ⏤ позволяет у функций фиксировать параметры, например: partial(operator.add, 10) ⏤ это функция, которая добавляет 10, то есть аналог: lambda x: operator.add(10, х), ну или lambda x: 10 + х.
* repeat ⏤ генерирует значения по кругу, например, repeat(7) создаст бесконечную последовательность: 7, 7, 7,...
* starmap ⏤ аналог встроенной функции map, ниже объясяем разницу.

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

#### Generators

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

#### `map(func, iterable)`

map в каком-то смысле является аналогом generator comprehension.

Первый параметр ⏤ это функция, которую map применяет к компонентам второго параметра, который должен быть iterable (например, list).
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

#### `map(func, iterable1, iterable2, ...)`

map может работать сразу с несколькими iterables. В этом случае, map применяет функцию к значениям из всех последовательностей, а значит функция должна работать с несколькими аргументами. Вот два примера:
```py
square_values = map(operator.mul, values, values)
```
```py
square_values = map(operator.pow, values, repeat(2))
```
Попробуем проявить креативность и накидать ещё однострочных решений. Все они должны произвести тот же самый список квадратов оригинальных чисел.

#### Generator + `zip(iterable1, iterable2, ...)`

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

### `starmap(func, iterable of tuples)` + `zip`

starmap ⏤ это аналог map, но умеет распаковывать кортежи (tuples) автоматически:
```py
square_values = starmap(operator.mul, zip(values, values))
```
```py
square_values = starmap(operator.pow, zip(values, repeat(2)))
```
#### Что тут происходит?

Ну и два самых странных решения:
```py
square_values = map(operator.mul, *[values]*2)
```
```py
square_values = map(int(2).__rpow__, values)
```
Code: https://onlinegdb.com/N6qx5p-Da

---

### `filter` vs. list/generator comprehension (June 3))

Начинаем с импорта:
```py
from functools import partial
import operator
```
* `partial` ⏤ фиксирует аргументы у данной функции. Например: `partial(int.__and__, 1)` создаёт новую функцию, которая принимает один аргумент, скажем x, и вычисляет `1 & x`. Это аналог: `lambda x: int.__and__,(1, х)`, ну или ещё проще: `lambda x: 1 & х`.

* Напомним, что в данном случае речь идёт об двоичном, побитовом AND (Bitwise AND). Фактически оставляем самый младший бит в x, а остальные обнуляются. Это более хитрый способ посчитать: `x % 2`.

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
Как и ранее накидаем как можно больше различных вариантов сделать тоже самое. Например, используем короткую форму if и команду ...:
```py
odd_values = []
for v in values:
    odd_values.append(v) if v % 2 == 1 else ...

print(odd_values)
```
Интересный момент, команда ... является аналогом pass, но последняя, в данном случае, не работает. Есть идеи почему?

#### Generator

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

#### Generator Expression

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
* также как и `v % 2 == 1` и `v & 1 == 1`. 
* Заметим, что if v % 2 эквивалентно `if v % 2 != 0`. А в данном случае, это тоже самое, что `if v % 2 == 1`.

Если заменить круглые скобки (v for v ...) на квадратные [v for v ...], получим list comprehenstion.
Помним разницу между lazy evaluation и eager evaluation?

#### filter(func, iterable)

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

#### filter и функция одного аргумента

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

#### filter+partial

Воспользыемся двоичными операторами, у которых, с помощью partial, зафиксируем первый агрумент:
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

### `map`+`filter` vs. list/generator comprehension

Комбинируем два предудущих поста. Теперь наша цель ⏤ найти в списке values все нечётные числа и поместить их квадраты в sq_odd_values. Начнём с простого решения:
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

#### Generators

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

Несложно заменить композидцию генераторов одним:
```py
def square_odd(values):
    for v in values:
        (yield v**2) if v % 2 == 1 else ...

sq_odd_values = square_odd(values)
```

#### Generator Expressions

Вложенные generator expressions и нет (по аналогии со списками):
```py
sq_odd_values = (v**2 for v in (v for v in values if v % 2 == 1))
```
```py
sq_odd_values = (v**2 for v in values if v % 2 == 1)
```

#### `map`/`filter`

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

В общем случае: после сортировки слов, на месте r будет находится слово words[indexes[r]].

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

Вроде не сложно. Можно сократить количество строк, используя разные list/dict comprehension. А в качестве упражнения, попробуем вместить весь код в одну строчку (это для тех, кто дотянет до конца!).

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

### Пять задач (LeetCode/easy) с решением в одну строчку (June 24)

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
def majority_еlement(nums: List[int]) -> int:
    return next(v for v,c in Counter(nums).items() if c > len(nums) // 2, None)
```
https://leetcode.com/problems/majority-element/

#### 229. Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊ n / 3 ⌋ times.
```py
def majority_elements(nums: List[int]) -> List[int]:
    return [v for v,c in Counter(nums).items() if c > len(nums) // 3]
```
https://leetcode.com/problems/majority-element-ii/

#### 217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array and return false if every element is distinct.
```py
def contains_dup(nums: List[int]) -> bool:
    return any(c >= 2 for c in Counter(nums).values())
```
```py
def contains_dup(nums: List[int]) -> bool:
    return max(Counter(nums).values()) >= 2
```
https://leetcode.com/problems/contains-duplicate/

#### 350. Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays.
```py
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    return (Counter(nums1) & Counter(nums2)).elements()
```
https://leetcode.com/problems/intersection-of-two-arrays-ii/

---

### Callable в Python (Aug 18)

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

В следующем примере объекты двух классов являются Callable, поскольку у них реализован специальный скрытый метод `__call__`:
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

Стандартная функция all возвращает True если все значения равны True, фактически это тоже самое что `... and ... and ...` .

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
Чтобы избежать многократного создания списков (из-за рекурсивных вызовов) и копирования слов из спика в списов, рекурсивная функция может просто добавлять все найденные слова в один и тот же список:
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


### Что такое строки? (Oct 17)

ЧАСТЬ 1

В Python доступен встроенный тип данных: str (строка). Строки используются для представления текста, слов и отдельных символов. Например: `'Hello World!'` — это константная строка (имеет тип str).

Строка — это последовательность символов конечной длинны.

#### Strings in C ('71), Oberon ('89)

В языках программирования предыдущего поколения, таких как C (1971) и Oberon (1989), строки имели минимальную поддержку (со стороны ЯП). Обычно строки представлялись в виде массива символов, а для обозначения конца строки использовался специальный символ с кодом 0.

В Python такое можно представить в виде списка (list), который может быть частично заполнен символами.

Хотите посчитать длину строки?

Бежим по массиву символов пока не встретим специальный символ "конец строки".

Строки можно было менять, поскольку строка — это просто массив символов (list в Python).

#### Strings in Java ('95), Golang ('09), Python ('91)

Языки программирования нового поколения, такие как Java (1995), Golang (2009) и Python (1991), вводят отдельный тип "строка" (String в Java, string в Golang, str в Python). В новых ЯП строки обычно делают неизменяемыми (immutable/unmodifiable), что делает работу с ними более удобным (почему?).

Так сделано в Python, Golang и Java (и много где ещё).

#### Custom string implementation based on tuples

А что если бы в Python не было бы типа str, можно было бы реализовать свои "строки"?

С некоторыми оговорками и ограничениями, можно, хотя не получим такого-же удобства, как со встроенным типом str.

Для введения новых типов, в Python используется конструкция определения класса (class). Проще всего строку в Python можно реализовать с помощью кортежа (tuple) символов — да, нам всё-же нужны отдельные символы.

Почему используем кортеж, а не список?

Списки можно менять, а кортежи — нет, прям как стандартные строки, так что tuple подходит нам более органично.

Назовём наш строковый тип: TStr, префикс "T" — от слова "tuple", то есть делаем строки на основе tuples.

Начнём с определения класса TStr, введением конструктора (`__init__`) и метода (`__len__`):
```py
class TStr:
    def __init__(self, chars: str = '') -> None:
        self.chars = tuple(chars)

    def __len__(self) -> int:
        return len(self.chars)
```
Объекты класса TStr содержат атрибут chars (символы) — который содержит в tuple отдельные символы.

Метод `__len__` считает длину строки, что равно длине кортежа (`self.chars`). Определение метода `__len__` позволяет использовать объекты TStr в функции len, например теперь такой код будет корректно работать:
```py
s = TStr('Hello World!')
print(len(s))

s = TStr()
print(len(s))
```
Output:
```
12
0
```
К сожалению, попытка вывести на экран объекты TStr при помощи print провалится:
```py
s = TStr('Hello')
print(s)
print(s.chars)
```
Output:
```
<__main__.TStr object at 0x7fb5f424abe0>
('H', 'e', 'l', 'l', 'o')
```
Первый print неявно пытается преобразовать TStr в тип str. Это можно починить определением метода `__str__`:
```py
    def __str__(self) -> str:
        return ''.join(self.chars)
```
Метод `__str__` сливает все символы кортежа (`self.chars`) в нормальную строку (типа str). Теперь получим:
```
Hello
('H', 'e', 'l', 'l', 'o')
```
Разумеется, в гипотетическом Python, без типа str, метод `__str__` был бы не таким, так что это ещё одно необходимое допущение, которое мы делаем для удобства.

Напомним, что встроенные строки (str) позволяют производить множество операций, например: 
слияние, повторение, выделение отдельных символов или подстрок по индексам. 
* Строки можно сравнивать и использовать в качестве ключей в словарях. 
* Строки имеют много методов, например startswith, endswith, find, replace и т.д. 

Всё это можно реализовать в TStr и это будет работать как в стандартном str.

Продолжение следует.

Code: https://onlinegdb.com/PEyCCALh0

---

### Увлекательная симметрия с Черепашкой (Oct 17) 

Как вы думаете, что нарисует следующий алгоритм?

1. Рисуем равносторонний треугольник.
2. Рисуем точку в любом месте внутри треугольника.
3. Следующую точку рисуем посередине между текущей точкой и случайно выбранной вершиной треугольника.
4. Бесконечно долго повторяем последний шаг (3).

Постепенно будет создаваться фрактал из вложенных треугольников.

Давайте попробуем отобразить это на Python. Для графики используем весёлый модуль turtle (черепашка).

Это та самая Черепашка, с которой дети учатся программированию. 

Черепашка может делать следующие операции:

* `down`/`up`: опустить или поднять хвост
* `left`/`right`: повернуться налево или направо
* `forward`: прыгнуть вперёд
* `setpos`: прыгнуть в определенную позицию

Главное, что если черепашка перемещается с опущенным хвостом, то она оставляет след (рисует).

Начнём писать код.

Импортируем черепашку (turtle) и модуль работы со случайными числами (random) —нужно выбирать вершину случайным образом):

```py
import random, turtle

side = 600
vertexes = []
```

* `side` — длинна стороны треугольника, а
* `vertexes` — список координат трёх вершин треугольника.

Устанавливаем максимальную скорость, цвет хвоста и заливки, а также прыгаем в начальную позицию:

```py
turtle.speed(0)
turtle.color('red', 'yellow')
turtle.up()
turtle.setpos(-side / 2, side / 2)
turtle.down()
```

Теперь нарисуем треугольник, и запомним в списке vertexes все его вершины:

```py
turtle.begin_fill()

for _ in range(3):
    turtle.forward(side)
    turtle.right(120)
    vertexes.append(turtle.pos())

turtle.end_fill()
```
Три раза делам следующее: прыгаем вперёд (вдоль стороны треугольника), поворачиваемся на 120 градусов (создаём внутренний угол: 180 - 120 = 60), и запоминаем вершину треугольника в vertexes.

* `begin_fill`/`end_fill` — позволяют залить треугольник неким цветом — это необязательно, можно эти вызовы убрать.

До входа в бесконечный цикл создаём три переменных:

* `total_dots` — для подсчёта нарисованных точек (это необязательно).
* `x`, `y` — положение текущей точки (начнём с 0,0)

```py
total_dots = 0
x = y = 0
while True:
    v_x, v_y = vertexes[random.randint(0, 2)]
    x = (x + v_x) / 2
    y = (y + v_y) / 2
```

* `randint(0, 2)` генерирует случайное целое число от 0 до 2 (включительно) — то есть случайно выбираем вершину.

Далее в том же цикле синим цветом рисуем точку с диаметром 3:

```py
    turtle.up()
    turtle.setpos(x, y)
    turtle.down()
    turtle.dot(3, 'blue')
```

Обновляем статистику нарисованных точек и выводим в консоль каждую тысячу (это необязательно делать).

```py
    total_dots += 1
    if total_dots % 1000 == 0:
        print(f'total dots drawn: {total_dots}')
```
Всё! Запускам с PyCharm и ждём, минут 5, а можно и часик.... К 10,000 точек картинка получается очень даже ничего так.

Медитация!

Code: https://onlinegdb.com/qrT12YxnT

---


### Что такое строки? (Oct 19)

ЧАСТЬ 2

В части 1 мы начали реализовывать класс TStr (строки) на основе tuples (кортежей символов). Вот что у нас уже получилось:
```py
class TStr:
    def __init__(self, chars: str = '') -> None:
        self.chars = tuple(chars)

    def __len__(self) -> int:
        return len(self.chars)

    def __str__(self) -> str:
        return ''.join(self.chars)
```
Следующий метод `__repr__` создаёт строковое представление объекта. 
Отметим, что метод `__str__` вызывается функцией str, a `__repr__` вызывается `repr`. 
Это ещё один случай, когда нам без стандартных строк не обойтись:
```py
    def __repr__(self) -> str:
        return f'{type(self).__name__}("{self}")'
```
Теперь следующий кусок кода будет правильно работать (попробуйте без `__repr__`):
```py
hello = TStr('Hello')
world = TStr('World!')
space = TStr(' ')

print([hello, space, world])
```
Output:
```
[TStr("Hello"), TStr(" "), TStr("World!")]
```

#### TStr concatanation & repetition

Следующие методы необходимы для слияния строк (concatanation) и повторения (repetition).
```py
    def __add__(self, s) -> 'TStr':
        return TStr(self.chars + s.chars)

    def __mul__(self, n: int) -> 'TStr':
        return TStr(n * self.chars)

    def __rmul__(self, n: int) -> 'TStr':
        return TStr(n * self.chars)
```
Отметим, что эти операции основаны на кортежах, то есть используют (делегируют) соответствующие операции над tuple: concatantation и repetition.

Пример, где эти методы используются:
```py
print(hello + space + world)
print(world * 3)
print(3 * world)
```
Output:
```
Hello World!
World!World!World!
World!World!World!
```
Метод `__add__` вызывается там, где над объектами TStr применяется оператор + (concatanation), а `__mul__` и `__rmul__`, там где над TStr и int применяется оператор * (repetition).

#### TStr comparison

Хотим сравнивать объекты TStr, как это позволяют обычные строки? Хотим сортировать списки из TStr? Значит необходимо добавить следующие методы:
```py
    def __eq__(self, x: object) -> bool:
        return self.chars == x.chars

    def __lt__(self, x: 'TStr') -> bool:
        return self.chars < x.chars

    def __le__(self, x: 'TStr') -> bool:
        return self == x or self < x
```
* `__eq__` вызывается операцией `==`,
* `__lt__` вызывается операцией `<`,
* `__le__` вызывается операцией `<=`.

Теперь применим сортировку:
```py
words = [world, hello]
words.sort()
print(words)
```
Output:
```
[TStr("Hello"), TStr("World!")]
```

#### Hashable TStr in `set` & `dict`

Чтобы иметь возможность использовать TStr в set и dict (в качестве ключа), необходимо TStr сделать "hashable", то есть добавить:
```py
    def __hash__(self) -> int:
        return hash(self.chars)
```
Метод `__hash__` вызывается функцией `hash`, которую мы применяем в `__hash__`, 
но уже над значениями типа tuple (`self.chars`) — опять делегируем функциональность к tuple.
Теперь можно создать множество из TStr, как это позволяет стандартный str:
```py
print(set(words))
```
Output:
```
{TStr("Hello"), TStr("World!")}
```
Попробуйте использовать TStr как ключи в `dict` — должно работать. 
А потом уберите `__hash__`, что будет?

#### `TStr[i]`, `TStr[beg:end:step]`, iteration over `TStr`

Теперь предоставим доступ к отдельным символам по индексу, как это позволяют стандартные строки:

```py
    def __getitem__(self, i: int) -> 'TStr':
        return TStr(self.chars[i])
```

Такой код будет работать:

```py
print([hello[0], hello[-1], hello[1:3], hello[:-1], hello[:], hello[::-1]])
```

Output:
```
[TStr("H"), TStr("o"), TStr("el"), TStr("Hell"), TStr("Hello"), TStr("olleH")]
```
Замечательно работают отрицательные индексы и даже взятие подстроки (slices). Работает также шаг и получение перевертыша. Магия! Опять делегировали функционал к tuple! Насколько всё-таки близки строки и tuples.

Следующий код тоже работает благодаря __getitem__:
```py
print(list(hello))
print(list(reversed(hello)))
```
Output:
```
[TStr("H"), TStr("e"), TStr("l"), TStr("l"), TStr("o")]
[TStr("o"), TStr("l"), TStr("l"), TStr("e"), TStr("H")]
```

#### Пробег по символам (TStr стал перечислимым типом):
```py
for ch in hello:
    print(repr(ch))
```
Output:
```
TStr("H")
TStr("e")
TStr("l")
TStr("l")
TStr("o")
```
Можно пробежаться по символам и их соединить:
```py
import functools
res = functools.reduce(lambda x,y: x+y, hello, TStr())
print(repr(res))
```
Output:
```
TStr("Hello")
```
Продолжение следует...

Code: https://onlinegdb.com/2ohZlESkI_

---

### Что такое строки? (Oct 20)

ЧАСТЬ 3

В частях 1 и 2 мы реализовывали часть класса TStr:
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

#### String slicing in Python vs. Java

Благодаря методу `__getitem__`, из строк можно вытаскивать отдельные символы (`s[i]`) или подстроки (`s[beg:end:step]`). 
В Python можно использовать slicing как для строк так и для списков и кортежей. 
Несмотря на то, что строки и slicing присутствуют как в Python, так и в Java и Golang, функциональность slicing реализована по-разному. 
Вернее сделаны разные оптимизации.

Например в Java, при создании подстроки, символы не копируются в новую строку. Вместо этого, созданная подстрока просто указывает на тот же массив символов, который используется в оригинальной строке.

В Python, slicing честно копирует все символы в новую строку.

Иногда подход Java сработает лучше, а иногда подход Python будет работать лучше. При этом разные подходы не меняют правильность работы slicing — это просто вопрос оптимизации под конкретные случаи.

Представьте, что дана очень длинная строка из которой мы создаём короткую подстроку (slice). Что будет происходить в Java и Python?

#### `s.find(x)` vs. `x in s`

Если реализовать метод `s.find(x)` (возвращает индекс подстроки `x` в `s`, или -1 если подстрока `x` не найдена в `s`), 
то можно бесплатно получить и операцию `x in s` 
(которая делегирует проверку в метод `__contains__`):

```py
    def find(self, x: 'TStr') -> int:
        return next((i for i in range(len(self)-len(x)+1) if self[i:i+len(x)] == x), -1)
```
```py
    def __contains__(self, x: 'TStr') -> bool:
        return self.find(x) >= 0
```

Теперь будет работать такой код:

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
```
0
5
6
-1
```

```
True
True
True
False
startswith & endswith
```

Добавим методы:
```py
    def startswith(self, prefix: 'TStr') -> bool:
        return self[:len(prefix)] == prefix

    def endswith(self, suffix: 'TStr') -> bool:
        return self[-len(suffix):] == suffix
```
И проверим:
```py
for w in hello, space, world, hello+space:
    print(hello_world.startswith(w))
```
```py
for w in world, hello, space, space+world:
    print(hello_world.endswith(w))
```
Output:
```
True
False
False
True
```
```
True
False
False
True
```

#### s.replace(old, new)

Метод `replace` реализован через рекурсию, получаем очень простой код:

```py
    def replace(self, old: 'TStr', new: 'TStr') -> 'TStr':
        k = self.find(old)
        return self[:k] + new + self[k+len(old):].replace(old, new) if k >= 0 else self
```

Пример:

```py
print(hello_world.replace(TStr('l'), TStr('L')*3))
```

Output:

```
HeLLLLLLo WorLLLd!
```

Code: https://onlinegdb.com/0CqoCkOm-

---

### Что такое строки? (Oct 23)

ЧАСТЬ 4

В предыдущих частях, была реализована часть класса TStr (строки на основе tuples). 
Вот что получилось:

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

Теперь рассмотрим как реализовать метод `join`. 
Хотим чтобы заработал следующий код:

```py
space = TStr(' ')
words = [TStr('hello'), TStr('my'), TStr('dear'), TStr('friend')]

print(repr(space.join(words)))
print(repr(space.join([TStr('hello')])))
print(repr(space.join([])))

print(repr(TStr(':').join([TStr('hello')]*5)))
```

Output:

```
TStr("hello my dear friend")
TStr("hello")
TStr("")
TStr("hello:hello:hello:hello:hello")
```

Метод `join` аккумулирует все символы в списке `res` (имеет тип: `list[str]`), 
который в конце конвертируется в tuple и передаётся в конструктор TStr:

```py
    def join(self, sequence: Iterable['TStr']) -> 'TStr':
        res: list[str] = []
        for word in sequence:
            if res:
                res.extend(self.chars)

            res.extend(word.chars)

        return TStr(tuple(res))
```
Тут у нас проблема, поскольку `__init__` ожидает строку, а не tuple. 
Исправляем `__init__`:

```py
    def __init__(self, chars: str | tuple[str] = ()) -> None:
        self.chars = chars if type(chars) == tuple else tuple(chars)
```

Поясним, во время исполнения вызова метода: `space.join(words)`, в цикле `for`,
* `self` — это `space`,
* `sequence` — это `words`, а
* `word` — это элементы `words` (`sequence`).
 
Если предположить, что список слов может быть огромен, 
то метод `join` выделит огромный список символов (размером больше, чем сумма всех символов во всех словах). 
Далее из списка будет создан кортеж, который у будет частью результата (TStr). 
Фактически зря использовали память под списков, ведь нам нужен кортеж. 
Можно ли улучшить?

Следующая версия использует генератор (функция `yield_chars`):

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
Можно и в одну, но очень длинную, строку:
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
Остальные методы (из str) можно дописать (в TStr) без особых проблем, какие-то из них будут более сложными, а какие-то более простыми.

Чем еще отличаются строки в разных ЯП, кроме возможности модифицировать и оптимизаций?

Главной задачей строк — это поддержка текста, который, на самом деле, может содержать не только English, но и другие разные языки.

Вопрос как правильно кодировать буквы разных алфавитов (кириллица, китайский, иврит) — является наиболее важной и трудной задачей. Подходы к кодировкам разнятся у разных ЯП, есть даже разница в подходах между Python 2 и Python 3. Совершенно верно, строки в Python 2 не совместимы сo строками в Python 3.

Code: https://onlinegdb.com/o_vdN5LO7

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

Step 4: Теперь разобьем текст на слова, и пробежимся по по каждому слову:
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
Теперь все перемешанные слова можно соеденить в `pigged_text`:

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

---

