def power(a, n):
    num = 1
    for i in range(n):
        num *= a
    return num


num = int(input("Введите число: "))
pow = int(input("Введите степень: "))
print(power(num, pow))
