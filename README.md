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

## [Project: Mortgage Calculator](mortgage_calculator.md)

## [Misc](misc.md)

## [Programming Languages Overview](programming_languages_overview.md)

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