import timeit
import matplotlib.pyplot as plt


in_test = timeit.Timer("'test' in x", globals=globals())

n = [i for i in range(1000000, 10000001, 1000000)]
list_time = []
st_time = []

for i in n:
	x = list(range(i))
	x.append("test")
	time = in_test.timeit(number=5)
	list_time.append(time)

	x = set(range(i))
	x.add("test")
	time = in_test.timeit(number=5)
	st_time.append(time)

plt.plot(n, list_time, label="List")
plt.plot(n, st_time, label="Set")
plt.ylabel("time")
plt.xlabel("count")
plt.legend()
plt.show()
plt.close()
