from queue import Queue
from Queue import Queue as myQueue
import matplotlib.pyplot as plt
import timeit

def check_push(q, length):
	if isinstance(q, myQueue):
		for i in range(length):
			q.enqueue(i)
	elif isinstance(q, Queue):
		for i in range(length):
			q.put(i)

def check_pop(q, length):
	if isinstance(q, myQueue):
		for _ in range(length):
			q.dequeue()
	elif isinstance(q, Queue):
		for _ in range(length):
			q.get()

myQ = myQueue()
Q = Queue()
time_pop1 = []
time_pop2 = []
time_put1 = []
time_put2 = []
lengths = [100, 1000, 10000]
for i in lengths:
	time_put1.append(timeit.timeit(f"check_push(myQ, {i})", number=1, globals=globals()))
	time_put2.append(timeit.timeit(f"check_push(Q, {i})", number=1, globals=globals()))
	time_pop1.append(timeit.timeit(f"check_pop(myQ, {i})", number=1, globals=globals()))
	time_pop2.append(timeit.timeit(f"check_pop(Q, {i})", number=1, globals=globals()))

plt.subplot(1, 2, 1)
plt.title("Put")
plt.xlabel("length")
plt.ylabel("time")
plt.plot(lengths, time_put1, label="myQueue")
plt.plot(lengths, time_put2, label="Queue")
plt.legend()
plt.subplot(1, 2, 2)
plt.title("Pop")
plt.xlabel("length")
plt.ylabel("time")
plt.plot(lengths, time_pop1, label="myQueue")
plt.plot(lengths, time_pop2, label="Queue")
plt.legend()
plt.show()
plt.close()