import numpy as np

# a
arr_1 = np.full((3, 4), 3)
# b
arr_2 = np.random.randint(0, 10, size=(2, 4))
# c
print(arr_1.size)
print(arr_2.size)
# d
print(np.row_stack((arr_1, arr_2)))
# e
arr_3 = np.array((1, 8, 6, 5, 8, 3))
# f
arr_4 = arr_3 * 3 + 1
# g
arr_5 = arr_3.reshape((2, 3))
# h
print(np.amin(arr_5, 1))
# i
print(arr_5.mean())
# j
arr_6 = np.arange(11) ** 2
# k
print(arr_6[1::2])
# l
print(arr_6[::-1])
# m
arr_6[1::2] = 2
# n
print(49 in arr_6)
# o
A = np.random.randint(-10, 11, size=(4, 4))
B = A[A < 0]
