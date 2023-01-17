import timeit
import matplotlib.pyplot as plt


del_lst = timeit.Timer("del x[0]", globals=globals())
del_dct = timeit.Timer("del x[list(x.keys())[0]]", globals=globals())


n = [i for i in range(1000000, 10000001, 1000000)]
list_time = []
dict_time = []

for i in n:
	x = list(range(i))
	time = del_lst.timeit(number=5)
	list_time.append(time)

	x = {i: i for i in range(i)}
	time = del_dct.timeit(number=5)
	dict_time.append(time)

plt.plot(n, list_time, label="List")
plt.plot(n, dict_time, label="Dict")
plt.ylabel("time")
plt.xlabel("count")
plt.legend()
plt.show()
plt.close()