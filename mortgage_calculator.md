# Project: Mortgage Calculator

## Mortgage Calculator: namedtuple, custom types, operator overloading (May 16)

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

### Функция `payment()`

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

### Тип `Dollar`

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

## Backend на FastAPI: mortgage calculator (May 23)

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

### `main.py` и запуск WEB-сервиса:

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

### Loan Calculator

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

### Форматирование JSON

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

### Interactive API docs

FastAPI также генерирует точку вызова для интерактивного API. Пока бежит ваш сервис, наберите в браузере следующий URL:

http://127.0.0.1:8000/docs

Должна генерироваться страница для вызова двух функций: `Root Read` и `Amortization Loan`.

Кликаем на стрелочки и далее на "Try it out" и "Execute"!

Получили очень простой UI, через который можно взаимодействовать с сервисом

Full Code: https://onlinegdb.com/7FLyB8K7P

See https://fastapi.tiangolo.com/
