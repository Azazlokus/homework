def transpose(matr):
    res = []
    n = len(matr)
    m = len(matr[0])
    for i in range(m):
        temp = []
        for j in range(n):
            temp += [matr[j][i]]
        res += [temp]
    matr[:] = res


matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)
