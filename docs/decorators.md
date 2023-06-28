# Decorators

## Декораторы ⏤ Part 1 (May 17)

Покажем, как к некой функции добавить дополнительные свойства без того, чтобы менять её код. 
Пусть, например, у нас есть функция:
```py
def test_func(x, y):
    ...
```
Один из простых способов достичь этого ⏤ это написать декоратор.
В качестве примера, можно создать decorator, который при вызове функции печатает входные параметры и возвращаемое значение.

Чтобы применить декоратор, скажем `log_call`, к функции `test_func`, нужно декорировать последнюю специальным образом, добавив `@log_call` перед определением функции:
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
Первая и предпоследняя строки печатаются самим декоратором `log_call`, который реализован следующим образом:
```py
def log_call(some_func):
    def call_it(*args):
        print(f'{some_func.__name__}({",".join(str(arg) for arg in args)})')
        ret = some_func(*args)
        print(f'{some_func.__name__}: {ret}')
        return ret

    return call_it
```
Как видим, декоратор `log_call` ⏤ это функция, которая принимает на вход другую функцию (`some_func`). 
Декоратор оборачивает вызов some_func в другую функцию `call_it`, которая как раз и выводит на экран

* имя вызванной (декодируемой) функции: `some_func.__name__`,
* переданные параметры: `",".join(str(arg) for arg in args)` и
* результирующее значение: `ret`.

Заметим, что `call_it()` запаковывает все полученные параметры в tuple: args. 
А далее, распаковывает кортеж при передаче параметров в функцию `some_func()`.

Code: https://onlinegdb.com/kML69mab7

---

## Декораторы ⏤ Part 2 (May 18)

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
В переменной depth (да, тут используем список из одного элемента, почему так?) сохраняем глубину рекурсивного вызова. От depth зависит сдвиг вправо (индентация).

Оператор `try-finally` для учебного примера не обязателен, но тут мы хотим показать, что при любой аварии нужно вернуть depth на прежнее значение. 
Попробуйте убрать `try-finally` и искусственно добавить вызов исключительной ситуации (например поделите на 0) ⏤ в результате индентация сломается.

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
