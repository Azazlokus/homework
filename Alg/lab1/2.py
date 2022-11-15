from random import randint
import matplotlib.pyplot as plt
import timeit


def find1(lst: list):  # 1 O(n)
    x = []
    for _ in range(3):
        x.append(max(lst))
        lst.remove(max(lst))
    return x


def find2(lst: list):  # 2 O(n^2)
    for i in range(len(lst)-1):
    	for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst[0:3]


n = [i for i in range(1000, 10001, 1000)]
time = [[], []]

for i in n:
    rand_lst = [randint(0, 100) for _ in range(i)]
    time_func = timeit.timeit(
        f"find1({rand_lst})", number=1, globals=globals())
    time[0].append(time_func)
    time_func = timeit.timeit(
        f"find2({rand_lst})", number=1, globals=globals())
    time[1].append(time_func)

plt.plot(n, time[0], label="find1 O(n)")
plt.plot(n, time[1], label="find2 O(n^2)")
plt.legend()
plt.show()
plt.close()
