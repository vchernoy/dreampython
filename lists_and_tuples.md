# Lists & Tuples

## Unpacking in Python (May 9)

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

## Инициализируем многомерные массивы (lists) в Python правильно! (May 12)

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

## Operator `star` for lists and tuples:

### List repetition:
```py
values = [2, 5, 13]
repeated_values = values * 2
print(repeated_values)
```
Output:
```
[2, 5, 13, 2, 5, 13]
```
### Partial unpacking:
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
### Arguments unpacking:
```py
print(values)
print(*values)
```
Output:
```
[2, 5, 13]
2 5 13
```
### Yet another argument unpacking:
```py
def impress(a, b, c):
    print(a, b, c)

impress(*values)
```
Output:
```
2 5 13
```
### Functions with arbitrary number of positional argument:
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

## The Art of Print (May 15)

### Print string and list of its letters:
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
### Print list with sep:
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
### Apply str.join to list:
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
### Apply str.join to str:
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
### Print f-strings:
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
