def factorials(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


for fact in factorials(7):
    print(fact, end=" ")
