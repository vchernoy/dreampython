# Math

## Основы Time/Space Complexity

ПРИМЕР 1

Функция принимает список чисел и каждое возводит в квадрат.
```py
def apply_square(nums: list[float]) -> None:
    for i in range(len(nums)):
        nums[i] = nums[i]**2
```
Заметим, что функция ничего не возвращает, а просто меняет свой аргумент, то есть у функции есть side-effect, и она не является pure-function.

Как долго будет работать функция, и сколько дополнительной памяти использует для своей работы?

Прям в секундах и байтах посчитать довольно сложно, но обычно это и не требуется.

Ответ нужно дать в терминах зависимости от размера входных параметров, причём используя асимптотическую нотацию.

Данная функция принимает список, допустим размера n (=len(nums)) и содержит цикл, который выполнит n итераций.

На каждую итерацию приходится группа из элементарных операций, количество и время выполнения которых (почти) не зависит от размера входных данных.

Делаем вывод, что время работы цикла (и самой функции) пропорционально n (или proportional to input size).

Записывают это так:

* Time Complexity: $\mathcal{O}(n)$,
* where $n$ is the input size

$\mathcal{O}$ (или big- $\mathcal{O}$) ⏤ это форма асимптотической записи.

Например, если
* $f(n) = 5 \cdot n + 1000$

Можно записать:
* $f(n) = \mathcal{O}(n)$

То есть $f(n)$, с ростом $n$, растет не быстрее, чем линейно от $n$.
* $g(n) = 10$

Можно записать:
* $g(n) = \mathcal{O}(n)$

Хотя очевидно, что $g(n)$ ⏤ это постоянная функция, и вообще не растёт.

То есть $\mathcal{O}(n)$ ⏤ это некий верхний предел на скорость роста.

Более точно можно было бы записать:
* $g(n) = \mathcal{O}(1)$

То есть $g(n)$ растёт примерно как обычная (любая!) константа.

Кроме $\mathcal{O}()$ используют и другие нотации, например: $\mathcal{\Omega}()$, $\mathcal{\Theta}()$, $\mathcal{o}()$ ⏤ про них как нибудь в другой раз.

Что насчёт памяти?

Функция (почти) не использует дополнительную память.

Даже если $n$ (размер списка) будет огромным, от этого запросы на дополнительную память (кроме input) у данной функции не вырастут.

А значит имеем:
* Space Complexity: $\mathcal{O}(1)$

ПРИМЕР 2
```py
def squares_of1(nums: list[float]) -> list[float]:
    squares = []
    for num in nums:
        squares.append(num**2)
    return squares
```

Это pure-function, нет side-effects.

Функция создаёт новый список, который содержит квадраты полученного списка.

Из-за дополнительной памяти, space complexity пропорционально размеру nums.

* Time Complexity: $\mathcal{O}(n)$,
* Space Complexity: $\mathcal{O}(n)$,
* where $n$ is len(nums)

Время работы $\mathcal{O}(n)$ поскольку время работы append почти не зависит от длинны списка, куда добавляется новый элемент.

Вернее так: иногда append работает очень долго ($\mathcal{O}(n)$), но в большинстве случаев быстро ($\mathcal{O}(1)$).

В среднем, на n операций, получим, что append работает $\mathcal{O}(1)$.

Более точная фраза: amortized averaged time is $\mathcal{O}(1)$.

Можно сказать следующее:

Time and Space Complexity is proportional to the input size.

The algorithm runs in linear time and space.

ПРИМЕР 3:
```py
def squares_of2(nums: list[float]) -> list[float]:
    squares = []
    for num in nums:
        squares = squares + [num**2]
    return squares
```

Функция использует конкатенацию списков вместо append.

И это делает значительно замедляет работу цикла, ведь list-concatenation всегда работает пропорционально размеру соединяемых списков.

На каждой итерации список (и время) постепенно растёт до $\mathcal{O}(n)$.

Количество итераций $n$, умножаем на $\mathcal{O}(n)$, и получим: $\mathcal{O}(n^2)$.

* Time Complexity: $\mathcal{O}(n^2)$.
* Space Complexity: $\mathcal{O}(n)$.
* The algorithm runs in polynomial time and space.

Функция требует много памяти, постоянно создаёт всё более длинный список.

То есть суммарный размера запроса по памяти тоже будет $\mathcal{O}(n^2)$.

Но поскольку временные списки не используются в будущих итерациях, runtime system будут их удалять.

Поэтому строго говоря, Space Complexity: $\mathcal{O}(n)$.

Заметим, что если вместо:
```py
        squares = squares + [num**2]
```
использовать
```py
        squares += [num**2]
```
или
```py
        squares.extend(num**2)
```
то время работы было бы таким же как и для append (в примере 2).

ПРИМЕР 4

То же самое, что и пример 2, но используем List Comprehension.
```py
def squares_of3(nums: list[float]) -> list[float]:
    return [num**2 for num in nums]
```
Это принципиально не меняет поведение алгоритма:
* Time Complexity: $\mathcal{O}(n)$
* Space Complexity: $\mathcal{O}(n)$

The algorithm runs in linear time and space.

ПРИМЕР 5:
```py
def squares_of4(nums: list[float]) -> list[float]:
    squares = []
    for num in nums:
        squares.append(num)

    for i in range(len(nums)):
        squares[i] = squares[i]**2

    return squares
```    
Первый цикл копирует все элементы в новый список.

Второй цикл возводит в квадрат.
* Time Complexity: $\mathcal{O}(n) + \mathcal{O}(n) = \mathcal{O}(n)$
* Space Complexity: $\mathcal{O}(n)$

Как видим, хоть практически функция изменилась, скорее всего будет менее эффективна, но с точки зрения асимптотики ничего не поменялось.

The algorithm runs in linear time and space.

ПРИМЕР 6
```py
def squares_of5(nums: list[float]) -> list[float]:
    squares = nums[:]
    apply_square(squares)
    return squares
```
Тоже вначале копируем список (но без цикла), а потом вызываем функцию apply_square (из примера 1).

Результат тот же, каждая из этих операцию берёт $\mathcal{O}(n)$.

* Time Complexity: $\mathcal{O}(n) + \mathcal{O}(n) = \mathcal{O}(n)$
* Space Complexity: $\mathcal{O}(n)$
* The algorithm runs in linear time and space.

---

## Немного алгебры

### $\mathcal{O}(1)$
* $1000 = \mathcal{O}(1)$
* $1000 \cdot \mathcal{O}(1) = \mathcal{O}(1)$
* $\mathcal{O}(1) \cdot \mathcal{O}(1) = \mathcal{O}(1)$
* $1000 / n = \mathcal{O}(1)$
* $\mathcal{O}(n) / n = \mathcal{O}(1)$

### $\mathcal{O}(n)$
* $\mathcal{O}(n) + \mathcal{O}(n) = \mathcal{O}(n)$
* $1000 \cdot \mathcal{O}(n) = \mathcal{O}(n)$
* $\mathcal{O}(1000 \cdot n) = \mathcal{O}(n)$
* $\mathcal{O}(1) \cdot \mathcal{O}(n) = \mathcal{O}(n)$
* $\mathcal{O}(n) + \mathcal{O}(1) = \mathcal{O}(n)$
* $n \cdot \mathcal{O}(1) = \mathcal{O}(n)$
* $1000 \cdot n + 1000 \cdot \mathcal{O}(n) + 1000 \cdot n \cdot \mathcal{O}(1) = \mathcal{O}(n)$

### $\mathcal{O}(n^2)$
* $100  \cdot  n^2 + 100 \cdot n + 1000 = \mathcal{O}(n^2)$
* $n \cdot \mathcal{O}(n) + n^2  \cdot \mathcal{O}(1) = \mathcal{O}(n^2)$
* $\mathcal{O}(n) \cdot \mathcal{O}(n) = \mathcal{O}(n^2)$
* $1000 \cdot n^2 = \mathcal{O}(n^2)$ 

### $\mathcal{O}(n^3)$
* $n^2 \cdot \mathcal{O}(n) = \mathcal{O}(n^3)$
* $\mathcal{O}(n) \cdot \mathcal{O}(n) \cdot \mathcal{O}(n) = \mathcal{O}(n^3)$
* $4\cdot n^3 + 1000 \cdot n^2 + 10^30 = \mathcal{O}(n^3)$
