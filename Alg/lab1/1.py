import random
import matplotlib.pyplot as plt
import string
import timeit


def foo(s):  # s - строка
    val = 0
    for c in s:
        if c.isdigit():
            val += int(c)
    return val


def generate_random_str(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_str = ''.join([random.choice(letters_and_digits)
                       for _ in range(length)])
    return rand_str


lengths = [100000, 1000000, 10000000]
time = []
colors = ["red", "green", "blue"]
for i in lengths:
    rand_str = generate_random_str(i)
    time.append(timeit.timeit(
        f"foo('{rand_str}')", number=5, globals=globals()))

plt.plot(lengths, time)
plt.show()
plt.close()
