import sys
import random
import matplotlib.pyplot as plt
import timeit

items_ = {
    "вода": (2, 8),
    "книга": (2, 5),
    "еда": (3, 7),
    "куртка": (1, 3),
    "камера": (2, 4),
}
items_list = list(items_.keys())
max_size = 6
w = [it[0] for it in items_.values()]
p = [it[1] for it in items_.values()]
dict = {}


def search(w, p, n, bag_size, dict):
    if bag_size < 0:
        return -sys.maxsize
    if n < 0 or bag_size == 0:
        return 0

    include = p[n] + search(w, p, n-1, bag_size-w[n], dict)
    exclude = search(w, p, n-1, bag_size, dict)
    return max(include, exclude)


def search2(w, p, bag_size, items):
    items_list = list(items.keys())
    n = len(items)
    t = {}
    for i in range(n):
        t[w[i]/p[i]] = i

    keys = list(t.keys())
    keys.sort()

    w_ = 0
    p_ = 0
    ans = []
    for i in keys:
        if w_ + w[t[i]] <= bag_size:
            w_ = w_ + w[t[i]]
            p_ = p_ + p[t[i]]
            ans.append(items_list[t[i]])
    return ans, p_


def search3(w, p, bag_size, items):
    items_list = list(items.keys())
    n = len(items)
    bag = [[0] * (bag_size+1) for _ in range(n+1)]
    for i in range(1, n + 1):
        for k in range(1, bag_size + 1):
            if k >= w[i-1]:
                bag[i][k] = max(bag[i-1][k], bag[i-1][k-w[i-1]] + p[i-1])
            else:
                bag[i][k] = bag[i-1][k]

    ans = []
    k = bag_size
    p_ = 0
    for i in range(n, 0, -1):
        if bag[i][k] != bag[i-1][k]:
            ans.append(items_list[i-1])
            k -= w[i-1]
            p_ = p_ + p[i-1]
    return ans, p_


example_range = [1, 10, 100, 1000, 10000, 100000]
example_items = {}
max_size = 6
dict = {}
time = [[], [], []]
for i in example_range:
    for j in range(i):
        example_items[j] = (random.randint(1, max_size), random.randint(1, 10))
    w = [it[0] for it in example_items.values()]
    p = [it[1] for it in example_items.values()]
    # time[0].append(timeit.timeit(
    #     f"search({w}, {p}, {i-1}, {max_size}, {dict})", number=1, globals=globals()))
    #time[1].append(timeit.timeit(
    #   f"search2({w}, {p}, {max_size}, {example_items})", number=1, globals=globals()))
    time[2].append(timeit.timeit(
         f"search3({w}, {p}, {max_size}, {example_items})", number=1, globals=globals()))

#plt.plot(example_range, time[0], label="Полный перебор")
#plt.plot(example_range, time[1], label="Жадный алгоритм")
plt.plot(example_range, time[2], label="Динамическое программирование")
plt.ylabel("Время")
plt.xlabel("Кол-во элементов")
plt.legend()
plt.show()
plt.close()
