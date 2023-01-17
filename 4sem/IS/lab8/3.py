import numpy as np


def super_sort(rows, cols):
    A = np.random.randint(0, 101, size=(rows, cols))
    B = A.copy()
    B = np.sort(B, axis=0)
    B[:, ::2] = B[::-1, ::2]
    return A, B


A, B = super_sort(4, 4)
print('A:\n', A, '\nB:\n', B)
