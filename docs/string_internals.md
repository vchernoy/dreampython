# String Internals

## Что такое строки? ⏤ Part 1 (Oct 17)

В Python доступен встроенный тип данных: str (строка). Строки используются для представления текста, слов и отдельных символов. Например: `'Hello World!'` — это константная строка (имеет тип str).

Строка — это последовательность символов конечной длинны.

### Strings in C ('71), Oberon ('89)

В языках программирования предыдущего поколения, таких как C (1971) и Oberon (1989), строки имели минимальную поддержку (со стороны ЯП). Обычно строки представлялись в виде массива символов, а для обозначения конца строки использовался специальный символ с кодом 0.

В Python такое можно представить в виде списка (list), который может быть частично заполнен символами.

Хотите посчитать длину строки?

Бежим по массиву символов пока не встретим специальный символ "конец строки".

Строки можно было менять, поскольку строка — это просто массив символов (list в Python).

### Strings in Java ('95), Golang ('09), Python ('91)

Языки программирования нового поколения, такие как Java (1995), Golang (2009) и Python (1991), вводят отдельный тип "строка" (String в Java, string в Golang, str в Python).
В новых ЯП строки обычно делают неизменяемыми (immutable/unmodifiable), что делает работу с ними более удобным (почему?).

Так сделано в Python, Golang и Java (и много где ещё).

### Custom string implementation based on tuples

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

```text
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

```text
<__main__.TStr object at 0x7fb5f424abe0>
('H', 'e', 'l', 'l', 'o')
```

Первый print неявно пытается преобразовать TStr в тип str. Это можно починить определением метода `__str__`:

```py
    def __str__(self) -> str:
        return ''.join(self.chars)
```

Метод `__str__` сливает все символы кортежа (`self.chars`) в нормальную строку (типа str). Теперь получим:

```text
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

Code: [OnlineGDB](https://onlinegdb.com/PEyCCALh0)

---

## Что такое строки? ⏤ Part 2 (Oct 19)

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

```py
[TStr("Hello"), TStr(" "), TStr("World!")]
```

### TStr concatenation & repetition

Следующие методы необходимы для слияния строк (concatenation) и повторения (repetition).

```py
    def __add__(self, s) -> 'TStr':
        return TStr(self.chars + s.chars)

    def __mul__(self, n: int) -> 'TStr':
        return TStr(n * self.chars)

    def __rmul__(self, n: int) -> 'TStr':
        return TStr(n * self.chars)
```

Отметим, что эти операции основаны на кортежах, то есть используют (делегируют) соответствующие операции над tuple: concatenation и repetition.

Пример, где эти методы используются:

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

Метод `__add__` вызывается там, где над объектами TStr применяется оператор + (concatenation), а `__mul__` и `__rmul__`, там где над TStr и int применяется оператор * (repetition).

### TStr comparison

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

```py
[TStr("Hello"), TStr("World!")]
```

### Hashable TStr in `set` & `dict`

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

```py
{TStr("Hello"), TStr("World!")}
```

Попробуйте использовать TStr как ключи в `dict` — должно работать.
А потом уберите `__hash__`, что будет?

### `TStr[i]`, `TStr[beg:end:step]`, iteration over `TStr`

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

```py
[TStr("H"), TStr("o"), TStr("el"), TStr("Hell"), TStr("Hello"), TStr("olleH")]
```

Замечательно работают отрицательные индексы и даже взятие подстроки (slices). Работает также шаг и получение перевертыша. Магия! Опять делегировали функционал к tuple! Насколько всё-таки близки строки и tuples.

Следующий код тоже работает благодаря `__getitem__`:

```py
print(list(hello))
print(list(reversed(hello)))
```

Output:

```py
[TStr("H"), TStr("e"), TStr("l"), TStr("l"), TStr("o")]
[TStr("o"), TStr("l"), TStr("l"), TStr("e"), TStr("H")]
```

### Пробег по символам (TStr стал перечислимым типом)

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

Можно пробежаться по символам и их соединить:

```py
import functools
res = functools.reduce(lambda x,y: x+y, hello, TStr())
print(repr(res))
```

Output:

```py
TStr("Hello")
```

Продолжение следует...

Code: [OnlineGDB](https://onlinegdb.com/2ohZlESkI_)

---

## Что такое строки? ⏤ Part 3 (Oct 20)

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

### String slicing in Python vs. Java

Благодаря методу `__getitem__`, из строк можно вытаскивать отдельные символы (`s[i]`) или подстроки (`s[beg:end:step]`).
В Python можно использовать slicing как для строк, так и для списков и кортежей.
Несмотря на то, что строки и slicing присутствуют как в Python, так и в Java и Golang, функциональность slicing реализована по-разному.
Вернее сделаны разные оптимизации.

Например, в Java, при создании подстроки, символы не копируются в новую строку. Вместо этого, созданная подстрока просто указывает на тот же массив символов, который используется в оригинальной строке.

В Python, slicing честно копирует все символы в новую строку.

Иногда подход Java сработает лучше, а иногда подход Python будет работать лучше. При этом разные подходы не меняют правильность работы slicing — это просто вопрос оптимизации под конкретные случаи.

Представьте, что дана очень длинная строка из которой мы создаём короткую подстроку (slice). Что будет происходить в Java и Python?

### `s.find(x)` vs. `x in s`

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

```text
HeLLLLLLo WorLLLd!
```

Code: [OnlineGDB](https://onlinegdb.com/0CqoCkOm-)

---

## Что такое строки? ⏤ Part 4 (Oct 23)

В предыдущих частях, была реализована часть класса TStr (строки на основе tuples). Вот что получилось:

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

Теперь рассмотрим как реализовать метод `join`. Хотим чтобы заработал следующий код:

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

[code snippet](https://github.com/vchernoy/dreampython/blob/f310f4678e5bbacb72541d19a9104835a268210c/string_internals/tstr.py#LL54C1-L63C1)

Тут у нас проблема, поскольку `__init__` ожидает строку, а не tuple. Исправляем `__init__`:

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
Далее из списка будет создан кортеж, который будет частью результата (TStr).
Фактически зря использовали память под список, ведь нам нужен кортеж.
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

Вопрос как правильно кодировать буквы разных алфавитов (кириллица, китайский, иврит) — является наиболее важной и трудной задачей. Подходы к кодировкам разнятся у разных ЯП, есть даже разница в подходах между Python 2 и Python 3. Совершенно верно, строки в Python 2 не совместимы со строками в Python 3.

Code: [OnlineGDB](https://onlinegdb.com/o_vdN5LO7)
