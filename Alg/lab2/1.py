from random import randint
import timeit
import matplotlib.pyplot as plt


def selection_sort(lst: list):
    for i in range(0, len(lst) - 1):
        smallest = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[smallest]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]
    return lst


def quick_sort(lst: list):
	less = []
	equal = []
	greater = []
	if len(lst) > 1:
		pivot = lst[(len(lst)-1) // 2]
		for x in lst:
			if x > pivot:
				greater.append(x)
			elif x < pivot:
				less.append(x)
			else:
				equal.append(x)
		return quick_sort(less) + equal + quick_sort(greater)
	else:
		return lst


lenghts = [i for i in range(100, 1000, 100)]
time_rand = [[], []]
time_sort = [[], []]
time_rev = [[], []]
for i in lenghts:
    lst = [randint(0, 100) for _ in range(i)]
    sort_lst = [_ for _ in range(i)]
    reverse_lst = [_ for _ in range(i, 0, -1)]

    time_rand[0].append(timeit.timeit(
        f"selection_sort({lst})", number=1, globals=globals()))
    time_rand[1].append(timeit.timeit(
        f"quick_sort({lst})", number=1, globals=globals()))

    time_sort[0].append(timeit.timeit(
        f"selection_sort({sort_lst})", number=1, globals=globals()))
    time_sort[1].append(timeit.timeit(
        f"quick_sort({sort_lst})", number=1, globals=globals()))

    time_rev[0].append(timeit.timeit(
        f"selection_sort({reverse_lst})", number=1, globals=globals()))
    time_rev[1].append(timeit.timeit(
        f"quick_sort({reverse_lst})", number=1, globals=globals()))

plt.subplot(3, 1, 1)
plt.plot(lenghts, time_rand[0], label="selection_sort")
plt.plot(lenghts, time_rand[1], label="quick_sort")
plt.xlabel("lenght")
plt.ylabel("time")
plt.title("Random list")
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(lenghts, time_sort[0], label="selection_sort")
plt.plot(lenghts, time_sort[1], label="quick_sort")
plt.xlabel("lenght")
plt.ylabel("time")
plt.title("Sorted list")
plt.legend()
plt.subplot(3, 1, 3)
plt.plot(lenghts, time_rev[0], label="selection_sort")
plt.plot(lenghts, time_rev[1], label="quick_sort")
plt.xlabel("lenght")
plt.ylabel("time")
plt.title("Reverse list")
plt.legend()

plt.subplots_adjust(hspace=1)
plt.show()
plt.close()
