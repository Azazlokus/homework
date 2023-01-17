import numbers
from tempfile import tempdir


def matrix(n=1, m=0, a=0):
    if m == 0:
        m = n
    matr = []
    for i in range(n):
        line = []
        for j in range(m):
            line += [a]
        matr += [line]
    return matr


rows = matrix()
for row in rows:
    print(*row)
print()

rows = matrix(2)
for row in rows:
    print(*row)
print()

rows = matrix(3, 5)
for row in rows:
    print(*row)
print()

rows = matrix(2, 2, 7)
for row in rows:
    print(*row)
print()
