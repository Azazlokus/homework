number = int(input("Введите 4-значное число: "))
a = number % 10
number //= 10
b = number % 10
number //= 10
c = number % 10
d = number // 10
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    c, d = d, c
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if a == 0 and b:
    a, b = b, a
elif a == 0 and c:
    a, c = c, a
elif a == 0 and d:
    a, d = d, a
print(d + 10 * (c + 10 * (b + 10 * a)))
