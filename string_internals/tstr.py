class TStr:
    def __init__(self, chars=()) -> None:
        self.chars = chars if type(chars) == tuple else tuple(chars)

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
        return self[:k] + new + self[k + len(old):].replace(old, new) if k >= 0 else self

    def join(self, sequence) -> 'TStr':
        res: list[str] = []
        for word in sequence:
            if res:
                res.extend(self.chars)

            res.extend(word.chars)

        return TStr(tuple(res))


'''
Теперь рассмотрим как реализовать метод join. Хотим чтобы заработал следующий код:
'''

space = TStr(' ')
words = [TStr('hello'), TStr('my'), TStr('dear'), TStr('friend')]

print(repr(space.join(words)))
print(repr(space.join([TStr('hello')])))
print(repr(space.join([])))

print(repr(TStr(':').join([TStr('hello')] * 5)))

'''
Output:

TStr("hello my dear friend")
TStr("hello")
TStr("")
TStr("hello:hello:hello:hello:hello")


Метод join аккумулирует все символы в списке res (имеет тип: list[str]), 
который в конце конвертируется в tuple и передаётся в конструктор TStr:

Тут у нас проблема, поскольку __init__ ожидает строку, а не tuple. Исправляем __init__:

    def __init__(self, chars: str | tuple[str] = ()) -> None:
        self.chars = chars if type(chars) == tuple else tuple(chars)

Поясним, во время исполнения вызова метода: space.join(words), в цикле for, self -- это space, sequence -- это words, а ch -- это элементы words.

Если предположить, что список слов может быть огромен, то метод join выделит огромный список символов (размером больше, чем сумма всех символов во всех словах). Далее из списка будет создан кортеж, который у будет частью результата (TStr). Фактически зря использовали память под списков, ведь нам нужен кортеж. Можно ли улучшить?

Следующая версия использует генератор (функция yield_chars):

import itertools


   def join(self, sequence: Iterable['TStr']) -> 'TStr':
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

Можно и в одну, но очень длинную, строку:

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


Остальные методы (из str) можно дописать (в TStr) без особых проблем, какие-то из них будут более сложными, а какие-то более простыми.

Чем еще отличаются строки в разных ЯП, кроме возможности модифицировать и оптимизаций?

Главной задачей строк -- это поддержка текста, который, на самом деле, может содержать не только English, но и другие разные языки. 
Вопрос как правильно кодировать буквы разных алфавитов (кириллица, китайский, иврит) -- является наиболее важной и трудной задачей. Подходы к кодировкам разнятся у разных ЯП, есть даже разница в подходах между Python 2 и Python 3. 
Совершенно верно, строки в Python 2 не совместимы сo строками в Python 3.
'''
