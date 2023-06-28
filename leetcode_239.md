# LeetCode Problem 239: Sliding Window Maximum (Hard)

## LeetCode Problem 239: Sliding Window Maximum: Часть 1

You are given an array of integers nums. There is a sliding window of size k, moving from the very left of the array to the right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```
* Первое окно состоит из чисел: `[1,3,-1]`, а максимум: 3.
* Следующее окно: `[3,-1,-3]`, максимум этого окна: тоже 3.
* Третье окно: `[-1,-3,5]`, максимум: 5. и т.д.
* Последнее окно: `[3,6,7]`, а его максимум: 7.

Собираем все 6 максимумов и возвращаем списком: `[3,3,5,5,6,7]`.

На Python эту задачи легко решить, если не обращать внимание на Performance.
Простейшее решение, которое будет плохо работать при nums большого размера:
```py
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    window: list[int] = []
    max_sliding_win: list[int] = []

    for i in range(len(nums)):
        window.append(nums[i])
        if i >= k:
            window.remove(nums[i-k])

        if i >= k-1:
            max_sliding_win.append(max(window))

    return max_sliding_win
```
`window` — это текущее окно, на каждой итерации добавляем новый элемент. А если размер окна превышает k, то удаляем первый элемент.

Если окно имеет размер k, то считаем его максимум и записываем в `max_sliding_win`.

* Time Complexity: O(n²)

Где n — это размер nums.

Количество итераций: n, и (почти) на каждой итерации вычисляем максимум и удаляем первый элемент, что требует O(n).

В результате, получаем: n∙O(n) = O(n²).

На самом деле для этой задачи есть более быстрое решение, всего О(n log n), а это огромное улучшение, поскольку практически будет работать как O(n).

И действительно, эта задачка помечена в LeetCode как Hard и требует более эффективного решения, чем то что мы записали выше.

К сожалению, в Python нет разумных стандартных средств, чтобы реализовать O(n log n) решение.

Да, с Python можно пролететь на этом вопросе, даже если примерно знаете как решать.

Если интересно, в продолжении будет следующее:
* рассмотрим пример ADT (abstract data types) применительно к этой задаче;
* напишем более быстрые (но не оптимальные) решения этой задачи на Python: O(n √n);
* реализуем оптимальное решение используя другие языки программирования: C++, Java, Rust;
* узнаем, какие из языков программирования будут наиболее эффективны для этой задачи,
* а, какие языки программирования будут неэффективны, как Python.

----

## LeetCode Problem 239: Sliding Window Maximum. Часть 2: ADT

ADT, abstract data type (абстрактный тип данных) — это описание структуры данных в терминах операций, которые можно с этими данными делать.

ADT определяет операции, а не то как они должны быть реализованы.

В задаче Sliding Window Maximum нам нужен некий контейнер, назовём его MaxWindow, который может содержать числа и поддерживает следующие операции:
* добавить число;
* удалить данное число;
* посчитать максимум.

Для этих целей мы использовали конкретную структуру данных, питоновский list, и операции над ним: append, remove, max.
Формально, нам нужен тип данных (класс), со следующим методами:

```py
class MaxWindow:
    def add(self, val: int):
        pass

    def remove(self, val: int):
        pass

    def max(self) -> int:
        pass
```

К методам можно добавить @abstractmethod, подчеркнув, что это пока описание, без реализации.

Для этого абстрактного типа можно написать конкретную реализацию (даже несколько). Используем, например, стандартный list:

```py
class MaxArray:
    def __init__(self):
        self.values = []

    def add(self, val: int):
        self.values.append(val)

    def remove(self, val: int):
        self.values.remove(val)

    def max(self) -> int:
        return max(self.values)
```
Этот контейнер, очевидно, умеет делать все операции, которые определяет ADT MaxWindow.

Time Complexity:
* add: O(1)
* remove: O(m)
* max: O(m)

Где m — количество элементов в MaxArray.

Можно переписать решение задачи используя этот контейнер (вместо list):

```py
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    window = MaxArray()
    max_sliding_win: list[int] = []

    for i in range(len(nums)):
        window.add(nums[i])
        if i >= k:
            window.remove(nums[i-k])
        if i >= k-1:
            max_sliding_win.append(window.max())

    return max_sliding_win
```

Фактически мало что изменилось, и это хорошо, теперь у нас есть возможность реализовывать другие контейнеры с такими же операциями. При этом решение задачи (код) останется почти без изменений.

### Time Complexity

Два решения, на основе list и MaxWindow мало чем отличаются. Но давайте сделаем более точный анализ (для best-case и worst-case).

* Первые k итераций цикла вызывают только add, а следовательно каждая итерация выполняется за O(1).
* Следующие n-k итераций вызывают все три метода (add, remove, max), поэтому каждая итерация выполняются за O(k).

Time Complexity всего цикла (и решения): k∙O(1) + (n-k)∙O(k) = O(k∙(n - k)).

* Если k очень маленькое (k << n), то получим O(k∙n).
* Если k не зависит от n (k = const, k = O(1)), то получим линейное решение: O(n).
* Если k очень близко к n, так что k = n - O(1), то тоже получим: O(n).

То есть, если размер окна или очень маленький, или почти какой как размер nums, решение будет работать быстро (линейно от размера nums).

#### The Best Case Time Complexity: O(n).

При худших сценариях, когда k пропорционально n (k ~ n, k = O(n)), например, k = n / 2, получим:

#### The Worst Case Time Complexity: O(n²).

Если сможем реализовать контейнер (с операциями ADT MaxWindow), с более быстрыми операциями, то сможем улучшить Time Complexity и для решения задачи в целом.

---

## LeetCode Problem 239: Sliding Window Maximum. Часть 3: Медленные Решения на Python

Напомним, что операции remove и max класса MaxArray требуют O(m) времени, и только add выполняется за O(1). Можно ускорить max до O(1), если после каждого изменения контейнера сортировать все элементы:

```py
class SortedArray:
    def __init__(self):
        self.values: list[int] = []

    def add(self, val: int):
        self.values.append(val)
        self.values.sort()

    def remove(self, val: int):
        self.values.remove(val)
        self.values.sort()

    def max(self) -> int:
        return self.values[-1]
```

Но тогда add потеряет свою скорость:

Time Complexity:
* add: O(m)
* remove: O(m)
* max: O(1)

Где m — количество элементов в контейнере.

Чтобы использовать SortedArray в функции `max_sliding_window`, нужно заменить
```py
    window = MaxArray()
```
на
```py
    window = SortedArray()
```

И всё будет работать, поскольку оба класса имеют тот же набор методов, то есть реализуют, то же самый ADT (abstract data type) MaxWindow.

Заметим, что общий метод сортировки над произвольными данными требует O(m log m). Но в нашем случае, до каждого вызова sort() элементы контейнера уже почти упорядоченны. Python использует метод сортировки TimSort, который работает O(m) для отсортированного или почти отсортированного массива

На самом деле, для размеров реальных данных, log m растёт так медленно, что на практике можно полагать, что:
O(m log m) = О(m)

К сожалению, SortedArray не улучшит время работы `max_sliding_window`.

Можно ли лучше?

Нам требуется структура данных, которая умеет держать элементы в (почти) отсортированном виде, быстро добавлять/удалять и находить максимум. Такими свойствами обладают Searching Trees и MaxHeap.

В стандарте Питона нет деревьев, но есть MinHeap. Чтобы из Min сделать Max, инвертируем значения (5 станет -5):

```py
import heapq

class MaxHeap:
    def __init__(self):
        self.values: list[int] = []

    def add(self, val: int):
        heapq.heappush(self.values, -val)

    def remove(self, val: int):
        self.values.remove(-val)
        heapq.heapify(self.values)

    def max(self) -> int:
        return -self.values[0]
```

Time Complexity:
* add: O(log m)
* remove: O(m)
* max: O(1)

В методе remove мы не знаем как быстро удалить элемент из кучи (heap), приходится удалять как из обычного list за O(m). На самом деле, это лишь ограничения конкретной реализации Heap в Python. Если реализовать свой MaxHeap, то можно удалять за O(log m), если знать положение удаляемого элемента. А этого можно добиться воспользовавшись dict.

У такой реализации операции add и remove будут занимать O(log m), а max будет очень быстрой: О(1). И тогда время работы `max_sliding_window` существенно улучшится, до O(n log k).

Идея хорошая, но точно не на 15 мин: нужно знать как реализовать MaxHeap на деревьях (а не массивах) и скомбинировать с `dict`.

Такой же Time Complexity можно добиться и с использованием Searching Trees, но они недоступны в стандарте Python, и их реализация тоже нетривиальна.

Продолжим бороться с Python в следующем посту.

---

## LeetCode Problem 239: Sliding Window Maximum. Часть 4: Танцы с бубном в Python

Заметим, что, как и в стандартном set нам не важен порядок элементов в контейнере. Но в отличие от set, необходимо сохранить все дубликаты. Фактически речь идёт о Multiset.

В Python, Multiset можно реализовать с помощью Counter (создан на основе dict), который подсчитает количество копий каждого значения. Очень полезная структура данных.
```py
import collections

class MaxCount:
    def __init__(self):
        self.counts: collections.Counter[int] = collections.Counter()

    def add(self, val: int):
        self.counts[val] += 1

    def remove(self, val: int):
        self.counts[val] -= 1
        if self.counts[val] == 0:
            del self.counts[val]

    def max(self) -> int:
        return max(self.counts.keys())
```
Time Complexity:
* add: O(1)
* remove: O(1)
* max: O(m)

Этот подход тоже не улучшает скорость работы `max_sliding_window`, но может дать кое-какие идеи о том, как можно улучшить скорость работы метода max.

### Buckets

В условии задачи указано, что значения чисел находятся в пределах от -10,000 до 10,000. Разделим этот диапазон на 200 корзин, каждая покроет диапазон в 100 значений.

* Корзина с индексом 0: -10,000..-9,901
* Корзина с индексом 1: -9,900..-9,801
* Корзина с индексом 2: -9,800..-9,701
* ...
* Корзина с индексом 100: 0..99
* Корзина с индексом 101: 100..199
* ...
* Корзина с индексом 199: 9,900..9,999
* Корзина с индексом 200: 10,000..10,099

На самом деле корзин будет на одну больше (201), но это не важно.

Поиск максимального значения состоит из двух шагов:
1. ищем не пустую корзину с максимальным индексом и
2. находим максимум в этой корзине.

```py
import collections

class BucketCount:
    def __init__(self):
        self.MIN = -10 ** 4
        self.MAX = 10 ** 4
        self.CAP = 100
        self.NUM_BUCKETS = (self.MAX - self.MIN + self.CAP) // self.CAP

        self.buckets: tuple[collections.Counter[int], ...] \
            = tuple(collections.Counter() for _ in range(self.NUM_BUCKETS))

    def add(self, val: int):
        idx = (val - self.MIN) // self.CAP
        self.buckets[idx][val] += 1

    def remove(self, val: int):
        idx = (val - self.MIN) // self.CAP
        self.buckets[idx][val] -= 1

        if self.buckets[idx][val] == 0:
            del self.buckets[idx][val]

    def max(self) -> int:
        for idx in range(self.NUM_BUCKETS - 1, -1, -1):
            if self.buckets[idx]:
                return max(self.buckets[idx])
```

Average Case Time Complexity
* add: O(1)
* remove: O(1)
* max: O(b + m / b)

Где b — это количество корзин.

Функция f(b) = b + m / b принимает минимальное значение при b = m / b, то есть когда b = √m.

Мы не можем выбрать b динамически, но зная условия задачи, можно подобрать b = O(√n).

Тогда Time Complexity функции `max_sliding_window` составит:
* O(n √n),

Что заметно лучше, чем предыдущие решения (О(n²)).

Поскольку по условию задачи m ≤ n ≤ 100,000, то количество корзин должно быть примерно 200-400. Наилучшее значение можно найти экспериментально (тестами).

Все предыдущие решения падали на длинных тестах:

> Time Limit Exceeded.

И только это решение проходит все тесты.

**Задание:** стандартный пакет collections содержит много разных классов. Например, там есть deque, который можно использовать в нашей задаче. Берём MaxArray и заменяем list на deque.

Какое будет Time Complexity для полученного контейнера (назовём его MaxDeque)? Будет ли улучшение Time Complexity для `max_sliding_window`?

В следующих частях посмотрим как на этой задаче покажут себя языки-динозавры типа C++.

---

## LeetCode Problem 239: Sliding Window Maximum. Часть 5: C++ рулит

### C++

Простое, лаконичное и быстрое решение на C++ всего в 15 строчек:

```cpp
#include <set>
#include <vector>

std::vector<int> max_sliding_window(std::vector<int>& nums, int k) {
    std::multiset<int> window;
    std::vector<int> max_sliding_win;

    for (int i = 0; i < nums.size(); i++) {
        window.insert(nums[i]);
        if (i >= k) {
            window.erase(window.find(nums[i-k]));
        }
        if (i >= k-1) {
            max_sliding_win.push_back(*window.rbegin());
        }
    }
    return max_sliding_win;
}
```

* Time Complexity: О(n log k)

Стандартная библиотека C++ предоставляет контейнер `multiset`, основанный на BST (Binary Search Tree).

Multiset позволяет дубликаты, и даёт доступ к элементам за O(log m), где m — количество элементов в `multiset`.

Time Complexity решения на C++ гораздо лучше, чем у быстрого решения на Python (О(n log k) против O(n √n)). Причём решение на C++ раза в 3 короче решения на Python.

**Удивило ли вас это?**

### Rust

Rust — это прямой конкурент C++, тоже используется для разработки систем и ориентирован на скорость работы кода.

Rust не предлагает Multiset в стандартной библиотеке, но для наших целей можно использовать BTreeMap, который тоже основан на BST.

Решение выглядит более громоздким, из-за конвертации значений (можно сделать красивее?) и подсчёта копий значений.

```rust
use std::vec::Vec;
use std::collections::BTreeMap;

pub fn max_sliding_window(nums: Vec<i32>, _k: i32) -> Vec<i32> {
    let k = _k.try_into().unwrap();
    let mut window = BTreeMap::new();
    let mut max_sliding_win = Vec::new();

    for i in 0..nums.len() {
        window.entry(nums[i]).and_modify(|c| *c += 1).or_insert(1);
        if i >= k {
            let j = i - k;
            window.entry(nums[j]).and_modify(|c| *c -= 1);
            if *window.get(&nums[j]).unwrap() == 0 {
                window.remove(&nums[j]);
            }
        }
        if i >= k - 1 {
            max_sliding_win.push(*window.iter().next_back().unwrap().0);
        }
    }
    return max_sliding_win;
}
```

### Java

В стандартной библиотеке Java можно найти контейнер TreeMap, основанный на BST. Реализуем тот же подход, что использовали в Rust.

```java
import java.util.List;
import java.util.ArrayList;
import java.util.SortedMap;
import java.util.TreeMap;

public int[] maxSlidingWindow(int[] nums, int k) {
    List<Integer> maxSlidingWin = new ArrayList<>();
    SortedMap<Integer, Integer> window = new TreeMap<>();

    for (int i = 0; i < nums.length; i++) {
        window.compute(nums[i], (key, c) -> c != null ? c+1 : 1);
        if (i >= k) {
            window.compute(nums[i-k], (key, c) -> c > 1 ? c-1 : null);
        }
        if (i >= k-1) {
            maxSlidingWin.add(window.lastKey());
        }
    }
    return maxSlidingWin.stream().mapToInt(x -> x).toArray();
}
```

* Time Complexity: O(n log k)