def power(a, n):
    if n == 1:
        return a
    res = a * power(a, n - 1)
    return res


a = int(input("Введите число: "))
n = int(input("Введите степень: "))
print(power(a, n))
