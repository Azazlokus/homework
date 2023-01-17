import numpy as np


def solve(num: int):
    coeffs = []
    b = []
    for i in range(num):
        print(f"Введите коэффициенты {i+1} уравнения и свободный член:")
        inpt = input().split()
        while (len(inpt) != num + 1):
            print("Введите данные еще раз")
            inpt = input().split()
        coeffs.append(list(map(int, inpt[:-1])))
        b.append(int(inpt[-1]))

    if np.linalg.det(coeffs) != 0:
        x = np.linalg.solve(coeffs, b)
        return x
    else:
        return "Система не имеет решений (или имеет их бесконечно много)"


x = solve(2)
print(x)
