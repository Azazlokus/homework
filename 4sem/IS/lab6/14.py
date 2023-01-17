from math import sqrt
from random import randint


points = [(randint(-3, 3), randint(-3, 3)) for x in range(7)]
print("Координаты точек: ", *points)
print("Отсортированные точки: ", *sorted(points,
      key=lambda p: (sqrt(p[0] * p[0] + p[1] * p[1]), p[0], p[1])))
