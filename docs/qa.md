# QA ⏤ Quality Assurance

## QA Part 1: Intro

Quality Assurance (Обеспечение/проверка качества) существует практически в любой индустрии, иначе продукт в нормальном состоянии не покинул бы производственный процесс.

Поговорим в первую очередь про Software QA, то есть обеспечение качества разрабатываемого программного обеспечения (ПО), то есть качество программ.

Самая очевидная сфера Software QA — это проверка интерфейса программы, это может быть WEB, mobile app или другие виды интеракции между человеком и программой.

Грубо говоря, видит человек перед собой кнопочки, окошки, поля ввода, и должен там что-то ткнуть мышкой, чтобы программа как то отреагировала.

QA должен обеспечить корректное исполнение программы при любых действиях пользователя. То есть, на корректное поведение, программа должна дать правильный ответ, и при этом ничего лишнего не должно произойти. А на некорректное поведение клиента, программа должна не упасть, и адекватно отреагировать (сообщением на экране, подсказкой, и т.д). Разумеется, тоже не делать ничего лишнего, всё должно быть в рамках некой спецификации или описания.

Тестировщики, тестеры, QA testers как раз и занимаются проверкой программ на адекватное поведение. Обычно тестеры создают (или используют уже готовую) группу тестов и прогоняют все тесты на очередной версии программы.

Тестировка является частью рабочего цикла разработки ПО!

Например, разработчики выпускают новую версию (раз в месяц/неделю/день), а тестировщики прогоняют тесты, если находят дефекты (баги), передают всю информацию программистам на починку. И далее по-кругу!

---

## QA Part 2: Manual vs. Automation

Тестировка вручную (Manual QA): тестировщик симулирует поведение клиента, кликает мышкой, вводит данные, сверяет поведение программы с ожидаемым и так прогоняет все тесты один за другим.

Ручное тестирование обычно очень трудоёмко, приходится многократно повторять одни и те же тесты. В конце концов становится выгодным автоматизировать процесс тестирования (Automated QA). Это может произойти раньше, если автоматизацию написать относительно легко и спецификация продукта хорошо прописана. Чаще автоматизация тормозится постоянными изменениями в описание продукта, и тогда автоматизация тестирования может быть отодвинута ближе к официальным выпускам продукта.

Автоматизацию пишут на каком-то языке программирования (Java, Python), используя платформы и инфраструктуру подходящую для тестирования данного продукта. Автоматизация представляет собой группу программ, каждая из которых запускает отдельный тест, симулирующий определённое поведение пользователя. Написать такой тест обычно сложнее, чем протестировать в ручную, но потом повторные запуски готового теста значительно более дёшевы, чем ручное тестирование.

Автоматизация тестов окупается далеко не сразу, ведь
* во-первых написание тестов занимает время, а
* во-вторых спецификация продукта может сильно меняться, что может потребовать постоянного изменения и адаптации тестов, ведь тесты могут падать, не из-за того, что программа имеет дефект, а потому как тест устарел и не соответствует спецификации.

Вот и получается, что вначале идёт ручное тестирование — его легче начать, а за ним начинают разрабатывать автоматизацию, что может окупиться в долгосрочной перспективе!

---

## QA Part 3: Тестируем продукт

Например, возьмем... холодильник, ну какая разница в самом деле?! Да, большинство продуктов, наверное чисто software (то есть, создали программу её и тестируем), но есть же много и с hardware (то есть, с некой конструкцией, чипами, в коробочке, мобильные телефоны, например).

В холодильнике, например, есть кнопочки, дверца, сенсоры, чипы, а также и программа, контролирующая температуру или всякие режимы. Холодильник состоит из разных частей, со своим дизайном и управлением. Всё это можно тестировать по-отдельности и вместе.

* Тестированию подлежит как программное обеспечение, так и физические части. Автоматизацию проще написать именно для программы, причём можно сделать так, чтобы сигналы о нажатии кнопок пошли в программу от теста, а не от настоящего нажатия. Так что в этой части автоматизация сильно поможет.

* Что касается физических манипуляций, например, нажатие на кнопки (ice, water) и одновременное открытие холодильника, то тут уже проще послать тестера-человека производить ручное тестирование. Потому как разработка автоматизации, на начальном этапе будет дорогая. Человек посмотрит, покрутит за ручки и "крутёлки", зафиксирует проблемы и пошлёт разработчикам доделывать.

В какой-то момент, когда разработка продукта завершена и выходим на конвейерное производство, уже не выйдет вручную тестировать тысячи холодильников. Всё-таки нужна полная автоматизация. Робот будет крутить ручки и нажимать кнопки. Да, сам по себе такой робот — не простой продукт, его тоже нужно разработать и... протестировать!

**И действительно, а кто тестирует ... тесты и автоматизацию?**

В общем, продукты для тестирования могут быть очень sophisticated, и их разработкой могут заниматься целые фирмы, со своим тестированием!

Ещё одно замечание: полностью от manual QA уйти невозможно, где-то да оно обязано будет присутствовать!

---

## QA Part 4: Пессимисты vs. оптимистов

Чем отличается тестер от кодера (программиста)?

Одно из отличий состоит в том, как каждый относится к качеству продукта, количеству дефектов и соответствию спецификации и ожиданиям клиентов.

* **Тестер:** Очевидно новая версия продукта содержит множество багов, и вообще, скорее всего эта программа не рабочая. Сейчас я найду очевидные дефекты и "положу" программу (имеется ввиду crash).

* **Кодер:** Уверен, что уж сейчас исправил последнюю ошибку, программа побежит "как родная", а клиенты будут "пускать слюни" и выстраиваться в очереди, только чтобы прикоснуться к самому "прекрасному" созданию!

Ну в общем, думаю можно догадаться, что тестеры-пессимисты обычно оказываются правы! Опять баги, падения, отхождения от спецификации, зависания, посылка Тесла в космос, вместо приготовления чашечки кофе и т.д.

Вы пессимистично относитесь к корректности программ? Полагаете, что там точно скрываются ошибки и проблемы? Если замечаете что-то странное, продолжаете "рыться" и находите серьёзные проблемы? Вам доставляет некий кайф, когда вы выявляете на предсказуемое и неадекватное поведение продукта?

**Ну есть шанс, что профессия тестера вам зайдёт!**

Как вы может быть заметили, это мало связано с образованием или дипломами. Тестером могут предпочесть работать даже программисты (выпускники BSc in Computer Science). Всё зависит от того к чему больше тянет.

Например, кодеров больше "вставляет" от того, что они создают новые виртуальные миры, свои правила и абстрактные сущности. Программистам не будет в кайф сидеть и выискивать все баги до последнего... в чужом продукте/коде (ну за редким исключением).

Как увеличить шансы поиска работы тестером? В следующем посту, и речь не пойдёт о курсах! 🙂

---

## QA Part 5: Tips по поиску работы

Прошли вы курс по Manual QA, вроде как формально готовы тестировать ПО. Умеете читать Test Case Specification (пошаговое описание тестов), и возможно даже его выполнять. Вы знаете какие-то Bug Tracking System (куда посылать описание найденных дефектов). У вас есть бумажка о пройденном курсе (месячном? два месяца?).

**Каковы шансы, что потенциальный работодатель заинтересуется вашим скромным резюме?**

Поскольку требования к успешному завершению таких курсов невысокие, то и ожидания у работодателей к выпускникам таких курсов тоже соответствующее. Легко пройти курс, значит много похожих кандидатов. И все с "пустыми" резюме!

Ну не совсем с пустыми, некоторые кандидаты дорисовывает несуществующий опыт, internship. Кто-то может действительно ещё посмотрел на какой-нибудь язык программирования. Такие резюме будут несколько выделяться среди общей массы кандидатов.

**А как выделиться вам?**

На минуточку вспомним, как ищут работу программисты: кроме дипломов и опыта, они ещё пытаются участвовать в каких-то олимпиадах и open-source проектах, то есть программируют ради удовольствия, получения навыков и возможности где-то как-то засветиться.

С ручным тестированием сильно не разогнаться со сторонними проектами, но кое-что может сработать!

Подаёте заявку в какую-то контору? Изучите их сайт и продукты... **на предмет дефектов!** А вдруг найдёте?! Вот вам и дополнительный плюсик! Сопроводите своё резюме коротким Cover Letter — не обязательно официальным! Достаточно пару строк о том, что "у вас страсть к тестированию и продуктам этой компании-мечты", ну и "посмотрите у вас тут кое-что можно улучшить!".

Если где-то покопались и нашли потенциальные дефекты, попробуйте податься в эту компанию. Сколько багов тут в Facebook!

Удачи!

---

## QA Part 6: реально ли $300К в год?

В одной группе наткнулся на рекламу очередных курсов про QA. Конечно же авторы курса указывают на среднюю зарплату своих выпускников аж в 100 тыс. USD в год!

Хотел бы сразу предупредить, что статистика позволяет очень легко манипулировать данными и получать на выходе какой угодно результат. Хотите $100К — это можно сделать!

Нужно ли говорить, что зарплата зависят от таких параметров как location, remote или onsite, manual или automation, был у выпускника какой-то технический background до школы QA? Да и как учитывались те, кто ушёл с курса, не закончил, долго искал работу, не нашёл позицию, ну и т.д.! В общем, если нужно получить 2 + 2 = 5, то статистика это может вам устроить!

В реальности, скорее всего, большинство выпускников курсов QA будут долго искать первую работу, и им лучше преуменьшить свои ожидания по поводу первой зарплаты. Но сейчас немного не об этом.

Мне эта реклама напомнила другой давний публичный спор с одним руководителем таких QA школ. Тогда спор дошёл до того, что оппонент кинул в меня линк о статистике зарплат в **Netflix на позицию Dev in Test в $300K**.

Кто знает, как нанимает и платит Netflix, и что такое Dev in Test сразу поймут всю абсурдность данной ситуации.

Для остальных объясню почему это очень серьёзный промах. К слову, при осознании всей глупости, спорщик всё потер и более таких громких утверждений уже не делал.

Так о чём речь?

Роль Dev in Test — это не QA, и даже не QA Automation. Несколько более близкая позиция к этой: QA Infrastructure, но и то не совсем то.

Ключевой момент тут "Dev...", то есть речь идёт про Developer, то есть это позиция для программистов! Dev in Test разрабатывают системы для тестирования, иногда эти системы не проще, чем сам основной продукт, и эти системы тоже должен кто-то тестировать!

Дальше ещё хуже, Netflix — это компания, которая платит очень высокие гонорары. В неё попасть не так-то просто. Они обычно предлагали flat rate, то зарплата — это кэш, без акций и бонусов. И да, если брали, то зарплаты могли доходить до $250-500К в год! Ну это если брали!

Работа в Netflix очень стрессовая, это не расслабленный Google или спящий Microsoft, в Netflix работают много, и увольняют даже неплохих программистов за "Underperformed" часто и очень быстро!

Но и это ещё не всё!

**Netflix набирает инженеров только на senior positions**, то есть нужен опыт лет в 5, и они практически не берут fresh-grads!

Это всё очевидные вещи, для тех кто знаком с IT, но почему-то не для того создателя школы QA (точно уж и не помню кто там был).

Осторожнее, мечтать неплохо, но иногда всё же нужно возвращаться в реальность.

---

## QA Part 7: Black Box vs. White Box

### Black Box

Тестировщик выполняет тесты, симулируя возможные действия пользователя, производит манипуляции с продуктом, при этом не использует дополнительные знания, как этот продукт разработан. То есть не используются информация о внутреннем содержимом продукта — рассматриваем продукт как "чёрный ящик". Что и как там сделано внутри — нас не интересует.

Такой вид тестирования является стандартным. Тесты прописаны, делаем всё по шагам, записываем результаты, подаём отчёты по найденным дефектам.

### White Box

Тестировщик знает (примерно) как создан продукт, в курсе об особенностях реализации, и имея эту дополнительную информацию, пытается найти дефекты. Это более интересный и продвинутый вид тестирования. Необходимо на каком-то уровне иметь понимание о внутренностях продукта и уметь предсказывать аномальное поведение программы.

Поговорив с разработчиками, ознакомившись с архитектурой и реализацией продукта, можно придумать очень интересные сценарии тестов и, в конце концов, поставить в тупик весь отдел программистов. А если немного ознакомиться с кодом... посылаете баг и сразу указываете на строчку в коде, которая является причиной дефекта! Разумеется это не является частью работы тестера, но некоторые инженера QA заходят на столько далеко.

### Exploratory

Exploratory Testing используется... когда тесты ещё не написаны или нет на это времени. Тестировщик включает своё воображение и тестирует то, где ожидает найти ошибки. Такой вид тестирования используют и в дальнейшем, при крупных релизах, ведь наверняка простые, предсказуемые ошибки чинятся в первую очередь, а о хитрых дефектах могли и не подумать.

Такой вид тестирования может сочетаться как с Black Box, так и с White Box. Либо вы изучаете продукт и ищите ошибки, не зная внутренностей или у вас есть полный доступ к реализации и документации.

### Gray Box

Среднее между Black Box и White Box Testing. Тестируем продукт, имея доступ к документации, но не лезем смотреть в реализацию.