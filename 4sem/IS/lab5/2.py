from math import sqrt


def distance(x1, y1, x2, y2):
    dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist


print("Введите координаты точки 1 (x, y): ")
x1 = int(input())
y1 = int(input())
print("Введите координаты точки 2 (x, y): ")
x2 = int(input())
y2 = int(input())
print("Расстояние между точками 1 и 2 равно: ", distance(x1, y1, x2, y2))
