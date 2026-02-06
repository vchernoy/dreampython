# Strings and String Formatting

## Ways to Format Strings in Python (May 4)

The following statement prints text without additional processing:

```py
print("In 2021 the GDP of America is $22.99T")
```

We get:

```text
In 2021 the GDP of America is $22.99T
```

Suppose the parameters (country name, year, and GDP) are given in variables:

```py
year = 2021
country = 'America'
value = 22.99
```

The following ways of forming text produce the same result:

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

The most modern is the last option, which uses f-string (fast string).

Code in [OnlineGDB](https://onlinegdb.com/xQG_uyOnrj)

---

## Forming Single-line and Multi-line Text in Python (May 4)

The following four examples form single-line text:

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

Output to screen:

```text
"There should be no such thing as boring mathematics." -- Dijkstra's quote
```

And the following five examples form multi-line (more precisely, two-line) text:

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

Output to screen:

```text
"There should be no such thing as boring mathematics."
    -- Dijkstra's quote
```

The code to play: [OnlineGDB](https://onlinegdb.com/tVtkO7Mcc)

---

## Introduction to `str.split()` and `str.join()` Methods (May 4)

We use `split()` to divide text into words.

* For example: `text.split(' ')` divides the string text using the separator `' '` (space). The method returns a list of strings (list of str).

And to join words, we use the reverse method: `join()`.

* For example, `' '.join(words)` will join all words from the list words into one string, gluing them with the character `' '`:

```py
quote = 'Simplicity is prerequisite for reliability.'
print(f"Dijkstra's quote: {quote}")

words = quote.split(' ')
print(f"Split using ' ':  {words}")

text = ' '.join(words)
print(f"Join using ' ':   {text}")
print()
```

You can use method composition (call a method on the result of the previous method):

```py
print(' '.join(quote.split()))
print(' '.join(words).split(' '))
print()
```

And now let's compare that the result of the work of two functions produces the original:

```py
print(f'the produced text equals original quote: {text == quote}')
print()

print(f'" ".join(quote.split(" ")) == quote: {" ".join(quote.split(" ")) == quote}')

print(f'" ".join(words).split(" ") == words: {" ".join(words).split(" ") == words}')
```

Code to play: [OnlineGDB](https://onlinegdb.com/l1GEcnq3s)

