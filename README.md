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