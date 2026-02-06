# Decorators

## Decorators ⏤ Part 1 (May 17)

Let's show how to add additional properties to a function without changing its code. 
Suppose, for example, we have a function:
```py
def test_func(x, y):
    ...
```
One simple way to achieve this ⏤ is to write a decorator.
As an example, we can create a decorator that, when calling a function, prints the input parameters and return value.

To apply a decorator, say `log_call`, to the function `test_func`, we need to decorate the latter in a special way, adding `@log_call` before the function definition:
```py
@log_call
def test_func(x, y):
    print('I am doing some magic!')
    print(f'I am using the parameters: {x=}, {y=}')
    print('Biggest magic has done.')
    return 'done'
```
The effect of the decorator will appear when calling the function test_func:
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
The first and second-to-last lines are printed by the decorator `log_call` itself, which is implemented as follows:
```py
def log_call(some_func):
    def call_it(*args):
        print(f'{some_func.__name__}({",".join(str(arg) for arg in args)})')
        ret = some_func(*args)
        print(f'{some_func.__name__}: {ret}')
        return ret

    return call_it
```
As we can see, the decorator `log_call` ⏤ is a function that takes another function (`some_func`) as input. 
The decorator wraps the call to some_func in another function `call_it`, which outputs to the screen

* the name of the called (decorated) function: `some_func.__name__`,
* passed parameters: `",".join(str(arg) for arg in args)` and
* resulting value: `ret`.

Note that `call_it()` packs all received parameters into a tuple: args. 
And then, unpacks the tuple when passing parameters to the function `some_func()`.

Code: https://onlinegdb.com/kML69mab7

---

## Decorators ⏤ Part 2 (May 18)

Let's consider another simple decorator: @cache. This decorator remembers the result of a function call and on repeated calls with the same parameters uses the saved value.

Parameters passed to the function are used as a key in the cached dictionary, which stores return values.
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
Now, if we decorate the function with two decorators: @cache and @log_call as follows:
```py
@cache
@log_call
def test_func(x, y):
    print('I am doing some magic!')
    print(f'I am using the parameters: {x=}, {y=}')
    print('Biggest magic has done.')
    return 'done'
```
then on repeated calls to the function test_func:
```py
print(test_func(10, 'hi'))
print(test_func(10, 'hi'))
```
on the screen we'll get the following:
```
test_func(10,hi)
I am doing some magic!
I am using the parameters: x=10, y='hi'
Biggest magic has done.
test_func: done
done
done
```
The result of the second call ⏤ is just one line: done. The decorator remembered the answer (done) and simply returned it on repeated call.

If we call the function with other parameters, the function will execute as expected:
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
The decorator @cache is also sometimes called "memoize" (or "memoization"). Most often it can be found for recursive functions. For example, let's write a function that calculates Fibonacci numbers:
```py
@cache
@log_call
def fib(n: int) -> int:
    return fib(n - 1) + fib(n - 2) if n >= 2 else n
```
The function can optionally be decorated with @cache and/or @log_call.

Without memoization, calling fib(5) will produce a huge number of repeated recursive calls, try fib(5) with and without @cache. Actually @cache greatly reduces the execution time of the function for large n.

Let's return to the decorator @log_call, and add indentation (shifting "prints" to the right) depending on the depth of recursive calls:
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
In the variable depth (yes, here we use a list of one element, why so?) we save the depth of the recursive call. The shift to the right (indentation) depends on depth.

The `try-finally` operator is not necessary for a tutorial example, but here we want to show that in case of any failure we need to return depth to its previous value. 
Try removing `try-finally` and artificially add a call to an exceptional situation (for example divide by 0) ⏤ as a result, indentation will break.

Apply both decorators to fib():
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
We see how indentation works. Also we can see that a repeated call leads to an immediate answer!
In the functools module you can find standard decorators. For example, @functools.cache is already implemented there: https://docs.python.org/3/library/functools.html

Code: https://onlinegdb.com/zYm7xeYeg

