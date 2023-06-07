# Dream on Python

## Strings and String Formatting

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

## Operations `+` and `*` on Numbers, Strings, Lists, and Tuples


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


## [Lists & Tuples](lists_and_tuples.md)

## [Generators, Iterables, Callables](generators_iterables_callables.md)

## [Decorators](decorators.md)

## [List, Tuple, and Generator Comprehensions](list_tuple_generator_comprehensions.md)

## [String Internals](string_internals.md)

## [Solving Coding Problems](solving_coding_problems.md)

## Project: Mortgage Calculator

### Mortgage Calculator: namedtuple, custom types, operator overloading (May 16)

Возьмём учебный пример: подсчет процентов и выплат по fixed-rate mortgage. Допустим цена дома $500,000, начальный взнос: 20%. Это можно выразить следующим кодом на Python:
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
Теперь считаем выплаты как по процентам, так и возврат по ссуде. Вычисления скрыты в функции, которую разберём чуть позже.
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
def payment(balance: Dollar, term: int, rate: float) -> tuple[Dollar, Dollar]:
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

Тип namedtuple позволяет определить наименованные кортежи. Как раз Dollar ⏤ это кортеж из всего одной, но именованной компоненты: amount. Как и обычные tuple, namedtuple тоже является неизменяемым ⏤ ещё одно полезное свойство.

Можно конечно же использовать namedtuple напрямую, например так:
```py
Dollar = namedtuple('Dollar', 'amount', defaults=(1,))
```
Тут мы определяем новый тип: неизменяемый именованный кортеж с полем amount (со значением по умолчанию: 1). Но этого недостаточно, если хотим производить арифметические операции с объектами типа Dollar.

Поэтому Dollar наследует поле amount и свойства immutability, но определяет свои операторы. 
Например:
* `__mul__()` помогает переопределить оператор умножения значения типа Dollar на некое число. 
Результатом умножения будет значение типа Dollar. \
Это позволяет писать такой код: Dollar(500) * 10 ⏤ получим: Dollar(5000).

* Метод `__add__()` позволяет писать такой код: Dollar(500) + Dollar(80) ⏤ получим: Dollar(580).

* Метод `__truediv__()` позволяет считать:
```py
Dollar(500) / Dollar(10) = 50 или
Dollar(500) / 50 = Dollar(10).
```
* Метод `__str__()` красиво форматирует объекты типа Dollar, тут и появляется: $5,000 вместо 5000.

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

Уже знакомы с именованными кортежами? Объекты LoanPayments будут содержать информацию о выплатах за определённый срок. Например, за один месяц, год, весь период и т.д.:
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

JSON можно красиво отформатрировать с помощью вызова модуля: python3 -m json.tool. Запускаем в терминале следующую команду:
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


## Misc


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


### Что нового в Python 3.10 (May 22)

Для демонстрации некоторых старых и новых возможностей, напишем функции работы с арифметическими выражениями, представленными в виде вложенных списков.

Примеры:
* `[+, 10, 20, 30]` представляет (10 + 20 + 30), что равно: 60.
* `[*, 5, 10, [+, 10, 20]]`, что означает: (5 * 10 * (10 + 20)), и это равно: 1500.

Первым элементом списка идёт операция (+, *, можно ещё ввести: min, max, и т.д.), далее следуют операнды, к которым применяется эта операция. Причём каждый операнд может представлять тоже арифметическое выражение, представленное списком.

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
Output:
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

Заметим, что `[+, 5, 10]` и `[min, 5, 10]` должны отобразиться совершенно по-разному: (5 + 10) против min(5, 10). Поэтому используются ветки case. В конце концов сводим к вызову `joiner.join(to_str(expr[i]) for i in range(1, len(expr)))`.

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

Code: [https://onlinegdb.com/Q9M1jLNIo]

---


## Programming Languages Overview

### Part 1: Fortran, JS

Начнём обзор с совершенно непохожих языков программирования: древнего Фортрана и современного JavaScript.

Fortran -- был создан в конце 1950-х годов. Цели создания: численные вычисления. Использовали Fortran для математических расчётов в прикладных науках.

На данный момент шансы попасть на позицию, где может понадобиться Fortran -- ничтожно малы.

Так зачем я решил упомянуть о таком динозавре, да ещё и начал с него этот обзор?

* Во-первых, Fortran продолжает развиваться, были приняты новые стандарты Fortran 90, 95, 2003, 2008, 2018.

* Во-вторых, этот ЯП до сих пор достаточно популярен (в своём кругу).

* В третьих, Fortran занял определенную нишу (численные вычисления) и плотно там застрял.

Фортран -- это пример того, как некая технология (ЯП) может занять определённую нишу и остаться там навечно. Часто другие ЯП таким образом сравнивают с Фортраном.

#### Scripting Programming Languages

Обычно к этому классу причисляют: JavaScript, Python, Ruby, PHP.

JS (JavaScript) -- был создан в 1995. JS -- это ещё один ЯП, который имеет свою явную нишу. JS -- это в первую очередь WEB программирование и UI (user interface). Фактически это пример, аналогичный Фортрану: вряд ли кто-то сможет серьёзно потеснить JS на его поле.

Стоит заметить, что JS это не просто язык для UI, JS -- это целая экосистема из набора различных технологий, которые позволяют быстро разрабатывать полноценные WEB-приложения.

JS можно встретить во многих, особенно молодых, компаниях (в стартапах) -- где присутствует WEB, будет и JS в каком-то виде.

Многие coding bootcamps строят свои курсы на основе JS, это позволяет студентам создать полноценные проекты.


### Part 2: Python, C/C++

Python был создан в 1991 с целью написания скриптов. Название было придумано в честь британского комедийного телешоу: "Летающий цирк Монти Пайтона".

Python и JS несколько похожи по характеристикам и даже имеют некое пересечение по использованию в WEB программировании. Оба языка могут быть использованы для написания внутренней часть (backend) WEB. Но в отличие от JS, Питон не используется в разработке интерфейсной части (frontend) WEB.

Если вам нужно полноценное WEB приложение, то интерфейс пишут на JS, а внутреннюю часть на JS или Питоне (или ещё много на чём). То есть хоть Python и используется в WEB, но это не его главная ниша.

Так где же Питон является "Фортраном" своего времени?

Есть несколько областей, где Питон сидит довольно прочно: построение инфраструктуры (DevOps), тестирование (automation), и похоже настоящая ниша: численные методы, статистика, data processing, AI/ML.

Похоже Python — это современный Fortran — оба используются для математики, только Python больше для искусственного интеллекта.

Если брать coding bootcamp, которые преподают Python, то скорее всего там будет еще и JS, для написания интерфейсов (WEB frontend), a Питон будет использоваться для всего остального.

#### C/C++

Язык программирования C был создан в 1972 для разработки ОС (операционной системы) Unix. Это компилированный язык и совершенно не похож на JS или Python.

В своё время имел очень важные свойства: мог быть использован на разных платформах. На сегодняшний момент, несмотря на очевидную устарелость, C очень глубоко застрял в областях системного программирования: разработка ОС, компиляторов (других языков программирования), встроенных систем, и т.д. Например, первые версии Python были написаны на C.

Шансы работать с C или хотя бы познакомиться с ним, есть только у студентов и выпускников специальностей компьютерных наук, и то не в каждом университете.

C++ появился в 1983 году, как расширение языка C. Оба имеют похожие цели и используются в тех же областях. Для нашего обзора не так важно, чем они там отличаются.

Наверное имеет смысл упомянуть о такой особенности: C++ гораздо сложнее, чем C. Описание языка C занимает пару сот страниц, в то время как описание C++ — это тысячи страниц, причём ну очень сложного текста.

Найти профи, который бы знал 99.9% C++ не так-то просто, скорее всего такие уникумы сидят в комитете стандартизации самого языка.

В общем, ни C, ни C++ не встречаются на трехмесячных курсах, даже за полгода нереально существенно познакомиться даже с C, не говоря уже про C++.


### Part 3: Ruby vs. Python vs. JS

Ruby был создан в 1995 ⏤ в том же году, что и JS (JavaScript). Основная ниша Ruby ⏤ это серверное WEB-программирование, поэтому разумно его сравнить с другими конкурентами: Python и JS.

Ruby ⏤ более молодой ЯП, чем Python, но для разработки серверной части WEB приложение, Ruby предлагает более продвинутою платформу: "Ruby on Rails". Питоновский фреймворк: Django был выпущен позже и не получил такого распространения.

Хотя Ruby имеет потенциал, но кроме WEB, пока не завоевал серьёзных позиций в других сферах. От части это происходит из-за более компактного комьюнити, чем у Python.

Если сравнивать Ruby с JS, то последний предлагает гораздо большее количество платформ: Node.js, React, Angular. Также не забываем, что JS доминирует в клиентской части WEB, где фактически ни Python ни Ruby не являются ему конкурентами.

Очевидно имеем, что если хотим разработать WEB приложение (front-end + backend), то можно оставаться в рамках JS, а можно выбрать Ruby (или Python) для backend/server-side, а JS использовать для front-end/client-side.

По свойствам, эти три языка программирования несколько похожи, но наверное Python будет несколько проще изучать. Хотя если цель выйти на WEB front-end, то без JS никак. В coding boot camps, вы скорее всего, встретите комбинацию из этих языков программирования и их фреймворков.


### Part 4: Java

Java также был создан в 1995, но по целям и свойствам очень сильно отличается от JS, Python, Ruby. Java — это скорее, что-то среднее между C++ (помним этого монстра) и Python. То есть барьер входа в Java гораздо выше, чем в Python. Описание огромное, пакетов, платформ море, но не всё так страшно как в C++.

Если вспомнить немного истории, то Java был создан компанией Sun с целью выдавить компанию Microsoft со своей сферы. Особо это не помогло. Sun была куплена Oracle, а Microsoft выпустила свой аналог Java для Windows: C# (платформа .NET).

Изначально Java представляли как встроенную OS, ну там типа все чайники и утюги будут "говорить Java" (вам это ничего не напоминает?). Но сейчас конечно про это все забыли.

Да данный момент, Java широко используется в разработке WEB приложений и аппликаций для мобильных устройств (для ОС Android). Также Java можно встретить в тестировании, инфраструктуре, обработке данных и даже в AI.

Java — почти везде, и остаётся одним из самых популярных ЯП. Но скорее всего вы его встретите в более старых больших корпорациях. Молодые компании и стартапы предпочтут или что-то из тройки Python, Ruby, JS или какие-то более новые технологии.

Хотя позиции у Java всё ещё сильны, прямые приемники и разные конкуренты потихоньку оказывают на него давление: Scala, Kotlin (для Android), Golang (WEB), Python.



### Part 5: От Java к Scala и Kotlin

Напомню, что Java ⏤ это язык программирования общего назначения. По синтаксису более похож на C/C++/C#, но проще и дешевле в использовании. Java по сложности находится где-то посередине между чрезмерной сложностью C++ и компактностью Python.
Java также применяется в таких сферах как: тестирование, инфраструктура, AI и в разработке мобильных приложений для Andorid. Стоит отметить, что под Android используется несколько специфическая версия Java. Так что даже имея опыт в разработке на Java, придётся потратить некое время на изучение самой Android OS и на версию Java for Android (основанная на более старых стандартах Java).
Современные языки программирования Scala и Kotlin развивают платформу Java в разных направлениях, сохраняя с ней полную совместимость. В проектах на Scala можно использовать код на Java. То же самое справедливо и для Kotlin.

#### Scala

Разработка Scala началась в 2001 году в стенах академии в Швейцарии, а публичный выпуск состоялся в 2004 году.

Scala по началу постоянно ломала обратную совместимость с более старыми версиями. Это создавало огромные проблемы для адаптации этой платформы крупными компаниями. С одной стороны все были готовы уже бежать неважно куда от увядающей Java, а с другой стороны, переходы на новые версии Scala могли остановить проекты на неопределенное время.

Некоторые крупные компании полностью отказывались от Scala в пользу Java, например, LinkedIn. В то же время компания Twitter толкала Scala вперёд, не смотря ни на какие проблемы.

На данный момент релизы Scala более-менее стабилизировались, но развитие Scala также дало толчок и развитию Java. Так что в результате бурного перехода с Java на Scala так и не состоялось.

Основное отличие Scala от Java: уменьшение verbosity (многословие). Программы на Scala более компактны, чем аналогичные на Java. Меньше писать, лучше читать ⏤ меньше ошибок, вроде как бы так. В принципе, в этом смысле, у Scala та же идея, что и у Python ⏤ всё делать как можно короче и проще.

Но с другой стороны, Scala настолько мощный ЯП, что там можно создавать свои DSP (domain specific language). То есть, можно написать такую программу на Scala, что без дополнительных "подсказок", даже самый крутой специалист по Scala не сообразит, что это такое перед ним.

#### Kotlin

Kotlin был разработан российской компанией JetBrains в 2011. Авторам хотелось создать что-то "как в Scala, только быстрее, проще и под Android". Они так и сделали!

В 2017 году, компания Google, которая владеет Android OS, заявила о полной поддержке Kotlin в качестве платформы для разработки мобильных приложений под Android.

Так что если хотите разрабатывать мобильные приложения под Android то можно начинать сразу с Kotlin. Всё будет и быстрее и проще. Хотя в какой-то момент, придётся глянуть и на Java (в том числе на Java 1.6) и чуток ужаснуться.

Разумеется доступны всякие boot camps и курсы, обучающие разработке Android App на Kotlin с нуля.


## Bootcamps & Job search

### Coding Bootcamp: App Academy

Перед началом основных курсов, можно взять подготовительные 4-х недельные курсы, которые идут в двух вариантах: online и live. Если после подготовительных курсов студент не поступает на основной курс (bootcamp), они обещают вернуть деньги.
На подготовительном курсе изучают основы JavaScript.

#### Курсы интенсивной подготовки

App Academy позволяет оплатить всю сумму (lump sum) или же отодвинуть основную оплату на момент, когда студент находит работу с доходом $50,000+. Отсроченные выплаты требуют депозита в $3,000, также нужно иметь в виду, что суммарно такой вариант выходит дороже.

Предлагаются три программы (все online):

16-недель
* Изучают: Ruby, JavaScript, HTML, SQL, Git, AWS
* Цена: $17,000 (lump sum)
* В рассрочку: $23,000-27,000.

24-недели
* Изучают: Python, JavaScript, HTML, SQL, Git, Docker, Heroku
* Цена: $20,000 (lump sum)
* В рассрочку: $31,000.

48-недель (part-time)
* Изучают: Python, JavaScript, HTML, SQL, Git, Docker, Heroku
* Цена: $22,000 (lump sum)
* В рассрочку: $39,000.

На всех трёх курсах студенты изучают JavaScript, ну это и понятно, ведь он используется для построения клиентской части аппликаций (front-end). Для разработки серверной части (backend), первый курс использует Ruby как самую простую платформу, а два других курса: JavaScript и Python.



### Термины, которые можно встретить в Job Descriptions

* Front-end (client-side development) — разработка интерфейса WEB-страничек, предполагается использовать технологии: HTML, CSS, JavaScript, ReactJS
* Backend (server-side development) — разработка основной логики программы, сохранение данных о пользователе, технологии: различные ЯП, базы данных (ДБ), фреймфорки, библиотеки, облака, виртуализация.
* Full-stack (WEB development) — это Front-end + Backend, разрабатывается WEB приложение, как интерфейс, так и логика.

#### Front-end технологии:
* HTML — язык гипертекстовой разметки. HTML — основа всех WEB страничек. WEB-браузер понимает HTML и отображает страничку в окошке браузера согласно правилам HTML
* CSS — язык описания внешнего вида WEB странички. CSS дополняет HTML, позволяет навести красоту.
* JavaScript (JS) — язык программирования, который может быть использован как в backend, так и в front-end. JS может быть встроен в HTML, и это позволяет добавить динамику в WEB.

Front-end концепции:

* SPA (single-page applications) — одностраничное приложение. WEB приложение состоит из одной HTML странички, которая подгружает всё остальное через CSS и JS.
* AJAX (Asynchronous JS and XML) — подход к построению интерактивных одностраничных WEB-приложений.

JS front-end технологии:

* ReactJS — это библиотека, набор возможностей для разработки одностраничных WEB приложений на JS.
JSX (JavaScript XML) — расширение JS: позволяет встраивать HTML в JS. Используется в ReactJS.
* jQuery — более легковесная, чем ReactJS, библиотека.
* Angular — JS framework для разработки WEB приложений на JS/TypeScript.
* TypeScript — расширение JS: добавляет возможность указания типов в JS. Используется в Angular, и вообще backend.

#### Backend технологии

Языки программирования:

* Python, Ruby, JavaScript — с динамической типизацией.
* Golang, Java, C# (.NET) — со статической типизацией.

Платформы:

* Python: Django, Flask, FastAPI
* Ruby: Ruby on Rails
* JS: NodeJS (ExpressJS, Koa)
* C#: Asp .NET
* Java: Spring Boot

Базы данных:

* SQL — специальный язык для управления данными в реляционных базах данных.
* MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server — реляционные базы данных.
* NoSQL (Non-relational databases, Not Only SQL) — не реляционные ДБ. В NoSQL может использоваться что-то похожее на SQL.
* Couchbase, MongoDB, Amazon DynamoDB, Cassandra, HBase, Aerospike, Bigtable, Amazon DynamoDB — NoSQL базы данных
* In-memory DB — такие БД размещают данные в оперативной памяти компьютеров, могут сохранять данные и на жесткий диск, но гарантии целостности данных менее жёсткие.
* SQLite, VoltDB — in-memory, реляционные БД.
* Redis, Memcached — in-memory, не реляционные БД.

Специальные текстовые форматы:

* XML — для пересылки/принятия данных, для определения схемы данных.
* JSON — для хранения и отображения данных,
* YAML — более удобен для человека (чтение, написание).

#### Инфраструктура

Виртуализация, контейнеризация, Cloud:

* Virtual Machine (VM) — позволяет запускать одну ОС на другой ОС. Например, можно запустить полноценный Linux на компьютере под управлением Windows или MacOS.
* VMware, VirtualPC, VirtualBox — примеры таких продуктов, которые позволяют запускать VM
* Docker — контейнер, это легковесная виртуализация, при которой гостевая машина использует ОС хозяина. То есть можно запустить Linux на Linux, но не Windows на Linux.
* Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP), Oracle Cloud — виртуализация в облаке.

Source Control, Build System, CI/CD:

* Git — система контроля версий (позволяет хранение кода и командную разработку, то есть изменение кода)
* Build System — система для сборки продукта из исходного кода, например: Jenkins, GitLab, Bamboo
* CI/CD (Continuous Integration and Delivery) — метод разработки ПО, при котором запускаются проверки и тесты при инкрементальных изменениях кода.


## [Math](math.md)